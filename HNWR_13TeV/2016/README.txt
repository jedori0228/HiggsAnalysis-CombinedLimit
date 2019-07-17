Put below rootfiles inside $CMSSE_BASE/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/MergedRootfiles/ :

EE_Boosted_SR_Bkgd.root
EE_Boosted_SR_Signal.root
EE_Resolved_SR_Bkgd.root
EE_Resolved_SR_Signal.root
MuMu_Boosted_SR_Bkgd.root
MuMu_Boosted_SR_Signal.root
MuMu_Resolved_SR_Bkgd.root
MuMu_Resolved_SR_Signal.root

Then, 

cd $CMSSE_BASE/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/MergedRootfiles 
python ExtractHistograms.py
python makecard.py

You will have datacards and shapes in $CMSSE_BASE/src/HiggsAnalysis/CombinedLimit/HNWR_13TeV/2016/Ingredients/

