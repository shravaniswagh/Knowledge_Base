# Secret Leak in CI Logs Incident Response

This playbook provides step-by-step instructions for responding to a Secret Leak in CI Logs incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Secret Leak in CI Logs incident (`playbooks/02_Cloud_&_DevSecOps/secret_in_ci_logs/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"SECRET_EXPOSED"** string.
- **Automation Purpose**: Scrub Build Logs.

## Run the Detection Script

- `detect_secret_in_ci_logs.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the secret_in_ci_logs playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/secret_in_ci_logs
    ```
- Run the provided script:
    ```bash
    python scripts/detect_secret_in_ci_logs.py
    ```
