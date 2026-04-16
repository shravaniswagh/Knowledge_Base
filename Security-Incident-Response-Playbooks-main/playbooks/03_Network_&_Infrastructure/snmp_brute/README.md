# SNMP Brute Force Incident Response

This playbook provides step-by-step instructions for responding to a SNMP Brute Force incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a SNMP Brute Force incident (`playbooks/03_Network_&_Infrastructure/snmp_brute/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"SNMP_FAIL"** string.
- **Automation Purpose**: Update Community Strings.

## Run the Detection Script

- `detect_snmp_brute.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the snmp_brute playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/snmp_brute
    ```
- Run the provided script:
    ```bash
    python scripts/detect_snmp_brute.py
    ```
