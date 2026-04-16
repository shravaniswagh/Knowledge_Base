# Shadow IT Detection Incident Response

This playbook provides step-by-step instructions for responding to a Shadow IT Detection incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Shadow IT Detection incident (`playbooks/02_Cloud_&_DevSecOps/shadow_it/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"UNSANCTIONED_APP"** string.
- **Automation Purpose**: Block Unsanctioned SaaS.

## Run the Detection Script

- `detect_shadow_it.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the shadow_it playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/shadow_it
    ```
- Run the provided script:
    ```bash
    python scripts/detect_shadow_it.py
    ```
