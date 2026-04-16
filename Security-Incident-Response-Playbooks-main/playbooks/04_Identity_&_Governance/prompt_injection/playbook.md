# AI Prompt Injection Incident Response Playbook

## Phase 1: Identification
- [ ] Monitor logs for: `LLM_SYSTEM_OVERRIDE`
- [ ] Verify event timestamp and source IP.
- [ ] Run `scripts/detect_prompt_injection.py` to confirm the footprint.

## Phase 2: Containment
- [ ] Isolate the affected systems or user sessions.
- [ ] **Technical Mitigation**: Update Guardrails.
- [ ] Verify that no new instances of the `LLM_SYSTEM_OVERRIDE` signature are appearing.

## Phase 3: Eradication
- [ ] Root cause analysis: Identify why the `LLM_SYSTEM_OVERRIDE` activity succeeded.
- [ ] Apply security patches or configuration changes.
- [ ] Use Ansible to automate the cleanup.

## Phase 4: Recovery
- [ ] Re-enable services in a monitored state.
- [ ] Verify functional integrity.

## Phase 5: Lessons Learned
- [ ] Review the `prompt_injection` incident timeline.
- [ ] Improve detection rules for future occurrences.
