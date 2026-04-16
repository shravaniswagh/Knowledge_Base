# GDPR/PII Data Leak Incident Response

This playbook provides step-by-step instructions for responding to a GDPR/PII Data Leak incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a GDPR/PII Data Leak incident (`playbooks/04_Identity_&_Governance/gdpr_data_leak/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"PII_FOUND"** string.
- **Automation Purpose**: Redact Data Logs.

## Run the Detection Script

- `detect_gdpr_data_leak.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the gdpr_data_leak playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/gdpr_data_leak
    ```
- Run the provided script:
    ```bash
    python scripts/detect_gdpr_data_leak.py
    ```
