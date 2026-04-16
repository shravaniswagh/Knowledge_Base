# Shared Credential Usage Incident Response

This playbook provides step-by-step instructions for responding to a Shared Credential Usage incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Shared Credential Usage incident (`playbooks/04_Identity_&_Governance/shared_credential/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"CONCURRENT_LOGINS_DISTANT"** string.
- **Automation Purpose**: Force Individual Identity.

## Run the Detection Script

- `detect_shared_credential.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the shared_credential playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/shared_credential
    ```
- Run the provided script:
    ```bash
    python scripts/detect_shared_credential.py
    ```
