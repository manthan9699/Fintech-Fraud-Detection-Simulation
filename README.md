
# 💳Fintech Fraud Detection Simulation (Python)

### 🚀 Project Overview
This project is a rule-based fraud detection engine designed to identify suspicious patterns in financial transactions. It simulates a real-world Security Operations Center (SOC) environment for a Fintech platform, focusing on identifying anomalies that could indicate compromised accounts or automated attacks.

---

### 🔍 Key Features & Detection Rules
The system analyzes transaction data in real-time to flag three critical types of fraud:

1. **Velocity Attack Detection:** - Flags accounts with more than 3 transactions in under 60 seconds.
   - *Target:* Rapid-fire automated drainage of credit limits.

2. **Geographic Anomaly (Impossible Travel):**
   - Identifies transactions occurring in different locations faster than physical travel allows.
   - *Target:* Stolen credentials being used in a different region.

3. **Card Testing Patterns:**
   - Detects sequences of small-value transactions (under $2.00) used by hackers to verify if a card is active.
   - *Target:* Early-stage fraud before a large theft occurs.

---

### 🛠️ Technical Stack
- **Language:** Python 3.x
- **Library:** Pandas (for high-speed data manipulation)
- **Environment:** Mock SOC environment simulating EnKash-style corporate spend management.

---

### 📊 How to Run
1. Clone the repository: `git clone [YOUR_URL_HERE]`
2. Ensure you have the `transactions.csv` file in the same directory.
3. Run the detector: `python detector.py`

---

### 📈 Future Enhancements (EnKash Specific)
- **ML Integration:** Transition from rule-based to a Random Forest model to reduce False Positives.
- **Real-time API:** Migrating from CSV batch processing to a streaming API (FastAPI) for instant blocking.
- **MFA Trigger:** Integration with automated Multi-Factor Authentication for "High Risk" flags.

---
**Author:** Manthan Gaikwad  
**Goal:** Prepared for EnKash Campus Recruitment 2026.
