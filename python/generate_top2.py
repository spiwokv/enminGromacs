#!/usr/bin/python

import sys, math

ifile = open( sys.argv[1], "r").readlines()
chain = sys.argv[2]
data = []
cut_off = 15.0
gamma = 418.0

atomtypes = ["CA"]

for line in ifile:
  if line[0:4] == "ATOM":
    if (line[21] == chain) or (chain == "all"):
      #print line,
      if str.split(line[12:16])[0] in atomtypes:
        #sline = str.split(line)
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        data.append([x,y,z])
if len(data) < 1:
  print "Chain "+chain+" in molecule "+sys.argv[1]+" does not contain any atoms, exiting"
  exit()

ofile = open("topology.top", "w")

ofile.write( "; built from "+sys.argv[1]+" on atoms: ")
for atomtype in atomtypes:
  ofile.write("%s " % atomtype)
ofile.write( "\n\n")
ofile.write( "[ defaults ]\n")
ofile.write( "; nbfunc        comb-rule       gen-pairs       fudgeLJ fudgeQQ\n")
ofile.write( "1               2               no              0.0     0.0\n\n")
ofile.write( "[ atomtypes ]\n")
ofile.write( ";name  bond_type    mass    charge   ptype          sigma      epsilon\n")
ofile.write( "X              X      0.0000  0.0000  A   0.00000e+00  0.00000e+00\n\n")
ofile.write( "[ moleculetype ]\n")
ofile.write( "; Name            nrexcl\n")
ofile.write( "protein           0\n\n")
ofile.write( "[ atoms ]\n")
ofile.write( ";   nr       type  resnr residue  atom   cgnr     charge       mass  typeB    chargeB\n")
for i in range(len(data)):
  ofile.write( "%4i         X   %4i    XXX    CA    %4i    0.00000   12.00000\n" % ( i+1, i+1, i+1))
ofile.write( "\n")
ofile.write( "#define gamma %f\n\n" % gamma)
ofile.write( "[ bonds ]\n")
#ofile.write( 
#ofile.write( "[ distance_restraints ]"
#ofile.write( "; ai aj type index type  low up1 up2 fac"

k = 1
for i in range(len(data)):
  for j in range(i):
    dist = 0.0
    dist = dist + (data[i][0]-data[j][0])*(data[i][0]-data[j][0])
    dist = dist + (data[i][1]-data[j][1])*(data[i][1]-data[j][1])
    dist = dist + (data[i][2]-data[j][2])*(data[i][2]-data[j][2])
    dist = math.sqrt(dist)
    if dist<cut_off:
      #ofile.write( "%5i%5i%5i%10i%5i%10.5f%10.5f%10.5f%7.3f" % (i+1, j+1, 1, k, 1, 0.0, 0.1*dist, 666.0, gamma)
      #ofile.write( "%5i%5i%5i%10.5f%20.3f" % (i+1, j+1, 1, 0.1*dist, gamma)
      ofile.write( "%5i%5i%5i%10.5f   gamma\n" % (i+1, j+1, 1, 0.1*dist))
    k = k + 1
ofile.write( "\n")
ofile.write( "[ pairs ]\n\n")
ofile.write( "[ angles ]\n\n")
ofile.write( "[ dihedrals ]\n\n")
ofile.write( "[ system ]\n")
ofile.write( "protein\n\n")
ofile.write( "[ molecules ]\n")
ofile.write( "; Compound        nmols\n")
ofile.write( "protein           1\n\n")
ofile.close()

