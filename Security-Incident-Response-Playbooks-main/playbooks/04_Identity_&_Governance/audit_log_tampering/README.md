# Audit Log Deletion Incident Response

This playbook provides step-by-step instructions for responding to a Audit Log Deletion incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Audit Log Deletion incident (`playbooks/04_Identity_&_Governance/audit_log_tampering/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"CLEAR_EVT_LOGS"** string.
- **Automation Purpose**: Restore Remote Offsite Log.

## Run the Detection Script

- `detect_audit_log_tampering.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the audit_log_tampering playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/audit_log_tampering
    ```
- Run the provided script:
    ```bash
    python scripts/detect_audit_log_tampering.py
    ```
