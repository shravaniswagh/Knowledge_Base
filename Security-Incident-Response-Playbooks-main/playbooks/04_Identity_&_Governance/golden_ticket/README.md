# Golden Ticket (AD) Incident Response

This playbook provides step-by-step instructions for responding to a Golden Ticket (AD) incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a Golden Ticket (AD) incident (`playbooks/04_Identity_&_Governance/golden_ticket/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"KRBTGT_FORGED"** string.
- **Automation Purpose**: Reset KRBTGT account.

## Run the Detection Script

- `detect_golden_ticket.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the golden_ticket playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/golden_ticket
    ```
- Run the provided script:
    ```bash
    python scripts/detect_golden_ticket.py
    ```
