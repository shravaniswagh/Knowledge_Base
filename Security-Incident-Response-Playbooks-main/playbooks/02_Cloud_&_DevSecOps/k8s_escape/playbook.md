# K8s Pod Escape Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `HOST_MOUNT`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_k8s_escape.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Apply PSP.
- [ ] Verify that no new instances of the `HOST_MOUNT` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `HOST_MOUNT` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `k8s_escape` incident timeline.
- [ ] Improve detection rules for future occurrences.
