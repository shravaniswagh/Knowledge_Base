# ICMP Exfiltration Incident Response

This playbook provides step-by-step instructions for responding to a ICMP Exfiltration incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a ICMP Exfiltration incident (`playbooks/03_Network_&_Infrastructure/icmp_exfil/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"DATA_IN_PING"** string.
- **Automation Purpose**: Rate Limit ICMP.

## Run the Detection Script

- `detect_icmp_exfil.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the icmp_exfil playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/icmp_exfil
    ```
- Run the provided script:
    ```bash
    python scripts/detect_icmp_exfil.py
    ```
