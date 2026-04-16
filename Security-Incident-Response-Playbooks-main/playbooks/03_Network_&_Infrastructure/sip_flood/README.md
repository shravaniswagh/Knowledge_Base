# SIP/VoIP DDoS Incident Response

This playbook provides step-by-step instructions for responding to a SIP/VoIP DDoS incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a SIP/VoIP DDoS incident (`playbooks/03_Network_&_Infrastructure/sip_flood/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"VOIP_INVITE_FLOOD"** string.
- **Automation Purpose**: VoIP Gateway Filtering.

## Run the Detection Script

- `detect_sip_flood.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the sip_flood playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/sip_flood
    ```
- Run the provided script:
    ```bash
    python scripts/detect_sip_flood.py
    ```
