# Bluetooth Sniffing Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `BLE_SPOOF`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_bluetooth_sniff.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Faraday shield.
- [ ] Verify that no new instances of the `BLE_SPOOF` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `BLE_SPOOF` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `bluetooth_sniff` incident timeline.
- [ ] Improve detection rules for future occurrences.
