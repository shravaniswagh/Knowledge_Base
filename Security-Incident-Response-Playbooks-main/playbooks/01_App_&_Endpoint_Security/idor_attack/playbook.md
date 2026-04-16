# IDOR Attack Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `AUTH_BYPASS_ID`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_idor_attack.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Verify ID Ownership.
- [ ] Verify that no new instances of the `AUTH_BYPASS_ID` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `AUTH_BYPASS_ID` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `idor_attack` incident timeline.
- [ ] Improve detection rules for future occurrences.
