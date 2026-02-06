from enum import Enum
#severity enum class
class Severity(Enum):
    OK="ok"
    INVESTIGATE="investigate"
    ESCALATE="escalate"
    IGNORE ="ignore"
#pods lists
pods=[{"name":"workerload", "status": "running", "restarts": 1}, 
     {"name": "app", "status": "running", "restarts": 5},
        {"name": "database", "status": "Error", "restarts": 7},
        {"name": "cache", "status": "running", "restarts": 0},
        {"name": "dummy", "status": "Error", "restarts": 3},
        {"name":"payments", "status": "CrashLoopbackOff", "restarts": 10},
        {"name":"logical", "status": "Error", "restarts": 2},{"name":"network-1", "status": "running", "restarts": 6}]
#pod status function
def pod_severity(pod):
    if pod.get("name","unknown") == "payments":
        return Severity.IGNORE
    if pod.get("status", "unknown") != "running":
        return Severity.ESCALATE
    if pod.get("restarts", 0) > 10:
        return Severity.ESCALATE
    if pod.get("restarts", 0) > 5:
        return Severity.INVESTIGATE
    return Severity.OK
