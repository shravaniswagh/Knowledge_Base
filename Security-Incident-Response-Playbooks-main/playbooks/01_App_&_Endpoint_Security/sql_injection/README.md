# SQL Injection Incident Response

This playbook provides step-by-step instructions for responding to a SQL Injection incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a SQL Injection incident (`playbooks/01_App_&_Endpoint_Security/sql_injection/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"' OR 1=1 --"** string.
- **Automation Purpose**: WAF SQLi Blocking.

## Run the Detection Script

- `detect_sql_injection.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the sql_injection playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/sql_injection
    ```
- Run the provided script:
    ```bash
    python scripts/detect_sql_injection.py
    ```
