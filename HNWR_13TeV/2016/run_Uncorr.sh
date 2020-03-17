#!/bin/bash
for Year in 2016 2017 2018
do
  echo ${Year}
  python ExtractHistograms.py -y ${Year}
  python MakeCard_Uncorr.py -y ${Year}
done

python CombineYear.py
