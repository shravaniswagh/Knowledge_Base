# Massive File Deletion Incident Response

This playbook provides step-by-step instructions for responding to a Massive File Deletion incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Massive File Deletion incident (`playbooks/04_Identity_&_Governance/mass_deletion/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"5000_FILES_DELETED"** string.
- **Automation Purpose**: Snapshot Restoration.

## Run the Detection Script

- `detect_mass_deletion.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the mass_deletion playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/mass_deletion
    ```
- Run the provided script:
    ```bash
    python scripts/detect_mass_deletion.py
    ```
