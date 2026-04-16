# PowerShell Bypass Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `-ExecutionPolicy Bypass`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_powershell_bypass.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Constrained Lang.
- [ ] Verify that no new instances of the `-ExecutionPolicy Bypass` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `-ExecutionPolicy Bypass` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `powershell_bypass` incident timeline.
- [ ] Improve detection rules for future occurrences.
