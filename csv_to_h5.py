
from scipy.io import wavfile
import tables
import numpy as np
import pandas as pd
import h5py


from acoular import *
from pylab import *
arr= np.genfromtxt("sol_ust_ses_20_01_51k.csv", delimiter=";", skip_header=1)
sfreq=51200

ts = TimeSamples(data=arr)

ts.sample_freq=sfreq
ts.numsamples, ts.numchannels = ts.data.shape

hw=WriteH5(source=ts,name="")
hw.save()

