# Web Shell Detection Incident Response

This playbook provides step-by-step instructions for responding to a Web Shell Detection incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Web Shell Detection incident (`playbooks/01_App_&_Endpoint_Security/web_shell/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"shell.php?cmd="** string.
- **Automation Purpose**: Removing Web Shells.

## Run the Detection Script

- `detect_web_shell.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the web_shell playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/web_shell
    ```
- Run the provided script:
    ```bash
    python scripts/detect_web_shell.py
    ```
