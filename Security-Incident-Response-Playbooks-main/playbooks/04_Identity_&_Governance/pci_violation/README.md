# PCI-DSS Compliance Breach Incident Response

This playbook provides step-by-step instructions for responding to a PCI-DSS Compliance Breach incident in the **04_Identity_&_Governance** domain.

## Detection Logic & Sample Data

- A sample log file is used to simulate a PCI-DSS Compliance Breach incident (`playbooks/04_Identity_&_Governance/pci_violation/examples/sample_log.txt`).
- **Detection Pattern**: The script specifically searches logs for the **"CC_PLAINTEXT"** string.
- **Automation Purpose**: Pure Sensitive Logs.

## Run the Detection Script

- `detect_pci_violation.py` is the script used to **identify** this specific incident type.
- **Output**: The script generates `example_output.txt`, listing all detected occurrences.

## Run the Ansible Playbook
- Navigate to the pci_violation playbook directory:
    ```bash
    cd playbooks/04_Identity_&_Governance/pci_violation
    ```
- Run the provided script:
    ```bash
    python scripts/detect_pci_violation.py
    ```
