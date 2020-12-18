#!/bin/bash

cd CardForEachYear

for dirName in DYJets_MG_HT_Reweighted_Reshaped Others TT_TW NonPrompt
do

  cd ${dirName}

  for channel in EE MuMu
  do
    for region in Resolved Boosted
    do
      combineCards.py Run2016_${channel}_${region}_SR=2016_card_${channel}_${region}_SR_WR5000_N3000.txt Run2017_${channel}_${region}_SR=2017_card_${channel}_${region}_SR_WR5000_N3000.txt Run2018_${channel}_${region}_SR=2018_card_${channel}_${region}_SR_WR5000_N3000.txt &> YearCombined_card_${channel}_${region}_SR_WR5000_N3000.txt
    done
  done

  text2workspace.py YearCombined_card_EE_Boosted_SR_WR5000_N3000.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_EE_Resolved_SR_WR5000_N3000.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.txt --X-allow-no-signal
  cd -
done

cd ..

for sample in DYJets_MG_HT_Reweighted_Reshaped Others TT_TW NonPrompt
do
  mv CardForEachYear/${sample}/YearCombined_card_EE_Boosted_SR_WR5000_N3000.root ${sample}__YearCombined_card_EE_Boosted_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_Boosted_SR_WR5000_N3000.txt ${sample}__YearCombined_card_EE_Boosted_SR_WR5000_N3000.txt
  mv CardForEachYear/${sample}/YearCombined_card_EE_Resolved_SR_WR5000_N3000.root ${sample}__YearCombined_card_EE_Resolved_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_Resolved_SR_WR5000_N3000.txt ${sample}__YearCombined_card_EE_Resolved_SR_WR5000_N3000.txt

  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.root ${sample}__YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.txt ${sample}__YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.txt
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.root ${sample}__YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.txt ${sample}__YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.txt
done 

cd ..
