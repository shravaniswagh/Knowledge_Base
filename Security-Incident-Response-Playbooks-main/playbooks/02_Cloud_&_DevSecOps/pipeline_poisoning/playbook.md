# Pipeline Poisoning Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `RUNNER_INJECTION`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_pipeline_poisoning.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Harden Runner.
- [ ] Verify that no new instances of the `RUNNER_INJECTION` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `RUNNER_INJECTION` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `pipeline_poisoning` incident timeline.
- [ ] Improve detection rules for future occurrences.
