# Modbus Flood (SCADA) Incident Response

This playbook provides step-by-step instructions for responding to a Modbus Flood (SCADA) incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Modbus Flood (SCADA) incident (`playbooks/03_Network_&_Infrastructure/modbus_flood/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"MODBUS_DOS"** string.
- **Automation Purpose**: SCADA Network Sharding.

## Run the Detection Script

- `detect_modbus_flood.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the modbus_flood playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/modbus_flood
    ```
- Run the provided script:
    ```bash
    python scripts/detect_modbus_flood.py
    ```
