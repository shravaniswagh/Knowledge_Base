# IPv6 RA Flood Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `IPV6_RA_ANOMALY`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_ipv6_ra_flood.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Enable RA Guard.
- [ ] Verify that no new instances of the `IPV6_RA_ANOMALY` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `IPV6_RA_ANOMALY` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `ipv6_ra_flood` incident timeline.
- [ ] Improve detection rules for future occurrences.
