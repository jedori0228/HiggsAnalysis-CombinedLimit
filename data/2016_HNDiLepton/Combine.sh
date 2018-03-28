#!/bin/bash
for ch in MuMu ElEl MuEl
do
  for i in 20 30 40 50 60 70 75 80 85 90 100 125 150 200 250 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 1700
  do
    combineCards.py Name1=$ch"_Bin1/HN"$ch"_"$i".txt" Name2=$ch"_Bin2/HN"$ch"_"$i".txt" > $ch"_Combined/HN"$ch"_"$i".txt"
  done
done

for ch in MuMu ElEl MuEl
do
  for i in 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 1700 2000
  do
    combineCards.py Name1=$ch"_Bin1/HN"$ch"_"$i"_VBF.txt" Name2=$ch"_Bin2/HN"$ch"_"$i"_VBF.txt" > $ch"_Combined/HN"$ch"_"$i"_VBF.txt"
  done
done
