import os
import netCDF4
import numpy as np
import matplotlib.pyplot as plt

cell = 355
gp = 2412919

path_to_cell_file = os.path.join('path', 'to', 'SWI_TS', 'c_gls_SWI-TS_201412310000_C%04d_ASCAT_V3.0.1.nc' % cell)

with netCDF4.Dataset(path_to_cell_file) as ncdata:
    
    # find the index of the gp index in the cell file
    loc_idx = np.where(ncdata.variables['locations'][:] == gp)[0]
    
    # each variable is a 2D array of size locations x time
    # we want the slice of the array for our loc_idx for the whole time
    # the returned arrays are 2D, we select the first dimension with [0]
    swi20 = ncdata.variables['SWI_020'][loc_idx, :][0]
    qflag20 = ncdata.variables['QFLAG_020'][loc_idx, :][0]
    ssf = ncdata.variables['SSF'][loc_idx, :][0]
    
    # get the time units and convert from numbers to datetime format
    time_units = ncdata.variables['time'].units
    time = netCDF4.num2date(ncdata.variables['time'][:],time_units)
    
    # mask SWI and QFLAG for SSF values other than 1 (unfrozen)
    mask = ssf != 1
    swi20[mask] = np.nan
    qflag20[mask] = np.nan
    
    # plot the time series
    plt.plot(time, swi20, label='SWI T=20')
    plt.plot(time, qflag20, label='QFLAG T=20')
    plt.legend()
    plt.show()