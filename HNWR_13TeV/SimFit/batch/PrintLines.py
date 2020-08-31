import os

Dirs = [

'NEW_2020_08_28_203904__YearCombined_OverlapFixed_WideBin',
'NEW_2020_08_28_203906__Year2016_OverlapFixed_WideBin',
'NEW_2020_08_28_203907__Year2017_OverlapFixed_WideBin',
'NEW_2020_08_28_203908__Year2018_OverlapFixed_WideBin',


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



  print '    cp $basedirFromCMS2/$SKFlatANV/Limit/Asymptotic/'+Year+'/'+Dir+'/1D_${ch}_Combined_HalfN_Limit_vs_WR.pdf figures/'+Year+'/'
  print '    cp $basedirFromCMS2/$SKFlatANV/Limit/Asymptotic/'+Year+'/'+Dir+'/1D_${ch}_Combined_N100_Limit_vs_WR.pdf figures/'+Year+'/'

