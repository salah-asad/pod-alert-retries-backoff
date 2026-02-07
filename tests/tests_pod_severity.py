import unittest
import logging
logging.disable(logging.CRITICAL)
from pod_alert.pod_severity import pod_severity, Severity 

class TestPodAlerts(unittest.TestCase):
#test cases for pod severity function
 def test_ignore_payments_pod(self):
    payments_pod = {"name":"payments", "status": "CrashLoopbackOff", "restarts": 10}
    self.assertEqual(pod_severity(payments_pod), Severity.IGNORE)
 def test_escalate_unhealthy_pod(self):
    unhealthy_pod = {"name":"database", "status": "Error", "restarts": 7}
    self.assertEqual(pod_severity(unhealthy_pod), Severity.ESCALATE)
 def test_investigate_high_restarts(self):
    high_restart_pod = {"name":"network-1", "status": "running", "restarts": 6}
    self.assertEqual(pod_severity(high_restart_pod), Severity.INVESTIGATE)
 def test_escalate_very_high_restarts(self):
    very_high_restart_pod = {"name":"critical-service", "status": "running", "restarts": 11}
    self.assertEqual(pod_severity(very_high_restart_pod), Severity.ESCALATE)
 def test_ok_healthy_pod(self):
    healthy_pod = {"name":"app", "status": "running", "restarts": 2}
    self.assertEqual(pod_severity(healthy_pod), Severity.OK)
if __name__ == '__main__':
    unittest.main()
