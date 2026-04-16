# CSRF Attack Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `ORIGIN_MISMATCH`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_csrf_attack.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Anti-CSRF Tokens.
- [ ] Verify that no new instances of the `ORIGIN_MISMATCH` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `ORIGIN_MISMATCH` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `csrf_attack` incident timeline.
- [ ] Improve detection rules for future occurrences.
