# HIPAA Violation Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `PATIENT_PLAINTEXT`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_hipaa_violation.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Mask Data.
- [ ] Verify that no new instances of the `PATIENT_PLAINTEXT` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `PATIENT_PLAINTEXT` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `hipaa_violation` incident timeline.
- [ ] Improve detection rules for future occurrences.
