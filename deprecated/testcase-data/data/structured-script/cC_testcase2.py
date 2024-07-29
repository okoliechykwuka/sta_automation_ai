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

data_tc_01 = pd.DataFrame({
    "Prompt": ["Generate a robot framework test case for testing to Validate Merchant Is Able To Filter With Customer Number In Failed PayNOW Logins functionality of the PayNOW datadriver."],
    "Response": [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to filter with customer number in failed PayNOW logins functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${MERCHANT_DETAILS}          merchant_details

*** Test Cases ***
Validate Filter With Customer Number In Failed PayNOW Logins
    [Documentation]    Test case for validating that the merchant is able to filter with customer number in failed PayNOW logins functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Merchant Details    ${MERCHANT_DETAILS}
    Filter With Customer Number In Failed PayNOW Logins"""
    ],
    "Description": ["This test case checks the validation for filtering with customer number in failed PayNOW logins functionality of the PayNOW datadriver."],
    "Testcase name": ["Validate Filter With Customer Number In Failed PayNOW Logins"]
})

# TC_02: Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts
validate_able_number = pd.DataFrame({
    "Prompt": ["Generate a robot framework test case for testing to Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts functionality of the PayNOW datadriver."],
    "Response": [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to view number of recent and total login failed attempts functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${MERCHANT_DETAILS}          merchant_details

*** Test Cases ***
Validate View Number Of Recent And Total Login Failed Attempts
    [Documentation]    Test case for validating that the merchant is able to view number of recent and total login failed attempts functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Merchant Details    ${MERCHANT_DETAILS}
    View Number Of Recent And Total Login Failed Attempts"""
    ],
    "Description": ["This test case checks the validation for viewing number of recent and total login failed attempts functionality of the PayNOW datadriver."],
    "Testcase name": ["Validate View Number Of Recent And Total Login Failed Attempts"]
}
)
# TC_03: Validate Merchant Is Able To Expand And Collapse Customer Details In Failed PayNOW Logins
validate_expand_collapse = pd.DataFrame({
    "Prompt": ["Generate a robot framework test case for testing to Validate Merchant Is Able To Expand And Collapse Customer Details In Failed PayNOW Logins functionality of the PayNOW datadriver."],
    "Response": [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to expand and collapse customer details in failed PayNOW logins functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${MERCHANT_DETAILS}          merchant_details

*** Test Cases ***
Validate Expand And Collapse Customer Details In Failed PayNOW Logins
    [Documentation]    Test case for validating that the merchant is able to expand and collapse customer details in failed PayNOW logins functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Merchant Details    ${MERCHANT_DETAILS}
    Expand And Collapse Customer Details In Failed PayNOW Logins"""
    ],
    "Description": ["This test case checks the validation for expanding and collapsing customer details in failed PayNOW logins functionality of the PayNOW datadriver."],
    "Testcase name": ["Validate Expand And Collapse Customer Details In Failed PayNOW Logins"]
})

# TC_04: Validate Merchant Is Able To View First And Last Login Failed Attempt
validate_is_able_view = pd.DataFrame({
    "Prompt": ["Generate a robot framework test case for testing to Validate Merchant Is Able To View First And Last Login Failed Attempt functionality of the PayNOW datadriver."],
    "Response": [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to view first and last login failed attempt functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${MERCHANT_DETAILS}          merchant_details

*** Test Cases ***
Validate View First And Last Login Failed Attempt
    [Documentation]    Test case for validating that the merchant is able to view first and last login failed attempt functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Merchant Details    ${MERCHANT_DETAILS}
    View First And Last Login Failed Attempt"""
    ],
    "Description": ["This test case checks the validation for viewing first and last login failed attempt functionality of the PayNOW datadriver."],
    "Testcase name": ["Validate View First And Last Login Failed Attempt"]
})

# TC_01: Validate Merchant Is Able To Create And View Scheduled Payment Details
validate_create_scheduled = pd.DataFrame({
    "Prompt": ["Generate a robot framework test case for testing to Validate Merchant Is Able To Create And View Scheduled Payment Details functionality of the PayNOW datadriver."],
    "Response": [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to create and view scheduled payment details functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${MERCHANT_DETAILS}          merchant_details

*** Test Cases ***
Validate Create And View Scheduled Payment Details
    [Documentation]    Test case for validating that the merchant is able to create and view scheduled payment details functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Merchant Details    ${MERCHANT_DETAILS}
    Create Scheduled Payment
    View Scheduled Payment Details"""
    ],
    "Description": ["This test case checks the validation for creating and viewing scheduled payment details functionality of the PayNOW datadriver."],
    "Testcase name": ["Validate Create And View Scheduled Payment Details"]
})

# TC_02: Validate Merchant Is Able To Navigate To Customer Details From Scheduled Payments
validate_navigate_details = pd.DataFrame({
    "Prompt": ["Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details From Scheduled Payments functionality of the PayNOW datadriver."],
    "Response": [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to navigate to customer details from scheduled payments functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${MERCHANT_DETAILS}          merchant_details

*** Test Cases ***
Validate Navigate To Customer Details From Scheduled Payments
    [Documentation]    Test case for validating that the merchant is able to navigate to customer details from scheduled payments functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Merchant Details    ${MERCHANT_DETAILS}
    Navigate To Customer Details From Scheduled Payments"""
    ],
    "Description": ["This test case checks the validation for navigating to customer details from scheduled payments functionality of the PayNOW datadriver."],
    "Testcase name": ["Validate Navigate To Customer Details From Scheduled Payments"]
})

# TC_03: Validate Merchant Is Able To Navigate To Invoice Details Page From Scheduled Payments
validate_invoice_detail_page = pd.DataFrame({
    "Prompt": ["Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoice Details Page From Scheduled Payments functionality of the PayNOW datadriver."],
    "Response": [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to navigate to invoice details page from scheduled payments functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${MERCHANT_DETAILS}          merchant_details

*** Test Cases ***
Validate Navigate To Invoice Details Page From Scheduled Payments
    [Documentation]    Test case for validating that the merchant is able to navigate to invoice details page from scheduled payments functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Merchant Details    ${MERCHANT_DETAILS}
    Navigate To Invoice Details Page From Scheduled Payments"""
    ],
    "Description": ["This test case checks the validation for navigating to invoice details page from scheduled payments functionality of the PayNOW datadriver."],
    "Testcase name": ["Validate Navigate To Invoice Details Page From Scheduled Payments"]
})

validate_unable_to_process_transaction_with_more_than_due_amount_for_lumpsum = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To Process Transaction With More Than Due Amount For LumpSum functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to process transaction with more than due amount for LumpSum functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Unable To Process Transaction With More Than Due Amount For LumpSum
    [Documentation] Test case for validating that the merchant is unable to process transaction with more than due amount for LumpSum functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Attempt To Process Transaction With More Than Due Amount For LumpSum
    Validate Transaction Rejected"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process transaction with more than due amount for LumpSum functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Transaction With More Than Due Amount For LumpSum"
    ]
})

validate_unable_to_process_transaction_with_more_than_due_amount_for_specific_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To Process Transaction With More Than Due Amount for Specific Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to process transaction with more than due amount for specific invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Unable To Process Transaction With More Than Due Amount for Specific Invoice
    [Documentation] Test case for validating that the merchant is unable to process transaction with more than due amount for specific invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Attempt To Process Transaction With More Than Due Amount for Specific Invoice
    Validate Transaction Rejected"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process transaction with more than due amount for specific invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Transaction With More Than Due Amount for Specific Invoice"
    ]
})

validate_view_searched_with_customer_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Searched With Customer Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view searched with customer number functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Searched With Customer Number
    [Documentation] Test case for validating that the merchant is able to view searched with customer number functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Search With Customer Number
    Validate Search Results"""
    ],
    'Description': [
        "This test case checks the validation for viewing searched with customer number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Searched With Customer Number"
    ]
})

validate_unable_to_process_transaction_with_negative_amount_due_in_specific_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To Process Transaction With Negative Amount Due In Specific Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to process transaction with negative amount due in specific invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Unable To Process Transaction With Negative Amount Due In Specific Invoice
    [Documentation] Test case for validating that the merchant is unable to process transaction with negative amount due in specific invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Attempt To Process Transaction With Negative Amount Due In Specific Invoice
    Validate Transaction Rejected"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process transaction with negative amount due in specific invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Transaction With Negative Amount Due In Specific Invoice"
    ]
})

validate_view_surcharge_exempt_is_applied_for_customer_in_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Surcharge Exempt Is Applied For Customer In Virtual Terminal functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view surcharge exempt is applied for customer in virtual terminal functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Surcharge Exempt Is Applied For Customer In Virtual Terminal
    [Documentation] Test case for validating that the merchant is able to view surcharge exempt is applied for customer in virtual terminal functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Surcharge Exempt Applied In Virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for viewing surcharge exempt is applied for customer in virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge Exempt Is Applied For Customer In Virtual Terminal"
    ]
})

validate_view_surcharge_and_change_in_total_amount_after_selecting_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Surcharge And Change In Total Amount After Selecting Multiple Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view surcharge and change in total amount after selecting multiple invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Surcharge And Change In Total Amount After Selecting Multiple Invoices
    [Documentation] Test case for validating that the merchant is able to view surcharge and change in total amount after selecting multiple invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Select Multiple Invoices
    View Surcharge And Change In Total Amount"""
    ],
    'Description': [
        "This test case checks the validation for viewing surcharge and change in total amount after selecting multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge And Change In Total Amount After Selecting Multiple Invoices"
    ]
})

validate_view_surcharge_exempt_is_applied_for_customer_in_paynow = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Surcharge Exempt Is Applied For Customer In PayNOW functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view surcharge exempt is applied for customer in PayNOW functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Surcharge Exempt Is Applied For Customer In PayNOW
    [Documentation] Test case for validating that the merchant is able to view surcharge exempt is applied for customer in PayNOW functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Surcharge Exempt Applied In PayNOW"""
    ],
    'Description': [
        "This test case checks the validation for viewing surcharge exempt is applied for customer in PayNOW functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge Exempt Is Applied For Customer In PayNOW"
    ]
})

validate_view_invoices_count_and_status_for_successful_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoices Count And Status For Successful Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoices count and status for successful transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoices Count And Status For Successful Transaction
    [Documentation] Test case for validating that the merchant is able to view invoices count and status for successful transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoices Count And Status For Successful Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoices count and status for successful transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoices Count And Status For Successful Transaction"
    ]
})

validate_view_invoices_count_and_status_for_declined_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoices Count And Status For Declined Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoices count and status for declined transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoices Count And Status For Declined Transaction
    [Documentation] Test case for validating that the merchant is able to view invoices count and status for declined transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoices Count And Status For Declined Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoices count and status for declined transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoices Count And Status For Declined Transaction"
    ]
})

validate_view_transaction_details_after_processing_from_paynow = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Details after Processing From PayNow functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction details after processing from PayNow functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Details After Processing From PayNow
    [Documentation] Test case for validating that the merchant is able to view transaction details after processing from PayNow functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Details After Processing From PayNow"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction details after processing from PayNow functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Details After Processing From PayNow"
    ]
})

validate_view_method_after_ach_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Method After ACH Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view method after ACH transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Method After ACH Transaction
    [Documentation] Test case for validating that the merchant is able to view method after ACH transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Method After ACH Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing method after ACH transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Method After ACH Transaction"
    ]
})

validate_view_total_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Total Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view total invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Total Invoices
    [Documentation] Test case for validating that the merchant is able to view total invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Total Invoices"""
    ],
    'Description': [
        "This test case checks the validation for viewing total invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Total Invoices"
    ]
})

validate_send_email_for_selected_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send Email For the Selected Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to send email for the selected invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Send Email For the Selected Invoice
    [Documentation] Test case for validating that the merchant is able to send email for the selected invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Send Email For the Selected Invoice"""
    ],
    'Description': [
        "This test case checks the validation for sending email for the selected invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Send Email For the Selected Invoice"
    ]
})

validate_send_a_copy_of_receipt = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send A Copy Of Receipt functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to send a copy of receipt functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Send A Copy Of Receipt
    [Documentation] Test case for validating that the merchant is able to send a copy of receipt functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Send A Copy Of Receipt"""
    ],
    'Description': [
        "This test case checks the validation for sending a copy of receipt functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Send A Copy Of Receipt"
    ]
})

validate_send_email_for_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send Email for Multiple Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to send email for multiple invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Send Email for Multiple Invoices
    [Documentation] Test case for validating that the merchant is able to send email for multiple invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Send Email for Multiple Invoices"""
    ],
    'Description': [
        "This test case checks the validation for sending email for multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Send Email for Multiple Invoices"
    ]
})

validate_cancel_send_invoice_receipt = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Cancel Send Invoice Receipt functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to cancel send invoice receipt functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Cancel Send Invoice Receipt
    [Documentation] Test case for validating that the merchant is able to cancel send invoice receipt functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Cancel Send Invoice Receipt"""
    ],
    'Description': [
        "This test case checks the validation for canceling send invoice receipt functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Cancel Send Invoice Receipt"
    ]
})


validate_navigate_to_transaction_details_from_transaction_tab = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Transaction Details From Transaction Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to transaction details from transaction tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Transaction Details From Transaction Tab
    [Documentation] Test case for validating that the merchant is able to navigate to transaction details from transaction tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Transaction Details From Transaction Tab"""
    ],
    'Description': [
        "This test case checks the validation for navigating to transaction details from transaction tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Transaction Details From Transaction Tab"
    ]
})


validate_credit_card_surcharge_after_enabling_and_disabling_exempt_surcharge_for_a_customer = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Credit Card Surcharge After Enabling And Disabling Exempt Surcharge for A Customer functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to validate credit card surcharge after enabling and disabling exempt surcharge for a customer functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Credit Card Surcharge After Enabling And Disabling Exempt Surcharge for A Customer
    [Documentation] Test case for validating that the merchant is able to validate credit card surcharge after enabling and disabling exempt surcharge for a customer functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Validate Credit Card Surcharge After Enabling And Disabling Exempt Surcharge for A Customer"""
    ],
    'Description': [
        "This test case checks the validation for credit card surcharge after enabling and disabling exempt surcharge for a customer functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Credit Card Surcharge After Enabling And Disabling Exempt Surcharge for A Customer"
    ]
})

validate_invoice_email_after_enabling_and_disabling_pdf_setting = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Invoice Email After Enabling And Disabling PDF Setting functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to validate invoice email after enabling and disabling PDF setting functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Invoice Email After Enabling And Disabling PDF Setting
    [Documentation] Test case for validating that the merchant is able to validate invoice email after enabling and disabling PDF setting functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Validate Invoice Email After Enabling And Disabling PDF Setting"""
    ],
    'Description': [
        "This test case checks the validation for invoice email after enabling and disabling PDF setting functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Invoice Email After Enabling And Disabling PDF Setting"
    ]
})

validate_enable_and_disable_override_payment_method_by_customer = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Enable And Disable Override Payment Method By Customer functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to enable and disable override payment method by customer functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Enable And Disable Override Payment Method By Customer
    [Documentation] Test case for validating that the merchant is able to enable and disable override payment method by customer functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Enable And Disable Override Payment Method By Customer"""
    ],
    'Description': [
        "This test case checks the validation for enabling and disabling override payment method by customer functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enable And Disable Override Payment Method By Customer"
    ]
})

validate_enable_and_disable_customize_by_transaction_source = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Enable And Disable Customize By Transaction Source functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to enable and disable customize by transaction source functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Enable And Disable Customize By Transaction Source
    [Documentation] Test case for validating that the merchant is able to enable and disable customize by transaction source functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Enable And Disable Customize By Transaction Source"""
    ],
    'Description': [
        "This test case checks the validation for enabling and disabling customize by transaction source functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enable And Disable Customize By Transaction Source"
    ]
})

validate_view_invoice_number_and_email_format_in_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Number And Email Format In Email Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice number and email format in email details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Number And Email Format In Email Details
    [Documentation] Test case for validating that the merchant is able to view invoice number and email format in email details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoice Number And Email Format In Email Details"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice number and email format in email details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Number And Email Format In Email Details"
    ]
})

validate_view_provider_response_message_and_date_sent_in_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Provider Response Message And Date Sent In Email Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view provider response message and date sent in email details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Provider Response Message And Date Sent In Email Details
    [Documentation] Test case for validating that the merchant is able to view provider response message and date sent in email details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Provider Response Message And Date Sent In Email Details"""
    ],
    'Description': [
        "This test case checks the validation for viewing provider response message and date sent in email details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Provider Response Message And Date Sent In Email Details"
    ]
})

validate_view_multiple_invoices_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Multiple Invoices Email Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view multiple invoices email details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Multiple Invoices Email Details
    [Documentation] Test case for validating that the merchant is able to view multiple invoices email details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Multiple Invoices Email Details"""
    ],
    'Description': [
        "This test case checks the validation for viewing multiple invoices email details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Multiple Invoices Email Details"
    ]
})

validate_view_account_number_in_custom_fields = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Account Number In Custom Fields functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view account number in custom fields functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Account Number In Custom Fields
    [Documentation] Test case for validating that the merchant is able to view account number in custom fields functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Account Number In Custom Fields"""
    ],
    'Description': [
        "This test case checks the validation for viewing account number in custom fields functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Account Number In Custom Fields"
    ]
})

validate_enter_amount_to_pay_and_notes_in_specific_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Enter Amount To Pay And Notes In Specific Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to enter amount to pay and notes in specific invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Enter Amount To Pay And Notes In Specific Invoice
    [Documentation] Test case for validating that the merchant is able to enter amount to pay and notes in specific invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Enter Amount To Pay And Notes In Specific Invoice"""
    ],
    'Description': [
        "This test case checks the validation for entering amount to pay and notes in specific invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enter Amount To Pay And Notes In Specific Invoice"
    ]
})

validate_total_amount_updated_as_per_changes_in_invoices_due_amount = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Total Amount Is Updated As Per The changes in Invoices Due Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the total amount is updated as per the changes in invoices due amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Total Amount Is Updated As Per The changes in Invoices Due Amount
    [Documentation] Test case for validating that the total amount is updated as per the changes in invoices due amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Validate Total Amount Is Updated As Per The changes in Invoices Due Amount"""
    ],
    'Description': [
        "This test case checks the validation for updating total amount as per the changes in invoices due amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Total Amount Is Updated As Per The changes in Invoices Due Amount"
    ]
})

validate_view_invoice_count_in_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Count In Virtual Terminal functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice count in virtual terminal functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Count In Virtual Terminal
    [Documentation] Test case for validating that the merchant is able to view invoice count in virtual terminal functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoice Count In Virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice count in virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Count In Virtual Terminal"
    ]
})

validate_process_payment_by_selecting_apply_to_oldest = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Process Payment By Selecting Apply To Oldest functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to process payment by selecting apply to oldest functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Process Payment By Selecting Apply To Oldest
    [Documentation] Test case for validating that the merchant is able to process payment by selecting apply to oldest functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Select Apply To Oldest
    Process Payment"""
    ],
    'Description': [
        "This test case checks the validation for processing payment by selecting apply to oldest functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment By Selecting Apply To Oldest"
    ]
})

validate_process_payment_by_selecting_non_applied_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Process Payment By Selecting Non-Applied Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to process payment by selecting non-applied payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Process Payment By Selecting Non-Applied Payment
    [Documentation] Test case for validating that the merchant is able to process payment by selecting non-applied payment functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Select Non-Applied Payment
    Process Payment"""
    ],
    'Description': [
        "This test case checks the validation for processing payment by selecting non-applied payment functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment By Selecting Non-Applied Payment"
    ]
})

validate_process_payment_by_selecting_specific_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Process Payment By Selecting Specific Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to process payment by selecting specific invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Process Payment By Selecting Specific Invoice
    [Documentation] Test case for validating that the merchant is able to process payment by selecting specific invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Select Specific Invoice
    Process Payment"""
    ],
    'Description': [
        "This test case checks the validation for processing payment by selecting specific invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment By Selecting Specific Invoice"
    ]
})

validate_view_transaction_details_after_processing_form_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Details after Processing Form Virtual Terminal functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction details after processing form virtual terminal functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Details After Processing Form Virtual Terminal
    [Documentation] Test case for validating that the merchant is able to view transaction details after processing form virtual terminal functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Details After Processing"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction details after processing form virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Details After Processing Form Virtual Terminal"
    ]
})

validate_view_saved_credit_card_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Saved Credit Card Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view saved credit card details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Saved Credit Card Details
    [Documentation] Test case for validating that the merchant is able to view saved credit card details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Saved Credit Card Details"""
    ],
    'Description': [
        "This test case checks the validation for viewing saved credit card details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Saved Credit Card Details"
    ]
})

validate_view_saved_ach_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Saved ACH Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view saved ACH details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Saved ACH Details
    [Documentation] Test case for validating that the merchant is able to view saved ACH details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Saved ACH Details"""
    ],
    'Description': [
        "This test case checks the validation for viewing saved ACH details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Saved ACH Details"
    ]
})

validate_process_payment_through_saved_payment_method = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Process Payment Through Saved Payment Method functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to process payment through saved payment method functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Process Payment Through Saved Payment Method
    [Documentation] Test case for validating that the merchant is able to process payment through saved payment method functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Payment Through Saved Payment Method"""
    ],
    'Description': [
        "This test case checks the validation for processing payment through saved payment method functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment Through Saved Payment Method"
    ]
})

validate_delete_saved_payment_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Delete Saved Payment Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to delete saved payment details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Delete Saved Payment Details
    [Documentation] Test case for validating that the merchant is able to delete saved payment details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Delete Saved Payment Details"""
    ],
    'Description': [
        "This test case checks the validation for deleting saved payment details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Delete Saved Payment Details"
    ]
})

validate_navigate_to_invoices_tab_and_view_open_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoices Tab And View Open Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to invoices tab and view open invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Invoices Tab And View Open Invoices
    [Documentation] Test case for validating that the merchant is able to navigate to invoices tab and view open invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Invoices Tab
    View Open Invoices"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoices tab and viewing open invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Invoices Tab And View Open Invoices"
    ]
})

validate_view_only_past_due_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Only Past Due Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view only past due invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Only Past Due Invoices
    [Documentation] Test case for validating that the merchant is able to view only past due invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Only Past Due Invoices"""
    ],
    'Description': [
        "This test case checks the validation for viewing only past due invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Only Past Due Invoices"
    ]
})

validate_navigate_to_invoice_page_from_invoice_tab = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoice Page From Invoice Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to invoice page from invoice tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Invoice Page From Invoice Tab
    [Documentation] Test case for validating that the merchant is able to navigate to invoice page from invoice tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Invoice Page From Invoice Tab"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice page from invoice tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Invoice Page From Invoice Tab"
    ]
})

validate_navigate_to_invoice_delivery_tab = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoice Delivery Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to invoice delivery tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Invoice Delivery Tab
    [Documentation] Test case for validating that the merchant is able to navigate to invoice delivery tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Invoice Delivery Tab"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice delivery tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Invoice Delivery Tab"
    ]
})

validate_change_data_range_after_selecting_all_for_time_period_select_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Change Data Range After Selecting All For Time Period Select Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to change data range after selecting all for time period select invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Change Data Range After Selecting All For Time Period Select Invoices
    [Documentation] Test case for validating that the merchant is able to change data range after selecting all for time period select invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Change Data Range After Selecting All For Time Period Select Invoices"""
    ],
    'Description': [
        "This test case checks the validation for changing data range after selecting all for time period select invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Change Data Range After Selecting All For Time Period Select Invoices"
    ]
})

validate_disable_send_email_receipt = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Disable Send Email Receipt functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to disable send email receipt functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Disable Send Email Receipt
    [Documentation] Test case for validating that the merchant is able to disable send email receipt functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Disable Send Email Receipt"""
    ],
    'Description': [
        "This test case checks the validation for disabling send email receipt functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Disable Send Email Receipt"
    ]
})

validate_send_email_receipt_in_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send Email Receipt In Virtual Terminal functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to send email receipt in virtual terminal functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Send Email Receipt In Virtual Terminal
    [Documentation] Test case for validating that the merchant is able to send email receipt in virtual terminal functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Send Email Receipt In Virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for sending email receipt in virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Send Email Receipt In Virtual Terminal"
    ]
})

validate_error_message_when_process_payment_without_selecting_country = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To get Error Message When Process Payment Without Selecting Country functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to get error message when process payment without selecting country functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Error Message When Process Payment Without Selecting Country
    [Documentation] Test case for validating that the merchant is able to get error message when process payment without selecting country functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Payment Without Selecting Country
    Validate Error Message"""
    ],
    'Description': [
        "This test case checks the validation for getting an error message when processing payment without selecting country functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Error Message When Process Payment Without Selecting Country"
    ]
})

validate_error_message_when_process_payment_without_entering_amount = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Error Message When Process Payment Without Entering Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view error message when process payment without entering amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Error Message When Process Payment Without Entering Amount
    [Documentation] Test case for validating that the merchant is able to view error message when process payment without entering amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Payment Without Entering Amount
    Validate Error Message"""
    ],
    'Description': [
        "This test case checks the validation for viewing an error message when processing payment without entering amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Error Message When Process Payment Without Entering Amount"
    ]
})

validate_resend_receipt_with_valid_email_id_in_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Resend Receipt With Valid Email id In virtual Terminal functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to resend receipt with valid email id in virtual terminal functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Resend Receipt With Valid Email id In virtual Terminal
    [Documentation] Test case for validating that the merchant is able to resend receipt with valid email id in virtual terminal functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Resend Receipt With Valid Email id In virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for resending receipt with valid email id in virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Resend Receipt With Valid Email id In virtual Terminal"
    ]
})

validate_cancel_resend_receipt = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Cancel Resend Receipt functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to cancel resend receipt functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Cancel Resend Receipt
    [Documentation] Test case for validating that the merchant is able to cancel resend receipt functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Cancel Resend Receipt"""
    ],
    'Description': [
        "This test case checks the validation for cancelling resend receipt functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Cancel Resend Receipt"
    ]
})

validate_send_copy_email_receipt_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send A Copy Email Receipt In virtual Terminal functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to send a copy email receipt in virtual terminal functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Send A Copy Email Receipt In virtual Terminal
    [Documentation] Test case for validating that the merchant is able to send a copy email receipt in virtual terminal functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Send A Copy Email Receipt In virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for sending a copy email receipt in virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Send A Copy Email Receipt In virtual Terminal"
    ]
})

validate_close_transaction_confirmation_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able Close Transaction Confirmation Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to close transaction confirmation page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Close Transaction Confirmation Page
    [Documentation] Test case for validating that the merchant is able to close transaction confirmation page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Close Transaction Confirmation Page"""
    ],
    'Description': [
        "This test case checks the validation for closing transaction confirmation page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Close Transaction Confirmation Page"
    ]
})

validate_navigate_to_resent_invoice_tab = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Resent Invoice Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to resent invoice tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Resent Invoice Tab
    [Documentation] Test case for validating that the merchant is able to navigate to resent invoice tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Resent Invoice Tab"""
    ],
    'Description': [
        "This test case checks the validation for navigating to resent invoice tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Resent Invoice Tab"
    ]
})

validate_add_record = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Add Record functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to add record functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Add Record
    [Documentation] Test case for validating that the merchant is able to add record functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Add Record"""
    ],
    'Description': [
        "This test case checks the validation for adding record functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Add Record"
    ]
})

validate_prevent_override = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Prevent Override functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to prevent override functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Prevent Override
    [Documentation] Test case for validating that the merchant is able to prevent override functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Prevent Override"""
    ],
    'Description': [
        "This test case checks the validation for preventing override functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Prevent Override"
    ]
})

validate_edit_record = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Edit Record functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to edit record functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Edit Record
    [Documentation] Test case for validating that the merchant is able to edit record functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Edit Record"""
    ],
    'Description': [
        "This test case checks the validation for editing record functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Edit Record"
    ]
})

validate_view_invoice_data_with_date_filter = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Data With Date Filter In Virtual Terminal functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice data with date filter in virtual terminal functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Data With Date Filter In Virtual Terminal
    [Documentation] Test case for validating that the merchant is able to view invoice data with date filter in virtual terminal functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoice Data With Date Filter In Virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice data with date filter in virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Data With Date Filter In Virtual Terminal"
    ]
})

validate_select_all_invoices_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Select All Invoices In Virtual Terminal Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to select all invoices in virtual terminal tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Select All Invoices In Virtual Terminal Tab
    [Documentation] Test case for validating that the merchant is able to select all invoices in virtual terminal tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Select All Invoices In Virtual Terminal Tab"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoices in virtual terminal tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select All Invoices In Virtual Terminal Tab"
    ]
})

validate_view_customer_information = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Customer Information functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view customer information functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Customer Information
    [Documentation] Test case for validating that the merchant is able to view customer information functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Customer Information"""
    ],
    'Description': [
        "This test case checks the validation for viewing customer information functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Customer Information"
    ]
})

validate_view_surcharge_exempt_in_customer_information = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Surcharge Exempt In Customer Information functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view surcharge exempt in customer information functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Surcharge Exempt In Customer Information
    [Documentation] Test case for validating that the merchant is able to view surcharge exempt in customer information functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Surcharge Exempt In Customer Information"""
    ],
    'Description': [
        "This test case checks the validation for viewing surcharge exempt in customer information functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge Exempt In Customer Information"
    ]
})

validate_view_on_credit_hold_customers = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View On Credit Hold Customers functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view on credit hold customers functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View On Credit Hold Customers
    [Documentation] Test case for validating that the merchant is able to view on credit hold customers functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View On Credit Hold Customers"""
    ],
    'Description': [
        "This test case checks the validation for viewing on credit hold customers functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View On Credit Hold Customers"
    ]
})

validate_unable_to_view_invoices_in_paynow_when_disputed_is_enabled = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To View Invoices In PayNOW When Disputed Is Enabled functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to view invoices in PayNOW when disputed is enabled functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Unable To View Invoices In PayNOW When Disputed Is Enabled
    [Documentation] Test case for validating that the merchant is unable to view invoices in PayNOW when disputed is enabled functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Validate Unable To View Invoices In PayNOW When Disputed Is Enabled"""
    ],
    'Description': [
        "This test case checks the validation for being unable to view invoices in PayNOW when disputed is enabled functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To View Invoices In PayNOW When Disputed Is Enabled"
    ]
})

validate_view_invoices_in_paynow_when_disputed_is_disabled = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoices In PayNOW When Disputed Is Disabled functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoices in PayNOW when disputed is disabled functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoices In PayNOW When Disputed Is Disabled
    [Documentation] Test case for validating that the merchant is able to view invoices in PayNOW when disputed is disabled functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoices In PayNOW When Disputed Is Disabled"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoices in PayNOW when disputed is disabled functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoices In PayNOW When Disputed Is Disabled"
    ]
})

validate_view_average_invoice_age_and_credit_limit_in_customer_dashboard = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Average Invoice Age And Credit Limit In Customer Dashboard functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view average invoice age and credit limit in customer dashboard functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Average Invoice Age And Credit Limit In Customer Dashboard
    [Documentation] Test case for validating that the merchant is able to view average invoice age and credit limit in customer dashboard functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Average Invoice Age And Credit Limit In Customer Dashboard"""
    ],
    'Description': [
        "This test case checks the validation for viewing average invoice age and credit limit in customer dashboard functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Average Invoice Age And Credit Limit In Customer Dashboard"
    ]
})

validate_view_invoice_date_and_due_date_in_invoice_details_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Date And Due Date In Invoice Details Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice date and due date in invoice details page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Date And Due Date In Invoice Details Page
    [Documentation] Test case for validating that the merchant is able to view invoice date and due date in invoice details page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoice Date And Due Date In Invoice Details Page"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice date and due date in invoice details page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Date And Due Date In Invoice Details Page"
    ]
})

validate_view_days_overdue_and_due_amount_in_invoice_details_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Days Overdue And Due Amount In Invoice Details Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view days overdue and due amount in invoice details page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Days Overdue And Due Amount In Invoice Details Page
    [Documentation] Test case for validating that the merchant is able to view days overdue and due amount in invoice details page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Days Overdue And Due Amount In Invoice Details Page"""
    ],
    'Description': [
        "This test case checks the validation for viewing days overdue and due amount in invoice details page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Days Overdue And Due Amount In Invoice Details Page"
    ]
})

validate_view_email_clicked_date_and_count_in_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Email Clicked Date And Count In Email Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view email clicked date and count in email details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Email Clicked Date And Count In Email Details
    [Documentation] Test case for validating that the merchant is able to view email clicked date and count in email details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Email Clicked Date And Count In Email Details"""
    ],
    'Description': [
        "This test case checks the validation for viewing email clicked date and count in email details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Email Clicked Date And Count In Email Details"
    ]
})

validate_view_credit_count_and_credit_amount = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Credit Count And Credit Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view credit count and credit amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Credit Count And Credit Amount
    [Documentation] Test case for validating that the merchant is able to view credit count and credit amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Credit Count And Credit Amount"""
    ],
    'Description': [
        "This test case checks the validation for viewing credit count and credit amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Credit Count And Credit Amount"
    ]
})

validate_cancel_payment_method = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Cancel Payment Method functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to cancel payment method functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Cancel Payment Method
    [Documentation] Test case for validating that the merchant is able to cancel payment method functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Cancel Payment Method"""
    ],
    'Description': [
        "This test case checks the validation for canceling payment method functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Cancel Payment Method"
    ]
})

validate_add_new_payment_method_when_one_exists = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Add New Payment Method When One Exists functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to add new payment method when one exists functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Add New Payment Method When One Exists
    [Documentation] Test case for validating that the merchant is able to add new payment method when one exists functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Add New Payment Method When One Exists"""
    ],
    'Description': [
        "This test case checks the validation for adding new payment method when one exists functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Add New Payment Method When One Exists"
    ]
})

validate_enable_multiple_pdfs_in_emails = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Enable Multiple PDFs In Emails functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to enable multiple PDFs in emails functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Enable Multiple PDFs In Emails
    [Documentation] Test case for validating that the merchant is able to enable multiple PDFs in emails functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Enable Multiple PDFs In Emails"""
    ],
    'Description': [
        "This test case checks the validation for enabling multiple PDFs in emails functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enable Multiple PDFs In Emails"
    ]
})

pipeline.add_dataframe(data_tc_01)
pipeline.add_dataframe(validate_able_number)
pipeline.add_dataframe(validate_expand_collapse)
pipeline.add_dataframe(validate_is_able_view)
pipeline.add_dataframe(validate_create_scheduled)
pipeline.add_dataframe(validate_navigate_details)
pipeline.add_dataframe(validate_invoice_detail_page)
pipeline.add_dataframe(validate_unable_to_process_transaction_with_more_than_due_amount_for_lumpsum)
pipeline.add_dataframe(validate_unable_to_process_transaction_with_more_than_due_amount_for_specific_invoice)
pipeline.add_dataframe(validate_view_searched_with_customer_number)
pipeline.add_dataframe(validate_unable_to_process_transaction_with_negative_amount_due_in_specific_invoice)
pipeline.add_dataframe(validate_view_surcharge_exempt_is_applied_for_customer_in_virtual_terminal)
pipeline.add_dataframe(validate_view_surcharge_and_change_in_total_amount_after_selecting_multiple_invoices)
pipeline.add_dataframe(validate_view_surcharge_exempt_is_applied_for_customer_in_paynow)
pipeline.add_dataframe(validate_view_invoices_count_and_status_for_successful_transaction)
pipeline.add_dataframe(validate_view_invoices_count_and_status_for_declined_transaction)
pipeline.add_dataframe(validate_view_transaction_details_after_processing_from_paynow)
pipeline.add_dataframe(validate_view_method_after_ach_transaction)
pipeline.add_dataframe(validate_view_total_invoices)
pipeline.add_dataframe(validate_send_email_for_selected_invoice)
pipeline.add_dataframe(validate_send_a_copy_of_receipt)
pipeline.add_dataframe(validate_send_email_for_multiple_invoices)
pipeline.add_dataframe(validate_cancel_send_invoice_receipt)
pipeline.add_dataframe(validate_navigate_to_transaction_details_from_transaction_tab)
pipeline.add_dataframe(validate_credit_card_surcharge_after_enabling_and_disabling_exempt_surcharge_for_a_customer)
pipeline.add_dataframe(validate_invoice_email_after_enabling_and_disabling_pdf_setting)
pipeline.add_dataframe(validate_enable_and_disable_override_payment_method_by_customer)
pipeline.add_dataframe(validate_enable_and_disable_customize_by_transaction_source)
pipeline.add_dataframe(validate_view_invoice_number_and_email_format_in_email_details)
pipeline.add_dataframe(validate_view_provider_response_message_and_date_sent_in_email_details)
pipeline.add_dataframe(validate_view_multiple_invoices_email_details)
pipeline.add_dataframe(validate_view_account_number_in_custom_fields)
pipeline.add_dataframe(validate_enter_amount_to_pay_and_notes_in_specific_invoice)
pipeline.add_dataframe(validate_total_amount_updated_as_per_changes_in_invoices_due_amount)
pipeline.add_dataframe(validate_view_invoice_count_in_virtual_terminal)
pipeline.add_dataframe(validate_process_payment_by_selecting_apply_to_oldest)
pipeline.add_dataframe(validate_process_payment_by_selecting_non_applied_payment)
pipeline.add_dataframe(validate_process_payment_by_selecting_specific_invoice)
pipeline.add_dataframe(validate_view_transaction_details_after_processing_form_virtual_terminal)
pipeline.add_dataframe(validate_view_saved_credit_card_details)
pipeline.add_dataframe(validate_view_saved_ach_details)
pipeline.add_dataframe(validate_process_payment_through_saved_payment_method)
pipeline.add_dataframe(validate_delete_saved_payment_details)
pipeline.add_dataframe(validate_navigate_to_invoices_tab_and_view_open_invoices)
pipeline.add_dataframe(validate_view_only_past_due_invoices)
pipeline.add_dataframe(validate_navigate_to_invoice_page_from_invoice_tab)
pipeline.add_dataframe(validate_navigate_to_invoice_delivery_tab)
pipeline.add_dataframe(validate_change_data_range_after_selecting_all_for_time_period_select_invoices)
pipeline.add_dataframe(validate_disable_send_email_receipt)
pipeline.add_dataframe(validate_send_email_receipt_in_virtual_terminal)
pipeline.add_dataframe(validate_error_message_when_process_payment_without_selecting_country)
pipeline.add_dataframe(validate_error_message_when_process_payment_without_entering_amount)
pipeline.add_dataframe(validate_resend_receipt_with_valid_email_id_in_virtual_terminal)
pipeline.add_dataframe(validate_cancel_resend_receipt)
pipeline.add_dataframe(validate_send_copy_email_receipt_virtual_terminal)
pipeline.add_dataframe(validate_close_transaction_confirmation_page)
pipeline.add_dataframe(validate_navigate_to_resent_invoice_tab)
pipeline.add_dataframe(validate_add_record)
pipeline.add_dataframe(validate_prevent_override)
pipeline.add_dataframe(validate_edit_record)
pipeline.add_dataframe(validate_view_invoice_data_with_date_filter)
pipeline.add_dataframe(validate_select_all_invoices_virtual_terminal)
pipeline.add_dataframe(validate_view_customer_information)
pipeline.add_dataframe(validate_view_surcharge_exempt_in_customer_information)
pipeline.add_dataframe(validate_view_on_credit_hold_customers)
pipeline.add_dataframe(validate_unable_to_view_invoices_in_paynow_when_disputed_is_enabled)
pipeline.add_dataframe(validate_view_invoices_in_paynow_when_disputed_is_disabled)
pipeline.add_dataframe(validate_view_average_invoice_age_and_credit_limit_in_customer_dashboard)
pipeline.add_dataframe(validate_view_invoice_date_and_due_date_in_invoice_details_page)
pipeline.add_dataframe(validate_view_days_overdue_and_due_amount_in_invoice_details_page)
pipeline.add_dataframe(validate_view_email_clicked_date_and_count_in_email_details)
pipeline.add_dataframe(validate_view_credit_count_and_credit_amount)
pipeline.add_dataframe(validate_cancel_payment_method)
pipeline.add_dataframe(validate_add_new_payment_method_when_one_exists)
pipeline.add_dataframe(validate_enable_multiple_pdfs_in_emails)

# combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = '../json/cC_testcase_data.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = '../csv/cC_testcase_data.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")
