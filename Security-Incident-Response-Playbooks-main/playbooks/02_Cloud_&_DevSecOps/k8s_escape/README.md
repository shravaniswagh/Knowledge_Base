# Kubernetes Pod Escape Incident Response

This playbook provides step-by-step instructions for responding to a Kubernetes Pod Escape incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Kubernetes Pod Escape incident (`playbooks/02_Cloud_&_DevSecOps/k8s_escape/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"HOST_MOUNT"** string.
- **Automation Purpose**: Apply Pod Security Policy.

## Run the Detection Script

- `detect_k8s_escape.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the k8s_escape playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/k8s_escape
    ```
- Run the provided script:
    ```bash
    python scripts/detect_k8s_escape.py
    ```
