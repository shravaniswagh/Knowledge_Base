# Bluetooth Sniffing Incident Response

This playbook provides step-by-step instructions for responding to a Bluetooth Sniffing incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Bluetooth Sniffing incident (`playbooks/03_Network_&_Infrastructure/bluetooth_sniff/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"BLE_SPOOF"** string.
- **Automation Purpose**: Faraday Shielding.

## Run the Detection Script

- `detect_bluetooth_sniff.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the bluetooth_sniff playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/bluetooth_sniff
    ```
- Run the provided script:
    ```bash
    python scripts/detect_bluetooth_sniff.py
    ```
