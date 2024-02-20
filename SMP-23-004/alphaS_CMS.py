import numpy as np

alpha_S = [
     # CMS determinations from Vector Boson cross sections
     { "val": np.array([0.1175]), "er_up": np.array([0.0025]), "er_dn": np.array([0.0028]), 
       "obs": "W/Z cross sections", "sqrts": " (7, 8 TeV)", "ref": "JHEP 06:018", "year": "(2020)", "order": "NNLO" },

     # CMS determinations from ttbar cross section
     { "val": np.array([0.1151]), "er_up": np.array([0.0033]), "er_dn": np.array([0.0032]), 
       "obs": "t#bar{t} cross section", "sqrts": " (7 TeV)", "ref": "PLB 728:496", "year": "(2014)", "order": "NNLO" },

     { "val": np.array([0.1151]), "er_up": np.array([0.0040]), "er_dn": np.array([0.0035]), 
       "obs": "t#bar{t} cross section", "sqrts": " (13 TeV)", "ref": "EPJC 79:368", "year": "(2019)", "order": "NNLO" },

     { "val": np.array([0.1135]), "er_up": np.array([0.0021]), "er_dn": np.array([0.0017]),
       "obs": "t#bar{t} cross section", "sqrts": " (13 TeV)", "ref": "EPJC 80:658", "year": "(2020)", "order": "NLO" },
 
     # CMS determinations from jet observables
     { "val": np.array([0.1148]), "er_up": np.array([0.0055]), "er_dn": np.array([0.0055]),
       "obs": "R_{32}", "sqrts": " (7 TeV)", "ref": "EPJC 73:2604", "year": "(2013)", "order": "NLO" },

     { "val": np.array([0.1185]), "er_up": np.array([0.0063]), "er_dn": np.array([0.0042]),
       "obs": "Inclusive jet", "sqrts": " (7 TeV)", "ref": "EPJC 75:288", "year": "(2015)", "order": "NLO" },

     { "val": np.array([0.1171]), "er_up": np.array([0.0074]), "er_dn": np.array([0.0049]), 
       "obs": "3-jet mass", "sqrts": " (7 TeV)", "ref": "EPJC 75:186", "year": "(2015)", "order": "NLO" },
 
     { "val": np.array([0.1164]), "er_up": np.array([0.0060]), "er_dn": np.array([0.0043]), 
       "obs": "Inclusive jet", "sqrts": " (8 TeV)", "ref": "JHEP 03:156", "year": "(2017)", "order": "NLO" },
 
     { "val": np.array([0.1199]), "er_up": np.array([0.0034]), "er_dn": np.array([0.0025]),
       "obs": "Dijets (3D)", "sqrts": " (8 TeV)", "ref": "EPJC 77:746", "year": "(2017)", "order": "NLO" },
  
     { "val": np.array([0.1170]), "er_up": np.array([0.0019]), "er_dn": np.array([0.0019]),
       "obs": "Inclusive jet", "sqrts": " (13 TeV)", "ref": "JHEP 02:142", "year": "(2022)", "order": "NNLO" },

     { "val": np.array([0.1179]), "er_up": np.array([0.0019]), "er_dn": np.array([0.0019]),
       "obs": "Dijets (2D/3D)", "sqrts": " (13 TeV)", "ref": "arxiv:2312.16669", "year": "(2024)", "order": "NNLO" },
 
     { "val": np.array([0.1229]), "er_up": np.array([0.0040]), "er_dn": np.array([0.0050]),
       "obs": "Energy correlators", "sqrts": " (13 TeV)", "ref": "CMS-PAS-SMP-22-015", "year": "(2024)", "order": "NNLL" },
 
     { "val": np.array([0.1177]), "er_up": np.array([0.0117]), "er_dn": np.array([0.0074]),
       "obs": "R_{#Delta#phi}", "sqrts": " (13 TeV)", "ref": "CMS-PAS-SMP-22-005", "year": "(2024)", "order": "NLO" },

     # PDG 2023 world average
     { "val": np.array([0.1180]), "er_up": np.array([0.0009]), "er_dn": np.array([0.0009]),
       "obs": "World avg", "sqrts": "", "ref": "Prog. Theor. Exp. Phys. 083C01", "year": "(2023 update)", "order": "" }
]
