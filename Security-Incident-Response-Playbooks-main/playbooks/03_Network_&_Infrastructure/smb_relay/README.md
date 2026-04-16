# SMB Relay Attack Incident Response

This playbook provides step-by-step instructions for responding to a SMB Relay Attack incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a SMB Relay Attack incident (`playbooks/03_Network_&_Infrastructure/smb_relay/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"SMB_RELAY"** string.
- **Automation Purpose**: Enable SMB Signing.

## Run the Detection Script

- `detect_smb_relay.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the smb_relay playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/smb_relay
    ```
- Run the provided script:
    ```bash
    python scripts/detect_smb_relay.py
    ```
