# vim: tabstop=2 shiftwidth=2 softtabstop=2 expandtab autoindent smarttab
from manipulator import *
import random 


# sv_swarm

def testInteger():
  name = 'int1'
  pmin = -10 
  pmax = 10
  # vals = [random.randint(1, 100) for i in range(pmin, pmax+1)]
  p = IntegerParameter(name, pmin, pmax)
  v = -10
  pos = {name:0}
  gb = {name:4}
  lb = {name:9}
  p.sv_swarm(pos, gb, lb, 0.5, 0.3, 0.3, v)


def testBoolean():
  name = 'bool1'
  p = BooleanParameter(name)
  v = 0 
  pos = {name:0}
  gb = {name:1}
  lb = {name:0}
  p.sv_swarm(pos, gb, lb, 0.5, 0.3, 0.3)

def testPermutation():
  name = 'perm1'
  p = PermutationParameter(name, range(10))
  pos = {name: [7,3,1,4,2,5,8, 0,9,6]}
  gb = {name: [3,1,4,2,5,7,8,6,9,0]}
  lb = {name: [3,1,4,7,5,2,8, 0,9,6]}
  p.sv_swarm(pos, gb, lb, 0, 0.5, 0.5, 'CX')
  print pos

def testBooleanArray():
  name = 'BA'
  p = BooleanArray(name, 8)
  pos = {name: [1,0,0,1,0,0,1,1]}
  gb = {name: [1,0,0,0,0,0,0,0,]}
  lb = {name: [1,0,0,1,0,1,1,0]}
 # p.sv_swarm(pos, fb, lb, 0.5, 0.3, 0.3)
 # p.sv_swarm_parallel(pos, fb, lb, 0.5, 0.3, 0.3)
  p.sv_cross(pos, gb, lb, 'OX1', 0.5)
  print pos

def testFloatArray():
  pass 


testBooleanArray()

