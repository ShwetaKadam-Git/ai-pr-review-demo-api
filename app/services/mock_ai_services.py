import re

DEFAULT_RULES = [
    {"name": "no-bare-except", "severity": "error",
     "description": "Bare except clause catches all exceptions. Catch a specific type.",
     "keywords": ["except:"]},
    {"name": "no-print-statements", "severity": "warning",
     "description": "Remove debug print statements before merging.",
     "keywords": ["print("]},
    {"name": "no-hardcoded-secrets", "severity": "error",
     "description": "Do not hardcode API keys, passwords, or tokens.",
     "keywords": ["api_key =", "password =", "secret ="]},
]


def run_mock_review(files, policy_name):
    findings = []
    for file in files:
        lines = file.patch.splitlines()
        for idx, line in enumerate(lines, start=1):
            if not line.startswith("+") or line.startswith("+++"):
                continue
            content = line[1:]
            for rule in DEFAULT_RULES:
                if any(kw in content for kw in rule["keywords"]):
                    findings.append({
                        "severity": rule["severity"],
                        "rule": rule["name"],
                        "location": f"{file.filename}:{idx}",
                        "detail": rule["description"],
                    })
    return findings