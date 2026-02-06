import logging
import time

def fetch_with_retries(fn, retries=3, delay_between_retries=10):
    for attempt in range(retries):
        try:
            return fn()
        except Exception as e:
            logging.warning("Attempt %d/%d failed: %s", attempt + 1, retries, str(e))
            time.sleep(delay_between_retries*2**attempt)  # Exponential backoff
    raise RuntimeError("Operation failed after multiple retries")
