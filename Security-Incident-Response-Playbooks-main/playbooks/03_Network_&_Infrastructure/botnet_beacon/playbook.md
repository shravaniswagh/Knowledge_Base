# Botnet Heartbeat Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `C2_BEACON`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_botnet_beacon.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Isolate host.
- [ ] Verify that no new instances of the `C2_BEACON` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `C2_BEACON` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `botnet_beacon` incident timeline.
- [ ] Improve detection rules for future occurrences.
