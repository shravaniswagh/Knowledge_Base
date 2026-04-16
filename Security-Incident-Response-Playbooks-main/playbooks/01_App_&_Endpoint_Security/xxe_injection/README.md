# XML External Entity (XXE) Incident Response

This playbook provides step-by-step instructions for responding to a XML External Entity (XXE) incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a XML External Entity (XXE) incident (`playbooks/01_App_&_Endpoint_Security/xxe_injection/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"file:///etc/passwd"** string.
- **Automation Purpose**: Disable XML External Entities.

## Run the Detection Script

- `detect_xxe_injection.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the xxe_injection playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/xxe_injection
    ```
- Run the provided script:
    ```bash
    python scripts/detect_xxe_injection.py
    ```
