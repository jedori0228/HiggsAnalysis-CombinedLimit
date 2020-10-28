#!/usr/bin/env python

import os

Samples = [
'',
]

cards = [
'EE_Boosted_DYCR',
'EE_Boosted_SR_WR5000_N3000',
'EE_EMuShape_EMu_Resolved_SR',
'EE_EMuShape_SingleMuon_EMu_Boosted_CR',
'EE_Resolved_DYCR',
'EE_Resolved_SR_WR5000_N3000',
'MuMu_Boosted_DYCR',
'MuMu_Boosted_SR_WR5000_N3000',
'MuMu_EMuShape_EMu_Resolved_SR',
'MuMu_EMuShape_SingleElectron_EMu_Boosted_CR',
'MuMu_Resolved_DYCR',
'MuMu_Resolved_SR_WR5000_N3000',
]

for card in cards:

  channel = card.split('_')[0]

  for Sample in Samples:

    cardName = Sample+'YearCombined_card_'+card
    cmd = 'PostFitShapesFromWorkspace -w %s.root -d %s.txt -o output/hists_%s.root --postfit --sampling -f fitDiagnostics_YearCombined_card_CRAdded_%s_Combined_WR5000_N3000.root:fit_b --total-shapes'%(cardName,cardName,cardName,channel)
    print cmd
