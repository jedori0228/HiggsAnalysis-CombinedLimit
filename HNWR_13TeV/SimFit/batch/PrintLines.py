import os

Dirs = [
#'2020_08_07_012013__YearCombined_Unblind_CRSigsRemoved',
#'2020_08_07_012019__Year2016_Unblind_CRSigsRemoved',
#'2020_08_07_012025__Year2017_Unblind_CRSigsRemoved',
#'2020_08_07_012033__Year2018_Unblind_CRSigsRemoved',
#'2020_08_07_012351__YearCombined_Unblind_CRSigsRemoved_ExpObsSeparately',
#'2020_08_07_012358__Year2016_Unblind_CRSigsRemoved_ExpObsSeparately',
#'2020_08_07_012406__Year2017_Unblind_CRSigsRemoved_ExpObsSeparately',
#'2020_08_07_012411__Year2018_Unblind_CRSigsRemoved_ExpObsSeparately',

"NEW_2020_08_07_012013__YearCombined_Unblind_CRSigsRemoved",
"NEW_2020_08_07_012019__Year2016_Unblind_CRSigsRemoved",
"NEW_2020_08_07_012025__Year2017_Unblind_CRSigsRemoved",
"NEW_2020_08_07_012033__Year2018_Unblind_CRSigsRemoved",

]

print 'for dir in ',
for Dir in Dirs:
  print Dir,
print '\n'

for Dir in Dirs:

  words = Dir.split('_')
  Year = ""
  for word in words:
    if 'Year' in word:
      Year = word.replace('Year','')
      break

  if Year=='Combined':
    Year = 'YearCombined'

  cmd = 'cp '+Dir+'.txt /data6/Users/jskim/HNWR_Plotter/rootfiles/Run2Legacy_v4__Default/Limit/Asymptotic/'+Year
  print cmd

for Dir in Dirs:

  words = Dir.split('_')
  Year = ""
  for word in words:
    if 'Year' in word:
      Year = word.replace('Year','')
      break

  str_Year = Year
  if Year=='Combined':
    Year = '-1'

  cmd = 'root -l -b -q "src/Draw_Limit.C('+Year+', \\"'+Dir+'\\")" &> tmp/log_Limit_'+str_Year+'.log &'
  print cmd

for Dir in Dirs:
  words = Dir.split('_')
  Year = ""
  for word in words:
    if 'Year' in word:
      Year = word.replace('Year','')
      break
  if Year=='Combined':
    Year = 'YearCombined'

  print '    cp $basedirFromCMS2/$SKFlatANV/Limit/Asymptotic/'+Year+'/'+Dir+'/2D_${ch}.pdf figures/'+Year+'/'
