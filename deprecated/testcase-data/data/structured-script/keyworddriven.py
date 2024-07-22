import pandas as pd
import json
import sys
import os

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from data_pipeline import TestCasePipeline

pipeline = TestCasePipeline()

validate_schedule_automated_payments = pd.DataFrame({
    "Prompt": [
        "Generate a keyword-driven test case for TC_08 Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week"
    ],
    "Testcase Type": [
        "keyword-driven"

    ],
    "Testcase Name": [
        "Validate Schedule AutoPay"
    ],
    "Response": [
    """***Settings***
Library     SeleniumLibrary
    
***Test Cases***
Validate Schedule AutoPay
    [Arguments] ${day_of_week} ${payment_details}
    [Return] ${boolean}
    [Documentation] Checks if the customer is able to schedule AutoPay payments specifically on a Sunday; returns true if successful.""",  
    ],
    "Documentation": [
        "This test checks for the ability to schedule payments on Sundays, highlighting the critical role of specific days in payment processing",
        "This scenario sets up AutoPay for Omnicorp customers, using dynamic templates to adjust arguments based on customer data.",
    ]
})

omnicorp_autopay = pd.DataFrame({
    'Prompt': [
        "Create a keyword-driven test scenario for Omnicorp Autopay"
    ],
    'Testcase Type': [
        "Keyword-driven"
    ],

    'Testcase Name': [
        "Setup Omnicorp Autopay"
    ],
    'Response': [
        """***Settings***
    Library     SeleniumLibrary
        
    ***Test Cases***
    Setup Omnicorp Autopay
        [Arguments] ${customer_id} ${payment_info}
        [Return] ${setup_status}
        [Documentation] Sets up Autopay for a customer with given ID and payment information; returns setup status."""
    ],
    'Documentation': [
        "This scenario sets up AutoPay for Omnicorp customers, using dynamic templates to adjust arguments based on customer data."
    ]
})


# Adding dataframes to the pipeline
pipeline.add_dataframe(validate_schedule_automated_payments)
pipeline.add_dataframe(omnicorp_autopay)

# Combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = '../json/keyworddriven.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = '../csv/keyworddriven.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")