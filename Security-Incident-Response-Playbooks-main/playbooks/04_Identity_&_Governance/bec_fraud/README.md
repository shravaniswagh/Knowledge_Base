# Business Email Compromise Incident Response

This playbook provides step-by-step instructions for responding to a Business Email Compromise incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Business Email Compromise incident (`playbooks/04_Identity_&_Governance/bec_fraud/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"CEO_IMPERSONATE"** string.
- **Automation Purpose**: Enable External Flag.

## Run the Detection Script

- `detect_bec_fraud.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the bec_fraud playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/bec_fraud
    ```
- Run the provided script:
    ```bash
    python scripts/detect_bec_fraud.py
    ```
