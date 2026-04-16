# GraphQL Introspection Abuse Incident Response

This playbook provides step-by-step instructions for responding to a GraphQL Introspection Abuse incident in the **02_Cloud_&_DevSecOps** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a GraphQL Introspection Abuse incident (`playbooks/02_Cloud_&_DevSecOps/graphql_introspection/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"__SCHEMA"** string.
- **Automation Purpose**: Disable Introspection.

## Run the Detection Script

- `detect_graphql_introspection.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the graphql_introspection playbook directory:
    ```bash
    cd playbooks/02_Cloud_&_DevSecOps/graphql_introspection
    ```
- Run the provided script:
    ```bash
    python scripts/detect_graphql_introspection.py
    ```
