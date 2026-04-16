# Sensor Spoofing Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `ANOMALOUS_VALUE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_sensor_spoofing.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Zero Trust.
- [ ] Verify that no new instances of the `ANOMALOUS_VALUE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `ANOMALOUS_VALUE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `sensor_spoofing` incident timeline.
- [ ] Improve detection rules for future occurrences.
