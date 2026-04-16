# Dependency Confusion Incident Response

This playbook provides step-by-step instructions for responding to a Dependency Confusion incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Dependency Confusion incident (`playbooks/02_Cloud_&_DevSecOps/dependency_confusion/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"INTERNAL_PKG_MISMATCH"** string.
- **Automation Purpose**: Pin Private Scopes.

## Run the Detection Script

- `detect_dependency_confusion.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the dependency_confusion playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/dependency_confusion
    ```
- Run the provided script:
    ```bash
    python scripts/detect_dependency_confusion.py
    ```
