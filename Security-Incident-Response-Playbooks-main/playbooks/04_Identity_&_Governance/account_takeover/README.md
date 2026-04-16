# Account Takeover (ATO) Incident Response

This playbook provides step-by-step instructions for responding to a Account Takeover (ATO) incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Account Takeover (ATO) incident (`playbooks/04_Identity_&_Governance/account_takeover/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"GEO_SHIFT"** string.
- **Automation Purpose**: Force Multi-Factor Reset.

## Run the Detection Script

- `detect_account_takeover.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the account_takeover playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/account_takeover
    ```
- Run the provided script:
    ```bash
    python scripts/detect_account_takeover.py
    ```
