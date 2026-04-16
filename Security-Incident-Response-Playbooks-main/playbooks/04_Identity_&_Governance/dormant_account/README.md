# Dormant Account activity Incident Response

This playbook provides step-by-step instructions for responding to a Dormant Account activity incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Dormant Account activity incident (`playbooks/04_Identity_&_Governance/dormant_account/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"OLD_ACCOUNT_ACTIVATE"** string.
- **Automation Purpose**: Disable Inactive Accounts.

## Run the Detection Script

- `detect_dormant_account.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the dormant_account playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/dormant_account
    ```
- Run the provided script:
    ```bash
    python scripts/detect_dormant_account.py
    ```
