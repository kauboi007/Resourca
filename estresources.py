import qsharp
from qsharp_widgets import EstimateDetails

qsharp.init(project_root=".")
result = qsharp.estimate("mq.GRQ()")#qsharp code path

r = result 
print(f"Physical Qubits : {r['physicalCountsFormatted']['physicalQubits']}")
print(f"Runtime         : {r['physicalCountsFormatted']['runtime']}")
print(f"rQOPS           : {r['physicalCountsFormatted']['rqops']}")
print(f"Code Distance   : {r['logicalQubit']['codeDistance']}")
print(f"Logical Qubits  : {r['physicalCountsFormatted']['algorithmicLogicalQubits']}")
print(f"QEC Scheme      : {r['jobParams']['qecScheme']['name']}")