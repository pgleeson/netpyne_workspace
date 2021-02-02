
import sys
import pprint as pp

if '-nogui' in sys.argv:
    import netpyne
    netpyne.__gui__ = False

from hnn_simple import netParams, simConfig

for pop_id in netParams.popParams:
    pop = netParams.popParams[pop_id]
    pop['numCells']=1
    pop['gridSpacing']=None
    pop['yRange']=None

netParams.popParams['L2Basket']['cellsList'] = [{'x': 0, 'y': 0, 'z': 0}]
netParams.popParams['L2Pyr']['cellsList'] = [{'x': 100, 'y': 0, 'z': 0}]
netParams.popParams['L5Basket']['cellsList'] = [{'x': 200, 'y': 0, 'z': 0}]
netParams.popParams['L5Pyr']['cellsList'] = [{'x': 300, 'y': 0, 'z': 0}]
netParams.connParams = {}
del netParams.popParams['L2Pyr']
del netParams.popParams['L5Basket']
del netParams.popParams['L5Pyr']

for pop_id in list(netParams.popParams.keys())[:1]:
    netParams.stimSourceParams['Input_%s'%pop_id] = {'type': 'IClamp', 'del': 10, 'dur': 80, 'amp': 0.6}
    netParams.stimSourceParams['Input_%s_hyp'%pop_id] = {'type': 'IClamp', 'del': 110, 'dur': 80, 'amp': -0.2}
    netParams.stimTargetParams['Input_%s_targ'%pop_id] = {'source': 'Input_%s'%pop_id, 'sec':'soma', 'loc': 0.5, 'conds': {'pop':pop_id, 'cellList': range(1)}}
    netParams.stimTargetParams['Input_%s_hyp_targ'%pop_id] = {'source': 'Input_%s_hyp'%pop_id, 'sec':'soma', 'loc': 0.5, 'conds': {'pop':pop_id, 'cellList': range(1)}}

simConfig.saveDat = True
simConfig.analysis = {}
simConfig.duration = 220
pp.pprint(simConfig.todict())
pp.pprint(netParams.todict())

from netpyne import sim  # import netpyne sim module

if '-export' in sys.argv:

    sim.createExportNeuroML2(netParams = netParams,
                           simConfig = simConfig,
                           reference = 'HNN_pulse')  # create and export network to NeuroML 2
else:
    sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)  # create and simulate network

print('Done!')
