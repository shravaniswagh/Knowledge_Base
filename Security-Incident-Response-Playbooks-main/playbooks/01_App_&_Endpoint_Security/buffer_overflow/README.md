# Buffer Overflow Attempt Incident Response

This playbook provides step-by-step instructions for responding to a Buffer Overflow Attempt incident in the **01_App_&_Endpoint_Security** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Buffer Overflow Attempt incident (`playbooks/01_App_&_Endpoint_Security/buffer_overflow/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"SEGFAULT_DETECTED"** string.
- **Automation Purpose**: Enable ASLR/DEP.

## Run the Detection Script

- `detect_buffer_overflow.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the buffer_overflow playbook directory:
    ```bash
    cd playbooks/01_App_&_Endpoint_Security/buffer_overflow
    ```
- Run the provided script:
    ```bash
    python scripts/detect_buffer_overflow.py
    ```
