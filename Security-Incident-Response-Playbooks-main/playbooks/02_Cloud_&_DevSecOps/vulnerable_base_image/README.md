# Vulnerable Base Image Incident Response

This playbook provides step-by-step instructions for responding to a Vulnerable Base Image incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Vulnerable Base Image incident (`playbooks/02_Cloud_&_DevSecOps/vulnerable_base_image/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"CVE-CRITICAL"** string.
- **Automation Purpose**: Update Dockerfile Version.

## Run the Detection Script

- `detect_vulnerable_base_image.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the vulnerable_base_image playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/vulnerable_base_image
    ```
- Run the provided script:
    ```bash
    python scripts/detect_vulnerable_base_image.py
    ```
