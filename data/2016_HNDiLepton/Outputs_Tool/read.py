import os

def ReadLimit(filepath):
  lines = open(filepath).readlines()
  value = float(lines[len(lines)-1].split()[0])
  value = round(value,4)
  return str(value)

channels = ["MuMu", "ElEl", "MuEl"]
Bins = ["Bin1", "Bin2", "Combined"]

## no 80 GeV
masses = [20, 30, 40, 50, 60, 70, 75, 85, 90, 100, 125, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1700]
massesVBF = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1700, 2000]

counter = 0
for ch in channels:

  for Bin in Bins:

    outputdir = ch+"_"+Bin
    out = open(outputdir+'/result.txt','w')
    outVBF = open(outputdir+'/result_VBF.txt','w')

    for mass in masses:


      obs = ReadLimit(outputdir+"/obs_log_"+Bin+"_HN"+ch+"_"+str(mass)+".log")
      mean = ReadLimit(outputdir+"/exp_0.500_log_"+Bin+"_HN"+ch+"_"+str(mass)+".log")
      onesig_left = ReadLimit(outputdir+"/exp_0.160_log_"+Bin+"_HN"+ch+"_"+str(mass)+".log")
      onesig_right = ReadLimit(outputdir+"/exp_0.840_log_"+Bin+"_HN"+ch+"_"+str(mass)+".log")
      twosig_left = ReadLimit(outputdir+"/exp_0.025_log_"+Bin+"_HN"+ch+"_"+str(mass)+".log")
      twosig_right = ReadLimit(outputdir+"/exp_0.975_log_"+Bin+"_HN"+ch+"_"+str(mass)+".log")

      out.write(str(mass)+"\t"+obs+"\t"+mean+"\t"+onesig_left+"\t"+onesig_right+"\t"+twosig_left+"\t"+twosig_right+'\n')
      if mass < massesVBF[0]:
        outVBF.write(str(mass)+"\t"+obs+"\t"+mean+"\t"+onesig_left+"\t"+onesig_right+"\t"+twosig_left+"\t"+twosig_right+'\n')


    out.close()


    for mass in massesVBF:

      obs = ReadLimit(outputdir+"/obs_log_"+Bin+"_HN"+ch+"_"+str(mass)+"_VBF.log")
      mean = ReadLimit(outputdir+"/exp_0.500_log_"+Bin+"_HN"+ch+"_"+str(mass)+"_VBF.log")
      onesig_left = ReadLimit(outputdir+"/exp_0.160_log_"+Bin+"_HN"+ch+"_"+str(mass)+"_VBF.log")
      onesig_right = ReadLimit(outputdir+"/exp_0.840_log_"+Bin+"_HN"+ch+"_"+str(mass)+"_VBF.log")
      twosig_left = ReadLimit(outputdir+"/exp_0.025_log_"+Bin+"_HN"+ch+"_"+str(mass)+"_VBF.log")
      twosig_right = ReadLimit(outputdir+"/exp_0.975_log_"+Bin+"_HN"+ch+"_"+str(mass)+"_VBF.log")

      outVBF.write(str(mass)+"\t"+obs+"\t"+mean+"\t"+onesig_left+"\t"+onesig_right+"\t"+twosig_left+"\t"+twosig_right+'\n')

    outVBF.close()
