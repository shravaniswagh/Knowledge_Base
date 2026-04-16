# Mobile Jailbreak Detection Incident Response

This playbook provides step-by-step instructions for responding to a Mobile Jailbreak Detection incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Mobile Jailbreak Detection incident (`playbooks/01_App_&_Endpoint_Security/mobile_jailbreak/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"SU_BINARY_FOUND"** string.
- **Automation Purpose**: Wipe Application Data.

## Run the Detection Script

- `detect_mobile_jailbreak.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the mobile_jailbreak playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/mobile_jailbreak
    ```
- Run the provided script:
    ```bash
    python scripts/detect_mobile_jailbreak.py
    ```
