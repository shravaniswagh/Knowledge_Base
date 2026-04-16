# Pass-the-Hash (PtH) Incident Response

This playbook provides step-by-step instructions for responding to a Pass-the-Hash (PtH) incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Pass-the-Hash (PtH) incident (`playbooks/04_Identity_&_Governance/pass_the_hash/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"NTLM_ANOMALY"** string.
- **Automation Purpose**: LSA Protection Enable.

## Run the Detection Script

- `detect_pass_the_hash.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the pass_the_hash playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/pass_the_hash
    ```
- Run the provided script:
    ```bash
    python scripts/detect_pass_the_hash.py
    ```
