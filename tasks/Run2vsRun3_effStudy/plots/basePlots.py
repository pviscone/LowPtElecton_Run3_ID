from cmgrdf_cli.defaults import load_defaults
load_defaults("base_defaults")
from cmgrdf_cli.plots import Hist, Hist2D

plots={
    "main":[
        Hist("Electron_pt", "Electron_pt")
    ]
}
