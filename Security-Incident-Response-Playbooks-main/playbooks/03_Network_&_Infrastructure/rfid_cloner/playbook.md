# RFID Badge Cloner Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `DUPLICATE_BADGE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_rfid_cloner.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Disable Badge.
- [ ] Verify that no new instances of the `DUPLICATE_BADGE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `DUPLICATE_BADGE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `rfid_cloner` incident timeline.
- [ ] Improve detection rules for future occurrences.
