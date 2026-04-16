# Cloud Console Hijack Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `IMDS_SSRF`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_cloud_console_hijack.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Force MFA.
- [ ] Verify that no new instances of the `IMDS_SSRF` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `IMDS_SSRF` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `cloud_console_hijack` incident timeline.
- [ ] Improve detection rules for future occurrences.
