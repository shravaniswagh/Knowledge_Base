# Pass-the-Hash Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `NTLM_ANOMALY`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_pass_the_hash.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: LSA Protection.
- [ ] Verify that no new instances of the `NTLM_ANOMALY` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `NTLM_ANOMALY` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `pass_the_hash` incident timeline.
- [ ] Improve detection rules for future occurrences.
