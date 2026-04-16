# Dormant Account Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `OLD_ACTIVATE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_dormant_account.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Disable account.
- [ ] Verify that no new instances of the `OLD_ACTIVATE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `OLD_ACTIVATE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `dormant_account` incident timeline.
- [ ] Improve detection rules for future occurrences.
