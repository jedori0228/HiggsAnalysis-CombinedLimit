#!/bin/bash
for dir in  2020_07_27_122028__Year2016_FitDYDataNewKFactor 2020_07_27_122030__Year2017_FitDYDataNewKFactor 2020_07_27_122033__Year2018_FitDYDataNewKFactor 2020_07_27_122035__YearCombined_FitDYDataNewKFactor 
do
  ./read_Asymptotic.py -i $dir
done
