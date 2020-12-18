#!/usr/bin/env python

import os

Samples = [
'DYJets_MG_HT_Reweighted_Reshaped__',
'Others__',
'TT_TW__',
'NonPrompt__',
]

cards = [
'EE_Boosted_SR_WR5000_N3000',
'EE_Resolved_SR_WR5000_N3000',
'MuMu_Boosted_SR_WR5000_N3000',
'MuMu_Resolved_SR_WR5000_N3000',
]

for card in cards:

  channel = card.split('_')[0]

  for Sample in Samples:

    cardName = Sample+'YearCombined_card_'+card
    cmd = 'PostFitShapesFromWorkspace -w %s.root -d %s.txt -o output/hists_%s.root --postfit --sampling -f fitDiagnostics_YearCombined_card_CRAdded_%s_Combined_WR5000_N3000.root:fit_b --total-shapes --samples 2000'%(cardName,cardName,cardName,channel)
    print cmd
