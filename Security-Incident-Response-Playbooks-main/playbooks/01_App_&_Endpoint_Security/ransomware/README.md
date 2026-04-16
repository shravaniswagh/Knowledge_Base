# Ransomware Incident Response

This playbook provides step-by-step instructions for responding to a Ransomware incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Ransomware incident (`playbooks/01_App_&_Endpoint_Security/ransomware/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"FOUND"** string.
- **Automation Purpose**: ClamAV Quarantine.

## Run the Detection Script

- `detect_ransomware.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the ransomware playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/ransomware
    ```
- Run the provided script:
    ```bash
    python scripts/detect_ransomware.py
    ```
