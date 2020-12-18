#!/usr/bin/env python

import os

os.system('ls -1 201*card*SR_WR*.txt &> tmp.txt')
fnames = open('tmp.txt').readlines()
os.system('rm tmp.txt')

samples = [
'TT_TW',
'NonPrompt',
'DYJets_MG_HT_Reweighted_Reshaped',
'Others',
]

for sample in samples:
  os.system('mkdir -p '+sample)

for fname in fnames:
  fname = fname.strip('\n')
  lines = open(fname).readlines()
  index_ProcInfo_Start = 0
  index_Nuisacne_Start = 0
  for i in range(0,len(lines)):
    line = lines[i]
    if 'observation' in line:
      index_ProcInfo_Start = i+2
      break
  for i in range(0,len(lines)):
    line = lines[i]
    if 'rate ' in line:
      index_Nuisacne_Start = i+2
      break

  for sample in samples:
    os.system('mkdir -p '+sample)
    newfile = open(sample+'/'+fname,'w')

    for i in range(0,index_ProcInfo_Start):
      newfile.write(lines[i])

    words_ProcInfo_Start = lines[index_ProcInfo_Start+1].split()[1:]
    WriteOrNot = []
    for word in words_ProcInfo_Start:
      if 'WR' in word:
        WriteOrNot.append(True)
      else:
        if word==sample:
          WriteOrNot.append(True)
        else:
          WriteOrNot.append(False)
    for i in range(index_ProcInfo_Start,index_Nuisacne_Start-1):
      words = lines[i].split()
      newline = words[0]
      for j in range(1,len(words)):
        if WriteOrNot[j-1]:
          newline += ' '+words[j]
      newfile.write(newline+'\n')
    newfile.write('---------------------------------\n')

    for i in range(index_Nuisacne_Start,len(lines)):
      words = lines[i].split()

      if ('rateParam' in lines[i]):
        if (words[3]!=sample):
          continue
        else:
          newfile.write(lines[i])
          continue

      if 'autoMCStats' in lines[i]:
        newfile.write(lines[i])
        continue

      newline = words[0]+' '+words[1]
      for j in range(2,len(words)):
        if WriteOrNot[j-2]:
          newline += ' '+words[j]

      newfile.write(newline+'\n')


    newfile.close()
  
