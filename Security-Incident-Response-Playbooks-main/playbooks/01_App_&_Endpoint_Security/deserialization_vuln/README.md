# Insecure Deserialization Incident Response

This playbook provides step-by-step instructions for responding to a Insecure Deserialization incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Insecure Deserialization incident (`playbooks/01_App_&_Endpoint_Security/deserialization_vuln/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"JAVA_DESERIALIZE"** string.
- **Automation Purpose**: Strict Input Validation.

## Run the Detection Script

- `detect_deserialization_vuln.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the deserialization_vuln playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/deserialization_vuln
    ```
- Run the provided script:
    ```bash
    python scripts/detect_deserialization_vuln.py
    ```
