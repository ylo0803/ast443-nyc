import numpy as np
import os

os.mkdir('../temp')
os.chdir('../temp/')
data = np.genfromtxt('../topcat/FINAL_LIST.csv', delimiter=',', usecols=[0, 2, 4, 5, 6, 7, 8], skip_header=1)
name = np.genfromtxt('../topcat/FINAL_LIST.csv', delimiter=',', usecols=[3], skip_header=1, dtype=str)
depth, duration, p0, midtime, ra, dec, mag = data.T

mjd = 2458730

print()
print('Files to be Created: ', len(name))

input('\nEnter: ')

for i in range(len(name)):
    print()

    midtimes_future = np.array([midtime[i]])
    n = 1
    while midtimes_future[-1] < mjd+33:
        midtimes_future = np.append(midtimes_future, midtime[i] + p0[i] * n)
        n += 1

    for n in range(len(midtimes_future)):
        if midtimes_future[n] > mjd:
            os.system('echo \"'+str(ra[i])+' '+str(dec[i])+' '+str(midtimes_future[n])+'\"'+' >> '+str(name[i]))
