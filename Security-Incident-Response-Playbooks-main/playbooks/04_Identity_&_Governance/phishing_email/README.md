# Phishing Incident Incident Response

This playbook provides step-by-step instructions for responding to a Phishing Incident incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Phishing Incident incident (`playbooks/04_Identity_&_Governance/phishing_email/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"URL_SPOOF"** string.
- **Automation Purpose**: Domain Blocklisting.

## Run the Detection Script

- `detect_phishing_email.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the phishing_email playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/phishing_email
    ```
- Run the provided script:
    ```bash
    python scripts/detect_phishing_email.py
    ```
