# BEC Fraud Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `CEO_IMPERSONATE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_bec_fraud.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Enable Flag.
- [ ] Verify that no new instances of the `CEO_IMPERSONATE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `CEO_IMPERSONATE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `bec_fraud` incident timeline.
- [ ] Improve detection rules for future occurrences.
