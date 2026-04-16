# AI Model Inversion Incident Response

This playbook provides step-by-step instructions for responding to a AI Model Inversion incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a AI Model Inversion incident (`playbooks/04_Identity_&_Governance/model_inversion/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"TRAINING_DATA_EXTRACT"** string.
- **Automation Purpose**: Differential Privacy Audit.

## Run the Detection Script

- `detect_model_inversion.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the model_inversion playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/model_inversion
    ```
- Run the provided script:
    ```bash
    python scripts/detect_model_inversion.py
    ```
