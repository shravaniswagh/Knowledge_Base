# Terraform State Exposure Incident Response

This playbook provides step-by-step instructions for responding to a Terraform State Exposure incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Terraform State Exposure incident (`playbooks/02_Cloud_&_DevSecOps/terraform_state_leak/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"TF_STATE_PUBLIC"** string.
- **Automation Purpose**: Secure State Storage.

## Run the Detection Script

- `detect_terraform_state_leak.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the terraform_state_leak playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/terraform_state_leak
    ```
- Run the provided script:
    ```bash
    python scripts/detect_terraform_state_leak.py
    ```
