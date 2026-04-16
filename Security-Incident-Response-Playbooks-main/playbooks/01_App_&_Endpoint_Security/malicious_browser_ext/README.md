# Malicious Browser Extension Incident Response

This playbook provides step-by-step instructions for responding to a Malicious Browser Extension incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Malicious Browser Extension incident (`playbooks/01_App_&_Endpoint_Security/malicious_browser_ext/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"EXTENSION_KEYLOG"** string.
- **Automation Purpose**: Remove Unsanctioned Extension.

## Run the Detection Script

- `detect_malicious_browser_ext.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the malicious_browser_ext playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/malicious_browser_ext
    ```
- Run the provided script:
    ```bash
    python scripts/detect_malicious_browser_ext.py
    ```
