import os

Dirs = [
'2020_04_07_133406__Year2016_TTMC_UpdateCorrel_TopPtReweight',
'2020_04_07_133411__Year2017_TTMC_UpdateCorrel_TopPtReweight',
'2020_04_07_133417__Year2018_TTMC_UpdateCorrel_TopPtReweight',
'2020_04_07_133422__YearCombined_TTMC_UpdateCorrel_TopPtReweight',
]

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
