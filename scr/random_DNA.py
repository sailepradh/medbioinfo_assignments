#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, string
import sys

var = int(input("Length of DNA string: "))
def randDNA():
    print ("\n")
    print(">myrandomsequence")
    print (''.join(random.choice('ATGC') for x in range(var)))
    return

randDNA()

