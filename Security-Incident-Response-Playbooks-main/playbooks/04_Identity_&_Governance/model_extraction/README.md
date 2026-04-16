# AI Model Extraction (Cloning) Incident Response

This playbook provides step-by-step instructions for responding to a AI Model Extraction (Cloning) incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a AI Model Extraction (Cloning) incident (`playbooks/04_Identity_&_Governance/model_extraction/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"MODEL_STOLEN_PROBE"** string.
- **Automation Purpose**: Rate Limit AI Queries.

## Run the Detection Script

- `detect_model_extraction.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the model_extraction playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/model_extraction
    ```
- Run the provided script:
    ```bash
    python scripts/detect_model_extraction.py
    ```
