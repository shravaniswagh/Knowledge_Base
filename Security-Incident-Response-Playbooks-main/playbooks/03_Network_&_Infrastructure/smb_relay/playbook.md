# SMB Relay Attack Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `SMB_RELAY`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_smb_relay.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Enable Signing.
- [ ] Verify that no new instances of the `SMB_RELAY` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `SMB_RELAY` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `smb_relay` incident timeline.
- [ ] Improve detection rules for future occurrences.
