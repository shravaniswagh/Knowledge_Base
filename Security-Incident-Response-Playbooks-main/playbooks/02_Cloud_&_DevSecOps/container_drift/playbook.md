# Container Runtime Drift Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `BINARY_MODIFIED`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_container_drift.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Terminate Pods.
- [ ] Verify that no new instances of the `BINARY_MODIFIED` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `BINARY_MODIFIED` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `container_drift` incident timeline.
- [ ] Improve detection rules for future occurrences.
