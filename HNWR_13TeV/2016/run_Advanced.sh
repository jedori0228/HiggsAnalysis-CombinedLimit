#!/bin/bash
for Year in 2016 2017 2018
do
  echo "@@@@ Running "${Year}
  #python ExtractHistograms.py -y ${Year}
  python MakeCard_Advanced.py -y ${Year}
done

echo "@@@@ Now CombineYear.py each years"
python CombineYear.py
