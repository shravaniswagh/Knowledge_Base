# Docker Socket Exposure Incident Response

This playbook provides step-by-step instructions for responding to a Docker Socket Exposure incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Docker Socket Exposure incident (`playbooks/02_Cloud_&_DevSecOps/docker_sock/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"DOCKER_SOCK"** string.
- **Automation Purpose**: Remove Socket Mount.

## Run the Detection Script

- `detect_docker_sock.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the docker_sock playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/docker_sock
    ```
- Run the provided script:
    ```bash
    python scripts/detect_docker_sock.py
    ```
