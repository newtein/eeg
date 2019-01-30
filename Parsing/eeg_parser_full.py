"""
-------------------------------------------
Parser for Alcoholic EEG Dataset
-------------------------------------------
Pickled data tables stored in alcoholDb with .pkl extension
------------------------------------------
Written by : Himanshu Rajmane
------------------------------------------
"""

import os
import sys
import pickle as pk

pickle_dir = './alcoholDbFull'
if(not os.path.isdir(pickle_dir)):
    os.mkdir(pickle_dir)

# Default folder is set to the name of the smaller dataset, other folder names can be passed as a list
def list_dir(folder = ['eeg_full']):
    for fol in folder:
        root = fol
        subfolders = os.listdir(root)
        subfolders.sort()
        for subl in subfolders:
            branch = root + '/' + subl 
            files = os.listdir(branch)
            files.sort()
            for file in  files:
                node = branch + '/' + file 
                print(node)
                df = open(node).read().splitlines()
                table = {}
                for row in df:
                    if row.startswith("# S"):
                        line = row.split(' ')
                        case = line[1]
                        match = line[2].strip(',')
                        error = line[3]
                    if not row.startswith("#") and error != 'err':
                        row = row.split(' ')
                        table[row[1]] = []
                for row in df:
                    if not row.startswith("#") and error != 'err':
                        row = row.split(' ')
                        table[row[1]].append(float(row[3]))
                if error != 'err':
                    aachar = open(pickle_dir + '/' + file[0:-7] + "_" + case + '_' + match + "_trial_" + file[-3:] + ".pkl", 'wb')
                    pk.dump(table, aachar)    
                    aachar.close()
                else:
                    print("skipped error file: ", file)
                
list_dir()