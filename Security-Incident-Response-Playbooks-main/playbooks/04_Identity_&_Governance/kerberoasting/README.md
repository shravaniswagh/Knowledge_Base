# Kerberoasting (AD) Incident Response

This playbook provides step-by-step instructions for responding to a Kerberoasting (AD) incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Kerberoasting (AD) incident (`playbooks/04_Identity_&_Governance/kerberoasting/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"TGS_RC4"** string.
- **Automation Purpose**: Rotate AD SPN Key.

## Run the Detection Script

- `detect_kerberoasting.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the kerberoasting playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/kerberoasting
    ```
- Run the provided script:
    ```bash
    python scripts/detect_kerberoasting.py
    ```
