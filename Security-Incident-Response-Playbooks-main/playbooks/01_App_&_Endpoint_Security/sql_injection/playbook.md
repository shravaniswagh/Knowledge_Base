# SQL Injection Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `' OR 1=1 --`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_sql_injection.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: WAF SQLi Blocking.
- [ ] Verify that no new instances of the `' OR 1=1 --` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `' OR 1=1 --` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `sql_injection` incident timeline.
- [ ] Improve detection rules for future occurrences.
