# Rogue VPN Access Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `UNAUTH_TUNNEL`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_rogue_vpn.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Revoke Certs.
- [ ] Verify that no new instances of the `UNAUTH_TUNNEL` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `UNAUTH_TUNNEL` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `rogue_vpn` incident timeline.
- [ ] Improve detection rules for future occurrences.
