# PowerShell Script Bypass Incident Response

This playbook provides step-by-step instructions for responding to a PowerShell Script Bypass incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a PowerShell Script Bypass incident (`playbooks/04_Identity_&_Governance/powershell_bypass/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"-ExecutionPolicy Bypass"** string.
- **Automation Purpose**: Constrained Language Mode.

## Run the Detection Script

- `detect_powershell_bypass.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the powershell_bypass playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/powershell_bypass
    ```
- Run the provided script:
    ```bash
    python scripts/detect_powershell_bypass.py
    ```
