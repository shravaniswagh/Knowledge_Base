# Web Shell Detection Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `shell.php?cmd=`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_web_shell.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Removing Web Shells.
- [ ] Verify that no new instances of the `shell.php?cmd=` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `shell.php?cmd=` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `web_shell` incident timeline.
- [ ] Improve detection rules for future occurrences.
