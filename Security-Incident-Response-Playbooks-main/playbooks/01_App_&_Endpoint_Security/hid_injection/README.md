# HID Injection (Rubber Ducky) Incident Response

This playbook provides step-by-step instructions for responding to a HID Injection (Rubber Ducky) incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a HID Injection (Rubber Ducky) incident (`playbooks/01_App_&_Endpoint_Security/hid_injection/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"FAST_TYPING"** string.
- **Automation Purpose**: Disabling Rogue USB.

## Run the Detection Script

- `detect_hid_injection.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the hid_injection playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/hid_injection
    ```
- Run the provided script:
    ```bash
    python scripts/detect_hid_injection.py
    ```
