# RDS Database Leak Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `RDS_PUBLIC`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_rds_leak.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Secure RDS.
- [ ] Verify that no new instances of the `RDS_PUBLIC` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `RDS_PUBLIC` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `rds_leak` incident timeline.
- [ ] Improve detection rules for future occurrences.
