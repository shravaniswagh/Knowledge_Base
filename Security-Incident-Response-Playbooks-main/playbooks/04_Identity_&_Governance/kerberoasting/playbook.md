# Kerberoasting Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `TGS_RC4`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_kerberoasting.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Rotate AD Key.
- [ ] Verify that no new instances of the `TGS_RC4` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `TGS_RC4` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `kerberoasting` incident timeline.
- [ ] Improve detection rules for future occurrences.
