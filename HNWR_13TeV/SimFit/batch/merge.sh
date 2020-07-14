#!/bin/bash
for dir in  2020_07_13_195535__Year2016_SigPDFErr10Percent 2020_07_13_195537__Year2017_SigPDFErr10Percent 2020_07_13_195539__Year2018_SigPDFErr10Percent 2020_07_13_195540__YearCombined_SigPDFErr10Percent 
do
  ./read_Asymptotic.py -i $dir
done
