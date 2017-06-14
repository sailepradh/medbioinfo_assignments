#!/usr/bin/env python3
# -*- coding: utf-8 -*-

count=0
sequence=[]
with open('/Users/salendrapradh/Desktop/KTH_courses/Medbio/Applied_Bioinformatics/data/test.fastq','r') as f:
    for line in f:
        line=line.strip()
        if line.startswith('G') or line.startswith('A') or line.startswith('T') or line.startswith('C'):
            count = count+1
        if line.startswith('@'):
            sequence.append(line)
    print(count)
for element in sequence:
    print (element)
#### make the set for ATGC that would make it better 
#### theres is bug in the script as some lines could have @ starting with as well
