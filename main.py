import re
import os



def time_format(line):
    matchobj = re.match(r'^\[00:', line, re.M | re.I)
    if matchobj:
        listt = list(line)
        listt[6]="."
        line= ''.join(listt)
        time = re.match(r'\[([0-9][0-9]):([0-9][0-9])\.([0-9][0-9])\]', line, re.M | re.I)
        microsecond = time[1]
        line=line.replace(line[1:3], time[2])
        line=line.replace(':' + line[4:6] + '.', ':' + time[3] + '.')
        line=line.replace('.' + line[7:9] + ']', '.' + microsecond + ']')
    return line




if __name__ == "__main__":
    with open('text.txt','r') as f:
        for line in f.readlines():
            print(line)