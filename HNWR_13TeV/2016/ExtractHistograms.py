import os,ROOT
import argparse

parser = argparse.ArgumentParser(description='option')
parser.add_argument('-y', dest='Year')
args = parser.parse_args()

Year = args.Year

channels = [
"EE",
"MuMu",
]

regions = [
"Resolved",
"Boosted",
]

masses = open('masses.txt').readlines()
for i in range(0,len(masses)):
  masses[i] = masses[i].replace('WRtoNLtoLLJJ_','').strip('\n')

#### debug
#masses = [
#"WR4400_N400",
#"WR4400_N2200",
#"WR4400_N4300",
#]

for channel in channels:
  for region in regions:

    f_Bkgd_origin = ROOT.TFile('MergedRootfiles/'+Year+'/'+channel+'_'+region+'_SR_Bkgd.root')
    f_Sig_origin = ROOT.TFile('MergedRootfiles/'+Year+'/'+channel+'_'+region+'_SR_Signal.root')

    keys_Bkgd = f_Bkgd_origin.GetListOfKeys()
    keys_Sig = f_Sig_origin.GetListOfKeys()


    for mass in masses:

      out = ROOT.TFile('Ingredients/'+Year+'_'+channel+'_'+region+'_'+mass+'.root','RECREATE')

      for key in keys_Bkgd:
        h = f_Bkgd_origin.Get(key.GetName())
        out.cd()
        h.Write()
      for key in keys_Sig:

        if (key.GetName()==mass) or (mass+'_' in key.GetName()):

          h = f_Sig_origin.Get(key.GetName())
          out.cd()
          h.Write()

      out.Close()
