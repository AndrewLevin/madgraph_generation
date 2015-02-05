#!/bin/env python

import subprocess, sys, os, re, math

inputfilename=sys.argv[1]
outputfilename=sys.argv[2]

input_file = open(inputfilename)
output_file = open(outputfilename, 'w')

index=1

for line in input_file:

    if line == "      PARAMETER (             NCOMB=144)\n":
        output_file.write("      PARAMETER (             NCOMB=16)\n")
    elif "DATA (NHEL" in line:
        if line.split(',')[5] == " 0" and line.split(',')[6] == " 0":
            output_file.write(line.replace(line.split(',')[1],"  "+str(index)+")"))
            index=index+1
    else:
        output_file.write(line)

input_file.close()
output_file.close()
