import pandas as pd
import json
from testcase_pipeline import TestCasePipeline

pipeline = TestCasePipeline()

validate_account_number = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate account number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating account number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${CUSTOMER_DETAILS}          customer_details
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            1
${PAYMENT_METHOD}            ACH / eCheck
${ACH_ECHECK_DETAILS}        ACH_ECHECK_DETAILS
${ERROR_MESSAGE}             customer_details.Error_Message

*** Test Cases ***
Validate Account Number Functionality Of PayNOW
    [Documentation]    Test case for validating account number functionality of the PayNOW datadriver
    Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${NON_INTEGRATED_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter ACH/ECheck Details    ${ACH_ECHECK_DETAILS}
    Validate Errors After Clicking On Process Invoice    ${ERROR_MESSAGE}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the account number validation functionality for the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Account Number Functionality Of PayNOW"
    ]
})


validate_invoice_number = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate invoice number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating invoice number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${CUSTOMER_DETAILS}          customer_details
${PAYMENT_TYPE}              Lump Sum
${SPECIFIC_INVOICE}          specific_invoice
${ACH_ECHECK_DETAILS}        ACH_ECHECK_DETAILS
${ERROR_MESSAGE}             specific invoice.Error_Message

*** Test Cases ***
Validate Invoice Number Functionality Of PayNOW
    [Documentation]    Test case for validating invoice number functionality of the PayNOW datadriver
    Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${NON_INTEGRATED_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Click On Add Invoice    1
    Validate Invoice Details With Invalid Data    test_case_validation    ${SPECIFIC_INVOICE}
    Select Payment Method    ${ACH_ECHECK_DETAILS}
    Validate Errors After Clicking On Process Invoice    ${ERROR_MESSAGE}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the invoice number validation functionality for the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Invoice Number Functionality Of PayNOW"
    ]
})


validate_credit_card_number = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate credit card number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating credit card number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${CUSTOMER_DETAILS}          customer_details
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            1
${PAYMENT_METHOD}            Credit Card
${CREDITCARD_DETAILS}        creditcard_details
${ERROR_MESSAGE}             creditcard_details.Error_Message

*** Test Cases ***
Validate Credit Card Number Functionality Of PayNOW
    [Documentation]    Test case for validating credit card number functionality of the PayNOW datadriver
    Generate Random Customer Details
    Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${NON_INTEGRATED_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter Credit Card Values    ${CREDITCARD_DETAILS}
    Validate Errors After Clicking On Process Invoice    ${ERROR_MESSAGE}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the credit card number validation functionality for the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Credit Card Number Functionality Of PayNOW"
    ]
})


validate_routing_number = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate routing number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating routing number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${CUSTOMER_DETAILS}          customer_details
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            1
${PAYMENT_METHOD}            ACH / eCheck
${ACH_ECHECK_DETAILS}        echeck_details
${ERROR_MESSAGE}             Ach.Error_Message

*** Test Cases ***
Validate Routing Number Functionality Of PayNOW
    [Documentation]    Test case for validating routing number functionality of the PayNOW datadriver
    Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${NON_INTEGRATED_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter ACH/ECheck Values    ${ACH_ECHECK_DETAILS}
    Validate Errors After Clicking On Process Invoice    ${ERROR_MESSAGE}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the routing number validation functionality for the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Routing Number Functionality Of PayNOW"
    ]
})


validate_visa_debit_card = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate process payment with Visa Debit card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating process payment with Visa Debit card functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${CUSTOMER_DETAILS}          customer_details
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            1
${PAYMENT_METHOD}            Credit Card
${CREDITCARD_DETAILS}        creditcard_details
${ERROR_MESSAGE}             creditcard_details.Error_Message

*** Test Cases ***
Validate Process Payment With Visa Debit Card Functionality Of PayNOW
    [Documentation]    Test case for validating process payment with Visa Debit card functionality of the PayNOW datadriver
    Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${NON_INTEGRATED_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter Credit Card Values    ${CREDITCARD_DETAILS}
    Validate Errors After Clicking On Process Invoice    ${ERROR_MESSAGE}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the process payment functionality with Visa Debit card for the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment With Visa Debit Card Functionality Of PayNOW"
    ]
})


validate_invalid_account = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate customer is unable to login into Paynow with invalid account number and valid or invalid invoice number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is unable to log in to PayNOW with an invalid account number and valid or invalid invoice number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${ACCOUNT_NUMBER}            login_details.Account_Number
${INVOICE_NUMBER}            login_details.Invoice_Number
${ERROR_MESSAGE}             login_details.Error_Message
${ACCOUNT_NO}                login_details.Account_No
${CUSTOMER_NAME}             login_details.Customer_Name

*** Test Cases ***
Validate Customer Is Unable To Login With Invalid Account Number And Valid Or Invalid Invoice Number
    [Documentation]    Test case for validating that the customer is unable to log in to PayNOW with an invalid account number and valid or invalid invoice number functionality of the PayNOW datadriver
    Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}
    Enter Account Number And Invoice    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Validate Error Message Is Displayed    ${ERROR_MESSAGE}
    Validate Account Number Is Displayed    ${ACCOUNT_NO}    ${CUSTOMER_NAME}"""
    ],
    'Description': [
        "This test case checks the validation for customer login with an invalid account number and valid or invalid invoice number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Is Unable To Login With Invalid Account Number And Valid Or Invalid Invoice Number"
    ]
})


validate_without_invoice_number = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate customer is unable to login without invoice number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is unable to log in without an invoice number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${OMNICORP_MERCHANT}         OMNICORP_MERCHANT
${ACCOUNT_NUMBER}            login_details.Account_Number
${ERROR_MESSAGE}             login_details.Error_Message1

*** Test Cases ***
Validate Customer Is Unable To Login Without Invoice Number
    [Documentation]    Test case for validating that the customer is unable to log in without an invoice number functionality of the PayNOW datadriver
    Launch PayNow Application    ${OMNICORP_MERCHANT}
    Enter Account Number And Invoice Number    ${ACCOUNT_NUMBER}
    Validate Error Message For Empty Details    ${ACCOUNT_NUMBER}
    Validate Error Message Is Displayed    ${ERROR_MESSAGE}"""
    ],
    'Description': [
        "This test case checks the validation for customer login without an invoice number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Is Unable To Login Without Invoice Number"
    ]
})


validate_master_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate merchant is able to schedule payment with master credit card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the merchant is able to schedule payment with Master Credit Card functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${OMNICORP_MERCHANT}         OMNICORP_MERCHANT
${ACCOUNT_NUMBER}            account_number
${INVOICE_NUMBER}            invoice_number
${CUSTOMER_DETAILS}          customer_details
${CREDIT_CARD_NUMBER}        Scheduled_Payments.Creditcard_Number
${EXPIRY_DATE}               Scheduled_Payments.Expiry_Date
${CVV}                       Scheduled_Payments.CVV
${SCHEDULED_STATUS}          Scheduled_Payments.Status

*** Test Cases ***
Validate Merchant Is Able To Schedule Payment With Master Credit Card
    [Documentation]    Test case for validating that the merchant is able to schedule payment with Master Credit Card functionality of the PayNOW datadriver
    Launch PayNow Application    ${OMNICORP_MERCHANT}
    Enter Account Number And Invoice    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${OMNICORP_MERCHANT}
    Select Payment Method    Credit Card
    Enter Credit Card Details    ${CREDIT_CARD_NUMBER}    ${EXPIRY_DATE}    ${CVV}
    Select Payment Date    today+1
    Create Schedule Payment
    Send Event To Process Schedule Payment    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Validate Scheduled Payment Status    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    ${SCHEDULED_STATUS}"""
    ],
    'Description': [
        "This test case checks the validation for scheduling payment with Master Credit Card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Merchant Is Able To Schedule Payment With Master Credit Card"
    ]
})


validate_ct_state_payment = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate customer is able to process payment for CONNETICUT State (CT) with Credit card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to process payment for Connecticut State (CT) with Credit Card functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${STERLING_COOPER_MERCHANT}  STERLING_COOPER_MERCHANT
${ACCOUNT_NUMBER}            account_number
${INVOICE_NUMBER}            invoice_number
${STATES}                    states
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            1
${PAYMENT_METHOD}            Credit Card
${CREDIT_CARD_DETAILS}       CREDIT_CARD_DETAILS
${SURCHARGE_PERCENTAGE}      states.Surcharge_Percentage

*** Test Cases ***
Validate Customer Is Able To Process Payment For Connecticut State With Credit Card
    [Documentation]    Test case for validating that the customer is able to process payment for Connecticut State (CT) with Credit Card functionality of the PayNOW datadriver
    Send Request To Create Customer    ${STERLING_COOPER_MERCHANT}
    Send Request To Create Invoice For Customer    ${ACCOUNT_NUMBER}    ${STERLING_COOPER_MERCHANT}
    Launch PayNow Application    ${STERLING_COOPER_MERCHANT}
    Enter Account Number And Invoice    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Enter Customer Details    ${STATES}    ${STERLING_COOPER_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter Credit Card Details    ${CREDIT_CARD_DETAILS}
    Validate Surcharge Percentage Should Be Equal    ${SURCHARGE_PERCENTAGE}"""
    ],
    'Description': [
        "This test case checks the validation for processing payment for Connecticut State (CT) with Credit Card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Is Able To Process Payment For Connecticut State With Credit Card"
    ]
})


validate_me_state_payment = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate customer is able to process payment for MAINE State (ME) with Credit card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to process payment for Maine State (ME) with Credit Card functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${OMNICORP_MERCHANT}         OMNICORP_MERCHANT
${ACCOUNT_NUMBER}            account_number
${INVOICE_NUMBER}            invoice_number
${STATES}                    states
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            97.99
${PAYMENT_METHOD}            Credit Card
${CREDIT_CARD_DETAILS}       CREDIT_CARD_DETAILS
${SURCHARGE_PERCENTAGE}      states.Surcharge_Percentage

*** Test Cases ***
Validate Customer Is Able To Process Payment For Maine State With Credit Card
    [Documentation]    Test case for validating that the customer is able to process payment for Maine State (ME) with Credit Card functionality of the PayNOW datadriver
    Send Request To Create Customer    ${OMNICORP_MERCHANT}
    Send Request To Create Invoice For Customer    ${ACCOUNT_NUMBER}    ${OMNICORP_MERCHANT}
    Launch PayNow Application    ${OMNICORP_MERCHANT}
    Enter Account Number And Invoice    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Enter Customer Details    ${STATES}    ${OMNICORP_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter Credit Card Details    ${CREDIT_CARD_DETAILS}
    Validate Surcharge Percentage Should Be Equal    ${SURCHARGE_PERCENTAGE}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the validation for processing payment for Maine State (ME) with Credit Card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Is Able To Process Payment For Maine State With Credit Card"
    ]
})


validate_me_state_2_payment = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate customer is able to process payment for MAINE State (ME) 2 with Credit card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to process payment for Maine State (ME) 2 with Credit Card functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${OMNICORP_MERCHANT}         OMNICORP_MERCHANT
${ACCOUNT_NUMBER}            account_number
${INVOICE_NUMBER}            invoice_number
${STATES}                    states
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            97.99
${PAYMENT_METHOD}            Credit Card
${CREDIT_CARD_DETAILS}       CREDIT_CARD_DETAILS
${SURCHARGE_PERCENTAGE}      states.Surcharge_Percentage

*** Test Cases ***
Validate Customer Is Able To Process Payment For Maine State 2 With Credit Card
    [Documentation]    Test case for validating that the customer is able to process payment for Maine State (ME) 2 with Credit Card functionality of the PayNOW datadriver
    Send Request To Create Customer    ${OMNICORP_MERCHANT}
    Send Request To Create Invoice For Customer    ${ACCOUNT_NUMBER}    ${OMNICORP_MERCHANT}
    Launch PayNow Application    ${OMNICORP_MERCHANT}
    Enter Account Number And Invoice    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Enter Customer Details    ${STATES}    ${OMNICORP_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter Credit Card Details    ${CREDIT_CARD_DETAILS}
    Validate Surcharge Percentage Should Be Equal    ${SURCHARGE_PERCENTAGE}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the validation for processing payment for Maine State (ME) 2 with Credit Card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Is Able To Process Payment For Maine State 2 With Credit Card"
    ]
})


validate_autopay_sunday = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate customer is able to schedule autopay payments on a Sunday of the week functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to schedule autopay payments on a Sunday of the week functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${OMNICORP_MERCHANT}         OMNICORP_MERCHANT
${ACCOUNT_NUMBER}            account_number
${INVOICE_NUMBER}            invoice_number
${PAYMENT_DETAILS_DAY}       Payment_details.Day
${CARD_NUMBER}               4111111111111111

*** Test Cases ***
Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week
    [Documentation]    Test case for validating that the customer is able to schedule autopay payments on a Sunday of the week functionality of the PayNOW datadriver
    Send Request To Create Customer    ${OMNICORP_MERCHANT}
    Send Request To Create Invoice For Customer    ${ACCOUNT_NUMBER}    ${OMNICORP_MERCHANT}
    Login To PayNOW And Navigate To Autopay    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Select Specific Day Of The Week    ${PAYMENT_DETAILS_DAY}
    Select Invoices Due For The Payment
    Enter Customer And Credit Card Details For Autopay    ${CARD_NUMBER}
    Validate Created AutoPay Details For Specific Day    Days of Week    ${PAYMENT_DETAILS_DAY}
    Send Request To Create AutoPay For Specific Day    ${ACCOUNT_NUMBER}    ${CARD_NUMBER}    ${PAYMENT_DETAILS_DAY}
    Validate Created AutoPay Details For Specific Day    All Invoices Due    ${PAYMENT_DETAILS_DAY}
    Validate AutoPay Origin In Scheduled Payments    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    AutoPay"""
    ],
    'Description': [
        "This test case checks the validation for scheduling autopay payments on a Sunday of the week functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week"
    ]
})


validate_declined_card = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate customer is unable to process payment by a decline card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is unable to process payment by a declined card functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${CUSTOMER_DETAILS}          customer_details
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            1
${PAYMENT_METHOD}            Credit Card
${CARD_DETAILS}              card_details
${ERROR_MESSAGE}             card_details.Error_Message

*** Test Cases ***
Validate Customer Is Unable To Process Payment By A Declined Card
    [Documentation]    Test case for validating that the customer is unable to process payment by a declined card functionality of the PayNOW datadriver
    Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${NON_INTEGRATED_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter Credit Card Values    ${CARD_DETAILS}
    Validate Errors After Clicking On Process Invoice    ${ERROR_MESSAGE}"""
    ],
    'Description': [
        "This test case checks the validation for processing payment by a declined card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Customer Is Unable To Process Payment By A Declined Card"
    ]
})


validate_last_statement_payment = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing to validate non integrated customer is able to process the last statement payment using credit card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that a non-integrated customer is able to process the last statement payment using credit card functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${NON_INTEGRATED_MERCHANT}   NON_INTEGRATED_MERCHANT
${CUSTOMER_DETAILS}          customer_details
${PAYMENT_TYPE}              Lump Sum
${LUMPSUM_AMOUNT}            1
${PAYMENT_METHOD}            Credit Card
${CREDIT_CARD_DETAILS}       CREDIT_CARD_DETAILS
${ACH_ECHECK_DETAILS}        ACH_ECHECK_DETAILS

*** Test Cases ***
Validate Non Integrated Customer Is Able To Process The Last Statement Payment Using Credit Card
    [Documentation]    Test case for validating that a non-integrated customer is able to process the last statement payment using credit card functionality of the PayNOW datadriver
    Generate Random Customer Details
    Enter Customer Details    ${CUSTOMER_DETAILS}    ${NON_INTEGRATED_MERCHANT}
    Select Payment Type    ${PAYMENT_TYPE}
    Enter Lumpsum Amount    ${LUMPSUM_AMOUNT}
    Select Payment Method    ${PAYMENT_METHOD}
    Enter Credit Card Details    ${CREDIT_CARD_DETAILS}
    Validate Total Charges Under Summary Of Payment    $1.03
    Process Invoice Payment
    Validate Payment Receipt Is Generated
    Select Payment Method    ACH / eCheck
    Enter ACH/ECheck Details    ${ACH_ECHECK_DETAILS}
    Process Invoice Payment
    Validate Payment Receipt Is Generated"""
    ],
    'Description': [
        "This test case checks the validation for processing the last statement payment using credit card functionality of the PayNOW datadriver by a non-integrated customer."
    ],
    'Testcase name': [
        "Validate Non Integrated Customer Is Able To Process The Last Statement Payment Using Credit Card"
    ]
})


validate_icons_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate That Customer Is Able To Expand And Collapse Line Items With '+ & -' Icons In invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to expand and collapse line items with '+ & -' icons in invoice page functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVOICE_DETAILS}           invoice_details

*** Test Cases ***
Validate Expand And Collapse Line Items In Invoice Page
    [Documentation]    Test case for validating that the customer is able to expand and collapse line items with '+ & -' icons in invoice page functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Validate Expand Line Item    ${INVOICE_DETAILS}
    Validate Collapse Line Item    ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for expanding and collapsing line items with '+ & -' icons in the invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Expand And Collapse Line Items In Invoice Page"
    ]
})


validate_same_acc_type = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Add Two Or More ACHoreCheck Payment Method Of Same Account Type For Future Use functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that integrated customer is able to add two or more ACHoreCheck payment method of same account type for future use functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${ACH_DETAILS}               ach_details

*** Test Cases ***
Validate Add Multiple ACHoreCheck Payment Methods For Future Use
    [Documentation]    Test case for validating that integrated customer is able to add two or more ACHoreCheck payment method of same account type for future use functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Add ACHoreCheck Payment Method    ${ACH_DETAILS}
    Validate Payment Method Added Successfully
    Add Another ACHoreCheck Payment Method    ${ACH_DETAILS}
    Validate Both Payment Methods Are Saved"""
    ],
    'Description': [
        "This test case checks the validation for adding two or more ACHoreCheck payment methods of the same account type for future use functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Add Multiple ACHoreCheck Payment Methods For Future Use"
    ]
})



validate_business_savings = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Save ACHorEcheck For Future Use With Account Type - Business Savings functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that integrated customer is able to save ACHorEcheck for future use with account type - Business Savings functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${ACH_DETAILS}               ach_details

*** Test Cases ***
Validate Save ACHorEcheck For Future Use With Business Savings
    [Documentation]    Test case for validating that integrated customer is able to save ACHorEcheck for future use with account type - Business Savings functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Add ACHorEcheck Payment Method    ${ACH_DETAILS}    Business Savings
    Validate Payment Method Saved Successfully"""
    ],
    'Description': [
        "This test case checks the validation for saving ACHorEcheck for future use with account type - Business Savings functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Save ACHorEcheck For Future Use With Business Savings"
    ]
})


validate_future_checking = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Save ACHorEcheck for future Use With Account Type - Personal Checking functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that integrated customer is able to save ACHorEcheck for future use with account type - Personal Checking functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${ACH_DETAILS}               ach_details

*** Test Cases ***
Validate Save ACHorEcheck For Future Use With Personal Checking
    [Documentation]    Test case for validating that integrated customer is able to save ACHorEcheck for future use with account type - Personal Checking functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Add ACHorEcheck Payment Method    ${ACH_DETAILS}    Personal Checking
    Validate Payment Method Saved Successfully"""
    ],
    'Description': [
        "This test case checks the validation for saving ACHorEcheck for future use with account type - Personal Checking functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Save ACHorEcheck For Future Use With Personal Checking"
    ]
})

validate_integrated_personal_savings = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Save ACHorEcheck for future Use With Account Type - Personal Savings functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that integrated customer is able to save ACHorEcheck for future use with account type - Personal Savings functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${ACH_DETAILS}               ach_details

*** Test Cases ***
Validate Save ACHorEcheck For Future Use With Personal Savings
    [Documentation]    Test case for validating that integrated customer is able to save ACHorEcheck for future use with account type - Personal Savings functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Add ACHorEcheck Payment Method    ${ACH_DETAILS}    Personal Savings
    Validate Payment Method Saved Successfully"""
    ],
    'Description': [
        "This test case checks the validation for saving ACHorEcheck for future use with account type - Personal Savings functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Save ACHorEcheck For Future Use With Personal Savings"
    ]
})


validate_customer_method = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Save All Account Type In ACHorEcheck Payment Method For Future Use functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that integrated customer is able to save all account types in ACHorEcheck payment method for future use functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${ACH_DETAILS}               ach_details

*** Test Cases ***
Validate Save All Account Types In ACHorEcheck Payment Method For Future Use
    [Documentation]    Test case for validating that integrated customer is able to save all account types in ACHorEcheck payment method for future use functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Add ACHorEcheck Payment Method    ${ACH_DETAILS}    All Account Types
    Validate Payment Method Saved Successfully"""
    ],
    'Description': [
        "This test case checks the validation for saving all account types in ACHorEcheck payment method for future use functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Save All Account Types In ACHorEcheck Payment Method For Future Use"
    ]
})


validate_partial_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Not Able To Process Partial Payment For More Than Two Invoices Without Giving Notes For All functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is not able to process partial payment for more than two invoices without giving notes for all functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVOICE_DETAILS}           invoice_details

*** Test Cases ***
Validate Not Able To Process Partial Payment For More Than Two Invoices Without Notes
    [Documentation]    Test case for validating that the customer is not able to process partial payment for more than two invoices without giving notes for all functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Navigate To Invoices Page
    Select More Than Two Invoices
    Enter Partial Payment Amounts
    Attempt To Process Payment Without Notes
    Validate Error Message Displayed    ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for processing partial payment for more than two invoices without giving notes for all functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Not Able To Process Partial Payment For More Than Two Invoices Without Notes"
    ]
})


validate_customer_negative = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Unable To Change Amount To Pay To A Negative Value Or Value More Than Amount Due functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is unable to change amount to pay to a negative value or value more than amount due functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVOICE_DETAILS}           invoice_details

*** Test Cases ***
Validate Unable To Change Amount To Pay To Negative Or More Than Amount Due
    [Documentation]    Test case for validating that the customer is unable to change amount to pay to a negative value or value more than amount due functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Navigate To Invoices Page
    Select Invoice
    Attempt To Change Amount To Negative Value
    Validate Error Message Displayed    ${INVOICE_DETAILS}
    Attempt To Change Amount To More Than Amount Due
    Validate Error Message Displayed    ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for changing amount to pay to a negative value or value more than amount due functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Change Amount To Pay To Negative Or More Than Amount Due"
    ]
})


validate_checkbox = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Checkbox For An Invoice Gets Unchecked When Zero Amount To Pay Is Entered For That Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the checkbox for an invoice gets unchecked when zero amount to pay is entered for that invoice functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVOICE_DETAILS}           invoice_details

*** Test Cases ***
Validate Checkbox Unchecked When Zero Amount To Pay Entered
    [Documentation]    Test case for validating that the checkbox for an invoice gets unchecked when zero amount to pay is entered for that invoice functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Navigate To Invoices Page
    Select Invoice
    Enter Zero Amount To Pay
    Validate Checkbox Gets Unchecked    ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for checkbox getting unchecked for an invoice when zero amount to pay is entered for that invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Checkbox Unchecked When Zero Amount To Pay Entered"
    ]
})


validate_checkerdorticked = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Checkbox For An Invoice Gets Checkedorticked When A Non-zero Amount Is Entered In 'Amount To Pay' For That Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the checkbox for an invoice gets checked/ticked when a non-zero amount is entered in 'Amount To Pay' for that invoice functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVOICE_DETAILS}           invoice_details

*** Test Cases ***
Validate Checkbox Checked When Non-zero Amount Entered
    [Documentation]    Test case for validating that the checkbox for an invoice gets checked/ticked when a non-zero amount is entered in 'Amount To Pay' for that invoice functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Navigate To Invoices Page
    Select Invoice
    Enter Non-zero Amount To Pay
    Validate Checkbox Gets Checked    ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for the checkbox getting checked/ticked when a non-zero amount is entered in 'Amount To Pay' for that invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Checkbox Checked When Non-zero Amount Entered"
    ]
})


validate_openInvoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customers Is Able To View All Invoices Associated With The Account Number In Open Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customers are able to view all invoices associated with the account number in open invoices functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${ACCOUNT_NUMBER}            account_number
${INVOICE_DETAILS}           invoice_details

*** Test Cases ***
Validate View All Invoices Associated With Account Number
    [Documentation]    Test case for validating that the customers are able to view all invoices associated with the account number in open invoices functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Account Number    ${ACCOUNT_NUMBER}
    Navigate To Open Invoices Page
    Validate All Invoices Displayed    ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for viewing all invoices associated with the account number in open invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View All Invoices Associated With Account Number"
    ]
})


validate_unable_login = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Enter PayNOW Without Invoice Number And Unable To Login With invoice Without Entering Valid Invoice Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to enter PayNOW without invoice number and unable to login with invoice without entering valid invoice number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVALID_INVOICE_NUMBER}    invalid_invoice_number

*** Test Cases ***
Validate Enter PayNOW Without Invoice Number And Unable To Login With Invalid Invoice
    [Documentation]    Test case for validating that the customer is able to enter PayNOW without invoice number and unable to login with invoice without entering valid invoice number functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Attempt To Login Without Invoice Number
    Validate Unable To Login    ${INVALID_INVOICE_NUMBER}
    Attempt To Login With Invalid Invoice Number
    Validate Unable To Login    ${INVALID_INVOICE_NUMBER}"""
    ],
    'Description': [
        "This test case checks the validation for entering PayNOW without invoice number and unable to login with invoice without entering valid invoice number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enter PayNOW Without Invoice Number And Unable To Login With Invalid Invoice"
    ]
})


validate_unable_processpayment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Enter PayNOW Without Invoice Number And Unable To Process Payment For Invalid Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to enter PayNOW without invoice number and unable to process payment for invalid invoices functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVALID_INVOICE_NUMBER}    invalid_invoice_number

*** Test Cases ***
Validate Enter PayNOW Without Invoice Number And Unable To Process Invalid Invoices
    [Documentation]    Test case for validating that the customer is able to enter PayNOW without invoice number and unable to process payment for invalid invoices functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Attempt To Process Payment Without Invoice Number
    Validate Unable To Process Payment    ${INVALID_INVOICE_NUMBER}
    Attempt To Process Payment For Invalid Invoice
    Validate Unable To Process Payment    ${INVALID_INVOICE_NUMBER}"""
    ],
    'Description': [
        "This test case checks the validation for entering PayNOW without invoice number and unable to process payment for invalid invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enter PayNOW Without Invoice Number And Unable To Process Invalid Invoices"
    ]
})


validate_loading_invalid = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Enter PayNOW Without Invoice Number And Unable to Process Payment By Loading Invalid Account Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for validating that the customer is able to enter PayNOW without invoice number and unable to process payment by loading invalid account number functionality of the PayNOW datadriver
Library          SeleniumLibrary

*** Variables ***
${URL}                       https://example.com/paynow
${CUSTOMER_DETAILS}          customer_details
${INVALID_ACCOUNT_NUMBER}    invalid_account_number

*** Test Cases ***
Validate Enter PayNOW Without Invoice Number And Unable To Process Payment With Invalid Account Number
    [Documentation]    Test case for validating that the customer is able to enter PayNOW without invoice number and unable to process payment by loading invalid account number functionality of the PayNOW datadriver
    Launch PayNow Application    ${URL}
    Enter Customer Details    ${CUSTOMER_DETAILS}
    Attempt To Process Payment Without Invoice Number
    Validate Unable To Process Payment    ${INVALID_ACCOUNT_NUMBER}
    Attempt To Process Payment With Invalid Account Number
    Validate Unable To Process Payment    ${INVALID_ACCOUNT_NUMBER}"""
    ],
    'Description': [
        "This test case checks the validation for entering PayNOW without invoice number and unable to process payment by loading invalid account number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enter PayNOW Without Invoice Number And Unable To Process Payment With Invalid Account Number"
    ]
})


validate_valid_credentials = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Enter Into Paynow With Valid Credentials After Three Previous Failed Login Attempts functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings *** 
Documentation   Test cases for validating that the customer is able to enter into PayNOW with valid credentials after three previous failed login attempts functionality of the PayNOW datadriver
Library         SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${VALID_CREDENTIALS}        valid_credentials
${INVALID_CREDENTIALS}      invalid_credentials

*** Test Cases ***
Validate Enter Paynow With Valid Credentials After Three Failed Login Attempts
    [Documentation]             Test case for validating that the customer is able to enter into PayNOW with valid credentials after three previous failed login attempts functionality of the PayNOW datadriver
    Launch PayNow Application   ${URL}
    Attempt Login With Invalid Credentials ${INVALID_CREDENTIALS}
    Attempt Login With Invalid Credentials ${INVALID_CREDENTIALS}
    Attempt Login With Invalid Credentials ${INVALID_CREDENTIALS}
    Attempt Login With Valid Credentials ${VALID_CREDENTIALS}
    Validate Successful Login"""
    ],
    'Description': [
        "This test case checks the validation for entering into PayNOW with valid credentials after three previous failed login attempts functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Enter Paynow With Valid Credentials After Three Failed Login Attempts"
    ]
})


validate_supercharge_cache = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Surcharge Cache Is Cleared When Customer Switches Payment Methods From Saved Credit Card To ACHorECheck functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the surcharge cache is cleared when the customer switches payment methods from saved credit card to ACHorECheck functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${CREDIT_CARD_DETAILS}      credit_card_details
${ACH_DETAILS}              ach_details

*** Test Cases ***
Validate Surcharge Cache Cleared When Switching Payment Methods
    [Documentation] Test case for validating that the surcharge cache is cleared when the customer switches payment methods from saved credit card to ACHorECheck functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Payment Method ${CREDIT_CARD_DETAILS}
    Validate Surcharge Applied
    Switch To ACHorECheck Payment Method ${ACH_DETAILS}
    Validate Surcharge Cache Cleared"""
    ],
    'Description': [
        "This test case checks the validation for clearing the surcharge cache when the customer switches payment methods from saved credit card to ACHorECheck functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Surcharge Cache Cleared When Switching Payment Methods"
    ]
})


validate_discount_before_due_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Discount Amount Is Applied On Total Due Amount If Payment Is Made Before The Terms Discount Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer discount amount is applied on total due amount if payment is made before the terms discount date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DISCOUNT_DETAILS}         discount_details

*** Test Cases ***
Validate Discount Applied Before Terms Discount Date
    [Documentation] Test case for validating that the customer discount amount is applied on total due amount if payment is made before the terms discount date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Validate Total Due Amount ${DISCOUNT_DETAILS}
    Make Payment Before Discount Date
    Validate Discount Applied"""
    ],
    'Description': [
        "This test case checks the validation for applying customer discount amount on total due amount if payment is made before the terms discount date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Discount Applied Before Terms Discount Date"
    ]
})


validate_surcharge_per_state = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Surcharge Is Applied As Per The State And This Is Added With Payment Amount To Get The Total Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the surcharge is applied as per the state and this is added with payment amount to get the total amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${STATE_SURCHARGE_DETAILS}  state_surcharge_details

*** Test Cases ***
Validate Surcharge Applied As Per State
    [Documentation] Test case for validating that the surcharge is applied as per the state and this is added with payment amount to get the total amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select State ${STATE_SURCHARGE_DETAILS}
    Validate Surcharge Applied
    Validate Total Amount Including Surcharge"""
    ],
    'Description': [
        "This test case checks the validation for applying surcharge as per the state and this is added with payment amount to get the total amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Surcharge Applied As Per State"
    ]
})


validate_current_due_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate All Current Due Amount Invoice Are Selected When Customer Click On Current Due Amount Link In Outstanding Invoice functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that all current due amount invoices are selected when customer clicks on current due amount link in outstanding invoice functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${CURRENT_DUE_INVOICES}     current_due_invoices

*** Test Cases ***
Validate Current Due Amount Invoices Selected
    [Documentation] Test case for validating that all current due amount invoices are selected when customer clicks on current due amount link in outstanding invoice functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click Current Due Amount Link
    Validate All Current Due Invoices Selected ${CURRENT_DUE_INVOICES}"""
    ],
    'Description': [
        "This test case checks the validation for selecting all current due amount invoices when customer clicks on current due amount link in outstanding invoice functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Current Due Amount Invoices Selected"
    ]
})


validate_1_30_days_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate All Invoices Due for 1-30 Days Are Selected When Customer Clicks On 1-30 Amount link In Summary Of Outstanding Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that all invoices due for 1-30 days are selected when customer clicks on 1-30 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DUE_1_30_INVOICES}        due_1_30_invoices

*** Test Cases ***
Validate 1-30 Days Due Invoices Selected
    [Documentation] Test case for validating that all invoices due for 1-30 days are selected when customer clicks on 1-30 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click 1-30 Amount Link
    Validate All 1-30 Days Due Invoices Selected ${DUE_1_30_INVOICES}"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoices due for 1-30 days when customer clicks on 1-30 amount link in summary of outstanding invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate 1-30 Days Due Invoices Selected"
    ]
})


validate_31_60_days_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate All Invoices Due For 31-60 Days Are Selected When Customer Clicks On 31-60 Amount link In Summary Of Outstanding Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that all invoices due for 31-60 days are selected when customer clicks on 31-60 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DUE_31_60_INVOICES}       due_31_60_invoices

*** Test Cases ***
Validate 31-60 Days Due Invoices Selected
    [Documentation] Test case for validating that all invoices due for 31-60 days are selected when customer clicks on 31-60 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click 31-60 Amount Link
    Validate All 31-60 Days Due Invoices Selected ${DUE_31_60_INVOICES}"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoices due for 31-60 days when customer clicks on 31-60 amount link in summary of outstanding invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate 31-60 Days Due Invoices Selected"
    ]
})


validate_61_90_days_invoices = pd.DataFrame({
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

validate_over_90_days_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate All Invoices Due For Over 90 Days Are Selected When Customer Clicks On Over 90 Amount Link In Summary Of Outstanding Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that all invoices due for over 90 days are selected when customer clicks on over 90 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DUE_OVER_90_INVOICES}     due_over_90_invoices

*** Test Cases ***
Validate Over 90 Days Due Invoices Selected
    [Documentation] Test case for validating that all invoices due for over 90 days are selected when customer clicks on over 90 amount link in summary of outstanding invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click Over 90 Amount Link
    Validate All Over 90 Days Due Invoices Selected ${DUE_OVER_90_INVOICES}"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoices due for over 90 days when customer clicks on over 90 amount link in summary of outstanding invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Over 90 Days Due Invoices Selected"
    ]
})


validate_total_amount_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate All Invoice Are Selected When Customer Clicks On Total Amount Link In Summary of Outstanding Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that all invoices are selected when customer clicks on total amount link in summary of outstanding invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${TOTAL_INVOICES}           total_invoices

*** Test Cases ***
Validate Total Amount Invoices Selected
    [Documentation] Test case for validating that all invoices are selected when customer clicks on total amount link in summary of outstanding invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click Total Amount Link
    Validate All Invoices Selected ${TOTAL_INVOICES}"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoices when customer clicks on total amount link in summary of outstanding invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Total Amount Invoices Selected"
    ]
})


validate_expand_collapse_line_items = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate That Customer Is Able To Expand And Collapse Line Items In Invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to expand and collapse line items in invoice page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Expand And Collapse Line Items
    [Documentation] Test case for validating that the customer is able to expand and collapse line items in invoice page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Expand Line Items ${INVOICE_DETAILS}
    Collapse Line Items ${INVOICE_DETAILS}
    Validate Expand And Collapse Functionality"""
    ],
    'Description': [
        "This test case checks the validation for expanding and collapsing line items in invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Expand And Collapse Line Items"
    ]
})


validate_unable_login_empty_credentials = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Unable To Login Into Paynow With Empty Account Number And Invoice Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to login into Paynow with empty account number and invoice number functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${EMPTY_CREDENTIALS}        empty_credentials

*** Test Cases ***
Validate Unable To Login With Empty Credentials
    [Documentation] Test case for validating that the customer is unable to login into Paynow with empty account number and invoice number functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Attempt Login With Empty Credentials ${EMPTY_CREDENTIALS}
    Validate Login Failure"""
    ],
    'Description': [
        "This test case checks the validation for login failure with empty account number and invoice number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Login With Empty Credentials"
    ]
})


validate_click_close_payment_link = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Click on Payment Secured Link And Close It functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to click on payment secured link and close it functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_SECURED_LINK}     payment_secured_link

*** Test Cases ***
Validate Click And Close Payment Secured Link
    [Documentation] Test case for validating that the integrated customer is able to click on payment secured link and close it functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click Payment Secured Link ${PAYMENT_SECURED_LINK}
    Close Payment Secured Link
    Validate Link Closure"""
    ],
    'Description': [
        "This test case checks the validation for clicking and closing the payment secured link functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Click And Close Payment Secured Link"
    ]
})


validate_save_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Save Credit Card Payment Method For Future Use functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to save credit card payment method for future use functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${CREDIT_CARD_DETAILS}      credit_card_details

*** Test Cases ***
Validate Save Credit Card For Future Use
    [Documentation] Test case for validating that the integrated customer is able to save credit card payment method for future use functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Enter Credit Card Details ${CREDIT_CARD_DETAILS}
    Save Credit Card For Future Use
    Validate Credit Card Saved"""
    ],
    'Description': [
        "This test case checks the validation for saving credit card payment method for future use functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Save Credit Card For Future Use"
    ]
})


validate_add_multiple_credit_cards = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Able To Add Two or More Credit Cards For Future Use functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to add two or more credit cards for future use functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${CREDIT_CARD_1_DETAILS}    credit_card_1_details
${CREDIT_CARD_2_DETAILS}    credit_card_2_details

*** Test Cases ***
Validate Add Multiple Credit Cards For Future Use
    [Documentation] Test case for validating that the integrated customer is able to add two or more credit cards for future use functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Enter First Credit Card Details ${CREDIT_CARD_1_DETAILS}
    Save First Credit Card For Future Use
    Enter Second Credit Card Details ${CREDIT_CARD_2_DETAILS}
    Save Second Credit Card For Future Use
    Validate Multiple Credit Cards Saved"""
    ],
    'Description': [
        "This test case checks the validation for adding two or more credit cards for future use functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Add Multiple Credit Cards For Future Use"
    ]
})


validate_click_find_routing_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Click On 'Find Routing Number' In ACHorEcheck functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to click on 'Find Routing Number' in ACHorEcheck functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${FIND_ROUTING_NUMBER_LINK} find_routing_number_link

*** Test Cases ***
Validate Click On 'Find Routing Number' Link
    [Documentation] Test case for validating that the integrated customer is able to click on 'Find Routing Number' in ACHorEcheck functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Click On 'Find Routing Number' Link ${FIND_ROUTING_NUMBER_LINK}
    Validate Routing Number Link Clicked"""
    ],
    'Description': [
        "This test case checks the validation for clicking on 'Find Routing Number' in ACHorEcheck functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Click On 'Find Routing Number' Link"
    ]
})


validate_view_paid_status = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate That The Customer Is Able To View Paid Payment Status On Invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view paid payment status on invoice page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate View Paid Payment Status On Invoice Page
    [Documentation] Test case for validating that the customer is able to view paid payment status on invoice page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    View Paid Payment Status ${INVOICE_DETAILS}
    Validate Paid Payment Status Viewed"""
    ],
    'Description': [
        "This test case checks the validation for viewing paid payment status on invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Paid Payment Status On Invoice Page"
    ]
})


validate_resume_payment_process = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able Resume The Process Payment After Resolving Errors functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to resume the process payment after resolving errors functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Resume Process Payment After Resolving Errors
    [Documentation] Test case for validating that the customer is able to resume the process payment after resolving errors functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Attempt Process Payment ${INVOICE_DETAILS}
    Resolve Errors
    Resume Process Payment
    Validate Process Payment Resumed"""
    ],
    'Description': [
        "This test case checks the validation for resuming the process payment after resolving errors functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Resume Process Payment After Resolving Errors"
    ]
})


validate_navigate_to_gounified = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Navigate To Gounified Website From PayNOW Application functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to navigate to Gounified website from PayNOW application functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${GOUNIFIED_URL}            gounified_url

*** Test Cases ***
Validate Navigate To Gounified Website
    [Documentation] Test case for validating that the customer is able to navigate to Gounified website from PayNOW application functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Gounified Website ${GOUNIFIED_URL}
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating to Gounified website from PayNOW application functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Gounified Website"
    ]
})


validate_navigate_paynow_from_receipt = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Navigate To PayNOW Application From Payment Receipt Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to navigate to PayNOW application from payment receipt page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${RECEIPT_PAGE}             receipt_page

*** Test Cases ***
Validate Navigate To PayNOW From Receipt Page
    [Documentation] Test case for validating that the customer is able to navigate to PayNOW application from payment receipt page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Receipt Page ${RECEIPT_PAGE}
    Navigate To PayNOW Application
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating to PayNOW application from payment receipt page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To PayNOW From Receipt Page"
    ]
})


validate_view_paid_invoices_by_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To View Paid Invoices Depending On Selected Start Date And End Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view paid invoices depending on selected start date and end date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${START_DATE}               start_date
${END_DATE}                 end_date

*** Test Cases ***
Validate View Paid Invoices By Date Range
    [Documentation] Test case for validating that the customer is able to view paid invoices depending on selected start date and end date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Start Date ${START_DATE}
    Select End Date ${END_DATE}
    View Paid Invoices
    Validate Paid Invoices Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing paid invoices depending on selected start date and end date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Paid Invoices By Date Range"
    ]
})


# Create a DataFrame for the new test case
validate_payment_using_saved_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Process Payment By Using Saved Credit Card Payment Method functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to process payment by using saved credit card payment method functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${SAVED_CREDIT_CARD}        saved_credit_card

*** Test Cases ***
Validate Process Payment Using Saved Credit Card
    [Documentation] Test case for validating that the customer is able to process payment by using saved credit card payment method functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Saved Credit Card ${SAVED_CREDIT_CARD}
    Process Payment
    Validate Payment Processed"""
    ],
    'Description': [
        "This test case checks the validation for processing payment by using saved credit card payment method functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment Using Saved Credit Card"
    ]
})


validate_edit_nickname_saved_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Edit Only The Nickname Of The Customer In The Saved Payment Method functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to edit only the nickname of the customer in the saved payment method functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${SAVED_PAYMENT_METHOD}     saved_payment_method
${NEW_NICKNAME}             new_nickname

*** Test Cases ***
Validate Edit Nickname In Saved Payment Method
    [Documentation] Test case for validating that the customer is able to edit only the nickname of the customer in the saved payment method functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Saved Payment Method ${SAVED_PAYMENT_METHOD}
    Edit Nickname ${NEW_NICKNAME}
    Validate Nickname Edited"""
    ],
    'Description': [
        "This test case checks the validation for editing only the nickname of the customer in the saved payment method functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Edit Nickname In Saved Payment Method"
    ]
})



validate_close_delete_payment_popup = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Close(X) The Delete Payment Method Confirmation Pop-Up Window functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to close(X) the delete payment method confirmation pop-up window functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DELETE_CONFIRM_POPUP}     delete_confirm_popup

*** Test Cases ***
Validate Close Delete Payment Method Popup
    [Documentation] Test case for validating that the customer is able to close(X) the delete payment method confirmation pop-up window functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Trigger Delete Payment Method Popup ${DELETE_CONFIRM_POPUP}
    Close Delete Payment Method Popup
    Validate Popup Closed"""
    ],
    'Description': [
        "This test case checks the validation for closing(X) the delete payment method confirmation pop-up window functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Close Delete Payment Method Popup"
    ]
})


validate_process_payment_ach = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Process Payment By Using Saved ACHorECheck Payment Method functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to process payment by using saved ACHorECheck payment method functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${SAVED_ACH_METHOD}         saved_ach_method

*** Test Cases ***
Validate Process Payment Using Saved ACH Method
    [Documentation] Test case for validating that the customer is able to process payment by using saved ACHorECheck payment method functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Saved ACHorECheck Method ${SAVED_ACH_METHOD}
    Process Payment
    Validate Payment Processed"""
    ],
    'Description': [
        "This test case checks the validation for processing payment by using saved ACHorECheck payment method functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment Using Saved ACH Method"
    ]
})


validate_process_payment_multiple_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Process Payment For Multiple Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to process payment for multiple invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Process Payment For Multiple Invoices
    [Documentation] Test case for validating that the integrated customer is able to process payment for multiple invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Access Multiple Invoices ${INVOICE_DETAILS}
    Process Payment
    Validate Payment Successfully Processed"""
    ],
    'Description': [
        "This test case checks the validation for processing payment for multiple invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment For Multiple Invoices"
    ]
})


validate_invoice_number_checked = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate That Invoice Number Gets Checked After Clicking Pay Invoice Button On Invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the invoice number gets checked after clicking pay invoice button on invoice page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Invoice Number Checked After Clicking Pay Invoice Button
    [Documentation] Test case for validating that the invoice number gets checked after clicking pay invoice button on invoice page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Click Pay Invoice Button ${INVOICE_DETAILS}
    Validate Invoice Number Checked"""
    ],
    'Description': [
        "This test case checks the validation for invoice number getting checked after clicking pay invoice button on invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Invoice Number Checked After Clicking Pay Invoice Button"
    ]
})


validate_payment_credit_card = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Process Payment Through Credit Card functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to process payment through credit card functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${CREDIT_CARD_DETAILS}      credit_card_details

*** Test Cases ***
Validate Process Payment Through Credit Card
    [Documentation] Test case for validating that the integrated customer is able to process payment through credit card functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Credit Card Payment Method ${CREDIT_CARD_DETAILS}
    Process Payment
    Validate Payment Processed"""
    ],
    'Description': [
        "This test case checks the validation for processing payment through credit card functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment Through Credit Card"
    ]
})


validate_payment_achorecheck = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Process Payment Through ACHorECheck functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to process payment through ACHorECheck functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${ACH_DETAILS}              ach_details

*** Test Cases ***
Validate Process Payment Through ACHorECheck
    [Documentation] Test case for validating that the integrated customer is able to process payment through ACHorECheck functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select ACHorECheck Payment Method ${ACH_DETAILS}
    Process Payment
    Validate Payment Processed"""
    ],
    'Description': [
        "This test case checks the validation for processing payment through ACHorECheck functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Payment Through ACHorECheck"
    ]
})

validate_unable_process_overdue = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Unable To Process Payment More Than Due Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is unable to process payment more than due amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Unable To Process Payment More Than Due Amount
    [Documentation] Test case for validating that the integrated customer is unable to process payment more than due amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Attempt Process Payment More Than Due Amount ${INVOICE_DETAILS}
    Validate Payment Failure"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process payment more than due amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Payment More Than Due Amount"
    ]
})



validate_process_lump_sum_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Process The Lump Sum Payment Less Than Due Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to process the lump sum payment less than due amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Process Lump Sum Payment Less Than Due Amount
    [Documentation] Test case for validating that the integrated customer is able to process the lump sum payment less than due amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Attempt Process Lump Sum Payment ${INVOICE_DETAILS}
    Validate Payment Processed"""
    ],
    'Description': [
        "This test case checks the validation for processing the lump sum payment less than due amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Process Lump Sum Payment Less Than Due Amount"
    ]
})


validate_load_unpaid_invoice = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Load Unpaid Invoice When Entered Into Paynow Without Invoice Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to load unpaid invoice when entered into Paynow without invoice number functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${UNPAID_INVOICE_DETAILS}   unpaid_invoice_details

*** Test Cases ***
Validate Load Unpaid Invoice Without Invoice Number
    [Documentation] Test case for validating that the customer is able to load unpaid invoice when entered into Paynow without invoice number functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Load Unpaid Invoice ${UNPAID_INVOICE_DETAILS}
    Validate Unpaid Invoice Loaded"""
    ],
    'Description': [
        "This test case checks the validation for loading unpaid invoice when entered into Paynow without invoice number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Load Unpaid Invoice Without Invoice Number"
    ]
})


validate_total_amount_updated = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Total Amount Is Updated As Per The Changes In Invoices Due Amount functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the total amount is updated as per the changes in invoices due amount functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Total Amount Updated As Per Changes In Invoices Due Amount
    [Documentation] Test case for validating that the total amount is updated as per the changes in invoices due amount functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Update Invoices Due Amount ${INVOICE_DETAILS}
    Validate Total Amount Updated"""
    ],
    'Description': [
        "This test case checks the validation for total amount updating as per the changes in invoices due amount functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Total Amount Updated As Per Changes In Invoices Due Amount"
    ]
})


validate_filtered_invoices_displayed = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Only Filtered Invoices Are Displayed As Per The Filter Conditions functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that only filtered invoices are displayed as per the filter conditions functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${FILTER_CONDITIONS}        filter_conditions

*** Test Cases ***
Validate Only Filtered Invoices Displayed As Per Filter Conditions
    [Documentation] Test case for validating that only filtered invoices are displayed as per the filter conditions functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Apply Filter Conditions ${FILTER_CONDITIONS}
    Validate Filtered Invoices Displayed"""
    ],
    'Description': [
        "This test case checks the validation for only filtered invoices being displayed as per the filter conditions functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Only Filtered Invoices Displayed As Per Filter Conditions"
    ]
})


validate_select_pages_from_dropdown = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Select Pages From Dropdown In Specific Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to select pages from dropdown in specific invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DROPDOWN_OPTIONS}         dropdown_options

*** Test Cases ***
Validate Select Pages From Dropdown In Specific Invoices
    [Documentation] Test case for validating that the customer is able to select pages from dropdown in specific invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Pages From Dropdown ${DROPDOWN_OPTIONS}
    Validate Pages Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting pages from dropdown in specific invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select Pages From Dropdown In Specific Invoices"
    ]
})


validate_invoice_checkbox_default = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Invoice Check Box Should Be Checked By Default When It Passed Due Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the invoice check box should be checked by default when it passed due date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Invoice Check Box Checked By Default When Passed Due Date
    [Documentation] Test case for validating that the invoice check box should be checked by default when it passed due date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Validate Invoice Check Box Checked"""
    ],
    'Description': [
        "This test case checks the validation for invoice check box being checked by default when it passed due date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Invoice Check Box Checked By Default When Passed Due Date"
    ]
})


validate_view_payment_history = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To View Payment History Depending On Selected Start Date And End Date functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view payment history depending on selected start date and end date functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${START_DATE}               start_date
${END_DATE}                 end_date

*** Test Cases ***
Validate View Payment History By Date Range
    [Documentation] Test case for validating that the customer is able to view payment history depending on selected start date and end date functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Start Date ${START_DATE}
    Select End Date ${END_DATE}
    View Payment History
    Validate Payment History Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing payment history depending on selected start date and end date functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Payment History By Date Range"
    ]
})


validate_download_pdf_verify_data = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Download PDF From Invoice Page And Verify The Data functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to download PDF from invoice page and verify the data functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details
${PDF_DATA}                 pdf_data

*** Test Cases ***
Validate Download PDF And Verify Data
    [Documentation] Test case for validating that the customer is able to download PDF from invoice page and verify the data functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Download PDF ${INVOICE_DETAILS}
    Verify PDF Data ${PDF_DATA}
    Validate PDF Data Correctly Matched"""
    ],
    'Description': [
        "This test case checks the validation for downloading PDF from invoice page and verifying the data functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Download PDF And Verify Data"
    ]
})

validate_navigate_to_invoice_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate That Customer Is Able To Navigate To Invoice Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to navigate to invoice page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate To Invoice Page
    [Documentation] Test case for validating that the customer is able to navigate to invoice page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Invoice Page
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating to invoice page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Invoice Page"
    ]
})


# Create a DataFrame for the new test case
validate_login_with_empty_invoice_number = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Login Into Paynow With Empty Invoice Number functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to login into Paynow with empty invoice number functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Login With Empty Invoice Number
    [Documentation] Test case for validating that the customer is able to login into Paynow with empty invoice number functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Leave Invoice Number Empty
    Attempt Login
    Validate Login Successful"""
    ],
    'Description': [
        "This test case checks the validation for logging into Paynow with empty invoice number functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Login With Empty Invoice Number"
    ]
})


validate_verify_paid_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Verify Paid Invoices After Processing Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to verify paid invoices after processing payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Verify Paid Invoices After Processing Payment
    [Documentation] Test case for validating that the customer is able to verify paid invoices after processing payment functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Process Payment ${INVOICE_DETAILS}
    Verify Paid Invoices
    Validate Paid Invoices Verified"""
    ],
    'Description': [
        "This test case checks the validation for verifying paid invoices after processing payment functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Verify Paid Invoices After Processing Payment"
    ]
})


validate_unable_process_negative_amount = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Unable To Process Payment With Negative Amount Due functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to process payment with negative amount due functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${NEGATIVE_AMOUNT}          negative_amount

*** Test Cases ***
Validate Unable To Process Payment With Negative Amount Due
    [Documentation] Test case for validating that the customer is unable to process payment with negative amount due functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Enter Negative Amount ${NEGATIVE_AMOUNT}
    Attempt Process Payment
    Validate Payment Failure"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process payment with negative amount due functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Payment With Negative Amount Due"
    ]
})


validate_select_saved_payment_method = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Select One Of The Saved Payment Method functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to select one of the saved payment methods functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${SAVED_PAYMENT_METHOD}     saved_payment_method

*** Test Cases ***
Validate Select One Of The Saved Payment Method
    [Documentation] Test case for validating that the customer is able to select one of the saved payment methods functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Saved Payment Method ${SAVED_PAYMENT_METHOD}
    Validate Payment Method Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting one of the saved payment methods functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select One Of The Saved Payment Method"
    ]
})


validate_view_last_30_days_payment_history = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To View Last 30 Days Payment History functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view last 30 days payment history functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${START_DATE}               start_date
${END_DATE}                 end_date

*** Test Cases ***
Validate View Last 30 Days Payment History
    [Documentation] Test case for validating that the customer is able to view last 30 days payment history functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Start Date ${START_DATE}
    Select End Date ${END_DATE}
    View Payment History
    Validate Payment History Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing last 30 days payment history functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Last 30 Days Payment History"
    ]
})


validate_view_this_month_payment_history = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To View This Month Payment History functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view this month's payment history functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${START_DATE}               start_date
${END_DATE}                 end_date

*** Test Cases ***
Validate View This Month Payment History
    [Documentation] Test case for validating that the customer is able to view this month's payment history functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Start Date ${START_DATE}
    Select End Date ${END_DATE}
    View Payment History
    Validate Payment History Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing this month's payment history functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View This Month Payment History"
    ]
})


validate_view_last_month_payment_history = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To View Last Month Payment History functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view last month's payment history functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${START_DATE}               start_date
${END_DATE}                 end_date

*** Test Cases ***
Validate View Last Month Payment History
    [Documentation] Test case for validating that the customer is able to view last month's payment history functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Start Date ${START_DATE}
    Select End Date ${END_DATE}
    View Payment History
    Validate Payment History Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing last month's payment history functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Last Month Payment History"
    ]
})


validate_select_all_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Select All Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to select all invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Select All Invoices
    [Documentation] Test case for validating that the integrated customer is able to select all invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select All Invoices
    Validate All Invoices Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select All Invoices"
    ]
})


validate_select_all_due_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Select All Due Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to select all due invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Select All Due Invoices
    [Documentation] Test case for validating that the integrated customer is able to select all due invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select All Due Invoices
    Validate All Due Invoices Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting all due invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select All Due Invoices"
    ]
})


validate_select_all_invoice_on_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Select All Invoice On Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to select all invoice on page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Select All Invoice On Page
    [Documentation] Test case for validating that the integrated customer is able to select all invoice on page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select All Invoice On Page
    Validate All Invoice On Page Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting all invoice on page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select All Invoice On Page"
    ]
})


validate_unselect_all_invoices_on_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Unselect All Invoices On Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to unselect all invoices on page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Unselect All Invoices On Page
    [Documentation] Test case for validating that the integrated customer is able to unselect all invoices on page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Unselect All Invoices On Page
    Validate All Invoices On Page Unselected"""
    ],
    'Description': [
        "This test case checks the validation for unselecting all invoices on page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unselect All Invoices On Page"
    ]
})


validate_specific_invoice_details = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Specific Invoice Details In The Open Invoices Table functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating specific invoice details in the open invoices table functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Specific Invoice Details In Open Invoices Table
    [Documentation] Test case for validating specific invoice details in the open invoices table functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Open Invoices Table
    Validate Specific Invoice Details ${INVOICE_DETAILS}"""
    ],
    'Description': [
        "This test case checks the validation for specific invoice details in the open invoices table functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Specific Invoice Details In Open Invoices Table"
    ]
})


validate_navigate_to_payment_history_tab = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Navigate To Payment History Tab functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to navigate to payment history tab functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate To Payment History Tab
    [Documentation] Test case for validating that the customer is able to navigate to payment history tab functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Payment History Tab
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating to payment history tab functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Payment History Tab"
    ]
})



validate_select_today_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Select Today Date From Date Range functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to select today's date from date range functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${TODAY_DATE}               today_date

*** Test Cases ***
Validate Select Today Date From Date Range
    [Documentation] Test case for validating that the customer is able to select today's date from date range functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Today's Date ${TODAY_DATE}
    Validate Date Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting today's date from date range functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select Today Date From Date Range"
    ]
})


validate_select_yesterday_date = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Select Yesterday's Date From Date Range functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to select yesterday's date from date range functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${YESTERDAY_DATE}           yesterday_date

*** Test Cases ***
Validate Select Yesterday's Date From Date Range
    [Documentation] Test case for validating that the customer is able to select yesterday's date from date range functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Yesterday's Date ${YESTERDAY_DATE}
    Validate Date Selected"""
    ],
    'Description': [
        "This test case checks the validation for selecting yesterday's date from date range functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Select Yesterday's Date From Date Range"
    ]
})


# Create a DataFrame for the new test case
validate_selected_invoices_count = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To See Selected Invoices Count functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to see selected invoices count functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate See Selected Invoices Count
    [Documentation] Test case for validating that the customer is able to see selected invoices count functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Invoices
    Validate Selected Invoices Count Displayed"""
    ],
    'Description': [
        "This test case checks the validation for seeing selected invoices count functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate See Selected Invoices Count"
    ]
})


validate_cancel_login_with_invoice_popup = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Cancel Login With Invoice Pop-Up functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to cancel login with invoice pop-up functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Cancel Login With Invoice Pop-Up
    [Documentation] Test case for validating that the customer is able to cancel login with invoice pop-up functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Trigger Login With Invoice Pop-Up
    Cancel Pop-Up
    Validate Pop-Up Cancelled"""
    ],
    'Description': [
        "This test case checks the validation for canceling login with invoice pop-up functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Cancel Login With Invoice Pop-Up"
    ]
})


validate_process_lump_sum_payment = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Integrated Customer Is Able To Process The Lump Sum Payment functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the integrated customer is able to process the lump sum payment functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${LUMP_SUM_PAYMENT_DETAILS} lump_sum_payment_details

*** Test Cases ***
Validate Process The Lump Sum Payment
    [Documentation] Test case for validating that the integrated customer is able to process the lump sum payment functionality of the PayNOW datadriver
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

validate_amount_due_updated = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Amount Due Is Appropriately Updated In Current Days Past Due functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the amount due is appropriately updated in current days past due functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${CURRENT_DAYS_PAST_DUE}    current_days_past_due

*** Test Cases ***
Validate Amount Due Updated In Current Days Past Due
    [Documentation] Test case for validating that the amount due is appropriately updated in current days past due functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Past Due Invoices
    Validate Amount Due Updated ${CURRENT_DAYS_PAST_DUE}"""
    ],
    'Description': [
        "This test case checks the validation for amount due being appropriately updated in current days past due functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Amount Due Updated In Current Days Past Due"
    ]
})

validate_amount_due_1_31_days_past_due = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Amount Due Is Appropriately Updated In 1-31 Days Past Due functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the amount due is appropriately updated in 1-31 days past due functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DAYS_PAST_DUE}            days_past_due

*** Test Cases ***
Validate Amount Due Updated In 1-31 Days Past Due
    [Documentation] Test case for validating that the amount due is appropriately updated in 1-31 days past due functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Past Due Invoices
    Validate Amount Due Updated ${DAYS_PAST_DUE}"""
    ],
    'Description': [
        "This test case checks the validation for amount due being appropriately updated in 1-31 days past due functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Amount Due Updated In 1-31 Days Past Due"
    ]
})


validate_amount_due_31_60_days_past_due = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Amount Due Is Appropriately Updated In 31-60 Days Past Due functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the amount due is appropriately updated in 31-60 days past due functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DAYS_PAST_DUE}            days_past_due

*** Test Cases ***
Validate Amount Due Updated In 31-60 Days Past Due
    [Documentation] Test case for validating that the amount due is appropriately updated in 31-60 days past due functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Past Due Invoices
    Validate Amount Due Updated ${DAYS_PAST_DUE}"""
    ],
    'Description': [
        "This test case checks the validation for amount due being appropriately updated in 31-60 days past due functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Amount Due Updated In 31-60 Days Past Due"
    ]
})


validate_amount_due_61_90_days_past_due = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Amount Due Is Appropriately Updated In 61-90 Days Past Due functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the amount due is appropriately updated in 61-90 days past due functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DAYS_PAST_DUE}            days_past_due

*** Test Cases ***
Validate Amount Due Updated In 61-90 Days Past Due
    [Documentation] Test case for validating that the amount due is appropriately updated in 61-90 days past due functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Past Due Invoices
    Validate Amount Due Updated ${DAYS_PAST_DUE}"""
    ],
    'Description': [
        "This test case checks the validation for amount due being appropriately updated in 61-90 days past due functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Amount Due Updated In 61-90 Days Past Due"
    ]
})

validate_amount_due_over_90_days_past_due = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Amount Due Is Appropriately Updated In Over 90 Days Past Due functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the amount due is appropriately updated in over 90 days past due functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${DAYS_PAST_DUE}            days_past_due

*** Test Cases ***
Validate Amount Due Updated In Over 90 Days Past Due
    [Documentation] Test case for validating that the amount due is appropriately updated in over 90 days past due functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Past Due Invoices
    Validate Amount Due Updated ${DAYS_PAST_DUE}"""
    ],
    'Description': [
        "This test case checks the validation for amount due being appropriately updated in over 90 days past due functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Amount Due Updated In Over 90 Days Past Due"
    ]
})


validate_unable_to_process_fully_paid_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Unable To Process Fully Paid Invoices functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to process fully paid invoices functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${INVOICE_DETAILS}          invoice_details

*** Test Cases ***
Validate Unable To Process Fully Paid Invoices
    [Documentation] Test case for validating that the customer is unable to process fully paid invoices functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Process Fully Paid Invoices ${INVOICE_DETAILS}
    Validate Unable To Process"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process fully paid invoices functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Fully Paid Invoices"
    ]
})


validate_view_last_7_days_payment_history = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To View Last 7 Days Payment History functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to view last 7 days payment history functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${START_DATE}               start_date
${END_DATE}                 end_date

*** Test Cases ***
Validate View Last 7 Days Payment History
    [Documentation] Test case for validating that the customer is able to view last 7 days payment history functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Select Start Date ${START_DATE}
    Select End Date ${END_DATE}
    View Payment History
    Validate Payment History Displayed"""
    ],
    'Description': [
        "This test case checks the validation for viewing last 7 days payment history functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate View Last 7 Days Payment History"
    ]
})

validate_unable_to_process_payment_with_decline_check = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Unable To Process Payment With Decline Check functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is unable to process payment with decline check functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${CHECK_DETAILS}            check_details

*** Test Cases ***
Validate Unable To Process Payment With Decline Check
    [Documentation] Test case for validating that the customer is unable to process payment with decline check functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Attempt Process Payment With Decline Check ${CHECK_DETAILS}
    Validate Payment Declined"""
    ],
    'Description': [
        "This test case checks the validation for being unable to process payment with decline check functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Unable To Process Payment With Decline Check"
    ]
})

validate_payment_history_updated_as_receipt_generated = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Payment History Is Updated As Soon As Payment Receipt Generated functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the payment history is updated as soon as payment receipt generated functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_RECEIPT_DETAILS}  payment_receipt_details

*** Test Cases ***
Validate Payment History Updated As Soon As Receipt Generated
    [Documentation] Test case for validating that the payment history is updated as soon as payment receipt generated functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Generate Payment Receipt ${PAYMENT_RECEIPT_DETAILS}
    Validate Payment History Updated"""
    ],
    'Description': [
        "This test case checks the validation for payment history being updated as soon as payment receipt generated functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Payment History Updated As Soon As Receipt Generated"
    ]
})

validate_delete_saved_payment_method = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Delete Saved Payment Method functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to delete saved payment method functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details
${PAYMENT_METHOD_DETAILS}   payment_method_details

*** Test Cases ***
Validate Delete Saved Payment Method
    [Documentation] Test case for validating that the customer is able to delete saved payment method functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Saved Payment Methods
    Delete Saved Payment Method ${PAYMENT_METHOD_DETAILS}
    Validate Payment Method Deleted"""
    ],
    'Description': [
        "This test case checks the validation for deleting saved payment method functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Delete Saved Payment Method"
    ]
})

validate_navigate_to_next_page = pd.DataFrame({
    'Prompt': [
        "Generate a robot framework test case for testing to Validate Customer Is Able To Navigate To Next Page functionality of the PayNOW datadriver."
    ],
    'Response': [
        """*** Settings ***
Documentation          Test cases for validating that the customer is able to navigate to the next page functionality of the PayNOW datadriver
Library                SeleniumLibrary

*** Variables ***
${URL}                      https://example.com/paynow
${CUSTOMER_DETAILS}         customer_details

*** Test Cases ***
Validate Navigate To Next Page
    [Documentation] Test case for validating that the customer is able to navigate to the next page functionality of the PayNOW datadriver
    Launch PayNow Application ${URL}
    Enter Customer Details ${CUSTOMER_DETAILS}
    Navigate To Next Page
    Validate Navigation Successful"""
    ],
    'Description': [
        "This test case checks the validation for navigating to the next page functionality of the PayNOW datadriver."
    ],
    'Testcase name': [
        "Validate Navigate To Next Page"
    ]
})


# A D D  A L L  D A T A F R A M E S  T O  T H E  P I P E L I N E
pipeline.add_dataframe(validate_account_number)
pipeline.add_dataframe(validate_invoice_number)
pipeline.add_dataframe(validate_credit_card_number)
pipeline.add_dataframe(validate_customer_method)
pipeline.add_dataframe(validate_routing_number)
pipeline.add_dataframe(validate_visa_debit_card)
pipeline.add_dataframe(validate_invalid_account)
pipeline.add_dataframe(validate_without_invoice_number)
pipeline.add_dataframe(validate_master_credit_card)
pipeline.add_dataframe(validate_ct_state_payment)
pipeline.add_dataframe(validate_me_state_payment)
pipeline.add_dataframe(validate_me_state_2_payment)
pipeline.add_dataframe(validate_autopay_sunday)
pipeline.add_dataframe(validate_declined_card)
pipeline.add_dataframe(validate_last_statement_payment)
pipeline.add_dataframe(validate_icons_invoice)
pipeline.add_dataframe(validate_same_acc_type)
pipeline.add_dataframe(validate_business_savings)
pipeline.add_dataframe(validate_future_checking)
pipeline.add_dataframe(validate_integrated_personal_savings)
pipeline.add_dataframe(validate_customer_method)
pipeline.add_dataframe(validate_partial_payment)
pipeline.add_dataframe(validate_customer_negative)
pipeline.add_dataframe(validate_checkbox)
pipeline.add_dataframe(validate_checkerdorticked)
pipeline.add_dataframe(validate_openInvoices)
pipeline.add_dataframe(validate_unable_login)
pipeline.add_dataframe(validate_unable_processpayment)
pipeline.add_dataframe(validate_loading_invalid)
pipeline.add_dataframe(validate_valid_credentials)
pipeline.add_dataframe(validate_supercharge_cache)
pipeline.add_dataframe(validate_discount_before_due_date)
pipeline.add_dataframe(validate_surcharge_per_state)
pipeline.add_dataframe(validate_current_due_invoices)
pipeline.add_dataframe(validate_1_30_days_invoices)
pipeline.add_dataframe(validate_31_60_days_invoices)
pipeline.add_dataframe(validate_61_90_days_invoices)
pipeline.add_dataframe(validate_over_90_days_invoices)
pipeline.add_dataframe(validate_total_amount_invoices)
pipeline.add_dataframe(validate_expand_collapse_line_items)
pipeline.add_dataframe(validate_unable_login_empty_credentials)
pipeline.add_dataframe(validate_click_close_payment_link)
pipeline.add_dataframe(validate_save_credit_card)
pipeline.add_dataframe(validate_add_multiple_credit_cards)
pipeline.add_dataframe(validate_click_find_routing_number)
pipeline.add_dataframe(validate_view_paid_status)
pipeline.add_dataframe(validate_resume_payment_process)
pipeline.add_dataframe(validate_navigate_to_gounified)
pipeline.add_dataframe(validate_navigate_paynow_from_receipt)
pipeline.add_dataframe(validate_view_paid_invoices_by_date)
pipeline.add_dataframe(validate_payment_using_saved_card)
pipeline.add_dataframe(validate_edit_nickname_saved_payment)
pipeline.add_dataframe(validate_close_delete_payment_popup)
pipeline.add_dataframe(validate_process_payment_ach)
pipeline.add_dataframe(validate_process_payment_multiple_invoices)
pipeline.add_dataframe(validate_invoice_number_checked)
pipeline.add_dataframe(validate_payment_credit_card)
pipeline.add_dataframe(validate_payment_achorecheck)
pipeline.add_dataframe(validate_unable_process_overdue)
pipeline.add_dataframe(validate_process_lump_sum_payment)
pipeline.add_dataframe(validate_load_unpaid_invoice)
pipeline.add_dataframe(validate_total_amount_updated)
pipeline.add_dataframe(validate_filtered_invoices_displayed)
pipeline.add_dataframe(validate_select_pages_from_dropdown)
pipeline.add_dataframe(validate_invoice_checkbox_default)
pipeline.add_dataframe(validate_view_payment_history)
pipeline.add_dataframe(validate_download_pdf_verify_data)
pipeline.add_dataframe(validate_navigate_to_invoice_page)
pipeline.add_dataframe(validate_login_with_empty_invoice_number)
pipeline.add_dataframe(validate_verify_paid_invoices)
pipeline.add_dataframe(validate_unable_process_negative_amount)
pipeline.add_dataframe(validate_select_saved_payment_method)
pipeline.add_dataframe(validate_view_last_30_days_payment_history)
pipeline.add_dataframe(validate_view_this_month_payment_history)
pipeline.add_dataframe(validate_view_last_month_payment_history)
pipeline.add_dataframe(validate_select_all_invoices)
pipeline.add_dataframe(validate_select_all_due_invoices)
pipeline.add_dataframe(validate_select_all_invoice_on_page)
pipeline.add_dataframe(validate_unselect_all_invoices_on_page)
pipeline.add_dataframe(validate_specific_invoice_details)
pipeline.add_dataframe(validate_navigate_to_payment_history_tab)
pipeline.add_dataframe(validate_select_today_date)
pipeline.add_dataframe(validate_select_yesterday_date)
pipeline.add_dataframe(validate_selected_invoices_count)
pipeline.add_dataframe(validate_cancel_login_with_invoice_popup)
pipeline.add_dataframe(validate_process_lump_sum_payment)
pipeline.add_dataframe(validate_amount_due_updated)
pipeline.add_dataframe(validate_amount_due_1_31_days_past_due)
pipeline.add_dataframe(validate_amount_due_31_60_days_past_due)
pipeline.add_dataframe(validate_amount_due_61_90_days_past_due)
pipeline.add_dataframe(validate_amount_due_over_90_days_past_due)
pipeline.add_dataframe(validate_unable_to_process_fully_paid_invoices) 
pipeline.add_dataframe(validate_view_last_7_days_payment_history)
pipeline.add_dataframe(validate_unable_to_process_payment_with_decline_check)
pipeline.add_dataframe(validate_payment_history_updated_as_receipt_generated)
pipeline.add_dataframe(validate_delete_saved_payment_method)
pipeline.add_dataframe(validate_navigate_to_next_page)

# combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = 'data/payNow_datadriver.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = 'data/payNow_datadriver.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")