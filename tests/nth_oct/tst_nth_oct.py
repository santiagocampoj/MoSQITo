import matplotlib.pyplot as plt
import numpy as np

from mosqito.functions.shared.load import load
from mosqito.functions.oct3filter.oct3spec import oct3spec
from mosqito.functions.noctfilter.n_oct_filter import (
    getFrequencies,
    designFilters,
    analyseData,
)

signal, fs = load(
    True,
    "./validations/loudness_zwicker/data/ISO_532-1/Test signal 5 (pinknoise 60 dB).wav",
    calib=2 * 2 ** 0.5,
)
spec_third, third_axis = oct3spec(signal, fs)
plt.semilogx(third_axis, spec_third, label="oct3spec")

f_dict = getFrequencies(24, 12600, 3)
filters = designFilters(f_dict, fs, plot=False)
rmsData = analyseData(filters, signal, f_dict, plot=False)
spec_dB = 20 * np.log10((rmsData) / (2 * 10 ** -5))

plt.semilogx(third_axis, spec_dB, label="noctfilter")
plt.show()
pass