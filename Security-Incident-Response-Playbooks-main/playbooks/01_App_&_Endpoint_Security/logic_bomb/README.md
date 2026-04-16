# Logic Bomb Detection Incident Response

This playbook provides step-by-step instructions for responding to a Logic Bomb Detection incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Logic Bomb Detection incident (`playbooks/01_App_&_Endpoint_Security/logic_bomb/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"TIMESTAMP_TRIGGER"** string.
- **Automation Purpose**: Remove Scheduled Tasks.

## Run the Detection Script

- `detect_logic_bomb.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the logic_bomb playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/logic_bomb
    ```
- Run the provided script:
    ```bash
    python scripts/detect_logic_bomb.py
    ```
