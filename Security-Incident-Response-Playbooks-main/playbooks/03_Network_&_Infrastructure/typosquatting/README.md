# Typosquatting Domain Incident Response

This playbook provides step-by-step instructions for responding to a Typosquatting Domain incident in the **03_Network_&_Infrastructure** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Typosquatting Domain incident (`playbooks/03_Network_&_Infrastructure/typosquatting/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"LOOK_ALIKE"** string.
- **Automation Purpose**: Block Domain @ Proxy.

## Run the Detection Script

- `detect_typosquatting.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the typosquatting playbook directory:
    ```bash
    cd playbooks/03_Network_&_Infrastructure/typosquatting
    ```
- Run the provided script:
    ```bash
    python scripts/detect_typosquatting.py
    ```
