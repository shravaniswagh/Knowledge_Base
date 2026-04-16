# DNS Tunneling Incident Response

This playbook provides step-by-step instructions for responding to a DNS Tunneling incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a DNS Tunneling incident (`playbooks/03_Network_&_Infrastructure/dns_tunneling/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"DNS_TXT_EXFIL"** string.
- **Automation Purpose**: DNS Filtering.

## Run the Detection Script

- `detect_dns_tunneling.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the dns_tunneling playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/dns_tunneling
    ```
- Run the provided script:
    ```bash
    python scripts/detect_dns_tunneling.py
    ```
