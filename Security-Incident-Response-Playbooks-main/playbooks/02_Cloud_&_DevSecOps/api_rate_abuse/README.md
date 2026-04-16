# API Rate Limit Abuse Incident Response

This playbook provides step-by-step instructions for responding to a API Rate Limit Abuse incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a API Rate Limit Abuse incident (`playbooks/02_Cloud_&_DevSecOps/api_rate_abuse/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"RATE_LIMIT_HIT"** string.
- **Automation Purpose**: Apply API Quotas.

## Run the Detection Script

- `detect_api_rate_abuse.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the api_rate_abuse playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/api_rate_abuse
    ```
- Run the provided script:
    ```bash
    python scripts/detect_api_rate_abuse.py
    ```
