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

validate_unable_to_process_transaction_with_more_than_due_amount_for_lumpsum = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Unable To Process Transaction With More Than Due Amount For LumpSum functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is unable to process transaction with more than due amount for lump sum functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Unable To Process Transaction With More Than Due Amount For LumpSum
    [Documentation] Test case for validating that the merchant is unable to process transaction with more than due amount for lump sum functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Attempt To Process Transaction With More Than Due Amount For LumpSum
    Validate Transaction Failure"""
    ],
    'Description': [
        "This test case checks the validation for processing transaction with more than due amount for lump sum functionality of the PayNOW datadriver."
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
    Validate Transaction Failure"""
    ],
    'Description': [
        "This test case checks the validation for processing transaction with more than due amount for specific invoice functionality of the PayNOW datadriver."
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

validate_unable_to_process_negative_amount = pd.DataFrame({
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
    Validate Transaction Failure"""
    ],
    'Description': [
        "This test case checks the validation for processing transaction with negative amount due in specific invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Transaction With Negative Amount Due In Specific Invoice"
    ]
})

validate_surcharge_exempt_applied_virtual_terminal = pd.DataFrame({
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
    View Surcharge Exempt Status In Virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for viewing surcharge exempt is applied for customer in virtual terminal functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge Exempt Is Applied For Customer In Virtual Terminal"
    ]
})

validate_view_surcharge_and_change_in_total_amount = pd.DataFrame({
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
    View Surcharge And Total Amount Change"""
    ],
    'Description': [
        "This test case checks the validation for viewing surcharge and change in total amount after selecting multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge And Change In Total Amount After Selecting Multiple Invoices"
    ]
})

validate_view_surcharge_exempt_in_paynow = pd.DataFrame({
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
    View Surcharge Exempt Status In PayNOW"""
    ],
    'Description': [
        "This test case checks the validation for viewing surcharge exempt is applied for customer in PayNOW functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Surcharge Exempt Is Applied For Customer In PayNOW"
    ]
})

validate_custom_date_range_and_view_payment_status_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Custom Date Range And View Payment Status Summary And Payment Date In Grid functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to custom date range and view payment status summary and payment date in grid functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Custom Date Range And View Payment Status Summary And Payment Date In Grid
    [Documentation] Test case for validating that the merchant is able to custom date range and view payment status summary and payment date in grid functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Set Custom Date Range
    View Payment Status Summary And Payment Date In Grid"""
    ],
    'Description': [
        "This test case checks the validation for custom date range and viewing payment status summary and payment date in grid functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Custom Date Range And View Payment Status Summary And Payment Date In Grid"
    ]
})

validate_view_filtered_invoice_in_payment_status = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Filtered Invoice In Payment Status functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view filtered invoice in payment status functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Filtered Invoice In Payment Status
    [Documentation] Test case for validating that the merchant is able to view filtered invoice in payment status functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Apply Invoice Filter
    View Filtered Invoice In Payment Status"""
    ],
    'Description': [
        "This test case checks the validation for viewing filtered invoice in payment status functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Filtered Invoice In Payment Status"
    ]
})

validate_view_received_transactions_payment_status_and_payment_information = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Received Transactions Payment Status And Payment Information (i) In Payment Status functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view received transactions payment status and payment information (i) in payment status functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Received Transactions Payment Status And Payment Information (i) In Payment Status
    [Documentation] Test case for validating that the merchant is able to view received transactions payment status and payment information (i) in payment status functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Received Transactions Payment Status And Payment Information (i) In Payment Status"""
    ],
    'Description': [
        "This test case checks the validation for viewing received transactions payment status and payment information (i) in payment status functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Received Transactions Payment Status And Payment Information (i) In Payment Status"
    ]
})

validate_view_transaction_details_page_from_payment_status = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Transaction Details Page From Payment Status functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view transaction details page from payment status functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Transaction Details Page From Payment Status
    [Documentation] Test case for validating that the merchant is able to view transaction details page from payment status functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Transaction Details Page From Payment Status"""
    ],
    'Description': [
        "This test case checks the validation for viewing transaction details page from payment status functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Transaction Details Page From Payment Status"
    ]
})

validate_view_invoice_details_page_by_clicking_on_invoice_number_in_payment_status = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice Details Page By Clicking On Invoice Number In Payment Status functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view invoice details page by clicking on invoice number in payment status functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate View Invoice Details Page By Clicking On Invoice Number In Payment Status
    [Documentation] Test case for validating that the merchant is able to view invoice details page by clicking on invoice number in payment status functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click On Invoice Number In Payment Status
    View Invoice Details Page"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoice details page by clicking on invoice number in payment status functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoice Details Page By Clicking On Invoice Number In Payment Status"
    ]
})

validate_navigation_to_customer_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details Page By Clicking on Customer functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details page by clicking on customer functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigation to Customer Details
    [Documentation] Test case for validating that merchant is able to navigate to customer details page by clicking on customer functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click on Customer
    Validate Navigation to Customer Details Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details page by clicking on customer functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Navigation to Customer Details"
    ]
})

validate_email_format_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Email Format Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view email format details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Email Format Details
    [Documentation] Test case for validating that merchant is able to view email format details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Email Format Details
    Validate Email Format Details"""
    ],
    'Description': [
        "This test case checks the validation for viewing email format details functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Email Format Details"
    ]
})

validate_navigation_to_customer_details_by_customer_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details Page By Clicking on Customer Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details page by clicking on customer number functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigation to Customer Details by Customer Number
    [Documentation] Test case for validating that merchant is able to navigate to customer details page by clicking on customer number functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click on Customer Number
    Validate Navigation to Customer Details Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details page by clicking on customer number functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Navigation to Customer Details by Customer Number"
    ]
})

validate_navigation_to_customer_details_by_customer_name = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details Page By Clicking on Customer Name functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details page by clicking on customer name functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigation to Customer Details by Customer Name
    [Documentation] Test case for validating that merchant is able to navigate to customer details page by clicking on customer name functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click on Customer Name
    Validate Navigation to Customer Details Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details page by clicking on customer name functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Navigation to Customer Details by Customer Name"
    ]
})

validate_pdf_attached_status_in_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Pdf Attached Status In Email Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view pdf attached status in email details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate PDF Attached Status in Email Details
    [Documentation] Test case for validating that merchant is able to view pdf attached status in email details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Email Details
    Validate PDF Attached Status"""
    ],
    'Description': [
        "This test case checks the validation for viewing pdf attached status in email details functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate PDF Attached Status in Email Details"
    ]
})

validate_verification_of_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Verify Email Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to verify email details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Verification of Email Details
    [Documentation] Test case for validating that merchant is able to verify email details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Email Details
    Validate Email Verification"""
    ],
    'Description': [
        "This test case checks the validation for verifying email details functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Verification of Email Details"
    ]
})

validate_expand_and_collapse_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Expand And Collapse Email Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant is able to expand and collapse email details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${EMAIL_DETAILS}            email_details

*** Test Cases ***
Validate Expand And Collapse Email Details
    [Documentation] Test case for validating that Merchant is able to expand and collapse email details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Expand Email Details ${EMAIL_DETAILS}
    Collapse Email Details ${EMAIL_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for expanding and collapsing email details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Expand And Collapse Email Details"
    ]
})

validate_view_email_details_in_email_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Email Details In Email Summary functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant is able to view email details in email summary functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${EMAIL_SUMMARY}            email_summary

*** Test Cases ***
Validate View Email Details In Email Summary
    [Documentation] Test case for validating that Merchant is able to view email details in email summary functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Email Details In Email Summary ${EMAIL_SUMMARY}"""
    ],
    'Description': [
        "This test case checks the validation for viewing email details in email summary functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Email Details In Email Summary"
    ]
})

validate_view_email_details_in_next_and_previous_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Email Details In Next And Previous Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant is able to view email details in next and previous page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${EMAIL_PAGE}               email_page

*** Test Cases ***
Validate View Email Details In Next And Previous Page
    [Documentation] Test case for validating that Merchant is able to view email details in next and previous page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Email Details In Next And Previous Page ${EMAIL_PAGE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing email details in next and previous page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Email Details In Next And Previous Page"
    ]
})

validate_view_email_details_in_last_and_first_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Email Details In Last And First Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant is able to view email details in last and first page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${EMAIL_PAGE}               email_page

*** Test Cases ***
Validate View Email Details In Last And First Page
    [Documentation] Test case for validating that Merchant is able to view email details in last and first page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    View Email Details In Last And First Page ${EMAIL_PAGE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing email details in last and first page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Email Details In Last And First Page"
    ]
})

validate_reset_filter = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Reset Filter functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant is able to reset filter functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${FILTER}                   filter

*** Test Cases ***
Validate Reset Filter
    [Documentation] Test case for validating that Merchant is able to reset filter functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Reset Filter ${FILTER}"""
    ],
    'Description': [
        "This test case checks the validation for resetting filter functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Reset Filter"
    ]
})

validate_all_active_autopay_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View All Active AutoPay Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings *** 
Documentation          Test cases for validating that merchant is able to view all active AutoPay details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables *** 
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${ACTIVE_AUTOPAY_DETAILS}   active_autopay_details

*** Test Cases *** 
Validate All Active AutoPay Details
    [Documentation] Test case for validating that merchant is able to view all active AutoPay details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To AutoPay Details Page
    Validate Active AutoPay Details ${ACTIVE_AUTOPAY_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing all active AutoPay details for a merchant in the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate All Active AutoPay Details"
    ]
})

validate_all_inactive_autopay_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View All Inactive AutoPay Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings *** 
Documentation          Test cases for validating that merchant is able to view all inactive AutoPay details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables *** 
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INACTIVE_AUTOPAY_DETAILS} inactive_autopay_details

*** Test Cases *** 
Validate All Inactive AutoPay Details
    [Documentation] Test case for validating that merchant is able to view all inactive AutoPay details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To AutoPay Details Page
    Validate Inactive AutoPay Details ${INACTIVE_AUTOPAY_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing all inactive AutoPay details for a merchant in the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate All Inactive AutoPay Details"
    ]
})

validate_filter_auto_pay_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Filter Auto Pay Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to filter Auto Pay details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${FILTER_CRITERIA}          filter_criteria
${FILTERED_AUTOPAY_DETAILS} filtered_autopay_details

*** Test Cases ***
Validate Filter Auto Pay Details
    [Documentation] Test case for validating that merchant is able to filter Auto Pay details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To AutoPay Details Page
    Apply Filter ${FILTER_CRITERIA}
    Validate Filtered AutoPay Details ${FILTERED_AUTOPAY_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for filtering Auto Pay details for a merchant in the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Filter Auto Pay Details"
    ]
})

validate_cancel_autopay = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Cancel AutoPay functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to cancel AutoPay functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details
${AUTOPAY_TO_CANCEL}    autopay_to_cancel
${CANCELLED_AUTOPAY}    cancelled_autopay

*** Test Cases ***
Validate Cancel AutoPay
    [Documentation] Test case for validating that merchant is able to cancel AutoPay functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To AutoPay Details Page
    Cancel AutoPay ${AUTOPAY_TO_CANCEL}
    Validate AutoPay Cancelled ${CANCELLED_AUTOPAY}"""
    ],
    'Description': [
        "This test case checks the validation for cancelling AutoPay for a merchant in the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Cancel AutoPay"
    ]
})

validate_navigation_to_customer_details_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details Page From AutoPay functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details page from AutoPay functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details
${CUSTOMER_DETAILS_PAGE} customer_details_page

*** Test Cases ***
Validate Navigation To Customer Details Page
    [Documentation] Test case for validating that merchant is able to navigate to customer details page from AutoPay functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To AutoPay Details Page
    Navigate To Customer Details Page ${CUSTOMER_DETAILS_PAGE}"""
    ],
    'Description': [
        "This test case checks the validation for navigating to the customer details page from AutoPay for a merchant in the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Navigation To Customer Details Page"
    ]
})

validate_navigation_from_invoice_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Able To Navigate To PayNOW From Invoice Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to PayNOW from invoice details functionality of the PayNOW datadriver.
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details

*** Test Cases ***
Validate Navigation From Invoice Details
    [Documentation] Test case for validating that merchant is able to navigate to PayNOW from invoice details functionality of the PayNOW datadriver.
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Invoice Details
    Navigate To PayNOW From Invoice Details"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to navigate to PayNOW from invoice details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation From Invoice Details"
    ]
})

validate_navigation_from_customer_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To PayNOW From Customer Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to PayNOW from customer details functionality of the PayNOW datadriver.
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details

*** Test Cases ***
Validate Navigation From Customer Details
    [Documentation] Test case for validating that merchant is able to navigate to PayNOW from customer details functionality of the PayNOW datadriver.
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Customer Details
    Navigate To PayNOW From Customer Details"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to navigate to PayNOW from customer details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation From Customer Details"
    ]
})

validate_navigation_from_email = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To PayNOW From Email functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to PayNOW from email functionality of the PayNOW datadriver.
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details

*** Test Cases ***
Validate Navigation From Email
    [Documentation] Test case for validating that merchant is able to navigate to PayNOW from email functionality of the PayNOW datadriver.
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Email
    Navigate To PayNOW From Email"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to navigate to PayNOW from email functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation From Email"
    ]
})

validate_search_invoice_with_invoice_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Search Invoice Details With Invoice Number"
    ],
    'Response': [
        """*** Settings ***
Documentation          Validate Merchant Is Able To Search Invoice Details With Invoice Number
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com
${CUSTOMER_DETAILS}     customer_details

*** Test Cases ***
Validate Merchant Is Able To Search Invoice Details With Invoice Number
    [Documentation] Validate Merchant Is Able To Search Invoice Details With Invoice Number
    Launch Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Search Invoice By Invoice Number
    Validate Invoice Details Displayed"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to search invoice details with invoice number functionality."
    ],
    'Testcase name': [
        "Validate Merchant Is Able To Search Invoice Details With Invoice Number"
    ]
})

validate_search_invoice_with_customer_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Search Invoice Details With Customer Number"
    ],
    'Response': [
        """*** Settings ***
Documentation          Validate Merchant Is Able To Search Invoice Details With Customer Number
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com
${CUSTOMER_DETAILS}     customer_details

*** Test Cases ***
Validate Merchant Is Able To Search Invoice Details With Customer Number
    [Documentation] Validate Merchant Is Able To Search Invoice Details With Customer Number
    Launch Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Search Invoice By Customer Number
    Validate Invoice Details Displayed"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to search invoice details with customer number functionality."
    ],
    'Testcase name': [
        "Validate Merchant Is Able To Search Invoice Details With Customer Number"
    ]
})

validate_search_with_invoice_and_customer_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Search With Invoice And Customer Number"
    ],
    'Response': [
        """*** Settings ***
Documentation          Validate Merchant Is Able To Search With Invoice And Customer Number
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com
${CUSTOMER_DETAILS}     customer_details

*** Test Cases ***
Validate Merchant Is Able To Search With Invoice And Customer Number
    [Documentation] Validate Merchant Is Able To Search With Invoice And Customer Number
    Launch Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Search Invoice By Invoice And Customer Number
    Validate Invoice Details Displayed"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to search with invoice and customer number functionality."
    ],
    'Testcase name': [
        "Validate Merchant Is Able To Search With Invoice And Customer Number"
    ]
})

validate_invoice_summary_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoice, Order Date And Document Type In Invoice Summary"
    ],
    'Response': [
        """*** Settings ***
Documentation          Validate Merchant Is Able To View Invoice, Order Date And Document Type In Invoice Summary
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com
${CUSTOMER_DETAILS}     customer_details

*** Test Cases ***
Validate Merchant Is Able To View Invoice, Order Date And Document Type In Invoice Summary
    [Documentation] Validate Merchant Is Able To View Invoice, Order Date And Document Type In Invoice Summary
    Launch Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    View Invoice Summary
    Validate Invoice, Order Date And Document Type Displayed"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to view invoice, order date, and document type in invoice summary functionality."
    ],
    'Testcase name': [
        "Validate Merchant Is Able To View Invoice, Order Date And Document Type In Invoice Summary"
    ]
})

validate_email_address_in_email_detail = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Email Address In Email Detail"
    ],
    'Response': [
        """*** Settings ***
Documentation          Validate Merchant Is Able To View Email Address In Email Detail
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com
${CUSTOMER_DETAILS}     customer_details

*** Test Cases ***
Validate Merchant Is Able To View Email Address In Email Detail
    [Documentation] Validate Merchant Is Able To View Email Address In Email Detail
    Launch Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    View Email Detail
    Validate Email Address Displayed"""
    ],
    'Description': [
        "This test case checks the validation for merchant's ability to view email address in email detail functionality."
    ],
    'Testcase name': [
        "Validate Merchant Is Able To View Email Address In Email Detail"
    ]
})

validate_sending_invoice_email = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send Invoice Email From Invoice Details Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant Is Able To Send Invoice Email From Invoice Details Page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details
${INVOICE_DETAILS}      invoice_details

*** Test Cases ***
Validate Sending Invoice Email
    [Documentation] Test case for validating that Merchant Is Able To Send Invoice Email From Invoice Details Page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Invoice Details Page
    Click Send Invoice Email
    Validate Email Sent"""
    ],
    'Description': [
        "This test case checks the validation for sending invoice email from invoice details page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Sending Invoice Email"
    ]
})

validate_sending_invoice_email_copy = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Send Invoice Email Copy From Invoice Details Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant Is Able To Send Invoice Email Copy From Invoice Details Page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details
${INVOICE_DETAILS}      invoice_details

*** Test Cases ***
Validate Sending Invoice Email Copy
    [Documentation] Test case for validating that Merchant Is Able To Send Invoice Email Copy From Invoice Details Page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Invoice Details Page
    Click Send Invoice Email Copy
    Validate Email Copy Sent"""
    ],
    'Description': [
        "This test case checks the validation for sending invoice email copy from invoice details page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Sending Invoice Email Copy"
    ]
})

validate_cancelling_send_invoice_email_popup = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Cancel Send Invoice Email Popup functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant Is Able To Cancel Send Invoice Email Popup functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                  https://example.com/paynow
${MERCHANT_DETAILS}     merchant_details
${INVOICE_DETAILS}      invoice_details

*** Test Cases ***
Validate Cancelling Send Invoice Email Popup
    [Documentation] Test case for validating that Merchant Is Able To Cancel Send Invoice Email Popup functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Invoice Details Page
    Click Cancel on Send Invoice Email Popup
    Validate Popup Cancelled"""
    ],
    'Description': [
        "This test case checks the validation for cancelling send invoice email popup functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Cancelling Send Invoice Email Popup"
    ]
})

validate_navigation_to_virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Virtual Terminal By Clicking On Pay Invoice in Invoice Details Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant Is Able To Navigate To Virtual Terminal By Clicking On Pay Invoice in Invoice Details Tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Navigation To Virtual Terminal
    [Documentation] Test case for validating that Merchant Is Able To Navigate To Virtual Terminal By Clicking On Pay Invoice in Invoice Details Tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Invoice Details Tab
    Click Pay Invoice
    Validate Navigation to Virtual Terminal"""
    ],
    'Description': [
        "This test case checks the validation for navigating to virtual terminal by clicking on pay invoice in invoice details tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation To Virtual Terminal"
    ]
})

validate_navigation_to_invoice_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able Navigate To Invoice Page By Clicking On Customer View in Invoice Details Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant Is Able Navigate To Invoice Page By Clicking On Customer View in Invoice Details Page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Navigation To Invoice Page
    [Documentation] Test case for validating that Merchant Is Able Navigate To Invoice Page By Clicking On Customer View in Invoice Details Page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Invoice Details Page
    Click Customer View
    Validate Navigation to Invoice Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice page by clicking on customer view in invoice details page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation To Invoice Page"
    ]
})

validate_navigation_to_invoice_details_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoice Details Page From Invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant Is Able To Navigate To Invoice Details Page From Invoice Page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Navigation To Invoice Details Page
    [Documentation] Test case for validating that Merchant Is Able To Navigate To Invoice Details Page From Invoice Page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Invoice Page
    Click on Invoice
    Validate Navigation to Invoice Details Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice details page from invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation To Invoice Details Page"
    ]
})

validate_navigation_to_customer_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details By Clicking On Customer Name functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that Merchant Is Able To Navigate To Customer Details By Clicking On Customer Name functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigation To Customer Details
    [Documentation] Test case for validating that Merchant Is Able To Navigate To Customer Details By Clicking On Customer Name functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate to Customer Details
    Click on Customer Name
    Validate Navigation to Customer Details"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details by clicking on customer name functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation To Customer Details"
    ]
})

validate_navigation_to_customer_details_from_invoice_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details Page From Invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details page from invoice page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                 https://example.com/paynow
${INVOICE_PAGE}        invoice_page
${CUSTOMER_PAGE}       customer_page

*** Test Cases ***
Validate Navigate to Customer Details Page
    [Documentation] Test case for validating that merchant is able to navigate to customer details page from invoice page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Go To Invoice Page ${INVOICE_PAGE}
    Navigate To Customer Details Page ${CUSTOMER_PAGE}"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details page from invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate Navigate to Customer Details Page"
    ]
})

validate_view_sent_date_and_response_message = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Sent Date And Provider Response Message Of Email functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view sent date and provider response message of email functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                 https://example.com/paynow
${EMAIL_PAGE}          email_page
${SENT_DATE}           sent_date
${RESPONSE_MSG}        response_msg

*** Test Cases ***
Validate View Sent Date and Response Message
    [Documentation] Test case for validating that merchant is able to view sent date and provider response message of email functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Go To Email Page ${EMAIL_PAGE}
    Verify Sent Date ${SENT_DATE}
    Verify Provider Response Message ${RESPONSE_MSG}"""
    ],
    'Description': [
        "This test case checks the validation for viewing sent date and provider response message of email functionality of the PayNOW datadriver."
    ],
    'Testcase Name': [
        "Validate View Sent Date and Response Message"
    ]
})

validate_view_subject_and_sent_address = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Subject And Sent Address Of Email functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view subject and sent address of email functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${EMAIL_PAGE}               email_page
${SUBJECT}                  subject
${SENT_ADDRESS}             sent_address

*** Test Cases ***
Validate View Subject and Sent Address
    [Documentation] Test case for validating that merchant is able to view subject and sent address of email functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Go To Email Page ${EMAIL_PAGE}
    Verify Email Subject ${SUBJECT}
    Verify Sent Address ${SENT_ADDRESS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing subject and sent address of email functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Subject and Sent Address"
    ]
})

validate_view_format_type_for_single_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Format Type For Single Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view format type for single invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INVOICE_PAGE}             invoice_page
${FORMAT_TYPE}              format_type

*** Test Cases ***
Validate View Format Type for Single Invoice
    [Documentation] Test case for validating that merchant is able to view format type for single invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Go To Invoice Page ${INVOICE_PAGE}
    Verify Format Type ${FORMAT_TYPE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing format type for single invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Format Type for Single Invoice"
    ]
})

validate_view_format_type_for_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Format Type For Multiple Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to view format type for multiple invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INVOICE_PAGE}             invoice_page
${FORMAT_TYPE}              format_type

*** Test Cases ***
Validate View Format Type for Multiple Invoices
    [Documentation] Test case for validating that the merchant is able to view format type for multiple invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Go To Invoice Page ${INVOICE_PAGE}
    Verify Format Type ${FORMAT_TYPE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing format type for multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Format Type for Multiple Invoices"
    ]
})

validate_navigate_to_transaction_details_from_pending_payments = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Transaction Details From Pending Payments functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to transaction details from pending payments functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${PENDING_PAYMENTS}         pending_payments
${TRANSACTION_DETAILS}      transaction_details

*** Test Cases ***
Validate Navigate to Transaction Details from Pending Payments
    [Documentation] Test case for validating that merchant is able to navigate to transaction details from pending payments functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Go To Pending Payments ${PENDING_PAYMENTS}
    Navigate To Transaction Details ${TRANSACTION_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for navigating to transaction details from pending payments functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate to Transaction Details from Pending Payments"
    ]
})

validate_navigate_to_customer_details_from_invoice_summary = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details From Invoice Summary functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details from invoice summary functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INVOICE_SUMMARY}          invoice_summary
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate to Customer Details from Invoice Summary
    [Documentation] Test case for validating that merchant is able to navigate to customer details from invoice summary functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Go To Invoice Summary ${INVOICE_SUMMARY}
    Navigate To Customer Details ${CUSTOMER_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details from invoice summary functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate to Customer Details from Invoice Summary"
    ]
})

validate_navigation_to_customer_details_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details Page From Invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details page from invoice page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${CUSTOMER_DETAILS_PAGE}    customer_details_page

*** Test Cases ***
Validate Navigation To Customer Details Page
    [Documentation] Test case for validating that merchant is able to navigate to customer details page from invoice page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Invoice Page
    Click On Customer Name
    Validate Navigation To Customer Details Page ${CUSTOMER_DETAILS_PAGE}"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details page from invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation To Customer Details Page"
    ]
})

validate_email_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Sent Date And Provider Response Message Of Email functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view sent date and provider response message of email functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${EMAIL_DETAILS}            email_details
${SENT_DATE}                sent_date
${PROVIDER_RESPONSE}        provider_response

*** Test Cases ***
Validate Email Details
    [Documentation] Test case for validating that merchant is able to view sent date and provider response message of email functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Email Details ${EMAIL_DETAILS}
    View Sent Date ${SENT_DATE}
    View Provider Response Message ${PROVIDER_RESPONSE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing sent date and provider response message of email functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Email Details"
    ]
})

validate_email_subject_and_sent_address = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Subject And Sent Address Of Email functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view subject and sent address of email functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${EMAIL_DETAILS}            email_details
${SUBJECT}                  subject
${SENT_ADDRESS}             sent_address

*** Test Cases ***
Validate Email Subject And Sent Address
    [Documentation] Test case for validating that merchant is able to view subject and sent address of email functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Email Details ${EMAIL_DETAILS}
    View Subject ${SUBJECT}
    View Sent Address ${SENT_ADDRESS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing subject and sent address of email functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Email Subject And Sent Address"
    ]
})

validate_single_invoice_format_type = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Format Type For Single Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view format type for single invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INVOICE_DETAILS}          invoice_details
${FORMAT_TYPE}              format_type

*** Test Cases ***
Validate Single Invoice Format Type
    [Documentation] Test case for validating that merchant is able to view format type for single invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Invoice Details ${INVOICE_DETAILS}
    View Format Type ${FORMAT_TYPE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing format type for single invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Single Invoice Format Type"
    ]
})

validate_multiple_invoices_format_type = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Format Type For Multiple Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view format type for multiple invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INVOICE_DETAILS}          invoice_details
${FORMAT_TYPE}              format_type

*** Test Cases ***
Validate Multiple Invoices Format Type
    [Documentation] Test case for validating that merchant is able to view format type for multiple invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Invoice Details ${INVOICE_DETAILS}
    View Format Type ${FORMAT_TYPE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing format type for multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Multiple Invoices Format Type"
    ]
})

validate_navigation_to_transaction_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Transaction Details From Pending Payments functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to transaction details from pending payments functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${PENDING_PAYMENTS}         pending_payments
${TRANSACTION_DETAILS}      transaction_details

*** Test Cases ***
Validate Navigation To Transaction Details
    [Documentation] Test case for validating that merchant is able to navigate to transaction details from pending payments functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Pending Payments Details ${PENDING_PAYMENTS}
    Click On Transaction Details
    Validate Navigation To Transaction Details ${TRANSACTION_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for navigating to transaction details from pending payments functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation To Transaction Details"
    ]
})

validate_navigation_to_customer_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Customer Details From Invoice Summary functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to navigate to customer details from invoice summary functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${INVOICE_SUMMARY}          invoice_summary
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigation To Customer Details
    [Documentation] Test case for validating that merchant is able to navigate to customer details from invoice summary functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Invoice Summary Details ${INVOICE_SUMMARY}
    Click On Customer Name
    Validate Navigation To Customer Details ${CUSTOMER_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for navigating to customer details from invoice summary functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigation To Customer Details"
    ]
})

validate_expand_and_collapse_invoice_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able to Expand And Collapse Invoice Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to expand and collapse invoice details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Expand And Collapse Invoice Details
    [Documentation] Test case for validating that merchant is able to expand and collapse invoice details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Expand Invoice Details
    Validate Invoice Details Expanded ${INVOICE_DETAILS}
    Collapse Invoice Details
    Validate Invoice Details Collapsed ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for expanding and collapsing invoice details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Expand And Collapse Invoice Details"
    ]
})

validate_enable_only_show_past_due_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Enable Only show past due invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to enable only show past due invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${PAST_DUE_INVOICES}        past_due_invoices

*** Test Cases ***
Validate Enable Only Show Past Due Invoices
    [Documentation] Test case for validating that merchant is able to enable only show past due invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Enable Only Show Past Due Invoices
    Validate Only Past Due Invoices Shown ${PAST_DUE_INVOICES}"""
    ],
    'Description': [
        "This test case checks the validation for enabling only show past due invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enable Only Show Past Due Invoices"
    ]
})

validate_view_invoices_in_next_and_previous_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoices In Next And Previous Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view invoices in next and previous page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INVOICES_PAGE}            invoices_page

*** Test Cases ***
Validate View Invoices In Next And Previous Page
    [Documentation] Test case for validating that merchant is able to view invoices in next and previous page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Next Page
    Validate Invoices In Next Page ${INVOICES_PAGE}
    Navigate To Previous Page
    Validate Invoices In Previous Page ${INVOICES_PAGE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoices in next and previous page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoices In Next And Previous Page"
    ]
})

validate_view_invoices_in_last_and_first_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Invoices In Last And First Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view invoices in last and first page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INVOICES_PAGE}            invoices_page

*** Test Cases ***
Validate View Invoices In Last And First Page
    [Documentation] Test case for validating that merchant is able to view invoices in last and first page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Last Page Link
    Validate Last Page Invoices Displayed ${INVOICES_PAGE}
    Click First Page Link
    Validate First Page Invoices Displayed ${INVOICES_PAGE}"""
    ],
    'Description': [
        "This test case checks the validation for viewing invoices in last and first page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Invoices In Last And First Page"
    ]
})

validate_filter_invoice_data = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Filter Invoice Data In Invoice Details Grid functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to filter invoice data in invoice details grid functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${INVOICE_FILTER}           invoice_filter

*** Test Cases ***
Validate Filter Invoice Data
    [Documentation] Test case for validating that merchant is able to filter invoice data in invoice details grid functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Apply Invoice Filter ${INVOICE_FILTER}
    Validate Filtered Invoice Data Displayed ${INVOICE_FILTER}"""
    ],
    'Description': [
        "This test case checks the validation for filtering invoice data in invoice details grid functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Filter Invoice Data"
    ]
})

validate_view_email_clicked_date_and_count = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View The Email Clicked Date And Count When It Is Clicked functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view the email clicked date and count when it is clicked functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${EMAIL_CLICKED}            email_clicked

*** Test Cases ***
Validate View Email Clicked Date And Count
    [Documentation] Test case for validating that merchant is able to view the email clicked date and count when it is clicked functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Email Clicked Date Link
    Validate Email Clicked Date And Count Displayed ${EMAIL_CLICKED}"""
    ],
    'Description': [
        "This test case checks the validation for viewing the email clicked date and count when it is clicked functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Email Clicked Date And Count"
    ]
})

validate_view_line_items_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Line Items Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view line items details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${LINE_ITEMS}               line_items

*** Test Cases ***
Validate View Line Items Details
    [Documentation] Test case for validating that merchant is able to view line items details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Line Items Link
    Validate Line Items Details Displayed ${LINE_ITEMS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing line items details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Line Items Details"
    ]
})

validate_view_tracking_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Tracking Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view tracking details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${TRACKING_DETAILS}         tracking_details

*** Test Cases ***
Validate View Tracking Details
    [Documentation] Test case for validating that merchant is able to view tracking details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Tracking Details Link
    Validate Tracking Details Displayed ${TRACKING_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing tracking details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Tracking Details"
    ]
})

validate_view_financial_payments_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Financial Payments Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view financial payments details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${FINANCIAL_PAYMENTS}       financial_payments

*** Test Cases ***
Validate View Financial Payments Details
    [Documentation] Test case for validating that merchant is able to view financial payments details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Financial Payments Link
    Validate Financial Payments Details Displayed ${FINANCIAL_PAYMENTS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing financial payments details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Financial Payments Details"
    ]
})

validate_view_pending_payments_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To View Pending Payments Details functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that merchant is able to view pending payments details functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details
${PENDING_PAYMENTS}         pending_payments

*** Test Cases ***
Validate View Pending Payments Details
    [Documentation] Test case for validating that merchant is able to view pending payments details functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Click Pending Payments Link
    Validate Pending Payments Details Displayed ${PENDING_PAYMENTS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing pending payments details functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Pending Payments Details"
    ]
})

pipeline.add_dataframe(validate_unable_to_process_transaction_with_more_than_due_amount_for_lumpsum)
pipeline.add_dataframe(validate_unable_to_process_transaction_with_more_than_due_amount_for_specific_invoice)
pipeline.add_dataframe(validate_view_searched_with_customer_number)
pipeline.add_dataframe(validate_unable_to_process_negative_amount)
pipeline.add_dataframe(validate_surcharge_exempt_applied_virtual_terminal)
pipeline.add_dataframe(validate_view_surcharge_and_change_in_total_amount)
pipeline.add_dataframe(validate_view_surcharge_exempt_in_paynow)
pipeline.add_dataframe(validate_custom_date_range_and_view_payment_status_summary)
pipeline.add_dataframe(validate_view_filtered_invoice_in_payment_status)
pipeline.add_dataframe(validate_view_received_transactions_payment_status_and_payment_information)
pipeline.add_dataframe(validate_view_invoice_details_page_by_clicking_on_invoice_number_in_payment_status)
pipeline.add_dataframe(validate_navigation_to_customer_details)
pipeline.add_dataframe(validate_email_format_details)
pipeline.add_dataframe(validate_navigation_to_customer_details_by_customer_number)
pipeline.add_dataframe(validate_navigation_to_customer_details_by_customer_name)
pipeline.add_dataframe(validate_pdf_attached_status_in_email_details)
pipeline.add_dataframe(validate_verification_of_email_details)
pipeline.add_dataframe(validate_expand_and_collapse_email_details)
pipeline.add_dataframe(validate_view_email_details_in_email_summary)
pipeline.add_dataframe(validate_view_email_details_in_next_and_previous_page)
pipeline.add_dataframe(validate_view_email_details_in_last_and_first_page)
pipeline.add_dataframe(validate_reset_filter)
pipeline.add_dataframe(validate_all_active_autopay_details)
pipeline.add_dataframe(validate_filter_auto_pay_details)
pipeline.add_dataframe(validate_cancel_autopay)
pipeline.add_dataframe(validate_navigation_to_customer_details_page)
pipeline.add_dataframe(validate_navigation_from_invoice_details)
pipeline.add_dataframe(validate_navigation_from_customer_details)
pipeline.add_dataframe(validate_navigation_from_email)
pipeline.add_dataframe(validate_search_invoice_with_invoice_number)
pipeline.add_dataframe(validate_search_invoice_with_customer_number)
pipeline.add_dataframe(validate_search_with_invoice_and_customer_number)
pipeline.add_dataframe(validate_email_address_in_email_detail)
pipeline.add_dataframe(validate_sending_invoice_email)
pipeline.add_dataframe(validate_sending_invoice_email_copy)
pipeline.add_dataframe(validate_cancelling_send_invoice_email_popup)
pipeline.add_dataframe(validate_navigation_to_virtual_terminal)
pipeline.add_dataframe(validate_navigation_to_invoice_page)
pipeline.add_dataframe(validate_navigation_to_invoice_details_page)
pipeline.add_dataframe(validate_navigation_to_customer_details)
pipeline.add_dataframe(validate_navigation_to_customer_details_from_invoice_page)
pipeline.add_dataframe(validate_view_sent_date_and_response_message)
pipeline.add_dataframe(validate_view_subject_and_sent_address)
pipeline.add_dataframe(validate_view_format_type_for_single_invoice)
pipeline.add_dataframe(validate_view_format_type_for_multiple_invoices)
pipeline.add_dataframe(validate_navigate_to_transaction_details_from_pending_payments)
pipeline.add_dataframe(validate_navigate_to_customer_details_from_invoice_summary)
pipeline.add_dataframe(validate_navigation_to_customer_details_page)
pipeline.add_dataframe(validate_email_details)
pipeline.add_dataframe(validate_email_subject_and_sent_address)
pipeline.add_dataframe(validate_single_invoice_format_type)
pipeline.add_dataframe(validate_multiple_invoices_format_type)
pipeline.add_dataframe(validate_navigation_to_transaction_details)
pipeline.add_dataframe(validate_navigation_to_customer_details)
pipeline.add_dataframe(validate_expand_and_collapse_invoice_details)
pipeline.add_dataframe(validate_enable_only_show_past_due_invoices)
pipeline.add_dataframe(validate_view_invoices_in_next_and_previous_page)
pipeline.add_dataframe(validate_view_invoices_in_last_and_first_page)
pipeline.add_dataframe(validate_filter_invoice_data)
pipeline.add_dataframe(validate_view_email_clicked_date_and_count)
pipeline.add_dataframe(validate_view_line_items_details)
pipeline.add_dataframe(validate_view_tracking_details)
pipeline.add_dataframe(validate_view_financial_payments_details)
pipeline.add_dataframe(validate_view_pending_payments_details)

# combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = '../json/cC3_testcase.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = '../csv/cC3_testcase.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")