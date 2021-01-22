#import pylab as plt
import matplotlib.pyplot as plt
import acoular as ac
from os import path
import matplotlib.image as mpimg
import numpy as np

sol = "4mic_solalt.h5"
sag = "4mic_sagust.h5"
orta= "4mic_orta.h5"
sol2 = "sol_ust_ses_20_01.h5"
sag2= "sag_alt_ses_20_01.h5"

micgeofile = path.join(path.split(ac.__file__)[0],'xml','array_4_2.xml')
m = ac.MicGeom(from_file=micgeofile)
g = ac.RectGrid( x_min=-4, x_max=4, y_min=-2, y_max=2, z=0.3, increment=0.01)
t1 = ac.TimeSamples(name=sag2)
cal = ac.Calib(from_file='calibration.xml')
es = ac.EigSpectra(time_data=t1, block_size=512, window="Hanning", overlap='50%', calib=cal)
bb = ac.BeamformerBase(freq_data=es, grid=g, mpos=m, r_diag=False)



Lm = ac.L_p(bb.synthetic(500,0))
"""
plt.figure()
plt.imshow( Lm.T, origin='lower', vmin=Lm.max()-10, extent=g.extend(), interpolation='bicubic')


"""



img = plt.imshow( Lm.T, origin='lower', vmin=Lm.max()-10, extent=g.extend(), interpolation='bicubic')
plt.axis('off')

#plt.savefig("test.png", bbox_inches='tight')

plt.colorbar()

