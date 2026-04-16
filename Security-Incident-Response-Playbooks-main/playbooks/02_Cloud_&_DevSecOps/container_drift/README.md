# Container Runtime Drift Incident Response

This playbook provides step-by-step instructions for responding to a Container Runtime Drift incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Container Runtime Drift incident (`playbooks/02_Cloud_&_DevSecOps/container_drift/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"BINARY_MODIFIED_IN_POD"** string.
- **Automation Purpose**: Terminate Drifting Pods.

## Run the Detection Script

- `detect_container_drift.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the container_drift playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/container_drift
    ```
- Run the provided script:
    ```bash
    python scripts/detect_container_drift.py
    ```
