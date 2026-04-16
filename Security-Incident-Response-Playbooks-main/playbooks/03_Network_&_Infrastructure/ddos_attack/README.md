# DDoS Attack Incident Response

This playbook provides step-by-step instructions for responding to a DDoS Attack incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a DDoS Attack incident (`playbooks/03_Network_&_Infrastructure/ddos_attack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"FLOOD"** string.
- **Automation Purpose**: Iptables Rate Limiting.

## Run the Detection Script

- `detect_ddos_attack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the ddos_attack playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/ddos_attack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_ddos_attack.py
    ```
