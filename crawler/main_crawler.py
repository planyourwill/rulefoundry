import os
from logic.extractor import extract_rules
from filters.estate_filter import is_estate_relevant

def run_crawler():
    with open("tests/public_real_case.html", "r", encoding="utf-8") as f:
        html = f.read()

    rules = extract_rules(html)
    relevant_rules = [r for r in rules if is_estate_relevant(r)]

    with open("rules/rule_output.json", "w", encoding="utf-8") as out:
        import json
        json.dump(relevant_rules, out, indent=2)

    with open("logs/justification_log.txt", "w", encoding="utf-8") as log:
        for rule in relevant_rules:
            log.write(f"RULE: {rule['text']}
")
            log.write(f"  - Source: {rule['source']}
")
            log.write(f"  - Doctrines: {', '.join(rule['doctrines'])}

")

if __name__ == "__main__":
    run_crawler()
