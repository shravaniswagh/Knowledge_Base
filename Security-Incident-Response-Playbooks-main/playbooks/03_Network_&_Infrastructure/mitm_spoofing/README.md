# Man-in-the-Middle Incident Response

This playbook provides step-by-step instructions for responding to a Man-in-the-Middle incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Man-in-the-Middle incident (`playbooks/03_Network_&_Infrastructure/mitm_spoofing/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"ARP_SPOOF"** string.
- **Automation Purpose**: Enable Dynamic ARP.

## Run the Detection Script

- `detect_mitm_spoofing.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the mitm_spoofing playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/mitm_spoofing
    ```
- Run the provided script:
    ```bash
    python scripts/detect_mitm_spoofing.py
    ```
