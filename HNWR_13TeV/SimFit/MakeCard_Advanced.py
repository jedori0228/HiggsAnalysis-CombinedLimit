import os,ROOT
import argparse
from IsCorrelated import IsCorrelated

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

sig_systs = [
  #"Scale", ## Log normal
  "PDFError",
  "AlphaS",
]

#### TODO
#### can differ for different year
allsamples = [
'TTLX_powheg',
#'Multiboson',
#'ttX',
#'SingleTop',
#'WJets_MG_HT',
'DYJets_MG_HT_Reweighted',
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

    binname = region+"_"+channel

    for mass in masses:

      filename = channel+'_'+region+'.root'

      f = ROOT.TFile('Ingredients/'+Year+'_'+filename)
      samples = []
      for sample in allsamples:
        if f.Get(sample):
          samples.append(sample)


      out = open('Ingredients/'+Year+'_card_'+channel+'_'+region+'_'+mass+'.txt','w')

      alltext = ''

      print>>out,'''imax 1
jmax {1}
kmax *
---------------
shapes * * {0} $PROCESS $PROCESS_$SYSTEMATIC
---------------
bin {2}
observation -1
------------------------------'''.format(PWD+'/Ingredients/'+Year+'_'+filename, str(len(samples)),binname)
      line_1 = 'bin '+binname
      line_2 = 'process '+mass
      line_3 = 'process '+'0'
      line_4 = 'rate '+'-1'

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

      #### DY PDF
      DYNormline = 'DYNorm lnN -'
      for sample in samples:
        if 'DYJets_' in sample:
          DYNormline += ' 1.30'
        else:
          DYNormline += ' -'
      out.write(DYNormline+'\n')

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

      #### Signal only

      for syst in sig_systs:

        thisline = syst+' shapeN2 1'
        for sample in samples:
          thisline += ' -'
        out.write(thisline+'\n')

      #### Scale as log normal
      signalScaleLine = 'SignalScale lnN '
      h_SignalScale = f.Get(mass+'_ScaleIntegralSyst')
      if h_SignalScale:
        syst_SignalScale = 1.+h_SignalScale.GetBinContent(1)
        signalScaleLine = 'SignalScale lnN '+str(syst_SignalScale)+' -'*len(samples)
        out.write(signalScaleLine+'\n')

      #### ee
      if Year!="2016" and channel=="EE":

        #lineExtraEESyst = 'Run'+Year+'_FastSimHEEPSyst lnN 1.02'+' -'*len(samples)
        lineExtraEESyst = 'FastSimHEEPSyst lnN 1.02'+' -'*len(samples)
        out.write(lineExtraEESyst+'\n')


      #### Auto stat
      out.write('* autoMCStats 0 0 1\n')
      out.write('R_'+region+'_'+channel+'_'+Year+' rateParam '+region+'_'+channel+' TTLX_powheg 1\n')

      out.close()

## combine

#'combineCards.py Name1=card1.txt Name2=card2.txt .... > card.txt'

os.chdir('Ingredients/')

## CR+SR
print '@@@@ Combining SR and CR'
for region in regions:

  for channel in channels:

    print '@@@@   '+region+'\t'+channel

    for mass in masses:

      outname = Year+'_card_CRAdded_'+channel+'_'+region+'_'+mass+'.txt'

      CRCardName = Year+"_card_"+channel+"_EMuShape_EMu_Resolved_SR_"+mass+".txt"
      if region=="Boosted":
        if channel=="EE":
          CRCardName = Year+"_card_"+channel+"_EMuShape_SingleMuon_EMu_Boosted_CR_"+mass+".txt"
        elif channel=="MuMu":
          CRCardName = Year+"_card_"+channel+"_EMuShape_SingleElectron_EMu_Boosted_CR_"+mass+".txt"

      cmd = 'combineCards.py'
      cmd += ' SR='+Year+'_card_'+channel+'_'+region+'_'+mass+'.txt'
      cmd += ' CR='+CRCardName

      cmd += ' > '+outname

      #print cmd
      os.system(cmd)

for channel in channels:

  for mass in masses:

    outname = Year+'_card_CRAdded_'+channel+'_'+'Combined'+'_'+mass+'.txt'

    cmd = 'combineCards.py '

    counter = 0
    for region in regions:
      counter = counter+1
      source = Year+'_card_CRAdded_'+channel+'_'+region+'_'+mass+'.txt'
      cmd += channel+'_'+region+'='+source+' '
    cmd += ' > '+outname

    os.system(cmd)

os.chdir('../')


