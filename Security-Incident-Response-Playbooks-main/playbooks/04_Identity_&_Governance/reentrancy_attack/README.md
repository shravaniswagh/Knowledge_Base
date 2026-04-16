# Blockchain Reentrancy Incident Response

This playbook provides step-by-step instructions for responding to a Blockchain Reentrancy incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Blockchain Reentrancy incident (`playbooks/04_Identity_&_Governance/reentrancy_attack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"SMART_CONTRACT_LOOP"** string.
- **Automation Purpose**: Pause Smart Contract.

## Run the Detection Script

- `detect_reentrancy_attack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the reentrancy_attack playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/reentrancy_attack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_reentrancy_attack.py
    ```
