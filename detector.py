import pandas as pd

def analyze_transactions(file_path):
    df = pd.read_csv(file_path)
    alerts = []

    for index, row in df.iterrows():
        # RULE 1: Velocity Check (Time since last transaction < 1 minute)
        if row['time_since_last_min'] < 1:
            alerts.append(f"ALERT: Potential Velocity Attack on Card {row['card_number']} (ID: {row['transaction_id']})")

        # RULE 2: Card Testing (Amount < $2.00)
        elif row['amount'] < 2.00:
            alerts.append(f"ALERT: Card Testing Pattern Detected on Card {row['card_number']} (ID: {row['transaction_id']})")

        # RULE 3: Impossible Travel (Distance/Time anomaly)
        elif row['location'] != row['last_location'] and row['time_since_last_min'] < 30:
            alerts.append(f"ALERT: Geographic Anomaly on Card {row['card_number']} (ID: {row['transaction_id']})")

    return alerts

if __name__ == "__main__":
    results = analyze_transactions('transactions.csv')
    print("--- EnKash Fraud Detection System Scan Results ---")
    for alert in results:
        print(alert)