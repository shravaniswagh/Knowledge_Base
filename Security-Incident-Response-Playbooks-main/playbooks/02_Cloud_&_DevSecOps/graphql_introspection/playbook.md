# GraphQL Abuse Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `__SCHEMA`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_graphql_introspection.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Disable Schema.
- [ ] Verify that no new instances of the `__SCHEMA` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `__SCHEMA` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `graphql_introspection` incident timeline.
- [ ] Improve detection rules for future occurrences.
