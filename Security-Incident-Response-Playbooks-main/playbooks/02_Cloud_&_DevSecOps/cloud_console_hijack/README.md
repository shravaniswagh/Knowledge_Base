# Cloud Console Hijack Incident Response

This playbook provides step-by-step instructions for responding to a Cloud Console Hijack incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Cloud Console Hijack incident (`playbooks/02_Cloud_&_DevSecOps/cloud_console_hijack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"IMDS_SSRF"** string.
- **Automation Purpose**: Force Multi-Factor Reset.

## Run the Detection Script

- `detect_cloud_console_hijack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the cloud_console_hijack playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/cloud_console_hijack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_cloud_console_hijack.py
    ```
