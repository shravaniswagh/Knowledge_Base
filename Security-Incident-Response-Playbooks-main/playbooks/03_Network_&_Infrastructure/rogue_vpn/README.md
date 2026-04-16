# Rogue VPN Access Incident Response

This playbook provides step-by-step instructions for responding to a Rogue VPN Access incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Rogue VPN Access incident (`playbooks/03_Network_&_Infrastructure/rogue_vpn/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"UNAUTH_TUNNEL"** string.
- **Automation Purpose**: Revoke VPN Cert.

## Run the Detection Script

- `detect_rogue_vpn.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the rogue_vpn playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/rogue_vpn
    ```
- Run the provided script:
    ```bash
    python scripts/detect_rogue_vpn.py
    ```
