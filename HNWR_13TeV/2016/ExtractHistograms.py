import os,ROOT

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
#masses_tmp = masses
#masses = []
#masses.append(masses_tmp[0])

for channel in channels:
  for region in regions:

    f_Bkgd_origin = ROOT.TFile('MergedRootfiles/'+channel+'_'+region+'_SR_Bkgd.root')
    f_Sig_origin = ROOT.TFile('MergedRootfiles/'+channel+'_'+region+'_SR_Signal.root')

    keys_Bkgd = f_Bkgd_origin.GetListOfKeys()
    keys_Sig = f_Sig_origin.GetListOfKeys()


    for mass in masses:

      out = ROOT.TFile('Ingredients/'+channel+'_'+region+'_'+mass+'.root','RECREATE')

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
