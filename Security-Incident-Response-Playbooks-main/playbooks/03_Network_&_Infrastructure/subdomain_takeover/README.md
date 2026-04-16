# Subdomain Takeover Incident Response

This playbook provides step-by-step instructions for responding to a Subdomain Takeover incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Subdomain Takeover incident (`playbooks/03_Network_&_Infrastructure/subdomain_takeover/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"DEAD_CNAME"** string.
- **Automation Purpose**: Remove Orphaned DNS.

## Run the Detection Script

- `detect_subdomain_takeover.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the subdomain_takeover playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/subdomain_takeover
    ```
- Run the provided script:
    ```bash
    python scripts/detect_subdomain_takeover.py
    ```
