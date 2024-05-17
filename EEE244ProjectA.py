# TC-VC mappings for Endpoint 1, Endpoint 2, and Switch
endpoint1_tc_vc_mapping = {
    "TC0": "VC0",
    "TC1": "VC0",
    "TC2": "VC1",
    "TC3": "VC1",
    "TC4": "VC1",
    "TC5": "VC2",
    "TC6": "VC2",
    "TC7": "VC3"}

endpoint2_tc_vc_mapping = {
    "TC0": "VC0",
    "TC1": "VC0",
    "TC2": "VC1",
    "TC3": "VC1",
    "TC4": "VC1",
    "TC5": "VC1",
    "TC6": "VC1",
    "TC7": "VC2"}

switch_tc_vc_mapping = {
    "TC0": "VC0",
    "TC1": "VC0",
    "TC2": "VC1",
    "TC3": "VC1",
    "TC4": "VC1",
    "TC5": "VC2",
    "TC6": "VC2",
    "TC7": "VC3"}

# Traffic arriving at the switch
traffic = [
    ("MEMWR", "TC5", "Endpoint 1"),
    ("MEMRD", "TC5", "Endpoint 2"),
    ("CFGWR", "TC2", "Endpoint 1"),
    ("CFGRD", "TC5", "Endpoint 2"),
    ("MEMWR", "TC7", "Endpoint 1"),
    ("MEMWR", "TC0", "Endpoint 2")
]

# Buffer dictionary for the switch VC0-VC3
switch_buffers = {
    "VC0": [],
    "VC1": [],
    "VC2": [],
    "VC3": []
}

# Process traffic and update switch buffers
for operation, tc, endpoint in traffic:
    if endpoint == "Endpoint 1":
        if tc in endpoint1_tc_vc_mapping:
            vc = endpoint1_tc_vc_mapping[tc]
    else:
        if tc in endpoint2_tc_vc_mapping:
            vc = endpoint2_tc_vc_mapping[tc]

    # Update switch buffers
    if tc in switch_tc_vc_mapping:
        switch_buffers[switch_tc_vc_mapping[tc]].append((operation, vc, endpoint))
    else:
        print(f"Warning: TC {tc} not mapped in switch TC-VC mapping.")

# Sort traffic VC
for vc, traffic_list in switch_buffers.items():
    switch_buffers[vc] = sorted(traffic_list, key=lambda x: x[0])

# Display switch buffers
print("Switch VC0-VC3 Content:")
print("VC\tTraffic")
for vc, traffic_list in switch_buffers.items():
    print(f"{vc}\t{traffic_list}")