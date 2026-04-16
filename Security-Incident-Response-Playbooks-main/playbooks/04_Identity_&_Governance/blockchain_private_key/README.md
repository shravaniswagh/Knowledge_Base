# Private Key Data Spill Incident Response

This playbook provides step-by-step instructions for responding to a Private Key Data Spill incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Private Key Data Spill incident (`playbooks/04_Identity_&_Governance/blockchain_private_key/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"MNEMONIC_PHRASE"** string.
- **Automation Purpose**: Revoke Mnemonic/Keys.

## Run the Detection Script

- `detect_blockchain_private_key.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the blockchain_private_key playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/blockchain_private_key
    ```
- Run the provided script:
    ```bash
    python scripts/detect_blockchain_private_key.py
    ```
