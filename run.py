import logging

from pod_alert.retry import fetch_with_retries
from pod_alert.pod_severity import pod_severity
from pod_alert.alert import log_pod


logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

pods=[{"name":"workerload", "status": "running", "restarts": 1}, 
     {"name": "app", "status": "running", "restarts": 5},
        {"name": "database", "status": "Error", "restarts": 7},
        {"name": "cache", "status": "running", "restarts": 0},
        {"name": "dummy", "status": "Error", "restarts": 3},
        {"name":"payments", "status": "CrashLoopbackOff", "restarts": 10},
        {"name":"logical", "status": "Error", "restarts": 2},{"name":"network-1", "status": "running", "restarts": 6}]

def fetch_pod_data(pod):
    # Simulate transient failure
    if pod["name"] == "database":
        raise RuntimeError("API timeout")
    return pod

for pod in pods:
    try:
        fetched = fetch_with_retries(lambda p=pod: fetch_pod_data(p))
        severity = pod_severity(fetched)
        log_pod(severity, fetched)
    except Exception as e:
        logging.critical(f"Pod {pod['name']} failed after retries: {e}")
