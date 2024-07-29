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

validate_transaction_summary_view = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Number(#) And Amount($) Of Invoices, Credit Cards, And ACH Transactions In Transaction Summary functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view number(#) and amount($) of invoices, credit cards, and ACH transactions in transaction summary functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Transaction Summary View
    [Documentation] Test case for validating that the merchant is able to view number(#) and amount($) of invoices, credit cards, and ACH transactions in transaction summary functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Number And Amount Of Transactions Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing number(#) and amount($) of invoices, credit cards, and ACH transactions in transaction summary functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Transaction Summary View"
    ]
})

validate_navigate_to_customer_details_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details Page By Clicking On Customer Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to customer details page by clicking on customer number functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Customer Details Page
    [Documentation] Test case for validating that the merchant is able to navigate to customer details page by clicking on customer number functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Customer Number
    Validate Navigation To Customer Details Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details page by clicking on customer number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Customer Details Page"
    ]
})

validate_view_total_transactions_in_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Total Number(#) And Amount($) Of Transactions In The Transaction Summary functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the total number(#) and amount($) of transactions in the transaction summary functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Total Transactions In Summary
    [Documentation] Test case for validating that the merchant is able to view the total number(#) and amount($) of transactions in the transaction summary functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Total Number And Amount Of Transactions Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the total number(#) and amount($) of transactions in the transaction summary functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Total Transactions In Summary"
    ]
})

validate_view_change_in_transaction_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Change In Transaction Amount($) And Count(#) After One Process Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the change in transaction amount($) and count(#) after one process transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Change In Transaction Summary
    [Documentation] Test case for validating that the merchant is able to view the change in transaction amount($) and count(#) after one process transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process A Transaction
    View Transaction Summary
    Validate Change In Number And Amount Of Transactions Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the change in transaction amount($) and count(#) after one process transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Change In Transaction Summary"
    ]
})

validate_matrix_count_with_transactions_list_count = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate The Matrix Count(#) With The Transactions list Count functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the matrix count(#) matches with the transactions list count functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Matrix Count With Transactions List Count
    [Documentation] Test case for validating that the matrix count(#) matches with the transactions list count functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Matrix Count Matches Transactions List Count"""
    ],
    'Description': [
        "This test case checks the validation for matching the matrix count(#) with the transactions list count functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Matrix Count With Transactions List Count"
    ]
})

validate_auto_applied_checkbox_for_oldest_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Auto Applied Checkbox Checked For Apply To Oldest Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view auto applied checkbox checked for apply to oldest transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Auto Applied Checkbox For Oldest Transaction
    [Documentation] Test case for validating that the merchant is able to view auto applied checkbox checked for apply to oldest transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Auto Applied Checkbox Checked For Oldest Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing auto applied checkbox checked for apply to oldest transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Auto Applied Checkbox For Oldest Transaction"
    ]
})

validate_auto_applied_checkbox_for_specific_invoice_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Auto Applied Checkbox Checked For Specific Invoice Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view auto applied checkbox checked for specific invoice transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Auto Applied Checkbox For Specific Invoice Transaction
    [Documentation] Test case for validating that the merchant is able to view auto applied checkbox checked for specific invoice transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Auto Applied Checkbox Checked For Specific Invoice Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing auto applied checkbox checked for specific invoice transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Auto Applied Checkbox For Specific Invoice Transaction"
    ]
})

validate_ach_or_check_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View ACHorcheck Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view ACHorcheck transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View ACHorcheck Transaction
    [Documentation] Test case for validating that the merchant is able to view ACHorcheck transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate ACHorcheck Transaction Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing ACHorcheck transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View ACHorcheck Transaction"
    ]
})

validate_credit_card_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Credit Card Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view credit card transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Credit Card Transaction
    [Documentation] Test case for validating that the merchant is able to view credit card transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Credit Card Transaction Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing credit card transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Credit Card Transaction"
    ]
})

validate_transactions_after_navigation = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transactions After Navigating To Next Page And Previous Page In Grid functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transactions after navigating to next page and previous page in grid functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transactions After Page Navigation
    [Documentation] Test case for validating that the merchant is able to view transactions after navigating to next page and previous page in grid functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Next Page
    Navigate To Previous Page
    Validate Transactions Displayed After Page Navigation"""
    ],
    'Description': [
        "This test case checks the validation for viewing transactions after navigating to next page and previous page in grid functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transactions After Page Navigation"
    ]
})

validate_paid_ach_change = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Change In Paid ACH Count(#) And Amount($) After One Process Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the change in paid ACH count(#) and amount($) after one process transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Change In Paid ACH Count And Amount
    [Documentation] Test case for validating that the merchant is able to view the change in paid ACH count(#) and amount($) after one process transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process A Transaction
    View Transaction Summary
    Validate Change In Paid ACH Count And Amount"""
    ],
    'Description': [
        "This test case checks the validation for viewing the change in paid ACH count(#) and amount($) after one process transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Change In Paid ACH Count And Amount"
    ]
})

validate_paid_invoices_change = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Change In Paid Invoices Count(#) And Amount($) After One Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the change in paid invoices count(#) and amount($) after one transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Change In Paid Invoices Count And Amount
    [Documentation] Test case for validating that the merchant is able to view the change in paid invoices count(#) and amount($) after one transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process A Transaction
    View Transaction Summary
    Validate Change In Paid Invoices Count And Amount"""
    ],
    'Description': [
        "This test case checks the validation for viewing the change in paid invoices count(#) and amount($) after one transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Change In Paid Invoices Count And Amount"
    ]
})

validate_custom_date_range_and_view_transactions_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Custom Date Range And View Transactions Summary And Payment Date In Grid functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to custom date range and view transactions summary and payment date in grid functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Custom Date Range And View Transactions Summary
    [Documentation] Test case for validating that the merchant is able to custom date range and view transactions summary and payment date in grid functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Set Custom Date Range
    View Transaction Summary
    Validate Transactions Summary And Payment Date In Grid"""
    ],
    'Description': [
        "This test case checks the validation for custom date range and view transactions summary and payment date in grid functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Custom Date Range And View Transactions Summary"
    ]
})

validate_view_transaction_payment_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Payment Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction payment date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Payment Date
    [Documentation] Test case for validating that the merchant is able to view transaction payment date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Transaction Payment Date"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction payment date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Payment Date"
    ]
})

validate_view_invoice_count_successful_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Count For Successful Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice count for successful transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Count For Successful Transaction
    [Documentation] Test case for validating that the merchant is able to view invoice count for successful transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Invoice Count For Successful Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice count for successful transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Count For Successful Transaction"
    ]
})

validate_view_invoice_count_declined_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Count For A Declined Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice count for a declined transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Count For Declined Transaction
    [Documentation] Test case for validating that the merchant is able to view invoice count for a declined transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Invoice Count For Declined Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice count for a declined transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Count For Declined Transaction"
    ]
})

validate_view_invoices_count_multiple_transactions = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoices Count For Multiple Transactions functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoices count for multiple transactions functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoices Count For Multiple Transactions
    [Documentation] Test case for validating that the merchant is able to view invoices count for multiple transactions functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Invoices Count For Multiple Transactions"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoices count for multiple transactions functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoices Count For Multiple Transactions"
    ]
})

validate_view_partial_transactions_with_achorecheck = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Partial Transactions Processed With ACHorEcheck functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view partial transactions processed with ACHorEcheck functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Partial Transactions With ACHorEcheck
    [Documentation] Test case for validating that the merchant is able to view partial transactions processed with ACHorEcheck functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Partial Transactions With ACHorEcheck"""
    ],
    'Description': [
        "This test case checks the validation for viewing partial transactions processed with ACHorEcheck functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Partial Transactions With ACHorEcheck"
    ]
})

validate_view_partial_transactions_with_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Partial Transactions Processed With Credit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view partial transactions processed with credit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Partial Transactions With Credit Card
    [Documentation] Test case for validating that the merchant is able to view partial transactions processed with credit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Partial Transactions With Credit Card"""
    ],
    'Description': [
        "This test case checks the validation for viewing partial transactions processed with credit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Partial Transactions With Credit Card"
    ]
})

validate_view_payment_status_in_grid = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Payment Status In Grid functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view payment status in grid functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Payment Status In Grid
    [Documentation] Test case for validating that the merchant is able to view payment status in grid functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Payment Status In Grid"""
    ],
    'Description': [
        "This test case checks the validation for viewing payment status in grid functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Payment Status In Grid"
    ]
})

validate_send_receipt_with_valid_email_id = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send Receipt With Valid Email id functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to send receipt with valid email id functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${EMAIL}                    email@example.com

*** Test Cases ***
Validate Send Receipt With Valid Email id
    [Documentation] Test case for validating that the merchant is able to send receipt with valid email id functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Send Receipt ${EMAIL}
    Validate Receipt Sent"""
    ],
    'Description': [
        "This test case checks the validation for sending receipt with valid email id functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Send Receipt With Valid Email id"
    ]
})

validate_navigate_to_transaction_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Transaction Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to transaction details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Transaction Details
    [Documentation] Test case for validating that the merchant is able to navigate to transaction details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Transaction Details
    Validate Transaction Details Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to transaction details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Transaction Details"
    ]
})

validate_view_payment_type_details_for_ach_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Payment Type Details In Transaction Summary For ACH Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view payment type details in transaction summary for ACH payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Payment Type Details For ACH Payment
    [Documentation] Test case for validating that the merchant is able to view payment type details in transaction summary for ACH payment functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Payment Type Details For ACH Payment"""
    ],
    'Description': [
        "This test case checks the validation for viewing payment type details in transaction summary for ACH payment functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Payment Type Details For ACH Payment"
    ]
})

validate_view_payment_type_details_for_credit_card_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Payment Type Details In Transaction Summary For Credit Card Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view payment type details in transaction summary for credit card payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Payment Type Details For Credit Card Payment
    [Documentation] Test case for validating that the merchant is able to view payment type details in transaction summary for credit card payment functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Payment Type Details For Credit Card Payment"""
    ],
    'Description': [
        "This test case checks the validation for viewing payment type details in transaction summary for credit card payment functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Payment Type Details For Credit Card Payment"
    ]
})

validate_view_custom_fields_and_billing_info_in_transaction_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Custom Fields And Billing Info In Transaction Summary functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view custom fields and billing info in transaction summary functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Custom Fields And Billing Info In Transaction Summary
    [Documentation] Test case for validating that the merchant is able to view custom fields and billing info in transaction summary functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Custom Fields And Billing Info Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing custom fields and billing info in transaction summary functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Custom Fields And Billing Info In Transaction Summary"
    ]
})

validate_view_transaction_summary_for_approved_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Summary For Approved Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction summary for approved transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Summary For Approved Transaction
    [Documentation] Test case for validating that the merchant is able to view transaction summary for approved transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Approved Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction summary for approved transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Summary For Approved Transaction"
    ]
})

validate_view_transaction_summary_for_declined_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Summary For Declined Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction summary for declined transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Summary For Declined Transaction
    [Documentation] Test case for validating that the merchant is able to view transaction summary for declined transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Declined Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction summary for declined transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Summary For Declined Transaction"
    ]
})

validate_view_filtered_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Filtered Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view filtered transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${FILTER_CRITERIA}          filter_criteria

*** Test Cases ***
Validate View Filtered Transaction
    [Documentation] Test case for validating that the merchant is able to view filtered transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Apply Filter ${FILTER_CRITERIA}
    View Filtered Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing filtered transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Filtered Transaction"
    ]
})

validate_sort_transactions_by_type = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Sort Transactions By Type functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to sort transactions by type functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Sort Transactions By Type
    [Documentation] Test case for validating that the merchant is able to sort transactions by type functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Sort Transactions By Type
    Validate Sorted Transactions"""
    ],
    'Description': [
        "This test case checks the validation for sorting transactions by type functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Sort Transactions By Type"
    ]
})

validate_view_surcharge_amount_not_applied_for_ach_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Surcharge Amount Is Not Applied For ACH Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the surcharge amount is not applied for ACH transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Surcharge Amount Not Applied For ACH Transaction
    [Documentation] Test case for validating that the merchant is able to view the surcharge amount is not applied for ACH transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate No Surcharge For ACH Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing the surcharge amount is not applied for ACH transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge Amount Not Applied For ACH Transaction"
    ]
})

validate_view_surcharge_amount_applied_for_credit_card_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Surcharge Amount Applied For Credit Card Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the surcharge amount applied for credit card transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Surcharge Amount Applied For Credit Card Transaction
    [Documentation] Test case for validating that the merchant is able to view the surcharge amount applied for credit card transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Surcharge Amount For Credit Card Transaction"""
    ],
    'Description': [
        "This test case checks the validation for viewing the surcharge amount applied for credit card transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge Amount Applied For Credit Card Transaction"
    ]
})

validate_view_items_per_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Items Per Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view items per page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Items Per Page
    [Documentation] Test case for validating that the merchant is able to view items per page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Items Per Page
    Validate Items Per Page Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing items per page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Items Per Page"
    ]
})


validate_view_invoice_details_in_all_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Details In All Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice details in all transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Details In All Transaction
    [Documentation] Test case for validating that the merchant is able to view invoice details in all transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoice Details
    Validate Invoice Details Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice details in all transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Details In All Transaction"
    ]
})


validate_collapse_invoice_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Collapse Invoice Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to collapse invoice details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Collapse Invoice Details
    [Documentation] Test case for validating that the merchant is able to collapse invoice details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Collapse Invoice Details
    Validate Invoice Details Collapsed"""
    ],
    'Description': [
        "This test case checks the validation for collapsing invoice details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Collapse Invoice Details"
    ]
})

validate_navigate_to_invoice_details_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoice Details Page By Clicking On Invoice Number In All Transactions functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to invoice details page by clicking on invoice number in all transactions functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Invoice Details Page
    [Documentation] Test case for validating that the merchant is able to navigate to invoice details page by clicking on invoice number in all transactions functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Invoice Number
    Validate Navigation To Invoice Details Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice details page by clicking on invoice number in all transactions functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Invoice Details Page"
    ]
})

validate_cancel_send_receipt_popup = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Cancel Send Receipt Popup functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to cancel send receipt popup functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Cancel Send Receipt Popup
    [Documentation] Test case for validating that the merchant is able to cancel send receipt popup functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Open Send Receipt Popup
    Cancel Send Receipt Popup
    Validate Popup Canceled"""
    ],
    'Description': [
        "This test case checks the validation for canceling send receipt popup functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Cancel Send Receipt Popup"
    ]
})

validate_view_alert_popup_to_void_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Alert Popup To Void Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view alert popup to void transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Alert Popup To Void Transaction
    [Documentation] Test case for validating that the merchant is able to view alert popup to void transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Void Transaction
    Validate Alert Popup Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing alert popup to void transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Alert Popup To Void Transaction"
    ]
})

validate_view_avs_and_cvv_response_code_for_card_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View AVS And CVV Response Code For Card Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view AVS and CVV response code for card payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View AVS And CVV Response Code For Card Payment
    [Documentation] Test case for validating that the merchant is able to view AVS and CVV response code for card payment functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Card Payment Details
    Validate AVS And CVV Response Code"""
    ],
    'Description': [
        "This test case checks the validation for viewing AVS and CVV response code for card payment functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View AVS And CVV Response Code For Card Payment"
    ]
})

validate_view_transaction_summary_for_master_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Summary For Master Credit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction summary for Master credit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Summary For Master Credit Card
    [Documentation] Test case for validating that the merchant is able to view transaction summary for Master credit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Master Credit Card Transactions"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction summary for Master credit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Summary For Master Credit Card"
    ]
})

validate_view_transaction_summary_for_visa_debit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Summary For Visa Debit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction summary for Visa debit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Summary For Visa Debit Card
    [Documentation] Test case for validating that the merchant is able to view transaction summary for Visa debit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Visa Debit Card Transactions"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction summary for Visa debit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Summary For Visa Debit Card"
    ]
})

validate_view_amount_split_up_in_transaction_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Amount Split up In Transaction Summary functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the amount split up in transaction summary functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Amount Split Up In Transaction Summary
    [Documentation] Test case for validating that the merchant is able to view the amount split up in transaction summary functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Amount Split Up Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the amount split up in transaction summary functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Amount Split Up In Transaction Summary"
    ]
})

validate_view_settled_amount_for_successful_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Settled Amount For Successful Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view settled amount for successful transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Settled Amount For Successful Transaction
    [Documentation] Test case for validating that the merchant is able to view settled amount for successful transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate Settled Amount Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing settled amount for successful transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Settled Amount For Successful Transaction"
    ]
})

validate_view_settled_amount_for_declined_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To View Settled Amount For Declined Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to view settled amount for declined transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Settled Amount For Declined Transaction
    [Documentation] Test case for validating that the merchant is unable to view settled amount for declined transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate No Settled Amount For Declined Transaction"""
    ],
    'Description': [
        "This test case checks the validation for not viewing settled amount for declined transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Settled Amount For Declined Transaction"
    ]
})

validate_view_settled_amount_for_partial_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To View Settled Amount For Partial Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to view settled amount for partial transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Settled Amount For Partial Transaction
    [Documentation] Test case for validating that the merchant is unable to view settled amount for partial transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Summary
    Validate No Settled Amount For Partial Transaction"""
    ],
    'Description': [
        "This test case checks the validation for not viewing settled amount for partial transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Settled Amount For Partial Transaction"
    ]
})


validate_view_surcharge_amount_information = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Surcharge Amount Information (i) functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the surcharge amount information (i) functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View The Surcharge Amount Information (i)
    [Documentation] Test case for validating that the merchant is able to view the surcharge amount information (i) functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Surcharge Amount Information (i)
    Validate Surcharge Amount Information Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the surcharge amount information (i) functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View The Surcharge Amount Information (i)"
    ]
})


validate_view_change_due_amount_partial_payment_ach = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Change In Due Amount After Processing Partial Payment Using ACH functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the change in due amount after processing partial payment using ACH functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Change In Due Amount After Partial Payment Using ACH
    [Documentation] Test case for validating that the merchant is able to view the change in due amount after processing partial payment using ACH functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Partial Payment Using ACH
    Validate Change In Due Amount Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the change in due amount after processing partial payment using ACH functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Change In Due Amount After Partial Payment Using ACH"
    ]
})

validate_view_change_due_amount_full_payment_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Change In Due Amount After Full Payment Using Credit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the change in due amount after full payment using credit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Change In Due Amount After Full Payment Using Credit Card
    [Documentation] Test case for validating that the merchant is able to view the change in due amount after full payment using credit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Full Payment Using Credit Card
    Validate Change In Due Amount Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the change in due amount after full payment using credit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Change In Due Amount After Full Payment Using Credit Card"
    ]
})


validate_view_invoice_details_after_processing_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Invoice Details After Processing Multiple Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the invoice details after processing multiple invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Details After Processing Multiple Invoices
    [Documentation] Test case for validating that the merchant is able to view the invoice details after processing multiple invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Multiple Invoices
    Validate Invoice Details Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the invoice details after processing multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Details After Processing Multiple Invoices"
    ]
})


validate_view_payment_application_option_when_processed_through_specific_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Payment Application Option When Processed Through Specific Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view payment application option when processed through specific invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Payment Application Option When Processed Through Specific Invoice
    [Documentation] Test case for validating that the merchant is able to view payment application option when processed through specific invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Payment Through Specific Invoice
    Validate Payment Application Option Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing payment application option when processed through specific invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Payment Application Option When Processed Through Specific Invoice"
    ]
})

validate_view_payment_application_option_when_processed_through_lump_sum = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Payment Application Option When Processed Through Lump Sum functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view payment application option when processed through lump sum functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Payment Application Option When Processed Through Lump Sum
    [Documentation] Test case for validating that the merchant is able to view payment application option when processed through lump sum functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Process Payment Through Lump Sum
    Validate Payment Application Option Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing payment application option when processed through lump sum functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Payment Application Option When Processed Through Lump Sum"
    ]
})

validate_view_invoice_payment_details_tab = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Payment Details Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice payment details tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Payment Details Tab
    [Documentation] Test case for validating that the merchant is able to view invoice payment details tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Invoice Payment Details Tab"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice payment details tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Payment Details Tab"
    ]
})

validate_navigate_to_invoice_details_page_from_invoice_payment_details_tab = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoice Details Page From Invoice Payment Details Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to invoice details page from invoice payment details tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Invoice Details Page From Invoice Payment Details Tab
    [Documentation] Test case for validating that the merchant is able to navigate to invoice details page from invoice payment details tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Invoice Details Page From Invoice Payment Details Tab"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice details page from invoice payment details tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Invoice Details Page From Invoice Payment Details Tab"
    ]
})

validate_view_approved_transactions = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Approved Transactions functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view approved transactions functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Approved Transactions
    [Documentation] Test case for validating that the merchant is able to view approved transactions functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Approved Transactions"""
    ],
    'Description': [
        "This test case checks the validation for viewing approved transactions functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Approved Transactions"
    ]
})

validate_view_not_approved_transactions = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Not Approved Transactions functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view not approved transactions functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Not Approved Transactions
    [Documentation] Test case for validating that the merchant is able to view not approved transactions functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Not Approved Transactions"""
    ],
    'Description': [
        "This test case checks the validation for viewing not approved transactions functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Not Approved Transactions"
    ]
})

validate_view_refunded_amount_after_void_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Refunded Amount After Void Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view the refunded amount after void transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Refunded Amount After Void Transaction
    [Documentation] Test case for validating that the merchant is able to view the refunded amount after void transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Void Transaction
    Validate Refunded Amount Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing the refunded amount after void transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Refunded Amount After Void Transaction"
    ]
})

validate_unable_to_void_payment_second_time_for_same_transaction = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To Void Payment Second Time For The Same Transaction functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to void payment second time for the same transaction functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Unable To Void Payment Second Time For Same Transaction
    [Documentation] Test case for validating that the merchant is unable to void payment second time for the same transaction functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Void Transaction
    Attempt To Void Same Transaction Again
    Validate Unable To Void Second Time"""
    ],
    'Description': [
        "This test case checks the validation for not being able to void payment a second time for the same transaction functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Void Payment Second Time For Same Transaction"
    ]
})


pipeline.add_dataframe(validate_transaction_summary_view)
pipeline.add_dataframe(validate_navigate_to_customer_details_page)
pipeline.add_dataframe(validate_view_total_transactions_in_summary)
pipeline.add_dataframe(validate_view_change_in_transaction_summary)
pipeline.add_dataframe(validate_matrix_count_with_transactions_list_count)
pipeline.add_dataframe(validate_auto_applied_checkbox_for_oldest_transaction)
pipeline.add_dataframe(validate_auto_applied_checkbox_for_specific_invoice_transaction)
pipeline.add_dataframe(validate_ach_or_check_transaction)
pipeline.add_dataframe(validate_credit_card_transaction)
pipeline.add_dataframe(validate_transactions_after_navigation)
pipeline.add_dataframe(validate_paid_ach_change)
pipeline.add_dataframe(validate_paid_invoices_change)
pipeline.add_dataframe(validate_custom_date_range_and_view_transactions_summary)
pipeline.add_dataframe(validate_view_transaction_payment_date)
pipeline.add_dataframe(validate_view_invoice_count_successful_transaction)
pipeline.add_dataframe(validate_view_invoice_count_declined_transaction)
pipeline.add_dataframe(validate_view_invoices_count_multiple_transactions)
pipeline.add_dataframe(validate_view_partial_transactions_with_achorecheck)
pipeline.add_dataframe(validate_view_partial_transactions_with_credit_card)
pipeline.add_dataframe(validate_view_payment_status_in_grid)
pipeline.add_dataframe(validate_send_receipt_with_valid_email_id)
pipeline.add_dataframe(validate_navigate_to_transaction_details)
pipeline.add_dataframe(validate_view_payment_type_details_for_ach_payment)
pipeline.add_dataframe(validate_view_payment_type_details_for_credit_card_payment)
pipeline.add_dataframe(validate_view_custom_fields_and_billing_info_in_transaction_summary)
pipeline.add_dataframe(validate_view_transaction_summary_for_approved_transaction)
pipeline.add_dataframe(validate_view_transaction_summary_for_declined_transaction)
pipeline.add_dataframe(validate_view_filtered_transaction)
pipeline.add_dataframe(validate_sort_transactions_by_type)
pipeline.add_dataframe(validate_view_surcharge_amount_not_applied_for_ach_transaction)
pipeline.add_dataframe(validate_view_surcharge_amount_applied_for_credit_card_transaction)
pipeline.add_dataframe(validate_view_items_per_page)
pipeline.add_dataframe(validate_view_invoice_details_in_all_transaction)
pipeline.add_dataframe(validate_collapse_invoice_details)
pipeline.add_dataframe(validate_navigate_to_invoice_details_page)
pipeline.add_dataframe(validate_cancel_send_receipt_popup)
pipeline.add_dataframe(validate_view_alert_popup_to_void_transaction)
pipeline.add_dataframe(validate_view_avs_and_cvv_response_code_for_card_payment)
pipeline.add_dataframe(validate_view_transaction_summary_for_master_credit_card)
pipeline.add_dataframe(validate_view_transaction_summary_for_visa_debit_card)
pipeline.add_dataframe(validate_view_amount_split_up_in_transaction_summary)
pipeline.add_dataframe(validate_view_settled_amount_for_successful_transaction)
pipeline.add_dataframe(validate_view_settled_amount_for_declined_transaction)
pipeline.add_dataframe(validate_view_settled_amount_for_partial_transaction)
pipeline.add_dataframe(validate_view_surcharge_amount_information)
pipeline.add_dataframe(validate_view_change_due_amount_partial_payment_ach)
pipeline.add_dataframe(validate_view_change_due_amount_full_payment_credit_card)
pipeline.add_dataframe(validate_view_invoice_details_after_processing_multiple_invoices)
pipeline.add_dataframe(validate_view_payment_application_option_when_processed_through_specific_invoice)
pipeline.add_dataframe(validate_view_payment_application_option_when_processed_through_lump_sum)
pipeline.add_dataframe(validate_view_invoice_payment_details_tab)
pipeline.add_dataframe(validate_navigate_to_invoice_details_page_from_invoice_payment_details_tab)
pipeline.add_dataframe(validate_view_approved_transactions)
pipeline.add_dataframe(validate_view_not_approved_transactions)
pipeline.add_dataframe(validate_view_refunded_amount_after_void_transaction)
pipeline.add_dataframe(validate_unable_to_void_payment_second_time_for_same_transaction)


# combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = '../json/centralClient_test.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = '../csv/centralClient_test.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")