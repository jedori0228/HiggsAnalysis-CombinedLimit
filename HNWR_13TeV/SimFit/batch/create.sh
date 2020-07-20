JobName=DYCRmll800Applied

for Year in 2016 2017 2018 Combined
#for Year in 2018 Combined
do

  ./create-batch -n Year${Year}_${JobName} -l Year${Year}Cards.txt 
  #./create-batch -n HybridNew__Year${Year}_${JobName} -l Year${Year}Cards.txt --Full --nmax 100

done
