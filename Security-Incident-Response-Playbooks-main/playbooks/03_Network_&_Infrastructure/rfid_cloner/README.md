# RFID Badge Cloner Incident Response

This playbook provides step-by-step instructions for responding to a RFID Badge Cloner incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a RFID Badge Cloner incident (`playbooks/03_Network_&_Infrastructure/rfid_cloner/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"DUPLICATE_BADGE"** string.
- **Automation Purpose**: Disable Legacy Badge.

## Run the Detection Script

- `detect_rfid_cloner.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the rfid_cloner playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/rfid_cloner
    ```
- Run the provided script:
    ```bash
    python scripts/detect_rfid_cloner.py
    ```
