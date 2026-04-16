# Man-in-the-Middle Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `ARP_SPOOF`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_mitm_spoofing.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Enable Dynamic ARP.
- [ ] Verify that no new instances of the `ARP_SPOOF` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `ARP_SPOOF` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `mitm_spoofing` incident timeline.
- [ ] Improve detection rules for future occurrences.
