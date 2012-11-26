from system.pipeline import get_components
# get_components() returns a tuple with component names.
# The following code is assumed:
# def get_components():
#     return ('loader', 'processor', 'collector')

alarms = {}
components = get_components()

for i in range(len(components)):
    alarms[components[i]] = {'monitors': ['throughput'],
        'suppression': 'cruncher.suppressions.pipeline.maintenance',
        'threshold': {'datapoints': 3,
                      'lower': 1,
                      'percentile': 5,
                      'trigger': 'below',
                      'upper': '100'},
        'ticket': {'description': components[i] + ' is unexpectedly slow.',
                   'destination': 'team ' + components[i],
                   'impact': 2,
                   'title': components[i] + ' has stopped.'},
        'timeseries': {'dimensions': {'component': components[i]},
                        'metric': 'processed_items',
                        'summary stat': 'sum'}}
    if i:
        alarms[components[i]]['suppression'] += \
            ' OR cruncher.pipeline.%s.throughput' % components[i-1]
print alarms
