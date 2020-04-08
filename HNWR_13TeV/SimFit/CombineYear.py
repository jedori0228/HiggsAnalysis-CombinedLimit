import os,ROOT
import argparse

Years = [
"2016",
"2017",
"2018",
]

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
  "Combined",
]

channels = [
  'EE',
  'MuMu',
]

os.chdir('Ingredients/')

for region in regions:

  for channel in channels:

    for mass in masses:

      outname = 'YearCombined_card_CRAdded_'+channel+'_'+region+'_'+mass+'.txt'

      cmd = 'combineCards.py '

      counter = 0
      for Year in Years:
        counter = counter+1
        source = Year+'_card_CRAdded_'+channel+'_'+region+'_'+mass+'.txt'
        cmd += 'Run'+Year+'='+source+' '
      cmd += ' &> '+outname

      #print '@@@@ cmd = '+cmd
      os.system(cmd)

os.chdir('../')
