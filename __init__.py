#!/usr/bin/env python3

'''
A package for verifying modeled auroral precipitation against SSUSI
observations.
'''

import numpy as np
from spacepy.datamodel import dmarray, SpaceData
from spacepy.pybats import rim
from spacepy.plot import set_target


class PrecipFile(SpaceData):
    '''
    Lots of docs here!
    '''

    def __init__(self, *args, **kwargs):
        super(PrecipFile, self).__init__(*args, **kwargs)  # Init as SpaceData.

        self.attrs['nlon'] = 10
        self.attrs['nlat'] = 10
        self['avee'] = np.zeros(self.attrs['nlon'], self.attrs['nlat'])

    def calc_hp(self):
        '''
        Calculate hemispheric power.
        '''

        pass

        # self['ave'].sum()

    def add_hemi_plot(self, coord='mag', target=None, loc=111):
        '''
        Add a hemispheric plot figure.

        Parameters
        ==========
        coord : str, defaults to 'mag'
           Set coordinate system to use, either 'mag' or 'geo'.

        Other Parameters
        ================

        Returns
        =======
        fig : Matplotlib Figure object
            The figure on which the plot is made.
        ax : Matplotlib Axes object
            The axes on which the plot is made.

        Examples
        ========
        >>> import spacepy.pybats.bats as pbs
        >>> mhd = pbs.Bats2d('spacepy-code/spacepy/pybats/slice2d_species.out')
        >>> pbs._calc_ndens(mhd)
        '''
        pass


class SwmfPrecip(PrecipFile):
    '''
    Subclass for handling swmf output.
    '''

    def __init__(self, filename, *args, **kwargs):
        super(PrecipFile, self).__init__(*args, **kwargs)  # Init as SpaceData.

        self.attrs['file'] = filename

        data = rim.Iono(filename)

        self['avee'] = data['n_ave']

    def calc_hp(self):
        pass