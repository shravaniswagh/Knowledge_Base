# Azure Blob Misconfig Incident Response

This playbook provides step-by-step instructions for responding to a Azure Blob Misconfig incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Azure Blob Misconfig incident (`playbooks/02_Cloud_&_DevSecOps/azure_blob_exposure/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"BLOB_ANONYMOUS"** string.
- **Automation Purpose**: Secure Azure Blob Container.

## Run the Detection Script

- `detect_azure_blob_exposure.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the azure_blob_exposure playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/azure_blob_exposure
    ```
- Run the provided script:
    ```bash
    python scripts/detect_azure_blob_exposure.py
    ```
