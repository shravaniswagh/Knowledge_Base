# BGP Hijacking Detection Incident Response

This playbook provides step-by-step instructions for responding to a BGP Hijacking Detection incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a BGP Hijacking Detection incident (`playbooks/03_Network_&_Infrastructure/bgp_hijack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"ROUTE_ANOMALY"** string.
- **Automation Purpose**: Apply BGP Session Auth.

## Run the Detection Script

- `detect_bgp_hijack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the bgp_hijack playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/bgp_hijack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_bgp_hijack.py
    ```
