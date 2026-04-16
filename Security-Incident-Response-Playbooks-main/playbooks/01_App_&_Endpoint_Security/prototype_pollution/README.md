# Prototype Pollution Incident Response

This playbook provides step-by-step instructions for responding to a Prototype Pollution incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Prototype Pollution incident (`playbooks/01_App_&_Endpoint_Security/prototype_pollution/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"__proto__"** string.
- **Automation Purpose**: Freeze Objects.

## Run the Detection Script

- `detect_prototype_pollution.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the prototype_pollution playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/prototype_pollution
    ```
- Run the provided script:
    ```bash
    python scripts/detect_prototype_pollution.py
    ```
