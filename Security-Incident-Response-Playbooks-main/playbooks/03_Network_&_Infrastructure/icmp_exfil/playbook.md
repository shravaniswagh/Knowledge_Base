# ICMP Exfiltration Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `DATA_IN_PING`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_icmp_exfil.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Rate Limit ICMP.
- [ ] Verify that no new instances of the `DATA_IN_PING` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `DATA_IN_PING` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `icmp_exfil` incident timeline.
- [ ] Improve detection rules for future occurrences.
