# Brute Force (Web) Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `401 Unauthorized`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_brute_force_web.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Fail2Ban Activation.
- [ ] Verify that no new instances of the `401 Unauthorized` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `401 Unauthorized` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `brute_force_web` incident timeline.
- [ ] Improve detection rules for future occurrences.
