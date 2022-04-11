import dill
import pprint


with open("era5625_aaai.dill", "rb") as f:
    info = dill.load(f)
pprint.pprint(info)
