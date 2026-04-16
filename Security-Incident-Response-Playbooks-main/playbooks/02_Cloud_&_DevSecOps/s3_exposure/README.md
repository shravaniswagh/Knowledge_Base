# S3 Bucket Exposure Incident Response

This playbook provides step-by-step instructions for responding to a S3 Bucket Exposure incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a S3 Bucket Exposure incident (`playbooks/02_Cloud_&_DevSecOps/s3_exposure/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"PUBLIC_ACL"** string.
- **Automation Purpose**: Apply S3 Private Policy.

## Run the Detection Script

- `detect_s3_exposure.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the s3_exposure playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/s3_exposure
    ```
- Run the provided script:
    ```bash
    python scripts/detect_s3_exposure.py
    ```
