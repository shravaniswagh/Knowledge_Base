# AI Prompt Injection Incident Response

This playbook provides step-by-step instructions for responding to a AI Prompt Injection incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a AI Prompt Injection incident (`playbooks/04_Identity_&_Governance/prompt_injection/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"LLM_OVERRIDE_SYSTEM"** string.
- **Automation Purpose**: Update AI Guardrails.

## Run the Detection Script

- `detect_prompt_injection.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the prompt_injection playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/prompt_injection
    ```
- Run the provided script:
    ```bash
    python scripts/detect_prompt_injection.py
    ```
