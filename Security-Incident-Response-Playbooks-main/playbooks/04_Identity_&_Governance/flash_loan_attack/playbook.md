# Blockchain Flash Loan Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `ORACLE_MISMATCH`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_flash_loan_attack.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Oracle Safeguard.
- [ ] Verify that no new instances of the `ORACLE_MISMATCH` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `ORACLE_MISMATCH` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `flash_loan_attack` incident timeline.
- [ ] Improve detection rules for future occurrences.
