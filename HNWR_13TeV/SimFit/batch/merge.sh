#!/bin/bash
for dir in  2020_07_15_185034__Year2016_DYCRAddedWithShapeSyst 2020_07_15_185035__Year2017_DYCRAddedWithShapeSyst 2020_07_15_185036__Year2018_DYCRAddedWithShapeSyst 2020_07_15_185037__YearCombined_DYCRAddedWithShapeSyst 
do
  ./read_Asymptotic.py -i $dir
done
