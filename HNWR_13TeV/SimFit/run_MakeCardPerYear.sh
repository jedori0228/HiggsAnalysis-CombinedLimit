#!/bin/bash
Year=$1
python MakeEMuCard_Advanced.py -y ${Year} -c EE
python MakeEMuCard_Advanced.py -y ${Year} -c MuMu
python MakeCard_Advanced.py -y ${Year}
