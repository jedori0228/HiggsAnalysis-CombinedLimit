#JobName=PDFErrorFixedAgain
#JobName=PDFErrorFixedAgain_ExpObsSeparately
#JobName=SignalStrenghtChanged_Obs

#JobName=PDF38Removed_ExpObsSeparately
#JobName=PDF38Removed_Obs
#JobName=PDF38Removed_Exp_0p500

#JobName=PDFUpdated
#JobName=PDFUpdated_ExpObsSeparately

#JobName=PDFUpdated_Exp_0p840
#JobName=PDFUpdated_Exp_0p160

#JobName=OverlapFixed_WideBin
JobName=OverlapFixed_WideBin_ExpObsSeparately

WEBasedir=/data6/Users/jskim/HiggsCombined_CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/SimFit/workspace/

for Year in Combined 2016 2017 2018
#for Year in Combined
#for Year in 2017
do

  ./create-batch -n Year${Year}_${JobName} -l ${WEBasedir}/WS_${Year}.txt

  #./create-batch -n HybridNew__Year${Year}_${JobName} -l ${WEBasedir}/WS_${Year}.txt --Full --run Obs
  #./create-batch -n HybridNew__Year${Year}_${JobName} -l ${WEBasedir}/WS_${Year}.txt --Full --run 0.500

  #./create-batch -n HybridNew__Year${Year}_${JobName} -l ${WEBasedir}/WS_${Year}.txt --Full --run 0.840
  #./create-batch -n HybridNew__Year${Year}_${JobName} -l ${WEBasedir}/WS_${Year}.txt --Full --run 0.160

done
