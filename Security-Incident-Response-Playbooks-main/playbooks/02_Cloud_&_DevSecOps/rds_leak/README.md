# RDS Database Leak Incident Response

This playbook provides step-by-step instructions for responding to a RDS Database Leak incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a RDS Database Leak incident (`playbooks/02_Cloud_&_DevSecOps/rds_leak/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"RDS_LOGS_PUBLIC"** string.
- **Automation Purpose**: Secure RDS Instance.

## Run the Detection Script

- `detect_rds_leak.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the rds_leak playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/rds_leak
    ```
- Run the provided script:
    ```bash
    python scripts/detect_rds_leak.py
    ```
