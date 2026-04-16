# Sensor Data Spoofing Incident Response

This playbook provides step-by-step instructions for responding to a Sensor Data Spoofing incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Sensor Data Spoofing incident (`playbooks/03_Network_&_Infrastructure/sensor_spoofing/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"ANOMALOUS_VALUE"** string.
- **Automation Purpose**: Zero Trust Telemetry.

## Run the Detection Script

- `detect_sensor_spoofing.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the sensor_spoofing playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/sensor_spoofing
    ```
- Run the provided script:
    ```bash
    python scripts/detect_sensor_spoofing.py
    ```
