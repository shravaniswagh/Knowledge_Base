# GDPR Data Leak Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `PII_FOUND`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_gdpr_data_leak.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Redact Logs.
- [ ] Verify that no new instances of the `PII_FOUND` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `PII_FOUND` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `gdpr_data_leak` incident timeline.
- [ ] Improve detection rules for future occurrences.
