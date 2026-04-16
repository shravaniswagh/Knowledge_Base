# Brute Force (Web) Incident Response

This playbook provides step-by-step instructions for responding to a Brute Force (Web) incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Brute Force (Web) incident (`playbooks/01_App_&_Endpoint_Security/brute_force_web/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"401 Unauthorized"** string.
- **Automation Purpose**: Fail2Ban Activation.

## Run the Detection Script

- `detect_brute_force_web.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the brute_force_web playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/brute_force_web
    ```
- Run the provided script:
    ```bash
    python scripts/detect_brute_force_web.py
    ```
