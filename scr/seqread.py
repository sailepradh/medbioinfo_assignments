#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Usage = '''
seqread.py - version 1
Reads in file in fasta format into a list and a dictionary.

The resulting list is formatted as

[['name1', 'seq1seq1seq1seq1'],
 ['name2', 'seq2seq2seq2seq2']]


Usage:
    seq.read.py sequence.fasta'''



def complement(s):
    # returns complementary sequence
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)


def reverse(s):
    # reverse sequence
    txt = []
    for i in range(len(s) - 1, -1, -1):
        txt.append(s[i])
    return ''.join(txt)


def reversecomplement(s):
    # returns reverse complementary sequence
    s = reverse(s)
    s = complement(s)
    return s



import sys
from tranlation import translation

# Expects a filename as the argument

if len(sys.argv) < 2:
    print (Usage)
else:
    InfileName = sys.argv[1]
    Infile = open(InfileName, 'r')
    RecordNum = -1

    # Set up a blank list and blank dictionary

    Sequences = []
    SeqDict = {}

    for line in Infile:
        Line = line.strip()

        if Line[0] == '>':
            Name = Line[1:]
            Sequences.append([Name, ''])
            RecordNum += 1
            Seqkey = Name
            SeqDict[Seqkey] = ''

        else:
            if RecordNum > -1:
                Sequences[RecordNum][1] += Line
                SeqDict[Seqkey] += Line

    for Seq in Sequences:
        test = translation(reversecomplement(Seq[1].upper()))
        test2 = translation((Seq[1].upper()))
        names = Seq[0].split()
        #print (names[0])


        print (">"+Seq[0].split()[0]+"\n"+max(test,test2, key=len))
#print (Seq[0],":", (Seq[1].upper()))
#print (Seq[0],":", reversecomplement(Seq[1].upper()))

## close the file 
