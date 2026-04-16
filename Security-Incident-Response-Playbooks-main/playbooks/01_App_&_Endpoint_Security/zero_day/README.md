# Zero-Day Vulnerability Incident Response

This playbook provides step-by-step instructions for responding to a Zero-Day Vulnerability incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Zero-Day Vulnerability incident (`playbooks/01_App_&_Endpoint_Security/zero_day/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"PATH_TRAVERSAL"** string.
- **Automation Purpose**: Virtual Patching.

## Run the Detection Script

- `detect_zero_day.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the zero_day playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/zero_day
    ```
- Run the provided script:
    ```bash
    python scripts/detect_zero_day.py
    ```
