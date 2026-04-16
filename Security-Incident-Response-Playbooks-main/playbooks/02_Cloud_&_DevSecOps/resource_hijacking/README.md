# Resource Hijacking Incident Response

This playbook provides step-by-step instructions for responding to a Resource Hijacking incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Resource Hijacking incident (`playbooks/02_Cloud_&_DevSecOps/resource_hijacking/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"UNAUTHORIZED_CPU"** string.
- **Automation Purpose**: Clean Compute Assets.

## Run the Detection Script

- `detect_resource_hijacking.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the resource_hijacking playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/resource_hijacking
    ```
- Run the provided script:
    ```bash
    python scripts/detect_resource_hijacking.py
    ```
