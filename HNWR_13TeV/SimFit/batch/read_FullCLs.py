#!/usr/bin/env python

import os
import argparse
import datetime

parser = argparse.ArgumentParser(description='SKFlat Command')
parser.add_argument('-i', dest='Logdir')
args = parser.parse_args()

quants = [
"0.025","0.160","0.500","0.840","0.975"
]

if not args.Logdir:
  parser.error('-i : log directory name should be given')

Logdir = args.Logdir

os.system('ls -1 '+Logdir+'/job_*.log > tmp.txt')
lines = open('tmp.txt').readlines()
os.system('rm tmp.txt')

outfile = open(Logdir+'.txt','w')

n_job = len(lines)
for i in range(0,n_job):

  lines_log = open(lines[i].strip('\n')).readlines()

  #### Find which card is used
  CardUsed = ""
  for k in range(0,len(lines_log)):
    j = len(lines_log)-1-k
    line = lines_log[k]
    if "Input datacard" in line:
      CardUsed = line.split()[2]
      break
  if CardUsed=="":
    continue
  CardUsed = CardUsed.split('/')[-1].replace('.root','')
  print "@@@@ "+CardUsed

  ######        0        1        2       3          4        5
  ######     exp       +1        -1       +2       -2      obs
  limits = [9999999, 9999999, 9999999, 9999999, 9999999, 9999999]
  for quant in quants:

    #print quant

    this_limit = ""

    for j in range(0,len(lines_log)):
      line = lines_log[j]
      if "#### quant = "+quant in line:
        #### now, get the value

        Found = False
        for k in range(j+1,len(lines_log)):
          if "#### quant = " in lines_log[k]:
            break
          if "Limit: r" in lines_log[k]:
            words = lines_log[k].split()
            this_limit = words[3]
            break

    if quant=="0.025":
      limits[4] = this_limit
    elif quant=="0.160":
      limits[2] = this_limit
    elif quant=="0.500":
      limits[0] = this_limit
    elif quant=="0.840":
      limits[1] = this_limit
    elif quant=="0.975":
      limits[3] = this_limit

  for j in range(0,len(lines_log)):
    line = lines_log[j]
    if "### Running observed limit" in line:
      for k in range(j+1,len(lines_log)):
        if "-- Hybrid New --" in lines_log[k]:
          words = lines_log[k+1].split()
          limits[5] = words[3]
          break

  # CardUsed = card_EE_Combined_WR5000_N4200
  #            YearCombined_card_EE_Boosted_WR1000_N100.txt
  words = CardUsed.split('_')
  if len(words)<4:
    continue
  cardinfo = words[2]+'\t'+words[3]+'\t'+words[4].replace('WR','')+'\t'+words[5].replace('N','')

  #if Expected_Central=="":
  #  print cardinfo

  #0.025 0.160 0.500 0.840 0.975
  outfile.write(cardinfo+'\t'+limits[0]+'\t'+limits[1]+'\t'+limits[2]+'\t'+limits[3]+'\t'+limits[4]+'\t'+limits[5]+'\n')

'''
 -- AsymptoticLimits ( CLs ) --
Observed Limit: r < 546.5518
Expected  2.5%: r < 1.1521
Expected 16.0%: r < 1.5664
Expected 50.0%: r < 2.2344
Expected 84.0%: r < 3.2497
Expected 97.5%: r < 4.5513

Done in 0.00 min (cpu), 0.00 min (real)
'''
