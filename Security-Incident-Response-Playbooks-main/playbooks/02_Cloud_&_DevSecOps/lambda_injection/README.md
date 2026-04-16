# Serverless Lambda Injection Incident Response

This playbook provides step-by-step instructions for responding to a Serverless Lambda Injection incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Serverless Lambda Injection incident (`playbooks/02_Cloud_&_DevSecOps/lambda_injection/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"FUNC_OVR_WRITE"** string.
- **Automation Purpose**: Apply Lambda IAM Roles.

## Run the Detection Script

- `detect_lambda_injection.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the lambda_injection playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/lambda_injection
    ```
- Run the provided script:
    ```bash
    python scripts/detect_lambda_injection.py
    ```
