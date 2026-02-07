# Pod Alerting with Retries and Backoff

This repository demonstrates pod alerting logic with retry and backoff mechanisms to improve reliability when handling transient failures during pod status evaluation.

## What this repo shows
- Clear pod severity classification logic
- Retry and backoff handling for transient failures
- Separation of concerns (logic vs orchestration)
- Unit testing of failure and success paths

## What this repo does NOT try to be
- A full Kubernetes monitoring system
- A production-ready alerting platform
- A CLI or long-running service

The goal is to demonstrate reliability-aware control flow in Python, suitable for platform engineering workflows.

## How to run
```bash
python run.py
