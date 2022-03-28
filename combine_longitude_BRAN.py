#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:15:58 2022

@author: samantha
"""

import xarray as xr

bran_east = xr.open_dataset("BRAN_ssh_daily_1993-01-01_1.nc")
bran_west = xr.open_dataset("BRAN_ssh_daily_1993-01-01_2.nc")

# Visualize
bran_west.eta_t.isel(Time=0).plot(x="xt_ocean")
bran_east.eta_t.isel(Time=0).plot(x="xt_ocean")

# Change longitude values for 
bran_west.coords['xt_ocean'] = bran_west.coords['xt_ocean'] - 360

# Concatenate along the xt_ocean dimension, that is the longitude
bran = xr.concat([bran_west, bran_east], dim="xt_ocean")

# Visualize again to see if it's correct
bran.eta_t.isel(Time=0).plot(x="xt_ocean")

# Save the data to a new netCDF file
bran.to_netcdf("BRAN_ssh_daily_1993-01-01.nc")