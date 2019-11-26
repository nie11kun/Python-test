from subprocess import Popen, PIPE

site = 'https://niekun.net/index.php/2019/10/'
path = '/mnt/c/Users/HJ_NK/Documents/'

print('downloading')

cmd = 'cd .. && cd {} && sudo wget -m -p -k {}'.format(path, site)
#cmd = 'cd .. && pwd'
p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()
#it = iter(p[1].decode("utf-8").split('\n'))

try:
    file1 = open("file.txt", "w")
    #file1.write("{}\n".format(str(p[1], 'utf-8')))
    
    for line in p[1].decode("utf-8", 'ignore').split('\n'):
        file1.write("{}\n".format(line))
        if "FINISHED" in line: 
            print('finished')
    
finally:
    file1.close()
