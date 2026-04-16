# Clipboard Data Leak Incident Response

This playbook provides step-by-step instructions for responding to a Clipboard Data Leak incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Clipboard Data Leak incident (`playbooks/01_App_&_Endpoint_Security/data_leak_clipboard/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"CLIPBOARD_EXPOSE"** string.
- **Automation Purpose**: Disable Shared Clipboard.

## Run the Detection Script

- `detect_data_leak_clipboard.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the data_leak_clipboard playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/data_leak_clipboard
    ```
- Run the provided script:
    ```bash
    python scripts/detect_data_leak_clipboard.py
    ```
