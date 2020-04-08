import os,ROOT
import argparse
from IsCorrelated import IsCorrelated

parser = argparse.ArgumentParser(description='option')
parser.add_argument('-y', dest='Year')
parser.add_argument('-c', dest='Channel')
args = parser.parse_args()

Year = args.Year
channel = args.Channel

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

all_masses = open('masses.txt').readlines()
masses = []
for mass in all_masses:
  if "#" in mass:
    continue
  masses.append(mass)
for i in range(0,len(masses)):
  masses[i] = masses[i].replace('WRtoNLtoLLJJ_','').strip('\n')

#### Debug
#masses = [
#"WR4000_N3000",
#]
####

regions = [
  ["EMu_Resolved_SR","Resolved_EMu"],
  ["SingleElectron_EMu_Boosted_CR","Boosted_EMu_MuJet"],
  ["SingleMuon_EMu_Boosted_CR","Boosted_EMu_ElJet"],
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
'VVV',
'VV',
'ttX',
'SingleTop',
'WJets_MG_HT',
'DYJets_MG_HT_Reweighted',
]

for mass in masses:

  for iregion in regions:

    region = iregion[0]
    region_alias = iregion[1]
    ResolvedORBoosted = ""

    if "Resolved" in region:
      ResolvedORBoosted = "Resolved"
    elif "Boosted" in region:
      ResolvedORBoosted = "Boosted"
    else:
      print "WTF??"

    filename = channel+"_"+region+'.root'

    f = ROOT.TFile('Ingredients/'+Year+'_'+filename)
    samples = []
    for sample in allsamples:
      if f.Get(sample):
        samples.append(sample)
    #### check signal
    h_Sig = f.Get(mass)
    if not h_Sig:
      print 'No signal for '+mass+' in '+channel+'\t'+region
      print '--> file : '+'Ingredients/'+Year+'_'+filename
      print '--> hname = '+mass

    out = open('Ingredients/'+Year+'_card_'+channel+'_EMuShape_'+region+'_'+mass+'.txt','w')

    alltext = ''

    print>>out,'''imax 1
jmax {1}
kmax *
---------------
shapes * * {0} $PROCESS $PROCESS_$SYSTEMATIC
---------------
bin {2}
observation -1
------------------------------'''.format(PWD+'/Ingredients/'+Year+'_'+filename, str(len(samples)),region_alias)
    line_1 = 'bin '+region_alias
    line_2 = 'process '+mass
    line_3 = 'process '+'0'
    line_4 = 'rate '+'-1'

    counter = 1
    for sample in samples:
      line_1 += ' '+region_alias
      line_2 += ' '+sample
      line_3 += ' '+str(counter)
      line_4 += ' -1'
      counter += 1

    out.write(line_1+'\n')
    out.write(line_2+'\n')
    out.write(line_3+'\n')
    out.write(line_4+'\n')
    out.write('---------------------------------\n')

    #### DY PDF
    DYNormline = 'DYNorm lnN -'
    for sample in samples:
      if 'DYJets_' in sample:
        DYNormline += ' 1.03'
      else:
        DYNormline += ' -'
    out.write(DYNormline+'\n')

    ### now syst
    for syst in systs:

      #### Exception control
      if Year=="2018" and syst=="Prefire":
        continue
      if "Resolved" in region and syst=="LSFSF":
        continue
      if region=="SingleElectron_EMu_Boosted_CR" and "Muon" in syst:
        continue
      if region=="SingleMuon_EMu_Boosted_CR" and "Electron" in syst:
        continue

      thisline = 'Run'+Year+'_'+syst+' shapeN2 1'
      if IsCorrelated(syst):
        thisline = syst+' shapeN2 1'

      for sample in samples:
        if "EMuMethod" in sample:
          thisline += ' -'
        else:
          thisline += ' 1'
      out.write(thisline+'\n')

    #### ZPt reweight
    #ZPtRwline = 'Run'+Year+'_ZPtRw'+' shapeN2 -'
    ZPtRwline = 'ZPtRw'+' shapeN2 -'
    for sample in samples:
      if 'DYJets_' in sample:
        ZPtRwline += ' 1'
      else:
        ZPtRwline += ' -'
    out.write(ZPtRwline+'\n')

    #### TODO ####
    #### TopPtReweight
    #TopPtRwline = 'TopPtRw lnN -'
    #for sample in samples:
    #  if sample=="TTLX_powheg":
    #    TopPtRwline += ' 1'
    #  else:
    #    TopPtRwline += ' -'
    #out.write(TopPtRwline+'\n')

    NormSyst_Lumi = 'Run'+Year+'_Lumi'+' lnN'+(' '+LumiSyst)*(len(samples)+1)+'\n'
    out.write(NormSyst_Lumi)

    #### Auto stat
    out.write('* autoMCStats 0 0 1\n')
    out.write('R_'+ResolvedORBoosted+'_'+channel+'_'+Year+' rateParam '+region_alias+' TTLX_powheg 1\n')

    out.close()

  ## combine

  #'combineCards.py Name1=card1.txt Name2=card2.txt .... > card.txt'
