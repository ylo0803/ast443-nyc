import os


os.chdir('../temp')
files = os.listdir('.')

for file in files:
    os.system('python ../rdj2aau.py {0} {0}.utc'.format(file))
