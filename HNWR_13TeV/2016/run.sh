#!/bin/bash
#for Year in 2016 2017 2018
for Year in 2017
do
  echo ${Year}
  python ExtractHistograms.py -y ${Year}
  python MakeCard.py -y ${Year}
done

python CombineYear.py
