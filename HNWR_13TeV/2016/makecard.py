import os,ROOT

PWD = os.getcwd()

masses = open('masses.txt').readlines()
for i in range(0,len(masses)):
  masses[i] = masses[i].replace('WRtoNLtoLLJJ_','').strip('\n')

#### Debug
#masses_tmp = masses
#masses = []
#masses.append(masses_tmp[0])
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
    "MuonIDSF",
    "ElectronRes",
    "ElectronEn",
    "ElectronIDSF",
]

sig_systs = [
  "Scale",
  "PDFError",
  "AlphaS",
]

allsamples = [
"DYJets_MG_HT_Reweighted",
"EMu",
"WWW",
"WWZ",
"WZZ",
"ZZZ",
"WZ_pythia",
"ZZ_pythia",
"WW_pythia",
"ttW",
"ttZ",
"WJets_MG_HT",
"DYJets10to50_Reweighted",
]

for region in regions:

  for channel in channels:

    for mass in masses:

      filename = channel+'_'+region+'_'+mass+'.root'

      f = ROOT.TFile('Ingredients/'+filename)
      samples = []
      for sample in allsamples:
        if f.Get(sample):
          samples.append(sample)


      out = open('Ingredients/card_'+channel+'_'+region+'_'+mass+'.txt','w')

      alltext = ''

      print>>out,'''imax 1
jmax {1}
kmax *
---------------
shapes * * {0} $PROCESS $PROCESS_$SYSTEMATIC
---------------
bin bin1
observation -1
------------------------------'''.format(PWD+'/Ingredients/'+filename, str(len(samples)))
      line_1 = 'bin bin1'
      line_2 = 'process '+mass
      line_3 = 'process '+'0'
      line_4 = 'rate '+'-1'

      counter = 1
      for sample in samples:
        line_1 += ' bin1'
        line_2 += ' '+sample
        line_3 += ' '+str(counter)
        line_4 += ' -1'
        counter += 1

      out.write(line_1+'\n')
      out.write(line_2+'\n')
      out.write(line_3+'\n')
      out.write(line_4+'\n')
      out.write('---------------------------------\n')

      ### Signal stat
      SignalStat = 'SignalStat lnN 1'
      for sample in samples:
        SignalStat += ' -'
      out.write(SignalStat+'\n')

      ### Stat for each sample
      for sample in samples:

        statline_for_this_sample = sample+'Stat lnN -'

        for sample2 in samples:
          if sample==sample2:
            statline_for_this_sample += ' 1'
          else:
            statline_for_this_sample += ' -'

        out.write(statline_for_this_sample+'\n')

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
        thisline = syst+' shapeN2 1'
        for sample in samples:
          if sample=="EMu":
            thisline += ' -'
          else:
            thisline += ' 1'
        out.write(thisline+'\n')

      NormSyst_Lumi = 'Lumi lnN 1.03'

      #### Signal only

      for syst in sig_systs:

        thisline = syst+' shapeN2 1'
        for sample in samples:
          thisline += ' -'
        out.write(thisline+'\n')

      out.close()

## combine

#'combineCards.py Name1=card1.txt Name2=card2.txt .... > card.txt'

os.chdir('Ingredients')

for channel in channels:

  for mass in masses:

    outname = 'card_'+channel+'_'+'Combined'+'_'+mass+'.txt'

    cmd = 'combineCards.py '

    counter = 0
    for region in regions:
      counter = counter+1
      source = 'card_'+channel+'_'+region+'_'+mass+'.txt'
      cmd += 'Name'+str(counter)+'='+source+' '
    cmd += ' > '+outname

    os.system(cmd)

os.chdir('../')
