# Blockchain Flash Loan Attack Incident Response

This playbook provides step-by-step instructions for responding to a Blockchain Flash Loan Attack incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Blockchain Flash Loan Attack incident (`playbooks/04_Identity_&_Governance/flash_loan_attack/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"ORACLE_MISMATCH"** string.
- **Automation Purpose**: Enable Oracle Safeguard.

## Run the Detection Script

- `detect_flash_loan_attack.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the flash_loan_attack playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/flash_loan_attack
    ```
- Run the provided script:
    ```bash
    python scripts/detect_flash_loan_attack.py
    ```
