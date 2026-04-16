# Unauthorized Admin Creation Incident Response

This playbook provides step-by-step instructions for responding to a Unauthorized Admin Creation incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Unauthorized Admin Creation incident (`playbooks/04_Identity_&_Governance/unauthorized_admin/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"USER_ADDED_TO_ADMINS"** string.
- **Automation Purpose**: Revoke Admin Credentials.

## Run the Detection Script

- `detect_unauthorized_admin.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the unauthorized_admin playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/unauthorized_admin
    ```
- Run the provided script:
    ```bash
    python scripts/detect_unauthorized_admin.py
    ```
