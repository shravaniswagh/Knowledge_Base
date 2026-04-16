# DDoS Attack Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `FLOOD`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_ddos_attack.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Rate Limiting.
- [ ] Verify that no new instances of the `FLOOD` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `FLOOD` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `ddos_attack` incident timeline.
- [ ] Improve detection rules for future occurrences.
