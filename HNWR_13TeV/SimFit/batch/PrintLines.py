import os

Dirs = [
'2020_07_19_130454__Year2016_DYCRmll800Applied',
'2020_07_19_130455__Year2017_DYCRmll800Applied',
'2020_07_19_130456__Year2018_DYCRmll800Applied',
'2020_07_19_130457__YearCombined_DYCRmll800Applied',
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
