# Unauthorized Admin Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `USER_TO_ADMIN`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_unauthorized_admin.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Revoke Admin.
- [ ] Verify that no new instances of the `USER_TO_ADMIN` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `USER_TO_ADMIN` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `unauthorized_admin` incident timeline.
- [ ] Improve detection rules for future occurrences.
