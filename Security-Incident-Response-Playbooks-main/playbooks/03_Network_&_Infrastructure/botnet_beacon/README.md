# Botnet Heartbeat (C2) Incident Response

This playbook provides step-by-step instructions for responding to a Botnet Heartbeat (C2) incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Botnet Heartbeat (C2) incident (`playbooks/03_Network_&_Infrastructure/botnet_beacon/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"C2_BEACON"** string.
- **Automation Purpose**: Network Isolation.

## Run the Detection Script

- `detect_botnet_beacon.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the botnet_beacon playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/botnet_beacon
    ```
- Run the provided script:
    ```bash
    python scripts/detect_botnet_beacon.py
    ```
