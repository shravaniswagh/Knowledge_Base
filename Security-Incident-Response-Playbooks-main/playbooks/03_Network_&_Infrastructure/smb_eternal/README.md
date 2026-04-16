# SMB EternalBlue Detection Incident Response

This playbook provides step-by-step instructions for responding to a SMB EternalBlue Detection incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a SMB EternalBlue Detection incident (`playbooks/03_Network_&_Infrastructure/smb_eternal/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"ETERNAL_BLUE_SIG"** string.
- **Automation Purpose**: Disable SMBv1.

## Run the Detection Script

- `detect_smb_eternal.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the smb_eternal playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/smb_eternal
    ```
- Run the provided script:
    ```bash
    python scripts/detect_smb_eternal.py
    ```
