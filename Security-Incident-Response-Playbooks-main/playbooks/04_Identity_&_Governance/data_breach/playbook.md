# Data Breach Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `SENSITIVE_DATA_EXFIL`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_data_breach.py` to confirm the footprint.

## Phase 2: Containment (STOP THE BLEEDING)
- [ ] **Isolate Compromised Systems**: Disconnect or move to quarantine VLAN.
- [ ] **Disable Accounts/Credentials**: Force password resets and revoke API tokens.
- [ ] **Technical Mitigation**: Block Malicious Perimeter IPs.
- [ ] **Preserve Evidence**: Forensic imaging and centralized log collection.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `SENSITIVE_DATA_EXFIL` activity occurred.
- [ ] Patch known vulnerabilities and harden configurations.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity for all restored systems.

## Phase 5: Lessons Learned
- [ ] Review the `data_breach` incident timeline.
- [ ] Improve detection rules for future occurrences.
