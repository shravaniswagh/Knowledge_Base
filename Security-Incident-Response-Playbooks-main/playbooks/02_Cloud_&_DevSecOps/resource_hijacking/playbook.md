# Resource Hijacking Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `UNAUTHORIZED_CPU`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_resource_hijacking.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Clean Assets.
- [ ] Verify that no new instances of the `UNAUTHORIZED_CPU` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `UNAUTHORIZED_CPU` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `resource_hijacking` incident timeline.
- [ ] Improve detection rules for future occurrences.
