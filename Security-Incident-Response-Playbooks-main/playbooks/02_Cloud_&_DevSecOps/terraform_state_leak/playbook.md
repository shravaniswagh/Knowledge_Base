# TF State Exposure Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `TF_STATE_PUBLIC`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_terraform_state_leak.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Secure State.
- [ ] Verify that no new instances of the `TF_STATE_PUBLIC` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `TF_STATE_PUBLIC` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `terraform_state_leak` incident timeline.
- [ ] Improve detection rules for future occurrences.
