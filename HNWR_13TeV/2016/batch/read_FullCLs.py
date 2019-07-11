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
  CardUsed = CardUsed.split('/')[-1].replace('.txt','')
  #print "@@@@ "+CardUsed

  limits = []
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

    limits.append(this_limit)

  # CardUsed = card_EE_Combined_WR5000_N4200
  words = CardUsed.split('_')
  cardinfo = words[1]+'\t'+words[2]+'\t'+words[3].replace('WR','')+'\t'+words[4].replace('N','')

  #if Expected_Central=="":
  #  print cardinfo

  print cardinfo+'\t'+limits[0]+'\t'+limits[1]+'\t'+limits[2]+'\t'+limits[3]+'\t'+limits[4]


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
