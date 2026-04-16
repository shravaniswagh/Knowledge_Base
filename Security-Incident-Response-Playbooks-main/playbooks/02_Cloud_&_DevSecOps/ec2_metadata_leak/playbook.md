# EC2 Metadata Leak Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `METADATA_REQUEST`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_ec2_metadata_leak.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Enforce IMDSv2.
- [ ] Verify that no new instances of the `METADATA_REQUEST` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `METADATA_REQUEST` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `ec2_metadata_leak` incident timeline.
- [ ] Improve detection rules for future occurrences.
