
import sys

if '-nogui' in sys.argv:
    import netpyne
    netpyne.__gui__ = False

from hnn_simple import netParams, simConfig

simConfig.verbose = True

from netpyne import sim  # import netpyne sim module

sim.createExportNeuroML2(netParams = netParams,
                       simConfig = simConfig,
                       reference = 'HNN')  # create and export network to NeuroML 2

print('Done!')
