# Vulnerable Image Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `CVE-CRITICAL`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_vulnerable_base_image.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Update Version.
- [ ] Verify that no new instances of the `CVE-CRITICAL` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `CVE-CRITICAL` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `vulnerable_base_image` incident timeline.
- [ ] Improve detection rules for future occurrences.
