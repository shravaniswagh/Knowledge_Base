# DNS Tunneling Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `DNS_TXT_EXFIL`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_dns_tunneling.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: DNS Filtering.
- [ ] Verify that no new instances of the `DNS_TXT_EXFIL` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `DNS_TXT_EXFIL` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `dns_tunneling` incident timeline.
- [ ] Improve detection rules for future occurrences.
