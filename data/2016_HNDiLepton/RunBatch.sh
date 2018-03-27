#!/bin/bash
date
BASEDIR=/data7/Users/jskim/CMSSW_7_4_7/src/HiggsAnalysis/CombinedLimit/data/2016_HNDiLepton/

cardpath=$1
name=$2
outputpath=$3
quant=$4
echo "[bash] cardpath : "$cardpath
echo "[bash] name : "$name
echo "[bash] quant : "$quant

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /data7/Users/jskim/CMSSW_7_4_7/src/
export SCRAM_ARCH=slc6_amd64_gcc491
cmsenv
cd /data7/Users/jskim/CMSSW_7_4_7/src/HiggsAnalysis/CombinedLimit/data/2016_HNDiLepton/

## Full CLs ##

if [ -z "$4" ]; then
  echo "## Running Observed Limit ##"
  echo "combine -M HybridNew --frequentist --testStat LHC -H ProfileLikelihood $BASEDIR/$cardpath -n $name" -T 4000
  combine -M HybridNew --frequentist --testStat LHC -H ProfileLikelihood $BASEDIR/$cardpath -n $name -T 4000
  echo "combine done"
  cd include
  root -l -b -q "ReadLimitFromTree.C(\""$BASEDIR"/higgsCombine"$name".HybridNew.mH120.root\")" &> $BASEDIR/$outputpath
  rm $BASEDIR/"higgsCombine"$name".HybridNew.mH120.root"


else
  echo "## Running Expected Limit ##"
  echo "## expectedFromGrid = "$expectedFromGrid
  echo "combine -M HybridNew --frequentist --testStat LHC -H ProfileLikelihood $BASEDIR/$cardpath -n $name --expectedFromGrid $quant" -T 4000
  combine -M HybridNew --frequentist --testStat LHC -H ProfileLikelihood $BASEDIR/$cardpath -n $name --expectedFromGrid $quant -T 4000
  echo "combine done"
  cd include
  root -l -b -q "ReadLimitFromTree.C(\""$BASEDIR"/higgsCombine"$name".HybridNew.mH120.quant"$quant".root\")" &> $BASEDIR/$outputpath
  rm $BASEDIR/"higgsCombine"$name".HybridNew.mH120.quant"$quant".root"


fi

date

