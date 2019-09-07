import numpy as np
import os

os.chdir('../temp/')
names = np.genfromtxt('../topcat/FINAL_LIST.csv', delimiter=',', usecols=[3], skip_header=1, dtype=str)
other_data = np.genfromtxt('../topcat/FINAL_LIST.csv', delimiter=',', usecols=[0, 2, 8], skip_header=1)
depth, duration, mag = other_data.T

for n in range(len(names)):
    file = '{0}.utc'.format(names[n])

    print(file)
    transits = np.loadtxt(file, dtype=str)
    az, alt, time = transits.T
    az = az.astype(float)
    alt = alt.astype(float)

    for i in range(len(az)):
        if alt[i] >= 40:
            print('{2}  {0:6.3f}  {1:5.3f}  {3:4.4f}  {4:3.2f}  {5:4.3f}'.format(
                az[i], alt[i], time[i], depth[n], duration[n], mag[n]))

    print()

os.chdir('..')
os.system('rm -Rf temp/')
