# Mobile Cert Pinning Bypass Incident Response

This playbook provides step-by-step instructions for responding to a Mobile Cert Pinning Bypass incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Mobile Cert Pinning Bypass incident (`playbooks/01_App_&_Endpoint_Security/mobile_cert_pinning/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"FRIDA_DETECTED"** string.
- **Automation Purpose**: Kill Mobile Process.

## Run the Detection Script

- `detect_mobile_cert_pinning.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the mobile_cert_pinning playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/mobile_cert_pinning
    ```
- Run the provided script:
    ```bash
    python scripts/detect_mobile_cert_pinning.py
    ```
