from CMGRDF.cms.eras import lumis as lumi

P = "/eos/user/p/pviscone/EGM"

eras = [""]

era_paths_Data = {era: (P, "", "") for era in eras}
era_paths_MC = {era: (P, "", "") for era in eras}

for era in eras:
    lumi[era] = 100

PFs = []
PMCs = []
