import os
import xarray as xr
import numpy as np
import xesmf as xe
import matplotlib.pyplot as plt
import cmocean.cm as cm
from dask.diagnostics import ProgressBar

import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import ListedColormap
import matplotlib.ticker as mticker

'''
These scripts are for processing high-frequency radar data (HFR) from NOAA IOOS.
'''

def time_density(ds: xr.Dataset, var: str, dim="time"): # make sure there is indeed a "time" dimension
    da = ds[var]
    valid_counts = da.notnull().sum(dim)
    total_steps = ds.dims[dim]
    return (valid_counts / total_steps) * 100