import pandas as pd
import json
from testcase_pipeline import TestCasePipeline

pipeline = TestCasePipeline()

validate_unable_to_create_autopay_past_500_days = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Unable To Create AutoPay For The Invoices that Past 500 days functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to create AutoPay for the invoices that past 500 days functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Unable To Create AutoPay For The Invoices that Past 500 days
    [Documentation] Test case for validating that the customer is unable to create AutoPay for the invoices that past 500 days functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Create AutoPay For Past 500 Days Invoices ${INVOICE_DETAILS}
    Validate Unable To Create AutoPay"""
    ],
    'Description': [
        "This test case checks the validation for being unable to create AutoPay for the invoices that past 500 days functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Create AutoPay For The Invoices that Past 500 days"
    ]
})

validate_unable_to_create_autopay_due_more_than_31_days = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Unable To Create AutoPay For The Invoices That Due More Than 31 Days functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to create AutoPay for the invoices that due more than 31 days functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Unable To Create AutoPay For The Invoices That Due More Than 31 Days
    [Documentation] Test case for validating that the customer is unable to create AutoPay for the invoices that due more than 31 days functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Create AutoPay For Due More Than 31 Days Invoices ${INVOICE_DETAILS}
    Validate Unable To Create AutoPay"""
    ],
    'Description': [
        "This test case checks the validation for being unable to create AutoPay for the invoices that due more than 31 days functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Create AutoPay For The Invoices That Due More Than 31 Days"
    ]
})


validate_schedule_autopay_daily = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule AutoPay Payments On A Daily Basis functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule AutoPay payments on a daily basis functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${AUTOPAY_DETAILS}          autopay_details

*** Test Cases ***
Validate Schedule AutoPay Payments On A Daily Basis
    [Documentation] Test case for validating that the customer is able to schedule AutoPay payments on a daily basis functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule AutoPay Payments On A Daily Basis ${AUTOPAY_DETAILS}
    Validate AutoPay Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling AutoPay payments on a daily basis functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule AutoPay Payments On A Daily Basis"
    ]
})

validate_schedule_autopay_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule AutoPay For Credit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule AutoPay for credit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${AUTOPAY_DETAILS}          autopay_details

*** Test Cases ***
Validate Schedule AutoPay For Credit Card
    [Documentation] Test case for validating that the customer is able to schedule AutoPay for credit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule AutoPay For Credit Card ${AUTOPAY_DETAILS}
    Validate AutoPay Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling AutoPay for credit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule AutoPay For Credit Card"
    ]
})

validate_schedule_autopay_debit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule AutoPay For Debit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule AutoPay for debit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${AUTOPAY_DETAILS}          autopay_details

*** Test Cases ***
Validate Schedule AutoPay For Debit Card
    [Documentation] Test case for validating that the customer is able to schedule AutoPay for debit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule AutoPay For Debit Card ${AUTOPAY_DETAILS}
    Validate AutoPay Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling AutoPay for debit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule AutoPay For Debit Card"
    ]
})

validate_delete_saved_autopay_schedule = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Delete Saved AutoPay Schedule functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to delete saved AutoPay schedule functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${AUTOPAY_DETAILS}          autopay_details

*** Test Cases ***
Validate Delete Saved AutoPay Schedule
    [Documentation] Test case for validating that the customer is able to delete saved AutoPay schedule functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Delete Saved AutoPay Schedule ${AUTOPAY_DETAILS}
    Validate AutoPay Schedule Deleted"""
    ],
    'Description': [
        "This test case checks the validation for deleting saved AutoPay schedule functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Delete Saved AutoPay Schedule"
    ]
})

validate_schedule_autopay_monthly = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule AutoPay Payments on a Designated Monthly Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule AutoPay payments on a designated monthly date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${AUTOPAY_DETAILS}          autopay_details

*** Test Cases ***
Validate Schedule AutoPay Payments on a Designated Monthly Date
    [Documentation] Test case for validating that the customer is able to schedule AutoPay payments on a designated monthly date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule AutoPay Payments on a Designated Monthly Date ${AUTOPAY_DETAILS}
    Validate AutoPay Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling AutoPay payments on a designated monthly date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule AutoPay Payments on a Designated Monthly Date"
    ]
})


# Create a DataFrame for the new test case
validate_non_integrated_customer_lump_sum_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Process The Lump Sum Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to process the lump sum payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${LUMP_SUM_PAYMENT_DETAILS} lump_sum_payment_details

*** Test Cases ***
Validate Process The Lump Sum Payment
    [Documentation] Test case for validating that the non-integrated customer is able to process the lump sum payment functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Process Lump Sum Payment ${LUMP_SUM_PAYMENT_DETAILS}
    Validate Payment Processed"""
    ],
    'Description': [
        "This test case checks the validation for processing the lump sum payment functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process The Lump Sum Payment"
    ]
})

validate_non_integrated_customer_payment_selected_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Process The Payment Only Against The Selected Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to process the payment only against the selected invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${SELECTED_INVOICE_DETAILS} selected_invoice_details

*** Test Cases ***
Validate Process Payment Only Against The Selected Invoice
    [Documentation] Test case for validating that the non-integrated customer is able to process the payment only against the selected invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Invoice For Payment ${SELECTED_INVOICE_DETAILS}
    Process Payment
    Validate Payment Processed Only For Selected Invoice"""
    ],
    'Description': [
        "This test case checks the validation for processing the payment only against the selected invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment Only Against The Selected Invoice"
    ]
})


validate_non_integrated_customer_no_routing_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Unable To Process The Payment Without Entering Routing Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is unable to process the payment without entering routing number functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Unable To Process Payment Without Entering Routing Number
    [Documentation] Test case for validating that the non-integrated customer is unable to process the payment without entering routing number functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Process Payment Without Routing Number
    Validate Unable To Process Payment"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process the payment without entering routing number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Payment Without Entering Routing Number"
    ]
})

validate_non_integrated_customer_remove_selected_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Remove Selected Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to remove selected invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${SELECTED_INVOICE_DETAILS} selected_invoice_details

*** Test Cases ***
Validate Remove Selected Invoice
    [Documentation] Test case for validating that the non-integrated customer is able to remove selected invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Invoice For Removal ${SELECTED_INVOICE_DETAILS}
    Remove Selected Invoice
    Validate Invoice Removed"""
    ],
    'Description': [
        "This test case checks the validation for removing selected invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Remove Selected Invoice"
    ]
})

validate_default_checkbox_states = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Default Checkbox States For Payment Authorization And Send-Email Receipt functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating the default checkbox states for payment authorization and send-email receipt functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Default Checkbox States
    [Documentation] Test case for validating the default checkbox states for payment authorization and send-email receipt functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Validate Default Checkbox States"""
    ],
    'Description': [
        "This test case checks the validation for default checkbox states for payment authorization and send-email receipt functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Default Checkbox States"
    ]
})


validate_unable_to_process_payment_without_authorization = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Unable To Process Payment Without Selecting Payment Authorization functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to process payment without selecting payment authorization functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Unable To Process Payment Without Selecting Payment Authorization
    [Documentation] Test case for validating that the customer is unable to process payment without selecting payment authorization functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Process Payment Without Selecting Payment Authorization
    Validate Unable To Process Payment"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process payment without selecting payment authorization functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Payment Without Selecting Payment Authorization"
    ]
})


validate_navigate_to_payment_authorization_screen = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Navigate To Payment Authorization Screen After Clicking On Payment Authorization Link functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to navigate to payment authorization screen after clicking on payment authorization link functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate To Payment Authorization Screen
    [Documentation] Test case for validating that the customer is able to navigate to payment authorization screen after clicking on payment authorization link functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click On Payment Authorization Link
    Validate Navigation To Payment Authorization Screen"""
    ],
    'Description': [
        "This test case checks the validation for navigating to payment authorization screen after clicking on payment authorization link functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Payment Authorization Screen"
    ]
})

validate_payment_selected_invoice_achorecheck = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Process The Payment Only Against The Selected Invoice Using ACHoreCheck functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to process the payment only against the selected invoice using ACHoreCheck functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${SELECTED_INVOICE_DETAILS} selected_invoice_details

*** Test Cases ***
Validate Process Payment Only Against The Selected Invoice Using ACHoreCheck
    [Documentation] Test case for validating that the non-integrated customer is able to process the payment only against the selected invoice using ACHoreCheck functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Invoice For Payment ${SELECTED_INVOICE_DETAILS}
    Process Payment Using ACHoreCheck
    Validate Payment Processed Only For Selected Invoice"""
    ],
    'Description': [
        "This test case checks the validation for processing the payment only against the selected invoice using ACHoreCheck functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment Only Against The Selected Invoice Using ACHoreCheck"
    ]
})

validate_add_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Add Multiple Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to add multiple invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Add Multiple Invoices
    [Documentation] Test case for validating that the non-integrated customer is able to add multiple invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Add Multiple Invoices ${INVOICE_DETAILS}
    Validate Multiple Invoices Added"""
    ],
    'Description': [
        "This test case checks the validation for adding multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Add Multiple Invoices"
    ]
})

validate_differential_surcharge_colorado = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Differential Surcharge Amount Applied When Colorado State Is Selected functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the differential surcharge amount is applied when Colorado state is selected functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${STATE_DETAILS}            state_details

*** Test Cases ***
Validate Differential Surcharge Amount Applied When Colorado State Is Selected
    [Documentation] Test case for validating that the differential surcharge amount is applied when Colorado state is selected functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Colorado State ${STATE_DETAILS}
    Validate Differential Surcharge Amount Applied"""
    ],
    'Description': [
        "This test case checks the validation for differential surcharge amount being applied when Colorado state is selected functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Differential Surcharge Amount Applied When Colorado State Is Selected"
    ]
})


validate_invoice_details_not_changed_for_unselected_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate For The Invoices Which Are NOT Selected For Removing, The Invoice Details Are NOT Changed functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that for the invoices which are not selected for removing, the invoice details are not changed functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Invoice Details Not Changed For Unselected Invoices
    [Documentation] Test case for validating that for the invoices which are not selected for removing, the invoice details are not changed functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Remove Selected Invoices
    Validate Invoice Details Not Changed For Unselected Invoices ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for the invoice details not being changed for the invoices which are not selected for removing functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Invoice Details Not Changed For Unselected Invoices"
    ]
})

validate_surcharge_avoided_message = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Gets A Message That Surcharge Can Be Avoided By Paying With ACH Or Debit card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer gets a message that surcharge can be avoided by paying with ACH or debit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Surcharge Avoided Message
    [Documentation] Test case for validating that the non-integrated customer gets a message that surcharge can be avoided by paying with ACH or debit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Payment
    Validate Surcharge Avoided Message Displayed"""
    ],
    'Description': [
        "This test case checks the validation for getting a message that surcharge can be avoided by paying with ACH or debit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Surcharge Avoided Message"
    ]
})


validate_select_account_type_achorecheck = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Select Account Type For ACHoreCheck functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to select account type for ACHoreCheck functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${ACCOUNT_TYPE}             account_type

*** Test Cases ***
Validate Select Account Type For ACHoreCheck
    [Documentation] Test case for validating that the non-integrated customer is able to select account type for ACHoreCheck functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Account Type For ACHoreCheck ${ACCOUNT_TYPE}
    Validate Account Type Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting account type for ACHoreCheck functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select Account Type For ACHoreCheck"
    ]
})

validate_navigate_back_from_achorecheck = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Navigate Back From ACHoreCheck functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to navigate back from ACHoreCheck functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate Back From ACHoreCheck
    [Documentation] Test case for validating that the non-integrated customer is able to navigate back from ACHoreCheck functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate Back From ACHoreCheck
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating back from ACHoreCheck functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate Back From ACHoreCheck"
    ]
})

validate_navigate_back_from_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able To Navigate Back From Credit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to navigate back from credit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate Back From Credit Card
    [Documentation] Test case for validating that the non-integrated customer is able to navigate back from credit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate Back From Credit Card
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating back from credit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate Back From Credit Card"
    ]
})


validate_surcharge_recalculated_when_state_changes = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate That Surcharge Amount Is Re-Calculated When Customer Changes The State functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the surcharge amount is re-calculated when customer changes the state functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${STATE_DETAILS}            state_details

*** Test Cases ***
Validate Surcharge Amount Re-Calculated When Customer Changes The State
    [Documentation] Test case for validating that the surcharge amount is re-calculated when customer changes the state functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Change State ${STATE_DETAILS}
    Validate Surcharge Amount Re-Calculated"""
    ],
    'Description': [
        "This test case checks the validation for re-calculating the surcharge amount when customer changes the state functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Surcharge Amount Re-Calculated When Customer Changes The State"
    ]
})

validate_create_and_clear_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Non Integrated Customer Is Able Create Multiple Invoices And Clear All Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the non-integrated customer is able to create multiple invoices and clear all invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Create Multiple Invoices And Clear All Invoices
    [Documentation] Test case for validating that the non-integrated customer is able to create multiple invoices and clear all invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Create Multiple Invoices ${INVOICE_DETAILS}
    Clear All Invoices
    Validate Multiple Invoices Created And Cleared"""
    ],
    'Description': [
        "This test case checks the validation for creating multiple invoices and clearing all invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Create Multiple Invoices And Clear All Invoices"
    ]
})

validate_send_invoice_receipt_to_email = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able Send Invoice Receipt To The Given Email Address functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to send invoice receipt to the given email address functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${EMAIL_ADDRESS}            email_address

*** Test Cases ***
Validate Send Invoice Receipt To The Given Email Address
    [Documentation] Test case for validating that the customer is able to send invoice receipt to the given email address functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Enter Email Address ${EMAIL_ADDRESS}
    Send Invoice Receipt
    Validate Invoice Receipt Sent"""
    ],
    'Description': [
        "This test case checks the validation for sending invoice receipt to the given email address functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Send Invoice Receipt To The Given Email Address"
    ]
})


validate_see_terms_conditions_privacy_policy = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To See Terms Conditions And Privacy Policy Screen functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to see terms, conditions, and privacy policy screen functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate See Terms Conditions And Privacy Policy Screen
    [Documentation] Test case for validating that the customer is able to see terms, conditions, and privacy policy screen functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Terms Conditions And Privacy Policy Screen
    Validate Terms Conditions And Privacy Policy Screen Displayed"""
    ],
    'Description': [
        "This test case checks the validation for seeing terms, conditions, and privacy policy screen functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate See Terms Conditions And Privacy Policy Screen"
    ]
})

validate_signout_from_payment_receipt = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Signout From The Payment Receipt functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to signout from the payment receipt functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Signout From The Payment Receipt
    [Documentation] Test case for validating that the customer is able to signout from the payment receipt functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Payment Receipt
    Signout
    Validate Signout Successful"""
    ],
    'Description': [
        "This test case checks the validation for signing out from the payment receipt functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Signout From The Payment Receipt"
    ]
})

validate_navigate_to_invoice_referral_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Navigate To The Customer Invoice Referral Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to navigate to the customer invoice referral page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate To The Customer Invoice Referral Page
    [Documentation] Test case for validating that the customer is able to navigate to the customer invoice referral page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Customer Invoice Referral Page
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating to the customer invoice referral page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To The Customer Invoice Referral Page"
    ]
})


validate_unable_to_process_transaction_with_negative_amount = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Unable To Process Transaction With Negative Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to process transaction with negative amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Unable To Process Transaction With Negative Amount
    [Documentation] Test case for validating that the customer is unable to process transaction with negative amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Process Transaction With Negative Amount
    Validate Unable To Process Transaction"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process transaction with negative amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Transaction With Negative Amount"
    ]
})

validate_message_sent_if_state_field_not_selected = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate That Application Sends Message If The State Field Is NOT Selected functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the application sends message if the state field is not selected functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Message Sent If State Field Is NOT Selected
    [Documentation] Test case for validating that the application sends message if the state field is not selected functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Process Transaction Without Selecting State
    Validate Message Sent If State Field Is NOT Selected"""
    ],
    'Description': [
        "This test case checks the validation for sending a message if the state field is not selected functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Message Sent If State Field Is NOT Selected"
    ]
})

validate_schedule_payment_for_past_invoice_due_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule Payment For Past Invoice Due Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule payment for past invoice due date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_DETAILS}          payment_details

*** Test Cases ***
Validate Schedule Payment For Past Invoice Due Date
    [Documentation] Test case for validating that the customer is able to schedule payment for past invoice due date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule Payment For Past Invoice Due Date ${PAYMENT_DETAILS}
    Validate Payment Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment for past invoice due date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule Payment For Past Invoice Due Date"
    ]
})

validate_schedule_payment_for_current_invoice_due_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule Payment For Current Invoice Due Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule payment for current invoice due date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_DETAILS}          payment_details

*** Test Cases ***
Validate Schedule Payment For Current Invoice Due Date
    [Documentation] Test case for validating that the customer is able to schedule payment for current invoice due date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule Payment For Current Invoice Due Date ${PAYMENT_DETAILS}
    Validate Payment Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment for current invoice due date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule Payment For Current Invoice Due Date"
    ]
})


validate_schedule_payment_for_future_invoice_due_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule Payment For Future Invoice Due Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule payment for future invoice due date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_DETAILS}          payment_details

*** Test Cases ***
Validate Schedule Payment For Future Invoice Due Date
    [Documentation] Test case for validating that the customer is able to schedule payment for future invoice due date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule Payment For Future Invoice Due Date ${PAYMENT_DETAILS}
    Validate Payment Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment for future invoice due date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule Payment For Future Invoice Due Date"
    ]
})

validate_schedule_payment_to_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule Payment To Multiple Invoices For Current Invoice Due Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule payment to multiple invoices for current invoice due date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_DETAILS}          payment_details

*** Test Cases ***
Validate Schedule Payment To Multiple Invoices For Current Invoice Due Date
    [Documentation] Test case for validating that the customer is able to schedule payment to multiple invoices for current invoice due date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule Payment To Multiple Invoices For Current Invoice Due Date ${PAYMENT_DETAILS}
    Validate Payment Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment to multiple invoices for current invoice due date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule Payment To Multiple Invoices For Current Invoice Due Date"
    ]
})

validate_schedule_payment_to_multiple_invoices_past_due_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule Payment To Multiple Invoices For Past Invoice Due Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule payment to multiple invoices for past invoice due date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_DETAILS}          payment_details

*** Test Cases ***
Validate Schedule Payment To Multiple Invoices For Past Invoice Due Date
    [Documentation] Test case for validating that the customer is able to schedule payment to multiple invoices for past invoice due date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule Payment To Multiple Invoices For Past Invoice Due Date ${PAYMENT_DETAILS}
    Validate Payment Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment to multiple invoices for past invoice due date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule Payment To Multiple Invoices For Past Invoice Due Date"
    ]
})

validate_schedule_payment_to_multiple_invoices_future_due_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule Payment To Multiple Invoices For Future Invoice Due Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule payment to multiple invoices for future invoice due date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_DETAILS}          payment_details

*** Test Cases ***
Validate Schedule Payment To Multiple Invoices For Future Invoice Due Date
    [Documentation] Test case for validating that the customer is able to schedule payment to multiple invoices for future invoice due date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule Payment To Multiple Invoices For Future Invoice Due Date ${PAYMENT_DETAILS}
    Validate Payment Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment to multiple invoices for future invoice due date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule Payment To Multiple Invoices For Future Invoice Due Date"
    ]
})


validate_schedule_payment_to_multiple_invoices_multiple_due_dates = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Schedule Payment To Multiple Invoices With Multiple Invoice Due Dates functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to schedule payment to multiple invoices with multiple invoice due dates functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_DETAILS}          payment_details

*** Test Cases ***
Validate Schedule Payment To Multiple Invoices With Multiple Invoice Due Dates
    [Documentation] Test case for validating that the customer is able to schedule payment to multiple invoices with multiple invoice due dates functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Schedule Payment To Multiple Invoices With Multiple Invoice Due Dates ${PAYMENT_DETAILS}
    Validate Payment Scheduled"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment to multiple invoices with multiple invoice due dates functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Schedule Payment To Multiple Invoices With Multiple Invoice Due Dates"
    ]
})

validate_view_scheduled_payment_date_and_origin_in_scheduled_payments = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To View Scheduled Payment Date And Origin In Scheduled Payments functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view scheduled payment date and origin in scheduled payments functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate View Scheduled Payment Date And Origin In Scheduled Payments
    [Documentation] Test case for validating that the customer is able to view scheduled payment date and origin in scheduled payments functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    View Scheduled Payment Date And Origin In Scheduled Payments
    Validate Scheduled Payment Date And Origin Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing scheduled payment date and origin in scheduled payments functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Scheduled Payment Date And Origin In Scheduled Payments"
    ]
})

validate_navigate_to_invoice_page_in_schedule_payments = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Merchant Is Able To Navigate To Invoice Page In Schedule Payments functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the merchant is able to navigate to invoice page in schedule payments functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${MERCHANT_DETAILS}         merchant_details

*** Test Cases ***
Validate Navigate To Invoice Page In Schedule Payments
    [Documentation] Test case for validating that the merchant is able to navigate to invoice page in schedule payments functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Merchant Details ${MERCHANT_DETAILS}
    Navigate To Invoice Page In Schedule Payments
    Validate Navigation To Invoice Page"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice page in schedule payments functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Invoice Page In Schedule Payments"
    ]
})


# A D D  A L L  D A T A F R A M E S  T O  T H E  P I P E L I N E
pipeline.add_dataframe(validate_unable_to_create_autopay_past_500_days)
pipeline.add_dataframe(validate_unable_to_create_autopay_due_more_than_31_days)
pipeline.add_dataframe(validate_schedule_autopay_daily)
pipeline.add_dataframe(validate_schedule_autopay_credit_card)
pipeline.add_dataframe(validate_schedule_autopay_debit_card)
pipeline.add_dataframe(validate_delete_saved_autopay_schedule)
pipeline.add_dataframe(validate_schedule_autopay_monthly)
pipeline.add_dataframe(validate_non_integrated_customer_lump_sum_payment)
pipeline.add_dataframe(validate_non_integrated_customer_payment_selected_invoice)
pipeline.add_dataframe(validate_non_integrated_customer_no_routing_number) 
pipeline.add_dataframe(validate_non_integrated_customer_remove_selected_invoice)
pipeline.add_dataframe(validate_default_checkbox_states)
pipeline.add_dataframe(validate_unable_to_process_payment_without_authorization)
pipeline.add_dataframe(validate_navigate_to_payment_authorization_screen)
pipeline.add_dataframe(validate_payment_selected_invoice_achorecheck)
pipeline.add_dataframe(validate_add_multiple_invoices) 
pipeline.add_dataframe(validate_differential_surcharge_colorado)
pipeline.add_dataframe(validate_invoice_details_not_changed_for_unselected_invoices)
pipeline.add_dataframe(validate_surcharge_avoided_message)
pipeline.add_dataframe(validate_select_account_type_achorecheck)
pipeline.add_dataframe(validate_navigate_back_from_achorecheck)
pipeline.add_dataframe(validate_navigate_back_from_credit_card)
pipeline.add_dataframe(validate_surcharge_recalculated_when_state_changes)
pipeline.add_dataframe(validate_create_and_clear_multiple_invoices)
pipeline.add_dataframe(validate_send_invoice_receipt_to_email)
pipeline.add_dataframe(validate_see_terms_conditions_privacy_policy)
pipeline.add_dataframe(validate_signout_from_payment_receipt)
pipeline.add_dataframe(validate_navigate_to_invoice_referral_page)
pipeline.add_dataframe(validate_unable_to_process_transaction_with_negative_amount)
pipeline.add_dataframe(validate_message_sent_if_state_field_not_selected)
pipeline.add_dataframe(validate_schedule_payment_for_past_invoice_due_date)
pipeline.add_dataframe(validate_schedule_payment_for_current_invoice_due_date)
pipeline.add_dataframe(validate_schedule_payment_for_future_invoice_due_date)
pipeline.add_dataframe(validate_schedule_payment_to_multiple_invoices)
pipeline.add_dataframe(validate_schedule_payment_to_multiple_invoices_past_due_date)
pipeline.add_dataframe(validate_schedule_payment_to_multiple_invoices_future_due_date)
pipeline.add_dataframe(validate_schedule_payment_to_multiple_invoices_multiple_due_dates)
pipeline.add_dataframe(validate_view_scheduled_payment_date_and_origin_in_scheduled_payments)
pipeline.add_dataframe(validate_navigate_to_invoice_page_in_schedule_payments)

# combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = 'data/test_payNow.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = 'data/test_payNOW.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")