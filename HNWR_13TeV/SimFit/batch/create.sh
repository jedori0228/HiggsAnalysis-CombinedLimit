JobName=Unblind_CRSigsRemoved_ExpObsSeparately

for Year in Combined 2016 2017 2018
#for Year in Combined
#for Year in 2016
do

  ./create-batch -n Year${Year}_${JobName} -l Year${Year}Cards.txt 
  #./create-batch -n HybridNew__Year${Year}_${JobName} -l Year${Year}Cards.txt --Full --nmax 100

done
