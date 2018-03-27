#!/bin/bash
BASEDIR=/data7/Users/jskim/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/data/2016_HNDiLepton/

cardpath=$1
name=$2
outputpath=$3
echo "[bash] cardpath : "$cardpath
echo "[bash] name : "$name
echo "[bash] outputpath : "$outputpath

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /data7/Users/jskim/CMSSW_8_1_0/src/
export SCRAM_ARCH=slc6_amd64_gcc530
cmsenv
cd /data7/Users/jskim/CMSSW_8_1_0/src/HiggsAnalysis/CombinedLimit/data/2016_HNDiLepton/
combine -M Asymptotic $BASEDIR/$cardpath -n $name &> $BASEDIR/$outputpath
