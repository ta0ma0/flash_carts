import subprocess
import configparser
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", type=str,
                    help="filename dictionary")
args = parser.parse_args()
file_ = args.file

config = configparser.ConfigParser()
config.read('config.py')
# path = config['DICT']['path']
timeout = int(config['TIMEFLASH']['flash_timeout'])
interval = int(config['TIMEFLASH']['interval'])
stack = int(config['STACKWORDS']['count'])



def iter_stack():
    end_list = all_list
    count = 0
    subprocess.call(['notify-send', 'GO!', 'English flash cards', '-t', '1'])
    time.sleep(5)
    for el in end_list:
        subprocess.call(['notify-send', el[0], el[1]])
        time.sleep(interval)
        count += 1
        if len(end_list) == count:
            subprocess.call(['notify-send', 'End', 'Dict is empty'])
    


all_list = []
with open(file_, 'r') as dict:
    iteration = range(stack)
    for _ in iteration:
        line = dict.readline()
        list = line.split(';')[0:2]
        all_list.append(list)

while True:
    iter_stack()
        


