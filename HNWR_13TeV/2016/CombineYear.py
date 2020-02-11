import os,ROOT
import argparse

Years = [
"2016",
"2017",
"2018",
]

PWD = os.getcwd()

masses = open('masses.txt').readlines()
for i in range(0,len(masses)):
  masses[i] = masses[i].replace('WRtoNLtoLLJJ_','').strip('\n')

#masses = [
#"WR4400_N400",
#"WR4400_N2200",
#"WR4400_N4300",
#]

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

      outname = 'YearCombined_card_'+channel+'_'+region+'_'+mass+'.txt'

      cmd = 'combineCards.py '

      counter = 0
      for Year in Years:
        counter = counter+1
        source = Year+'_card_'+channel+'_'+region+'_'+mass+'.txt'
        cmd += 'Name'+str(counter)+'='+source+' '
      cmd += ' &> '+outname

      #print '@@@@ cmd = '+cmd
      os.system(cmd)

os.chdir('../')
