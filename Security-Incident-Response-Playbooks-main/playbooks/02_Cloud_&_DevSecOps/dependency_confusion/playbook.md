# Dependency Confusion Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `PKG_MISMATCH`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_dependency_confusion.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Pin Private.
- [ ] Verify that no new instances of the `PKG_MISMATCH` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `PKG_MISMATCH` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `dependency_confusion` incident timeline.
- [ ] Improve detection rules for future occurrences.
