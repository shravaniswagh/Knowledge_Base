# Data Integrity Failure Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `CHECKSUM_ERROR`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_data_corruption.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Consistency Check.
- [ ] Verify that no new instances of the `CHECKSUM_ERROR` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `CHECKSUM_ERROR` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `data_corruption` incident timeline.
- [ ] Improve detection rules for future occurrences.
