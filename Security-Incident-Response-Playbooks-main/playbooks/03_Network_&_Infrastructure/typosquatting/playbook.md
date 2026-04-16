# Typosquatting Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `LOOK_ALIKE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_typosquatting.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Block Proxy.
- [ ] Verify that no new instances of the `LOOK_ALIKE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `LOOK_ALIKE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `typosquatting` incident timeline.
- [ ] Improve detection rules for future occurrences.
