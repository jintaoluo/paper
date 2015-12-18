import numpy as np
#import pylab as plt
from matplotlib import pyplot as plt

from numpy import genfromtxt

bench_data = genfromtxt('data.txt', delimiter=',')

#--------------------------------------------------
fig, ax = plt.subplots()
ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 1 ], '-o')
ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 2 ], '-o')
ax.set_xscale('log', basex=2)
#ax.set_yscale('log', basex=10)
plt.xlim(4,2048)
plt.ylim(-1000,25000)
plt.xlabel('Data Points: 10E6 ')
plt.ylabel('Run Time : second')
plt.legend(['Xeon E5-1650@3.20GHz', 'Nvidia GTX780'], loc='upper left', shadow=True)
plt.grid()


#--------------------------------------------------
#plt.figure(1)
fig, ax = plt.subplots()
#plt.plot( np.log2(bench_data[ 8:16, 0 ]), np.log10(bench_data[ 8:16, 1 ]), '-o',ms=4, lw=1, alpha=1.0, mfc='orange')
#plt.plot( np.log2(bench_data[ 8:16, 0 ]), np.log10(bench_data[ 8:16, 2 ]), '-o',ms=4, lw=1, alpha=1.0, mfc='green')
ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 1 ], '-o')
ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 2 ], '-o')
ax.set_xscale('log', basex=2)
ax.set_yscale('log', basex=10)
plt.xlim(4,2048)
plt.xlabel('Data Points: 10E6 ')
plt.ylabel('Run Time : second')
plt.legend(['Xeon E5-1650@3.20GHz', 'Nvidia GTX780'], loc='upper left', shadow=True)
plt.grid()

#--------------------------------------------------
#plt.figure(2)
fig, ax = plt.subplots()
accel_makalu = bench_data[ 8:16, 1 ]/bench_data[ 8:16, 2 ]
plt.plot( bench_data[ 8:16, 0 ], accel_makalu, 'p-r')

accel_zuul = bench_data[ 8:14, 3 ]/bench_data[ 8:14, 4 ]
plt.plot( bench_data[ 8:14, 0 ], accel_zuul, 'p-g')

accel_sh = bench_data[ 8:16, 5 ]/bench_data[ 8:16, 6 ]
plt.plot( bench_data[ 8:16, 0 ], accel_sh, 'p-b')

ax.set_xscale('log', basex=2)
plt.xlim(4,2048)
plt.ylim(10,85)
plt.xlabel('Data Points: 10E6')
plt.ylabel('Acceleration: GPU on CPU')
plt.legend(['Xeon E5-1650@3.20GHz vs. GTX780', 'Xeon E5-2640@2.00GHz vs. GTX780', 'Xeon E5-2670@2.60GHz vs. GTX Titan'], loc='upper left', shadow=True)
plt.grid()

#--------------------------------------------------
fig, ax = plt.subplots()
mc, = ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 1 ], '-or' )
mg, = ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 2 ], '-or' )
zc, = ax.plot( bench_data[ 8:14, 0 ], bench_data[ 8:14, 3 ], '-og' )
zg, = ax.plot( bench_data[ 8:14, 0 ], bench_data[ 8:14, 4 ], '-og' )
sc, = ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 5 ], '-ob' )
sg, = ax.plot( bench_data[ 8:16, 0 ], bench_data[ 8:16, 6 ], '-ob' )

#plt.legend( (l1, l3, l5), ('M: 3.2GHz', 'z: 2.0GHz', 'sh: 2.6GHz'), 'upper left', shadow=True)
plt.legend( (mc, zc, sc), ('M: 3.2GHz + GTX780', 'z: 2.0GHz + GTX780', 'sh: 2.6GHz + GTX Titan'), 'lower right', shadow=True)

ax.set_xscale('log', basex=2)
ax.set_yscale('log', basex=10)
plt.xlim(4,2048)
plt.xlabel('Data Points: 10E6')


plt.show()