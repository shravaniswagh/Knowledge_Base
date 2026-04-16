# HIPAA Privacy violation Incident Response

This playbook provides step-by-step instructions for responding to a HIPAA Privacy violation incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a HIPAA Privacy violation incident (`playbooks/04_Identity_&_Governance/compliance_governance/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"PATIENT_RECORD_PLAINTEXT"** string.
- **Automation Purpose**: Apply Data Masking.

## Run the Detection Script

- `detect_compliance_governance.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the compliance_governance playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/compliance_governance
    ```
- Run the provided script:
    ```bash
    python scripts/detect_compliance_governance.py
    ```
