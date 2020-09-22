import os,ROOT
import argparse
from IsCorrelated import IsCorrelated

#########################
#### DY CR NO SIGNAL ####
#########################

parser = argparse.ArgumentParser(description='option')
parser.add_argument('-y', dest='Year')
args = parser.parse_args()

Year = args.Year

LumiSyst = "1.025"
if Year=="2016":
  LumiSyst = "1.025"
elif Year=="2017":
  LumiSyst = "1.023"
elif Year=="2018":
  LumiSyst = "1.025"
else:
  print "WTF"

print "@@@@ Year = "+Year
print "@@@@ Lumi err = "+LumiSyst

PWD = os.getcwd()

OthersNormSyst = '1.50'

regions = [
  "Resolved",
  "Boosted",
]

channels = [
  'EE',
  'MuMu',
]

systs =[
    "JetRes",
    "JetEn",
    "MuonEn",
    "MuonRecoSF",
    "MuonIDSF",
    "MuonISOSF",
    "MuonTriggerSF",
    "ElectronRes",
    "ElectronEn",
    "ElectronRecoSF",
    "ElectronIDSF",
    "ElectronTriggerSF",
    "LSFSF",
    "PU",
    "Prefire",
]

allsamples = [
'TTLX_powheg',
'DYJets_MG_HT_Reweighted_Reshaped',
"Others",
]

for region in regions:

  EMuSyst = "1.20"
  if region=="Resolved":
    EMuSyst = "1.20"
  elif region=="Boosted":
    EMuSyst = "1.30"
  else:
    print "WTF??"

  for channel in channels:

    binname = region+"_DYCR_"+channel

    filename = channel+'_'+region+'_DYCR.root'

    f = ROOT.TFile('Ingredients/'+Year+'_'+filename)
    samples = []
    for sample in allsamples:
      if f.Get(sample):
        samples.append(sample)


    out = open('Ingredients/'+Year+'_card_'+channel+'_'+region+'_DYCR.txt','w')

    alltext = ''

    print>>out,'''imax *
jmax *
kmax *
---------------
shapes * * {0} $PROCESS $PROCESS_$SYSTEMATIC
---------------
bin {2}
observation -1
------------------------------'''.format(PWD+'/Ingredients/'+Year+'_'+filename, str(len(samples)),binname)
    line_1 = 'bin'
    line_2 = 'process'
    line_3 = 'process'
    line_4 = 'rate'

    counter = 1
    for sample in samples:
      line_1 += ' '+binname
      line_2 += ' '+sample
      line_3 += ' '+str(counter)
      line_4 += ' -1'
      counter += 1

    out.write(line_1+'\n')
    out.write(line_2+'\n')
    out.write(line_3+'\n')
    out.write(line_4+'\n')
    out.write('---------------------------------\n')

    ### now syst
    for syst in systs:

      #### Exception control
      if channel=="EE" and "Muon" in syst:
        continue
      if channel=="MuMu" and "Electron" in syst:
        continue
      if Year=="2018" and syst=="Prefire":
        continue
      if region=="Resolved" and syst=="LSFSF":
        continue


      thisline = 'Run'+Year+'_'+syst+' shapeN2'
      if IsCorrelated(syst):
        thisline = syst+' shapeN2'

      for sample in samples:
        if "EMuMethod" in sample:
          thisline += ' -'
        else:
          thisline += ' 1'
      out.write(thisline+'\n')

    #### ZPt reweight
    #ZPtRwline = 'Run'+Year+'_ZPtRw'+' shapeN2'
    ZPtRwline = 'ZPtRw'+' shapeN2'
    for sample in samples:
      if 'DYJets_' in sample:
        ZPtRwline += ' 1'
      else:
        ZPtRwline += ' -'
    out.write(ZPtRwline+'\n')

    OthersNormSystName = 'OthersNormSyst_Resolved_'+channel+'_Run'+Year if ('Resolved' in region) else 'OthersNormSyst_Boosted_'+channel+'_Run'+Year
    OthersNormSystLine = OthersNormSystName+' lnN'
    for sample in samples:
      if 'Others' in sample:
        OthersNormSystLine += ' '+OthersNormSyst
      else:
        OthersNormSystLine += ' -'
    out.write(OthersNormSystLine+'\n')

    NBin = 9 if ('Resolved' in region) else 5
    ResolvedORBoosted = 'Resolved' if ('Resolved' in region) else 'Boosted'
    for iBin in range(0,NBin):
      DYReshapeSystline = 'Run'+Year+'_'+ResolvedORBoosted+'DYReshapeSystBin'+str(iBin)+' shapeN2'
      for sample in samples:
        if 'DYJets_' in sample:
          DYReshapeSystline += ' 1'
        else:
          DYReshapeSystline += ' -'
      out.write(DYReshapeSystline+'\n')

    NormSyst_Lumi = 'Run'+Year+'_Lumi'+' lnN'+(' '+LumiSyst)*(len(samples))+'\n'
    out.write(NormSyst_Lumi)

    #### Auto stat
    out.write('* autoMCStats 0 0 1\n')
    if "Boosted" in region:
      out.write('R_ttbar_'+region+'_'+channel+'_'+Year+' rateParam '+region+'_DYCR_'+channel+' TTLX_powheg 1\n')
    else:
      out.write('R_ttbar_'+region+'_'+Year+' rateParam '+region+'_DYCR_'+channel+' TTLX_powheg 1\n')
    out.write('R_DY_'+region+'_'+Year+' rateParam '+region+'_DYCR_'+channel+' DYJets_MG_HT_Reweighted_Reshaped 1\n')

    out.close()

## combine

#'combineCards.py Name1=card1.txt Name2=card2.txt .... > card.txt'
