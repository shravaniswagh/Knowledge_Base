# Insider Threat Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `LOG_AFTER_HOURS`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_insider_threat.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Lock Internal.
- [ ] Verify that no new instances of the `LOG_AFTER_HOURS` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `LOG_AFTER_HOURS` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `insider_threat` incident timeline.
- [ ] Improve detection rules for future occurrences.
