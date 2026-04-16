# VPC Peering Abuse Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `UNAUTHORIZED_PEER`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_vpc_peering_abuse.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Remove Peers.
- [ ] Verify that no new instances of the `UNAUTHORIZED_PEER` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `UNAUTHORIZED_PEER` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `vpc_peering_abuse` incident timeline.
- [ ] Improve detection rules for future occurrences.
