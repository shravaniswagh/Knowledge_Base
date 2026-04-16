# AI Model Extraction Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `CLONING_PROBE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_model_extraction.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Rate Limit.
- [ ] Verify that no new instances of the `CLONING_PROBE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `CLONING_PROBE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `model_extraction` incident timeline.
- [ ] Improve detection rules for future occurrences.
