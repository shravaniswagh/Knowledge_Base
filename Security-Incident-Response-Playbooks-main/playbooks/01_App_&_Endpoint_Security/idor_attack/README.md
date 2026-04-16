# Insecure Direct Object Ref (IDOR) Incident Response

This playbook provides step-by-step instructions for responding to a Insecure Direct Object Ref (IDOR) incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Insecure Direct Object Ref (IDOR) incident (`playbooks/01_App_&_Endpoint_Security/idor_attack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"AUTH_BYPASS_ID"** string.
- **Automation Purpose**: Verify ID Ownership.

## Run the Detection Script

- `detect_idor_attack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the idor_attack playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/idor_attack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_idor_attack.py
    ```
