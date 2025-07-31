import openpyxl
from openpyxl import Workbook
import json
import os

wb = Workbook()
ws = wb.active
ws.title = "Scan Results"
ws.append(["Type", "Severity", "Target", "Message"])

def add_trivy_results(trivy_json):
    # Vulnerabilities
    for result in trivy_json.get('Results', []):
        target = result.get('Target', '')
        # Vulnerabilities
        for vuln in result.get('Vulnerabilities', []):
            ws.append([
                "Vulnerability",
                vuln.get('Severity', ''),
                target,
                vuln.get('Title', vuln.get('Description', ''))
            ])
        # Secrets
        for secret in result.get('Secrets', []):
            ws.append([
                "Secret",
                secret.get('Severity', ''),
                target,
                secret.get('Title', secret.get('Description', ''))
            ])
        # Misconfigurations
        for misconf in result.get('Misconfigurations', []):
            ws.append([
                "Config",
                misconf.get('Severity', ''),
                target,
                misconf.get('Message', misconf.get('Description', ''))
            ])
        # Licenses
        for license in result.get('Licenses', []):
            ws.append([
                "License",
                license.get('Severity', ''),
                target,
                license.get('Title', license.get('Description', ''))
            ])

if os.path.exists('trivy-results.json'):
    with open('trivy-results.json') as f:
        trivy_json = json.load(f)
        add_trivy_results(trivy_json)

wb.save('scan-results.xlsx')
