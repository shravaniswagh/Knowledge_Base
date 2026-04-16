# Insider Threat Incident Response

This playbook provides step-by-step instructions for responding to a Insider Threat incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Insider Threat incident (`playbooks/04_Identity_&_Governance/insider_threat/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"AFTER_HOURS_ACCESS"** string.
- **Automation Purpose**: Lock Internal Accounts.

## Run the Detection Script

- `detect_insider_threat.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the insider_threat playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/insider_threat
    ```
- Run the provided script:
    ```bash
    python scripts/detect_insider_threat.py
    ```
