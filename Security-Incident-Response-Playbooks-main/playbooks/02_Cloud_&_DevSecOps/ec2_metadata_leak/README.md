# EC2 Metadata Leak Incident Response

This playbook provides step-by-step instructions for responding to a EC2 Metadata Leak incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a EC2 Metadata Leak incident (`playbooks/02_Cloud_&_DevSecOps/ec2_metadata_leak/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"AWS_METADATA_REQUEST"** string.
- **Automation Purpose**: Enforce IMDSv2 Only.

## Run the Detection Script

- `detect_ec2_metadata_leak.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the ec2_metadata_leak playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/ec2_metadata_leak
    ```
- Run the provided script:
    ```bash
    python scripts/detect_ec2_metadata_leak.py
    ```
