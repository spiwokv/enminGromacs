# ENM in Gromacs

This is a set of experimental scripts for Elastic Network Model MD in Gromacs.

To get Gromacs coordinates:
```bash
./generate_gro.py protein.pdb A
```
for chain A or:
```bash
./generate_gro.py protein.pdb all
```
for all chains.

To get Gromacs topology:
```bash
./generate_top2.py protein.pdb A
```
for chain A or:
```bash
./generate_top2.py protein.pdb all
```
for all chains.

Next try with `mdp` files provided.

