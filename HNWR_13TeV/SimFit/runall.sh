#!/bin/bash
./run_MakeCardPerYear.sh 2016 &> tmp/log_run_MakeCardPerYear_2016.log &
./run_MakeCardPerYear.sh 2017 &> tmp/log_run_MakeCardPerYear_2017.log &
./run_MakeCardPerYear.sh 2018 &> tmp/log_run_MakeCardPerYear_2018.log &

