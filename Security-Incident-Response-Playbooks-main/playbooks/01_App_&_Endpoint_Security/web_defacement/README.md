# Web Defacement Incident Response

This playbook provides step-by-step instructions for responding to a Web Defacement incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Web Defacement incident (`playbooks/01_App_&_Endpoint_Security/web_defacement/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"HASH_MISMATCH"** string.
- **Automation Purpose**: Restore from Git.

## Run the Detection Script

- `detect_web_defacement.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the web_defacement playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/web_defacement
    ```
- Run the provided script:
    ```bash
    python scripts/detect_web_defacement.py
    ```
