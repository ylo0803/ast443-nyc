import os


os.chdir('/home/nicholas/documents/schoolwork/ast443/lab1/temp/')
files = os.listdir('.')

for file in files:
    os.system('python ../rdj2aau.py {0} {0}.utc'.format(file))
