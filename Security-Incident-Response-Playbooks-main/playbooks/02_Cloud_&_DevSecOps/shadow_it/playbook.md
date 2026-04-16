# Shadow IT Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `UNSANCTIONED_APP`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_shadow_it.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Block SaaS.
- [ ] Verify that no new instances of the `UNSANCTIONED_APP` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `UNSANCTIONED_APP` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `shadow_it` incident timeline.
- [ ] Improve detection rules for future occurrences.
