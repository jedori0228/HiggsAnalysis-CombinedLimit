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
#"WR5000_N100",
#"WR5000_N3000",
#]
####
