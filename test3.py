import time
#using subprocess module for runnig shell scripts
import subprocess
import os
import shlex   #makes it easy to pass arguments to shell functions

pdb_file = 'antibody.pdb'  #change this to system output using os package
args = 'SequenceOnly '
command_string = './foldx --command=' + args + '--pdb=' + pdb_file

###  foldx command tutorial (official manual useless) at
### https://evosite3d.blogspot.com/2016/04/tutorial-estimating-stability-effect-of.html

subprocess.call(shlex.split(command_string))   # Runs the foldx script