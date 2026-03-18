def analyze_transactions(transactions):
    categories = {
        "normal": [],
        "large": [],
        "high_risk": [],
        "invalid": []
    }

    for t in transactions:
        if t <= 0:
            categories["invalid"].append(t)
        elif t <= 500:
            categories["normal"].append(t)
        elif t <= 2000:
            categories["large"].append(t)
        else:
            categories["high_risk"].append(t)

    valid_transactions = [t for t in transactions if t > 0]

    total_value = sum(valid_transactions)
    num_transactions = len(transactions)

    frequent = num_transactions > 5
    large_spending = total_value > 5000
    suspicious = len(categories["high_risk"]) >= 3

    risk = "Low Risk"

    if suspicious or (large_spending and frequent):
        risk = "High Risk"
    elif frequent or large_spending:
        risk = "Moderate Risk"

    if num_transactions > 1:
        if risk == "Low Risk":
            risk = "Moderate Risk"
        elif risk == "Moderate Risk":
            risk = "High Risk"

    summary = (total_value, num_transactions)

    print("Categorized Transactions:", categories)
    print("Total Transaction Value:", total_value)
    print("Number of Transactions:", num_transactions)
    print("Summary (Tuple):", summary)
    print("Final Risk:", risk)

    return risk


print("Test Case 1:")
analyze_transactions([100, 200, 300, 400])

print("\nTest Case 2:")
analyze_transactions([1000, 1500, 2500, 3000, 700, 800])

print("\nTest Case 3:")
analyze_transactions([0, -50, 100, 600, 2500])