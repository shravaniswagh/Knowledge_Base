# Cert Pinning Bypass Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `FRIDA_DETECTED`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_mobile_cert_pinning.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Kill Process.
- [ ] Verify that no new instances of the `FRIDA_DETECTED` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `FRIDA_DETECTED` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `mobile_cert_pinning` incident timeline.
- [ ] Improve detection rules for future occurrences.
