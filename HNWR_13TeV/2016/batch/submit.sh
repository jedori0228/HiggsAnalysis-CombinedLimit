#!/bin/bash
for dir in 2020_02_15_234024__Year2016_WideBin_STXsecFixed 2020_02_15_234025__Year2017_WideBin_STXsecFixed 2020_02_15_234026__Year2018_WideBin_STXsecFixed 2020_02_15_234027__YearCombined_WideBin_STXsecFixed

do
  cd $dir
  condor_submit submit.sh
  cd ..
done
