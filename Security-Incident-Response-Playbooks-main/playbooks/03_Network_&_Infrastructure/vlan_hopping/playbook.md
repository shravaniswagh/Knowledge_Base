# VLAN Hopping Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `TRUNK_ABUSE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_vlan_hopping.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Disable Trunking.
- [ ] Verify that no new instances of the `TRUNK_ABUSE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `TRUNK_ABUSE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `vlan_hopping` incident timeline.
- [ ] Improve detection rules for future occurrences.
