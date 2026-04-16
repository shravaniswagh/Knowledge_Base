# CloudTrail Disabling Incident Response

This playbook provides step-by-step instructions for responding to a CloudTrail Disabling incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a CloudTrail Disabling incident (`playbooks/02_Cloud_&_DevSecOps/cloudtrail_disabling/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"STOP_LOGGING"** string.
- **Automation Purpose**: Restore CloudTrail Hub.

## Run the Detection Script

- `detect_cloudtrail_disabling.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the cloudtrail_disabling playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/cloudtrail_disabling
    ```
- Run the provided script:
    ```bash
    python scripts/detect_cloudtrail_disabling.py
    ```
