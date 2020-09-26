import os,ROOT
import argparse
from IsCorrelated import IsCorrelated

##########################
#### EMu CR NO SIGNAL ####
##########################

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

NonPromptNormSyst = '2.00'
OthersNormSyst = '1.50'

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
'TT_TW',
'DYJets_MG_HT_Reweighted_Reshaped',
"NonPrompt",
"Others",
]

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

  out = open('Ingredients/'+Year+'_card_'+channel+'_EMuShape_'+region+'.txt','w')

  alltext = ''

  print>>out,'''imax *
jmax *
kmax *
---------------
shapes * * {0} $PROCESS $PROCESS_$SYSTEMATIC
---------------
bin {2}
observation -1
------------------------------'''.format(PWD+'/Ingredients/'+Year+'_'+filename, str(len(samples)),region_alias)
  line_1 = 'bin'
  line_2 = 'process'
  line_3 = 'process'
  line_4 = 'rate'

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

  NonPromptNormSystName = ''
  if region_alias=='Boosted_EMu_ElJet':
    NonPromptNormSystName = 'NonPromptNormSyst_Boosted_EE_Run'+Year
  elif region_alias=='Boosted_EMu_MuJet':
    NonPromptNormSystName = 'NonPromptNormSyst_Boosted_MuMu_Run'+Year
  else:
    NonPromptNormSystName = 'NonPromptNormSyst_Resolved_Run'+Year
  NonPromptNormSystLine = NonPromptNormSystName+' lnN'
  for sample in samples:
    if 'NonPrompt' in sample:
      NonPromptNormSystLine += ' '+NonPromptNormSyst
    else:
      NonPromptNormSystLine += ' -'
  out.write(NonPromptNormSystLine+'\n')

  OthersNormline = 'OthersNorm'+' lnN'
  for sample in samples:
    if 'Others' in sample:
      OthersNormline += ' '+OthersNormSyst
    else:
      OthersNormline += ' -'
  out.write(OthersNormline+'\n')

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
  if region_alias=='Boosted_EMu_ElJet':
    out.write('R_ttbar_Boosted_EE_'+Year+' rateParam '+region_alias+' TT_TW 1\n')
  elif region_alias=='Boosted_EMu_MuJet':
    out.write('R_ttbar_Boosted_MuMu_'+Year+' rateParam '+region_alias+' TT_TW 1\n')
  else:
    out.write('R_ttbar_'+ResolvedORBoosted+'_'+Year+' rateParam '+region_alias+' TT_TW 1\n')

  out.close()

## combine

#'combineCards.py Name1=card1.txt Name2=card2.txt .... > card.txt'
