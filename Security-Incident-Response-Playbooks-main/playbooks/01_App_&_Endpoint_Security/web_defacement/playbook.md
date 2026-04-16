# Web Defacement Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `HASH_MISMATCH`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_web_defacement.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Restore from Git.
- [ ] Verify that no new instances of the `HASH_MISMATCH` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `HASH_MISMATCH` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `web_defacement` incident timeline.
- [ ] Improve detection rules for future occurrences.
