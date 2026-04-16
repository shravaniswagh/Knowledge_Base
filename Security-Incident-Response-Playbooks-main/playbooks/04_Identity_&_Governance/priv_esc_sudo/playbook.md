# Privilege Escalation Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `NOT_IN_SUDOERS`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_priv_esc_sudo.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Revoke Sudoers.
- [ ] Verify that no new instances of the `NOT_IN_SUDOERS` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `NOT_IN_SUDOERS` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `priv_esc_sudo` incident timeline.
- [ ] Improve detection rules for future occurrences.
