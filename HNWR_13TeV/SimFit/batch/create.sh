JobName=TTMC_UpdateCorrel_TopPtReweight

for Year in 2016 2017 2018 Combined
do

  ./create-batch -n Year${Year}_${JobName} -l Year${Year}Cards.txt 

done
