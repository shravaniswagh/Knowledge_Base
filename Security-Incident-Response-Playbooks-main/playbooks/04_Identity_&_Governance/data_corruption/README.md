# Data Integrity Failure Incident Response

This playbook provides step-by-step instructions for responding to a Data Integrity Failure incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Data Integrity Failure incident (`playbooks/04_Identity_&_Governance/data_corruption/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"CHECKSUM_ERROR"** string.
- **Automation Purpose**: Database Consistency Check.

## Run the Detection Script

- `detect_data_corruption.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the data_corruption playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/data_corruption
    ```
- Run the provided script:
    ```bash
    python scripts/detect_data_corruption.py
    ```
