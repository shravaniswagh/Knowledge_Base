# Cross-Site Request Forgery Incident Response

This playbook provides step-by-step instructions for responding to a Cross-Site Request Forgery incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Cross-Site Request Forgery incident (`playbooks/01_App_&_Endpoint_Security/csrf_attack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"ORIGIN_MISMATCH"** string.
- **Automation Purpose**: Require Anti-CSRF Tokens.

## Run the Detection Script

- `detect_csrf_attack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the csrf_attack playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/csrf_attack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_csrf_attack.py
    ```
