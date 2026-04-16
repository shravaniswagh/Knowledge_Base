# API Key Exposure Incident Response

This playbook provides step-by-step instructions for responding to a API Key Exposure incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a API Key Exposure incident (`playbooks/02_Cloud_&_DevSecOps/api_key_leak/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"AKIA"** string.
- **Automation Purpose**: Revoke API Keys.

## Run the Detection Script

- `detect_api_key_leak.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the api_key_leak playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/api_key_leak
    ```
- Run the provided script:
    ```bash
    python scripts/detect_api_key_leak.py
    ```
