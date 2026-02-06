import pytest
from pod_alert.retry import fetch_with_retries, pod_severity, Severity,RetryFailedError


def test_retry_success_after_failures(monkeypatch):
    call_count = {"count": 0}
    monkeypatch.setattr("time.sleep", lambda x: None)  # Skip actual sleep for testing

    def flaky_function():
        if call_count["count"] < 2:
            call_count["count"] += 1
            raise RuntimeError("Temporary failure")
        return "Success"

    from pod_alert_with_retries import fetch_with_retries

    result = fetch_with_retries(flaky_function, retries=5, delay_between_retries=0)
    assert result == "Success"
    assert call_count["count"] == 2

    def test_pod_severity_escalate_on_error():
        pod = {"name": "test-pod", "status": "Error", "restarts": 0}
        severity = pod_severity(pod)
        assert severity == Severity.ESCALATE
      
    def test_retry_failure():
        def always_fail():
            raise RuntimeError("Permanent failure")
        with pytest.raises(RuntimeError, match="Operation failed after multiple retries"):
            fetch_with_retries(always_fail, retries=3, delay_between_retries=0)
