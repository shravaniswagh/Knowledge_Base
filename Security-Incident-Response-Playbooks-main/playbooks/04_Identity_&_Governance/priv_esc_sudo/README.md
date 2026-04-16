# Privilege Escalation Incident Response

This playbook provides step-by-step instructions for responding to a Privilege Escalation incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Privilege Escalation incident (`playbooks/04_Identity_&_Governance/priv_esc_sudo/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"NOT_IN_SUDOERS"** string.
- **Automation Purpose**: Revoke Sudoers Access.

## Run the Detection Script

- `detect_priv_esc_sudo.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the priv_esc_sudo playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/priv_esc_sudo
    ```
- Run the provided script:
    ```bash
    python scripts/detect_priv_esc_sudo.py
    ```
