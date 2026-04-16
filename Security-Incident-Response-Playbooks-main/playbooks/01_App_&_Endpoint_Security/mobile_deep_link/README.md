# Mobile Deep Link Exploit Incident Response

This playbook provides step-by-step instructions for responding to a Mobile Deep Link Exploit incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Mobile Deep Link Exploit incident (`playbooks/01_App_&_Endpoint_Security/mobile_deep_link/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"UNAUTHORIZED_DEEP_LINK"** string.
- **Automation Purpose**: Harden Link Handlers.

## Run the Detection Script

- `detect_mobile_deep_link.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the mobile_deep_link playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/mobile_deep_link
    ```
- Run the provided script:
    ```bash
    python scripts/detect_mobile_deep_link.py
    ```
