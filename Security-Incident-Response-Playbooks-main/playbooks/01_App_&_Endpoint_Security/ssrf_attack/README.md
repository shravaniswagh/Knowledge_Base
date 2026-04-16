# Server-Side Request Forgery Incident Response

This playbook provides step-by-step instructions for responding to a Server-Side Request Forgery incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Server-Side Request Forgery incident (`playbooks/01_App_&_Endpoint_Security/ssrf_attack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"metadata/v1"** string.
- **Automation Purpose**: Egress Filtering.

## Run the Detection Script

- `detect_ssrf_attack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the ssrf_attack playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/ssrf_attack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_ssrf_attack.py
    ```
