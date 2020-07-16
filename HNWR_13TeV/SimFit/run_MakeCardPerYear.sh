#!/bin/bash
Year=$1
python MakeEMuCard_Advanced.py -y ${Year} -c EE
python MakeEMuCard_Advanced.py -y ${Year} -c MuMu
python MakeDYCard_Advanced.py -y ${Year}
python MakeCard_Advanced.py -y ${Year}
