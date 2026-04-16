# IAM Role Abuse Incident Response

This playbook provides step-by-step instructions for responding to a IAM Role Abuse incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a IAM Role Abuse incident (`playbooks/02_Cloud_&_DevSecOps/iam_abuse/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"IAM_PRIV_ESC"** string.
- **Automation Purpose**: Revoke IAM Roles.

## Run the Detection Script

- `detect_iam_abuse.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the iam_abuse playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/iam_abuse
    ```
- Run the provided script:
    ```bash
    python scripts/detect_iam_abuse.py
    ```
