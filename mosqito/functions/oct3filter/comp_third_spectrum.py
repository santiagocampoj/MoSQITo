# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:10:45 2020

@author: wantysal
"""

# Standard import
import numpy as np

# Local imports
from mosqito.functions.oct3filter.oct3spec import oct3spec
from mosqito.functions.noctfilter.n_oct_filter import (
    getFrequencies,
    designFilters,
    analyseData,
)


def comp_third_spec(is_stationary, signal, fs):
    """Third-octave band spectrum calculation, with the corresponding
    bands center frequencies

    Parameters
    ----------
    is_stationary: boolean
        TRUE if the signal is stationary, FALSE if it is time-varying
    signal : numpy.array
        time signal values
    fs : integer
        sampling frequency


    Outputs
    --------
    spec_third : numpy.ndarray
        Third octave band spectrum of signal sig [dB re.2e-5 Pa]
    spec_third_freq : numpy.ndarray
        Corresponding third octave bands center frequencies
    """

    if is_stationary == True:
        spec_third, third_axis = oct3spec(signal, fs)
        f_dict = getFrequencies(25, 12500, 3)
        filters = designFilters(f_dict, fs, plot=False)
        rmsData = analyseData(filters, signal, f_dict, plot=False)
        spec_third = 20 * np.log10((rmsData) / (2 * 10 ** -5))

        time_axis = []
    # elif is_stationary == False:
    #     spec_third, third_axis, time_axis = calc_third_octave_levels(signal, fs)
    np.squeeze(spec_third)

    output = {
        "name": "Third-octave-spectrum",
        "values": spec_third,
        "freqs": third_axis,
        "time": time_axis,
    }

    return output
