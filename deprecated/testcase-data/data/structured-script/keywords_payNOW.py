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

validate_61_90_days_due_invoices_selected = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate All Invoices Due For 61-90 Days Are Selected When Customer Clicks On 61-90 Amount link In Summary Of Outstanding Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that all invoices due for 61-90 days are selected when customer clicks on 61-90 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DUE_61_90_INVOICES}       due_61_90_invoices

*** Test Cases ***
Validate 61-90 Days Due Invoices Selected
    [Documentation] Test case for validating that all invoices due for 61-90 days are selected when customer clicks on 61-90 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click 61-90 Amount Link
    Validate All 61-90 Days Due Invoices Selected ${DUE_61_90_INVOICES}"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoices due for 61-90 days when customer clicks on 61-90 amount link in summary of outstanding invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate 61-90 Days Due Invoices Selected"
    ]
})

validate_autopay_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate AutoPay functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the AutoPay functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${AUTOPAY_DETAILS}          autopay_details

*** Test Cases ***
Validate AutoPay
    [Documentation] Test case for validating the AutoPay functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Setup AutoPay ${AUTOPAY_DETAILS}
    Validate AutoPay Setup"""
    ],
    'Description': [
        "This test case checks the validation for AutoPay functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate AutoPay"
    ]
})

validate_common_api_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Common API functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the common API functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${API_DETAILS}              api_details

*** Test Cases ***
Validate Common API
    [Documentation] Test case for validating the common API functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter API Details ${API_DETAILS}
    Validate API Response"""
    ],
    'Description': [
        "This test case checks the validation for common API functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Common API"
    ]
})

validate_customer_api_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer API functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the customer API functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_API_DETAILS}     customer_api_details

*** Test Cases ***
Validate Customer API
    [Documentation] Test case for validating the customer API functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer API Details ${CUSTOMER_API_DETAILS}
    Validate API Response"""
    ],
    'Description': [
        "This test case checks the validation for customer API functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer API"
    ]
})

validate_invoice_api_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Invoice API functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the invoice API functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INVOICE_API_DETAILS}      invoice_api_details

*** Test Cases ***
Validate Invoice API
    [Documentation] Test case for validating the invoice API functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Invoice API Details ${INVOICE_API_DETAILS}
    Validate API Response"""
    ],
    'Description': [
        "This test case checks the validation for invoice API functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Invoice API"
    ]
})

validate_process_payment_api_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Process Payment API functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the process payment API functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${PAYMENT_API_DETAILS}      payment_api_details

*** Test Cases ***
Validate Process Payment API
    [Documentation] Test case for validating the process payment API functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Payment API Details ${PAYMENT_API_DETAILS}
    Validate API Response"""
    ],
    'Description': [
        "This test case checks the validation for process payment API functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment API"
    ]
})

validate_scheduled_payments_api_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Scheduled Payments API functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the scheduled payments API functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${SCHEDULED_API_DETAILS}    scheduled_api_details

*** Test Cases ***
Validate Scheduled Payments API
    [Documentation] Test case for validating the scheduled payments API functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Scheduled API Details ${SCHEDULED_API_DETAILS}
    Validate API Response"""
    ],
    'Description': [
        "This test case checks the validation for scheduled payments API functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Scheduled Payments API"
    ]
})

validate_common_open_invoices_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Common Open Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the common open invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${COMMON_INVOICE_DETAILS}   common_invoice_details

*** Test Cases ***
Validate Common Open Invoices
    [Documentation] Test case for validating the common open invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Common Invoice Details ${COMMON_INVOICE_DETAILS}
    Validate Open Invoices Displayed"""
    ],
    'Description': [
        "This test case checks the validation for common open invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Common Open Invoices"
    ]
})

validate_customer_payment_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the customer payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_PAYMENT_DETAILS} customer_payment_details

*** Test Cases ***
Validate Customer Payment
    [Documentation] Test case for validating the customer payment functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Payment Details ${CUSTOMER_PAYMENT_DETAILS}
    Validate Payment Processed"""
    ],
    'Description': [
        "This test case checks the validation for customer payment functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Payment"
    ]
})

validate_integrated_open_invoices_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Open Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the integrated open invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INTEGRATED_INVOICE_DETAILS} integrated_invoice_details

*** Test Cases ***
Validate Integrated Open Invoices
    [Documentation] Test case for validating the integrated open invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Integrated Invoice Details ${INTEGRATED_INVOICE_DETAILS}
    Validate Open Invoices Displayed"""
    ],
    'Description': [
        "This test case checks the validation for integrated open invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Integrated Open Invoices"
    ]
})

validate_payment_status_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Payment Status functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the payment status functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${PAYMENT_STATUS_DETAILS}   payment_status_details

*** Test Cases ***
Validate Payment Status
    [Documentation] Test case for validating the payment status functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Payment Status Details ${PAYMENT_STATUS_DETAILS}
    Validate Payment Status Displayed"""
    ],
    'Description': [
        "This test case checks the validation for payment status functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Payment Status"
    ]
})

validate_nonintegrated_open_invoices_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non-Integrated Open Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the non-integrated open invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${NONINTEGRATED_INVOICE_DETAILS} nonintegrated_invoice_details

*** Test Cases ***
Validate Non-Integrated Open Invoices
    [Documentation] Test case for validating the non-integrated open invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Non-Integrated Invoice Details ${NONINTEGRATED_INVOICE_DETAILS}
    Validate Open Invoices Displayed"""
    ],
    'Description': [
        "This test case checks the validation for non-integrated open invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Non-Integrated Open Invoices"
    ]
})

validate_user_login_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate User Login functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the user login functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${USER_LOGIN_DETAILS}       user_login_details

*** Test Cases ***
Validate User Login
    [Documentation] Test case for validating the user login functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter User Login Details ${USER_LOGIN_DETAILS}
    Validate Login Successful"""
    ],
    'Description': [
        "This test case checks the validation for user login functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate User Login"
    ]
})

validate_omnicorp_autopay_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Omnicorp Autopay functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the omnicorp autopay functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${OMNICORP_AUTOPAY_DETAILS} omnicorp_autopay_details

*** Test Cases ***
Validate Omnicorp Autopay
    [Documentation] Test case for validating the omnicorp autopay functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Omnicorp Autopay Details ${OMNICORP_AUTOPAY_DETAILS}
    Validate Autopay Setup"""
    ],
    'Description': [
        "This test case checks the validation for omnicorp autopay functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Omnicorp Autopay"
    ]
})


validate_omnicorp_autopay_functionality = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Omnicorp Autopay functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the omnicorp autopay functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${OMNICORP_AUTOPAY_DETAILS} omnicorp_autopay_details

*** Test Cases ***
Validate Omnicorp Autopay
    [Documentation] Test case for validating the omnicorp autopay functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Omnicorp Autopay Details ${OMNICORP_AUTOPAY_DETAILS}
    Validate Autopay Setup"""
    ],
    'Description': [
        "This test case checks the validation for omnicorp autopay functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Omnicorp Autopay"
    ]
})

validate_omnicorp_open_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Omnicorp Open Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the omnicorp open invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${OMNICORP_INVOICE_DETAILS} omnicorp_invoice_details

*** Test Cases ***
Validate Omnicorp Open Invoices
    [Documentation] Test case for validating the omnicorp open invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Omnicorp Invoice Details ${OMNICORP_INVOICE_DETAILS}
    Validate Open Invoices Displayed"""
    ],
    'Description': [
        "This test case checks the validation for omnicorp open invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Omnicorp Open Invoices"
    ]
})

validate_omnicorp_scheduled_payments = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Omnicorp Scheduled Payments functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the omnicorp scheduled payments functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${OMNICORP_SCHEDULED_DETAILS} omnicorp_scheduled_details

*** Test Cases ***
Validate Omnicorp Scheduled Payments
    [Documentation] Test case for validating the omnicorp scheduled payments functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Omnicorp Scheduled Details ${OMNICORP_SCHEDULED_DETAILS}
    Validate Scheduled Payments"""
    ],
    'Description': [
        "This test case checks the validation for omnicorp scheduled payments functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Omnicorp Scheduled Payments"
    ]
})

validate_common_api = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Common API functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the common API functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${API_DETAILS}              api_details

*** Test Cases ***
Validate Common API
    [Documentation] Test case for validating the common API functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter API Details ${API_DETAILS}
    Validate API Response"""
    ],
    'Description': [
        "This test case checks the validation for common API functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Common API"
    ]
})

# A D D  A L L  D A T A F R A M E S  T O  T H E  P I P E L I N E
pipeline.add_dataframe(validate_61_90_days_due_invoices_selected)
pipeline.add_dataframe(validate_autopay_functionality)
pipeline.add_dataframe(validate_common_api_functionality)
pipeline.add_dataframe(validate_customer_api_functionality)
pipeline.add_dataframe(validate_invoice_api_functionality)
pipeline.add_dataframe(validate_process_payment_api_functionality)
pipeline.add_dataframe(validate_scheduled_payments_api_functionality)
pipeline.add_dataframe(validate_common_open_invoices_functionality)
pipeline.add_dataframe(validate_customer_payment_functionality)
pipeline.add_dataframe(validate_integrated_open_invoices_functionality)
pipeline.add_dataframe(validate_payment_status_functionality)
pipeline.add_dataframe(validate_nonintegrated_open_invoices_functionality)
pipeline.add_dataframe(validate_user_login_functionality)
pipeline.add_dataframe(validate_omnicorp_autopay_functionality)
pipeline.add_dataframe(validate_omnicorp_open_invoices)
pipeline.add_dataframe(validate_omnicorp_scheduled_payments)
pipeline.add_dataframe(validate_common_api)

# combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = '../json/keywords_payNow.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = '../csv/keywords_payNOW.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")