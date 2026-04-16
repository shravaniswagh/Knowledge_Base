# Blockchain Reentrancy Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `CONTRACT_LOOP`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_reentrancy_attack.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Pause Contract.
- [ ] Verify that no new instances of the `CONTRACT_LOOP` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `CONTRACT_LOOP` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `reentrancy_attack` incident timeline.
- [ ] Improve detection rules for future occurrences.
