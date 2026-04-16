# Azure Blob Misconfig Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `BLOB_ANONYMOUS`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_azure_blob_exposure.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Secure Container.
- [ ] Verify that no new instances of the `BLOB_ANONYMOUS` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `BLOB_ANONYMOUS` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `azure_blob_exposure` incident timeline.
- [ ] Improve detection rules for future occurrences.
