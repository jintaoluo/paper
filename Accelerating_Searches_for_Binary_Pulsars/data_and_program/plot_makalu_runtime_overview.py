import numpy as np
#import pylab as plt
from matplotlib import pyplot as plt

from numpy import genfromtxt

bench_data = genfromtxt('data.txt', delimiter=',')




#--------------------------------------------------
#plt.figure(1)
fig, ax = plt.subplots()
#plt.plot( np.log2(bench_data[ 0:8, 0 ]), np.log10(bench_data[ 0:8, 1 ]), '-o',ms=4, lw=1, alpha=1.0, mfc='orange')
#plt.plot( np.log2(bench_data[ 0:8, 0 ]), np.log10(bench_data[ 0:8, 2 ]), '-o',ms=4, lw=1, alpha=1.0, mfc='green')
ax.plot( bench_data[ 0:8, 0 ], bench_data[ 0:8, 1 ], '-o')
ax.plot( bench_data[ 0:8, 0 ], bench_data[ 0:8, 2 ], '-o')
ax.set_xscale('log', basex=2)
ax.set_yscale('log', basex=10)
plt.xlim(4,2048)
plt.xlabel('Number of data points (10e6)')
plt.ylabel('Run Time (s)')
plt.legend(['Intel Xeon E5-1650 3.20GHz', 'Nvidia GTX 780'], loc='upper left', shadow=False)
#plt.legend(['Intel Xeon E5-1650 3.20GHz', 'Nvidia GTX780'], loc='upper left', shadow=True)
plt.grid()
plt.savefig('makalu_runtime_overview.eps')



plt.show()