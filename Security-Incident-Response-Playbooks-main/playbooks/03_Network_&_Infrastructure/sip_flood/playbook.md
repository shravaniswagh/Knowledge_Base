# SIP/VoIP DDoS Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `INVITE_FLOOD`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_sip_flood.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Gateway Filter.
- [ ] Verify that no new instances of the `INVITE_FLOOD` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `INVITE_FLOOD` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `sip_flood` incident timeline.
- [ ] Improve detection rules for future occurrences.
