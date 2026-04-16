# Deep Link Exploit Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `UNAUTHORIZED_DEEP_LINK`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_mobile_deep_link.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Harden Link Handlers.
- [ ] Verify that no new instances of the `UNAUTHORIZED_DEEP_LINK` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `UNAUTHORIZED_DEEP_LINK` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `mobile_deep_link` incident timeline.
- [ ] Improve detection rules for future occurrences.
