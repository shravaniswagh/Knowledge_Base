# Keylogger Discovery Incident Response

This playbook provides step-by-step instructions for responding to a Keylogger Discovery incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Keylogger Discovery incident (`playbooks/01_App_&_Endpoint_Security/keylogger_discovery/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"KEY_LOG_SAVED"** string.
- **Automation Purpose**: Remove Keylogger Hook.

## Run the Detection Script

- `detect_keylogger_discovery.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the keylogger_discovery playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/keylogger_discovery
    ```
- Run the provided script:
    ```bash
    python scripts/detect_keylogger_discovery.py
    ```
