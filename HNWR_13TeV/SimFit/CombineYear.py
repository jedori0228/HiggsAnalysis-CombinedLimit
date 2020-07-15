import os,ROOT
import argparse
from Masses import *

Years = [
"2016",
"2017",
"2018",
]

PWD = os.getcwd()

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
