switch_buffers = {'VC0': [], 'VC1': [], 'VC2': [], 'VC3': []}

def process_traffic_endpoint1(endpoint, tc, data):
    if tc in [0, 1]:
        switch_buffers['VC0'].append((data, 'VC0', endpoint))
    elif tc == 2:
        switch_buffers['VC1'].append((data, 'VC1', endpoint))
    elif tc in [3, 4]:
        switch_buffers['VC2'].append((data, 'VC1', endpoint))
    elif tc == 5:
        switch_buffers['VC2'].append((data, 'VC2', endpoint))
    elif tc == 6:
        switch_buffers['VC2'].append((data, 'VC2', endpoint))
    elif tc == 7:
        switch_buffers['VC3'].append((data, 'VC3', endpoint))

def process_traffic_endpoint2(endpoint, tc, data):
    if tc in [0, 1]:
        switch_buffers['VC0'].append((data, 'VC0', endpoint))
    elif tc in [2, 3, 4]:
        switch_buffers['VC1'].append((data, 'VC1', endpoint))
    elif tc == 5:
        switch_buffers['VC2'].append((data, 'VC1', endpoint))
    elif tc == 6:
        switch_buffers['VC2'].append((data, 'VC1', endpoint))
    elif tc == 7:
        switch_buffers['VC2'].append((data, 'VC2', endpoint))

traffic_order = [
    ('Endpoint 1', 5, 'MEMWR'),
    ('Endpoint 2', 5, 'MEMRD'),
    ('Endpoint 1', 2, 'CFGWR'),
    ('Endpoint 2', 5, 'CFGRD'),
    ('Endpoint 1', 7, 'MEMWR'),
    ('Endpoint 2', 0, 'MEMWR')
]

for endpoint, tc, operation in traffic_order:
    if endpoint == 'Endpoint 1':
        process_traffic_endpoint1(endpoint, tc, operation)
    elif endpoint == 'Endpoint 2':
        process_traffic_endpoint2(endpoint, tc, operation)

vc0_traffic = sorted(switch_buffers['VC0'], key=lambda x: (x[1], x[0]))
vc1_traffic = sorted(switch_buffers['VC1'], key=lambda x: (x[1], x[0]))
vc2_traffic = sorted(switch_buffers['VC2'], key=lambda x: (x[1], x[0]))
vc3_traffic = sorted(switch_buffers['VC3'], key=lambda x: (x[1], x[0]))


print("Switch VC0-VC3 Content:")
print("VC\tTraffic")
print(f"VC0\t{vc0_traffic}")
print(f"VC1\t{vc1_traffic}")
print(f"VC2\t{vc2_traffic}")
print(f"VC3\t{vc3_traffic}")
