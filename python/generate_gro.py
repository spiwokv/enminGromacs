#!/usr/bin/python

import sys, math

ifile = open( sys.argv[1], "r").readlines()
chain = sys.argv[2]
data = []

atomtypes = ["CA"]

for line in ifile:
  if line[0:4] == "ATOM":
    if (line[21] == chain) or (chain=="all"):
      if str.split(line[12:16])[0] in atomtypes:
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        data.append([x,y,z])

ofile = open("structure.gro","w")
ofile.write("generated from %s\n" % sys.argv[1])
ofile.write("%6i\n" %  len(data))

for i in range(len(data)):
  line = data[i]
  x = 0.1*line[0]
  y = 0.1*line[1]
  z = 0.1*line[2]
  ofile.write(" %4iXXX    CA %5i%8.3f%8.3f%8.3f\n" % (i+1, i+1,x,y,z))
ofile.write("  10.00000  10.00000  10.00000\n")
ofile.close()

