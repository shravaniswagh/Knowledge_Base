# Subdomain Takeover Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `DEAD_CNAME`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_subdomain_takeover.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Remove DNS.
- [ ] Verify that no new instances of the `DEAD_CNAME` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `DEAD_CNAME` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `subdomain_takeover` incident timeline.
- [ ] Improve detection rules for future occurrences.
