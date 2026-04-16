# NTP Amplification Incident Response

This playbook provides step-by-step instructions for responding to a NTP Amplification incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a NTP Amplification incident (`playbooks/03_Network_&_Infrastructure/ntp_amplification/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"MON_GETLIST"** string.
- **Automation Purpose**: Secure NTP Config.

## Run the Detection Script

- `detect_ntp_amplification.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the ntp_amplification playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/ntp_amplification
    ```
- Run the provided script:
    ```bash
    python scripts/detect_ntp_amplification.py
    ```
