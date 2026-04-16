import re
import os

LOG_FILE = 'examples/sample_log.txt'
OUTPUT_FILE = 'examples/example_output.txt'

def detect_incident():
    pattern = r"file:///etc/passwd"
    with open(LOG_FILE, 'r') as file:
        logs = file.readlines()
    alerts = []
    for log in logs:
        if re.search(pattern, log):
            alerts.append(f"ALERT [XML External Entity (XXE)]: {log.strip()}")
    with open(OUTPUT_FILE, 'w') as file:
        for alert in alerts:
            file.write(f"{alert}\n")
            print(alert)

if __name__ == "__main__":
    detect_incident()
