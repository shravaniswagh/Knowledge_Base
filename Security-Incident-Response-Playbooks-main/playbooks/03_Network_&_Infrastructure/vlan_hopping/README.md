# VLAN Hopping Incident Response

This playbook provides step-by-step instructions for responding to a VLAN Hopping incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a VLAN Hopping incident (`playbooks/03_Network_&_Infrastructure/vlan_hopping/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"TRUNK_ABUSE"** string.
- **Automation Purpose**: Disable Dynamic Trunking.

## Run the Detection Script

- `detect_vlan_hopping.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the vlan_hopping playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/vlan_hopping
    ```
- Run the provided script:
    ```bash
    python scripts/detect_vlan_hopping.py
    ```
