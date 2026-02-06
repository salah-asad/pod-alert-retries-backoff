import logging
#logging configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
def log_pod(severity, pod):
    if severity == Severity.ESCALATE:
        logging.error(f"Pod {pod['name']} is escalated.")
    elif severity == Severity.INVESTIGATE:
        logging.warning(f"Pod {pod['name']} needs investigation.")
    elif severity == Severity.IGNORE:
        logging.info(f"Pod {pod['name']} is ignored.")
    else:
        logging.info(f"Pod {pod['name']} is healthy.")


