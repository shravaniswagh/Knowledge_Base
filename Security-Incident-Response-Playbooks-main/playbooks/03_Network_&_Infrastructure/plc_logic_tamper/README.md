# PLC Logic Tampering Incident Response

This playbook provides step-by-step instructions for responding to a PLC Logic Tampering incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a PLC Logic Tampering incident (`playbooks/03_Network_&_Infrastructure/plc_logic_tamper/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"PLC_CODE_CHANGE"** string.
- **Automation Purpose**: Restore PLC Firmware.

## Run the Detection Script

- `detect_plc_logic_tamper.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the plc_logic_tamper playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/plc_logic_tamper
    ```
- Run the provided script:
    ```bash
    python scripts/detect_plc_logic_tamper.py
    ```
