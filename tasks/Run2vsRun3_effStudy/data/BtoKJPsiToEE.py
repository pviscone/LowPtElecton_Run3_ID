from cmgrdf_cli.data import cms10

all_processes={
    "BuToKJPsiToEE2018" : {
        "groups" : [
            {
            "name": "BuToKJPsiToEE",
            "samples": {
                "BuToKJPsiToEE":
                    {
                    "xsec":1,
                    "path": "{name}/NANOAOD/2018/*.root"
                    },
                },
            "cut":"1",
            },
        ],
        "label":"BtoKJpsi(ee) 2018",
        "signal": False,
        "color": cms10[0],
    },
    "BuToKJPsiToEE2022" : {
        "groups" : [
            {
            "name": "BuToKJPsiToEE",
            "samples": {
                "BuToKJPsiToEE":
                    {
                    "xsec":1,
                    "path": "{name}/NANOAOD/2022/*.root"
                    },
                },
            "cut":"1",
            },
        ],
        "label":"BtoKJpsi(ee) 2022",
        "signal": True,
        "color": cms10[1],
    },
}