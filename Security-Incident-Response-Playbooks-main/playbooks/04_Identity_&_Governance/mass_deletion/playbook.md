# Mass File Deletion Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `MASS_DELETE_SIG`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_mass_deletion.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Restoration.
- [ ] Verify that no new instances of the `MASS_DELETE_SIG` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `MASS_DELETE_SIG` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `mass_deletion` incident timeline.
- [ ] Improve detection rules for future occurrences.
