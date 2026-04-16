# Local File Inclusion Incident Response

This playbook provides step-by-step instructions for responding to a Local File Inclusion incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Local File Inclusion incident (`playbooks/01_App_&_Endpoint_Security/local_file_inclusion/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"/etc/shadow"** string.
- **Automation Purpose**: Sanitize Path Input.

## Run the Detection Script

- `detect_local_file_inclusion.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the local_file_inclusion playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/local_file_inclusion
    ```
- Run the provided script:
    ```bash
    python scripts/detect_local_file_inclusion.py
    ```
