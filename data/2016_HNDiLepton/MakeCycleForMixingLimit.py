import os

channels = ["MuMu", "ElEl", "MuEl"]
Bins = ["Bin1", "Bin2", "Combined"]

masses = [20, 30, 40, 50, 60, 70, 75, 80, 85, 90, 100, 125, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1700]

out = open('run_Limit.sh','w')
out.write('#!/bin/bash\n')

BASEDIR = '/data7/Users/jskim/CMSSW_7_4_7/src/HiggsAnalysis/CombinedLimit/data/2016_HNDiLepton/'

quantiles = ["0.025","0.160","0.500","0.840","0.975"]

WhichQ = 'fastq'

for ch in channels:

  for Bin in Bins:

    for mass in masses:

      filename = "HN"+ch+"_"+str(mass)

      CardFilename = ch+"_"+Bin+"/HN"+ch+"_"+str(mass)+".txt"
      JobName = Bin+"_HN"+ch+"_"+str(mass)
      output = "log_"+Bin+"_HN"+ch+"_"+str(mass)+".log"

      outputdir = 'Outputs_Tool/'+ch+'_'+Bin
      os.system('mkdir -p '+outputdir)

      ## obs

      out.write("## "+JobName+" ##\n")
      cmd = 'qsub -q '+WhichQ
      cmd += ' -N obs_'+JobName
      cmd += ' -wd '+BASEDIR+'batchlog/'
      cmd += ' RunBatch.sh'
      ## RunBatch.sh arguments
      cmd += ' '+CardFilename
      cmd += ' obs_'+JobName
      cmd += ' '+outputdir+'/obs_'+output
      out.write(cmd+'\n')

      for q in quantiles:
        cmd = 'qsub -q '+WhichQ
        cmd += ' -N exp_'+q+'_'+JobName
        cmd += ' -wd '+BASEDIR+'batchlog/'
        cmd += ' RunBatch.sh'
        ## RunBatch.sh arguments
        cmd += ' '+CardFilename
        cmd += ' exp_'+q+'_'+JobName
        cmd += ' '+outputdir+'/exp_'+q+'_'+output
        cmd += ' '+q
        out.write(cmd+'\n')













