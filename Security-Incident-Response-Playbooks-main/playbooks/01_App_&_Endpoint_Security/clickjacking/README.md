# Clickjacking Incident Response

This playbook provides step-by-step instructions for responding to a Clickjacking incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Clickjacking incident (`playbooks/01_App_&_Endpoint_Security/clickjacking/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"FRAME_OVERLAY"** string.
- **Automation Purpose**: Set X-Frame-Options.

## Run the Detection Script

- `detect_clickjacking.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the clickjacking playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/clickjacking
    ```
- Run the provided script:
    ```bash
    python scripts/detect_clickjacking.py
    ```
