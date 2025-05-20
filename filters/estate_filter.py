def is_estate_relevant(rule):
    estate_keywords = [
        "will", "executor", "testamentary", "probate",
        "trust", "dependent", "capacity", "undue influence",
        "estate", "residue", "beneficiary", "support claim"
    ]
    return any(keyword in rule["text"].lower() for keyword in estate_keywords)
