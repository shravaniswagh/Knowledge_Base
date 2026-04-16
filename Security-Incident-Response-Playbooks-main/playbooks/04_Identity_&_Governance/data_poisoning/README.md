# AI Training Data Poisoning Incident Response

This playbook provides step-by-step instructions for responding to a AI Training Data Poisoning incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a AI Training Data Poisoning incident (`playbooks/04_Identity_&_Governance/data_poisoning/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"ANOMALOUS_DATA_INGEST"** string.
- **Automation Purpose**: Scrub Training Pipeline.

## Run the Detection Script

- `detect_data_poisoning.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the data_poisoning playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/data_poisoning
    ```
- Run the provided script:
    ```bash
    python scripts/detect_data_poisoning.py
    ```
