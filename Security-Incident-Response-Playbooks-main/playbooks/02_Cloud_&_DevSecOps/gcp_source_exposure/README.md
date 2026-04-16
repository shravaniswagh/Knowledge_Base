# GCP Source Repository Leak Incident Response

This playbook provides step-by-step instructions for responding to a GCP Source Repository Leak incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a GCP Source Repository Leak incident (`playbooks/02_Cloud_&_DevSecOps/gcp_source_exposure/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"GIT_PUSH_OUTSIDE_ORG"** string.
- **Automation Purpose**: Restrict GCP Repository.

## Run the Detection Script

- `detect_gcp_source_exposure.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the gcp_source_exposure playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/gcp_source_exposure
    ```
- Run the provided script:
    ```bash
    python scripts/detect_gcp_source_exposure.py
    ```
