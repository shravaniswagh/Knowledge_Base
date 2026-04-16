# VPC Peering Abuse Incident Response

This playbook provides step-by-step instructions for responding to a VPC Peering Abuse incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a VPC Peering Abuse incident (`playbooks/02_Cloud_&_DevSecOps/vpc_peering_abuse/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"UNAUTHORIZED_PEERING"** string.
- **Automation Purpose**: Remove Peer Connections.

## Run the Detection Script

- `detect_vpc_peering_abuse.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the vpc_peering_abuse playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/vpc_peering_abuse
    ```
- Run the provided script:
    ```bash
    python scripts/detect_vpc_peering_abuse.py
    ```
