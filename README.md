# DAY-6-Challenge-Smart-Transaction-Risk-Detector-
1. Algorithm Explanation:
  The program takes a list of transaction amounts as input.
  Each transaction is classified into categories like normal, large, high risk, or invalid using conditional statements.
  A dictionary is used to store categorized transactions.
  List comprehension is used to filter valid transactions and calculate the total value.
  The program then checks patterns such as transaction count, total spending, and number of high-risk transactions.
  Additionally, I included a personalization rule based on my register number, where risk increases if the number of transactions is greater than 1.
  Finally, the program assigns a risk level (Low, Moderate, High).
2.Logic Decision:
  One important logic decision I made was prioritizing high-risk transaction patterns over general conditions.
  If multiple high-risk transactions are found, the system directly classifies it as high risk.
  I also applied a personalization rule based on my register number (last digit = 1), where the risk level increases if transactions are more than 1.
  This makes the system stricter and adds uniqueness to my solution.
  Such customization reflects how real-world fraud detection systems may behave.
