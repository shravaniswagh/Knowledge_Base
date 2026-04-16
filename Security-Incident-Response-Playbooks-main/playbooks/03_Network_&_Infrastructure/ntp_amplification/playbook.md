# NTP Amplification Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `MON_GETLIST`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_ntp_amplification.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Secure NTP.
- [ ] Verify that no new instances of the `MON_GETLIST` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `MON_GETLIST` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `ntp_amplification` incident timeline.
- [ ] Improve detection rules for future occurrences.
