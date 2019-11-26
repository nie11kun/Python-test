import os
import glob

"""
filemain = 'abc.mp4'
extension = '.' + filemain.split('.')[1]

files = glob.glob('abc' + '*')

for file in files:
    cmd = 'mv ' + file + ' ' + file + extension
    os.system(cmd)
"""

arr = {'a':1, 'b':2, 'c':3}
for i in arr:
    print(arr.get(i))

a, b, c, d, e = range(5)
print(e)