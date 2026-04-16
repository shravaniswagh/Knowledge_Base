# Mobile SMS Interception Incident Response

This playbook provides step-by-step instructions for responding to a Mobile SMS Interception incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Mobile SMS Interception incident (`playbooks/01_App_&_Endpoint_Security/mobile_sms_intercept/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"SIM_SWAP_DETECTED"** string.
- **Automation Purpose**: Lock User Mobile Vault.

## Run the Detection Script

- `detect_mobile_sms_intercept.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the mobile_sms_intercept playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/mobile_sms_intercept
    ```
- Run the provided script:
    ```bash
    python scripts/detect_mobile_sms_intercept.py
    ```
