# DNS Cache Poisoning Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `DNS_BAIL_OUT`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_dns_cache_poison.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Flush Cache.
- [ ] Verify that no new instances of the `DNS_BAIL_OUT` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `DNS_BAIL_OUT` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `dns_cache_poison` incident timeline.
- [ ] Improve detection rules for future occurrences.
