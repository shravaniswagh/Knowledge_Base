# Lambda Injection Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `FUNC_OVR_WRITE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_lambda_injection.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Apply Lambda IAM.
- [ ] Verify that no new instances of the `FUNC_OVR_WRITE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `FUNC_OVR_WRITE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `lambda_injection` incident timeline.
- [ ] Improve detection rules for future occurrences.
