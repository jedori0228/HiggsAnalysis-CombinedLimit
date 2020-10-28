#!/bin/bash

## Getting card
for Year in 2016 2017 2018
do
  ## SR
  for channel in EE MuMu
  do
    for region in Resolved Boosted
    do
      cp ../Ingredients/${Year}_card_${channel}_${region}_SR_WR5000_N3000.txt ./CardForEachYear/
    done
  done
  ## CR
  for region in EE_EMuShape_EMu_Resolved_SR EE_Resolved_DYCR EE_EMuShape_SingleMuon_EMu_Boosted_CR EE_Boosted_DYCR MuMu_EMuShape_EMu_Resolved_SR MuMu_Resolved_DYCR MuMu_EMuShape_SingleElectron_EMu_Boosted_CR MuMu_Boosted_DYCR
  do
    cp ../Ingredients/${Year}_card_${region}.txt ./CardForEachYear/
  done
done

cd CardForEachYear/

./MakeCardForEachProcess.py

for dirName in "./"
do
  cd ${dirName}
  ## Merging SR
  for channel in EE MuMu
  do
    for region in Resolved Boosted
    do
      combineCards.py Run2016_${channel}_${region}_SR=2016_card_${channel}_${region}_SR_WR5000_N3000.txt Run2017_${channel}_${region}_SR=2017_card_${channel}_${region}_SR_WR5000_N3000.txt Run2018_${channel}_${region}_SR=2018_card_${channel}_${region}_SR_WR5000_N3000.txt &> YearCombined_card_${channel}_${region}_SR_WR5000_N3000.txt
    done
  done
  ## Merging DY CR
  for channel in EE MuMu
  do
    for region in Resolved Boosted
    do
      combineCards.py Run2016_${channel}${region}DYCR=2016_card_${channel}_${region}_DYCR.txt Run2017_${channel}${region}DYCR=2017_card_${channel}_${region}_DYCR.txt Run2018_${channel}${region}DYCR=2018_card_${channel}_${region}_DYCR.txt &> YearCombined_card_${channel}_${region}_DYCR.txt
    done
  done
  ## Merging Resolved EMu CR
  for channel in EE MuMu
  do
    region=Resolved
    combineCards.py Run2016_${channel}${region}EMuCR=2016_card_${channel}_EMuShape_EMu_${region}_SR.txt Run2017_${channel}${region}EMuCR=2017_card_${channel}_EMuShape_EMu_${region}_SR.txt Run2018_${channel}${region}EMuCR=2018_card_${channel}_EMuShape_EMu_${region}_SR.txt &> YearCombined_card_${channel}_EMuShape_EMu_${region}_SR.txt
  done
  ## Merging Boosted EMu with E-jet
  combineCards.py Run2016_EEBoostedEMuCR=2016_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.txt Run2017_EEBoostedEMuCR=2017_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.txt Run2018_EEBoostedEMuCR=2018_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.txt &> YearCombined_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.txt
  ## Mering Bosoted EMu with Mu-jet
  combineCards.py Run2016_MuMuBoostedEMuCR=2016_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.txt Run2017_MuMuBoostedEMuCR=2017_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.txt Run2018_MuMuBoostedEMuCR=2018_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.txt &> YearCombined_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.txt

  text2workspace.py YearCombined_card_EE_Boosted_DYCR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_EE_Boosted_SR_WR5000_N3000.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_EE_EMuShape_EMu_Resolved_SR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_EE_Resolved_DYCR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_EE_Resolved_SR_WR5000_N3000.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_Boosted_DYCR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_EMuShape_EMu_Resolved_SR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_Resolved_DYCR.txt --X-allow-no-signal
  text2workspace.py YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.txt --X-allow-no-signal
  cd -
done

cd ..

mv CardForEachYear/YearCombined* ./
for sample in 
do
  mv CardForEachYear/${sample}/YearCombined_card_EE_Boosted_DYCR.root ${sample}__YearCombined_card_EE_Boosted_DYCR.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_Boosted_DYCR.txt ${sample}__YearCombined_card_EE_Boosted_DYCR.txt
  mv CardForEachYear/${sample}/YearCombined_card_EE_Boosted_SR_WR5000_N3000.root ${sample}__YearCombined_card_EE_Boosted_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_Boosted_SR_WR5000_N3000.txt ${sample}__YearCombined_card_EE_Boosted_SR_WR5000_N3000.txt
  mv CardForEachYear/${sample}/YearCombined_card_EE_EMuShape_EMu_Resolved_SR.root ${sample}__YearCombined_card_EE_EMuShape_EMu_Resolved_SR.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_EMuShape_EMu_Resolved_SR.txt ${sample}__YearCombined_card_EE_EMuShape_EMu_Resolved_SR.txt
  mv CardForEachYear/${sample}/YearCombined_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.root ${sample}__YearCombined_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.txt ${sample}__YearCombined_card_EE_EMuShape_SingleMuon_EMu_Boosted_CR.txt
  mv CardForEachYear/${sample}/YearCombined_card_EE_Resolved_DYCR.root ${sample}__YearCombined_card_EE_Resolved_DYCR.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_Resolved_DYCR.txt ${sample}__YearCombined_card_EE_Resolved_DYCR.txt
  mv CardForEachYear/${sample}/YearCombined_card_EE_Resolved_SR_WR5000_N3000.root ${sample}__YearCombined_card_EE_Resolved_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_EE_Resolved_SR_WR5000_N3000.txt ${sample}__YearCombined_card_EE_Resolved_SR_WR5000_N3000.txt
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Boosted_DYCR.root ${sample}__YearCombined_card_MuMu_Boosted_DYCR.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Boosted_DYCR.txt ${sample}__YearCombined_card_MuMu_Boosted_DYCR.txt
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.root ${sample}__YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.txt ${sample}__YearCombined_card_MuMu_Boosted_SR_WR5000_N3000.txt
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_EMuShape_EMu_Resolved_SR.root ${sample}__YearCombined_card_MuMu_EMuShape_EMu_Resolved_SR.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_EMuShape_EMu_Resolved_SR.txt ${sample}__YearCombined_card_MuMu_EMuShape_EMu_Resolved_SR.txt
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.root ${sample}__YearCombined_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.txt ${sample}__YearCombined_card_MuMu_EMuShape_SingleElectron_EMu_Boosted_CR.txt
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Resolved_DYCR.root ${sample}__YearCombined_card_MuMu_Resolved_DYCR.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Resolved_DYCR.txt ${sample}__YearCombined_card_MuMu_Resolved_DYCR.txt
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.root ${sample}__YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.root
  mv CardForEachYear/${sample}/YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.txt ${sample}__YearCombined_card_MuMu_Resolved_SR_WR5000_N3000.txt
done
