
import sys

if '-nogui' in sys.argv:
    import netpyne
    netpyne.__gui__ = False

from hnn_simple import netParams, simConfig

from netpyne import sim  # import netpyne sim module

sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)  # create and simulate network

print('Done!')
