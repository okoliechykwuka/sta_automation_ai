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


web_login = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for a valid login.",
        "Generate a Robot Framework test case for an invalid email.",
        "Generate a Robot Framework test case for an invalid password."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for login functionality
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/login
${EMAIL}         user@example.com
${PASSWORD}      correct_password
${INVALID_EMAIL} invalid@example.com
${INVALID_PASSWORD} incorrect_password

*** Test Cases ***
Test Valid Login
    [Documentation]    Test case for a valid login
    Open Browser    ${URL}    chrome
    Enter Email Address Field    ${EMAIL}
    Enter Password Field    ${PASSWORD}
    Login To Client Central Application
    # Add validation steps to ensure login was successful
    Close Browser""",
        """*** Settings ***
Documentation    Test cases for login functionality
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/login
${EMAIL}         user@example.com
${PASSWORD}      correct_password
${INVALID_EMAIL} invalid@example.com
${INVALID_PASSWORD} incorrect_password

*** Test Cases ***
Test Invalid Email
    [Documentation]    Test case for an invalid email login
    Open Browser    ${URL}    chrome
    Enter Email Address Field    ${INVALID_EMAIL}
    Enter Password Field    ${PASSWORD}
    Login To Client Central Application
    Validate Error Message For Invalid Email Address
    Close Browser""",
        """*** Settings ***
Documentation    Test cases for login functionality
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/login
${EMAIL}         user@example.com
${PASSWORD}      correct_password
${INVALID_EMAIL} invalid@example.com
${INVALID_PASSWORD} incorrect_password

*** Test Cases ***
Test Invalid Password
    [Documentation]    Test case for an invalid password login
    Open Browser    ${URL}    chrome
    Enter Email Address Field    ${EMAIL}
    Enter Password Field    ${INVALID_PASSWORD}
    Login To Client Central Application
    Validate Error Message For Invalid Password
    Close Browser"""
    ],
    'Description': [
        "This test case checks if the login functionality works correctly with valid credentials.",
        "This test case checks if the login functionality displays an error message for an invalid email.",
        "This test case checks if the login functionality displays an error message for an invalid password."
    ],
    'Testcase name': [
        "Test Valid Login",
        "Test Invalid Email",
        "Test Invalid Password"
    ]
})

common_web = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for common merchants functionality."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for common merchants functionality
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/merchants
${BROWSER}       chrome
${EXCEL_PATH}    path/to/testdata.xlsx
${TC_ID}         TC_01
${SHEET_NAME}    Sheet1
${LOADING_TIMEOUT}    30
${LOCATOR}       element_locator

*** Test Cases ***
Test Common Merchants Functionality
    [Documentation]    Test case for common merchants functionality
    Launch Browser    ${BROWSER}    ${URL}
    Launch Web Application    ${BROWSER}    ${URL}
    Read TestData From Excel    ${EXCEL_PATH}    ${TC_ID}    ${SHEET_NAME}
    Wait Until Element Is Clickable And Click    ${LOCATOR}    ${LOADING_TIMEOUT}
    Scroll Till Element Is Visible    ${LOCATOR}
    Validate String Should Be Equal    expected_value    actual_value
    Validate Error Message Is Displayed    error_message
    Validate String Should Contain    expected_value    actual_value
    Validate String Should Not Contain    unexpected_value    actual_value
    Validate String Should Not Be Equal    unexpected_value    actual_value
    Click Until Element Is Invisible    ${LOCATOR}
    Scroll To Element    ${LOCATOR}
    Wait Till Loading Icon Is Invisible    ${LOCATOR}    ${LOADING_TIMEOUT}
    Fail And Take Screenshot    message
    # Add more test steps as needed
    Close Browser"""
    ],
    'Description': [
        "This test case checks the common functionalities of merchants in a web application."
    ],
    'Testcase name': [
        "Test Common Merchants Functionality"
    ]
})

homepage = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the homepage of all merchants."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the homepage of all merchants
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/merchants
${BROWSER}       chrome
${MODULE}        homepage_module
${MERCHANT}      sample_merchant

*** Test Cases ***
Test Homepage Of All Merchants
    [Documentation]    Test case for the homepage of all merchants
    Launch Browser    ${BROWSER}    ${URL}
    Select Module    ${MODULE}
    Select Merchant    ${MERCHANT}
    # Add more test steps to verify homepage elements
    Logout From Application
    Close Browser"""
    ],
    'Description': [
        "This test case checks the homepage functionalities for all merchants in a web application."
    ],
    'Testcase name': [
        "Test Homepage Of All Merchants"
    ]
})


web_tokens = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the tokens functionality of all merchants."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the tokens functionality of all merchants
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/merchants
${BROWSER}       chrome
${ACCOUNT_NUMBER} 123456
${INVOICE_TOKEN}  abcdef
${SESSION_ID}    session123
${INVOICE_NUMBER} inv123

*** Test Cases ***
Test Tokens Functionality Of All Merchants
    [Documentation]    Test case for the tokens functionality of all merchants
    Launch Browser    ${BROWSER}    ${URL}
    Navigate To Open Invoices Page From Email
    Navigate To Open Invoices Page With Invoice Token    ${ACCOUNT_NUMBER}    ${INVOICE_TOKEN}
    Navigate To Open Invoices Page With Session Token    ${ACCOUNT_NUMBER}    ${SESSION_ID}
    Validate PayNOW Open Invoices Page Is Displayed    ${INVOICE_NUMBER}
    Validate Open Invoices Page Is Displayed    ${INVOICE_NUMBER}
    # Add more test steps to verify token functionalities
    Close Browser"""
    ],
    'Description': [
        "This test case checks the tokens functionalities for all merchants in a web application."
    ],
    'Testcase name': [
        "Test Tokens Functionality Of All Merchants"
    ]
})

web_autopay = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the autopay service functionality of Omnicorp customers."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the autopay service functionality of Omnicorp customers
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/autopay
${BROWSER}       chrome
${CUSTOMER_NUMBER} 123456
${ACCOUNT_NUMBER}  account123
${INVOICE_NUMBER}  inv123
${PAYMENT_METHOD}  credit_card
${ALL_TRANSACTIONS_COUNT}  10
${EXPECTED_STATUS}  active
${EXPECTED_CUSTOMER_NUMBER}  123456
${EXPECTED_PAYMENT_TYPE}  credit_card
${EXPECTED_STATUS_ACTIVE}  active
${EXPECTED_STATUS_INACTIVE}  inactive

*** Test Cases ***
Test Autopay Service Functionality Of Omnicorp Customers
    [Documentation]    Test case for the autopay service functionality of Omnicorp customers
    Launch Browser    ${BROWSER}    ${URL}
    Select Status    active
    Navigate To AutoPay
    Validate AutoPay Details Are Displayed    ${EXPECTED_CUSTOMER_NUMBER}    ${EXPECTED_PAYMENT_TYPE}    ${EXPECTED_STATUS}
    Validate AutoPay Is Cancelled    ${ACCOUNT_NUMBER}
    Select Invoices Due For The Payment
    Filter Customer In AutoPay    ${CUSTOMER_NUMBER}
    Navigate To Customer Details Page From AutoPay    ${INVOICE_NUMBER}
    Get Total Number Of Transactions In AutoPay
    Cancel AutoPay
    Create AutoPay    ${CUSTOMER_NUMBER}    ${PAYMENT_METHOD}
    Select Saved Payment Method In Autopay    ${PAYMENT_METHOD}
    Validate Active Payment Details After Displayed    ${ALL_TRANSACTIONS_COUNT}    ${EXPECTED_STATUS_ACTIVE}
    Validate Inactive Payment Details Are Displayed    ${ALL_TRANSACTIONS_COUNT}    ${EXPECTED_STATUS_INACTIVE}
    Select Each Day As Payment Option
    Close Browser"""
    ],
    'Description': [
        "This test case checks the autopay service functionalities for Omnicorp customers in a web application."
    ],
    'Testcase name': [
        "Test Autopay Service Functionality Of Omnicorp Customers"
    ]
})

scheduled_payments = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the scheduled payment service functionality of Omnicorp customers."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the scheduled payment service functionality of Omnicorp customers
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/scheduled_payments
${BROWSER}       chrome
${ACCOUNT_NUMBER}  account123
${EXPECTED_STATUS}  scheduled
${EXPECTED_PAYMENT_DATE}  2024-06-15
${EXPECTED_PAYMENT_TYPE}  credit_card
${DAY}  7
${DATE}  2024-06-14

*** Test Cases ***
Test Scheduled Payment Service Functionality Of Omnicorp Customers
    [Documentation]    Test case for the scheduled payment service functionality of Omnicorp customers
    Launch Browser    ${BROWSER}    ${URL}
    Validate Last 7 Days And 30 Days Scheduled Payments    ${DAY}
    Validate Today And Yesterday Scheduled Payments    ${DATE}
    Create Scheduled Payment    ${ACCOUNT_NUMBER}
    Select Payment Date    ${DATE}
    Validate Last Month And This Month Date Scheduled Payments    ${DAY}
    Validate Status In Scheduled Payments    ${EXPECTED_STATUS}
    Validate Scheduled Payment Details Are Displayed    ${EXPECTED_PAYMENT_DATE}    ${EXPECTED_STATUS}    ${EXPECTED_PAYMENT_TYPE}
    Cancel Scheduled Payment
    Close Browser"""
    ],
    'Description': [
        "This test case checks the scheduled payment service functionalities for Omnicorp customers in a web application."
    ],
    'Testcase name': [
        "Test Scheduled Payment Service Functionality Of Omnicorp Customers"
    ]
})


web_customers = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the customer service functionality of Sterlincooper customers."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the customer service functionality of Sterlincooper customers
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/customer_service
${BROWSER}       chrome
${ACCOUNT_NUMBER}  account123
${INVOICE_NUMBER}  inv123
${EXPECTED_MESSAGE}  success
${NOTES}  "Customer requested an update"

*** Test Cases ***
Test Customer Service Functionality Of Sterlincooper Customers
    [Documentation]    Test case for the customer service functionality of Sterlincooper customers
    Launch Browser    ${BROWSER}    ${URL}
    Validate Open Invoice Is Displayed    ${INVOICE_NUMBER}
    Filter Details    ${ACCOUNT_NUMBER}
    Validate Prevent Override Is Displayed
    Navigate To Resend Receipt Page
    Cancel Send Invoice Receipt
    Enter Account Number And Invoice    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Enter Text In Notes    ${NOTES}
    Validate Payment Method Is Cancelled
    Validate Provider Response Message Is Displayed    ${EXPECTED_MESSAGE}
    Enter ACH/Echeck Details    checking    123456789    987654321    John Doe
    Close Browser"""
    ],
    'Description': [
        "This test case checks the customer service functionalities for Sterlincooper customers in a web application."
    ],
    'Testcase name': [
        "Test Customer Service Functionality Of Sterlincooper Customers"
    ]
})

failed_login_attempts = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the failed login attempts functionality of Sterlincooper customers."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the failed login attempts functionality of Sterlincooper customers
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/login
${BROWSER}       chrome
${ACCOUNT_NUMBER}  account123
${EXPECTED_RECENT_ATTEMPTS}  3
${EXPECTED_TOTAL_ATTEMPTS}  10
${EXPECTED_FIRST_ATTEMPT}  2024-06-01
${EXPECTED_LAST_ATTEMPT}  2024-06-14
${INVOICE_NUMBER}  inv123

*** Test Cases ***
Test Failed Login Attempts Functionality Of Sterlincooper Customers
    [Documentation]    Test case for the failed login attempts functionality of Sterlincooper customers
    Launch Browser    ${BROWSER}    ${URL}
    Login To PayNOW With Invalid Credentials    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Validate Number Of Recent Login Failed Attempts    ${ACCOUNT_NUMBER}    ${EXPECTED_RECENT_ATTEMPTS}
    Validate Total Number Of Login Failed Attempts    ${ACCOUNT_NUMBER}    ${EXPECTED_TOTAL_ATTEMPTS}
    Validate First Login Failed Attempt Is Displayed    ${ACCOUNT_NUMBER}    ${EXPECTED_FIRST_ATTEMPT}
    Validate Last Login Failed Attempt Is Displayed    ${ACCOUNT_NUMBER}    ${EXPECTED_LAST_ATTEMPT}
    Filter With Customer Number In Failed PayNOW Login    ${ACCOUNT_NUMBER}
    Validate Filterd Customer Number Is Displayed    ${ACCOUNT_NUMBER}
    Expand Customer Failed Login Details
    Validate Customer Failed Login Details Are Expanded    sterlincooper
    Collapse Customer Failed Login Details
    Validate Customer Failed Login Details Are Collapsed    sterlincooper
    Close Browser"""
    ],
    'Description': [
        "This test case checks the failed login attempts functionalities for Sterlincooper customers in a web application."
    ],
    'Testcase name': [
        "Test Failed Login Attempts Functionality Of Sterlincooper Customers"
    ]
})


web_dashboard = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the dashboard functionality of Sterlincooper dashboards."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the dashboard functionality of Sterlincooper dashboards web application
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/dashboard
${BROWSER}       chrome
${ACCOUNT_NUMBER}  account123
${EXPECTED_EMAIL}  email@example.com
${EXPECTED_DATE}  2024-06-14
${EXPECTED_SUBJECT}  Invoice Summary
${EXPECTED_EMAILFORMAT}  valid@example.com
${EXPECTED_PDFSTATUS}  attached
${CUSTOMER}  customer123
${FILTER_WITH}  filter123
${EXPECTED_COUNT}  5
${PAGE}  next
${DAY}  7

*** Test Cases ***
Test Dashboard Functionality Of Sterlincooper Dashboards
    [Documentation]    Test case for the dashboard functionality of Sterlincooper dashboards
    Launch Browser    ${BROWSER}    ${URL}
    Validate Details Are Displayed In Last Page
    Validate Details Are Displayed In First Page
    Send Invoice Email And Navigate To Email Summary    ${ACCOUNT_NUMBER}
    Expand Details In Email Summary
    Validate Email Summary Page Is Displayed    ${EXPECTED_DATE}
    Filter With Customer Number In Email Details    ${FILTER_WITH}    ${ACCOUNT_NUMBER}
    Validate Details Are Displayed In Next And Previous Pages    ${EXPECTED_COUNT}
    Validate Email Format In Email Details    ${EXPECTED_EMAILFORMAT}
    Navigate To Customer Details Page From Email Details    ${CUSTOMER}
    Validate Email Details Are Displayed    ${EXPECTED_EMAIL}    ${EXPECTED_DATE}    ${EXPECTED_SUBJECT}
    Reset Filter
    Validate Email Details Are Expanded In Email Summary
    Navigate To Customer Details Page From Email Summary
    Collapse Details In Email Summary
    Validate Email Details Are Collapsed In Email Summary
    Navigate To Pages    ${PAGE}
    Validate Reset Filter Details Are Displayed
    Validate Email Sent Date And Subject    ${EXPECTED_SUBJECT}    ${EXPECTED_EMAIL}
    Validate Email PDF Attachment Status    ${EXPECTED_PDFSTATUS}
    Navigate To Email Summary Page    ${DAY}
    Close Browser"""
    ],
    'Description': [
        "This test case checks the dashboard functionalities for Sterlincooper dashboards in a web application."
    ],
    'Testcase name': [
        "Test Dashboard Functionality Of Sterlincooper Dashboards"
    ]
})

# Creating a new dataframe in the desired format
web_invoices = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the invoices functionality of Sterlincooper service."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the invoices functionality of Sterlincooper service web application
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/invoices
${BROWSER}       chrome
${INVOICE_NUMBER}  inv123
${CUSTOMER_NUMBER}  customer123
${EXPECTED_DATE}  2024-06-14
${EXPECTED_STATUS}  success
${EXPECTED_EMAIL}  email@example.com

*** Test Cases ***
Test Invoices Functionality Of Sterlincooper Service
    [Documentation]    Test case for the invoices functionality of Sterlincooper service
    Launch Browser    ${BROWSER}    ${URL}
    Validate Transaction Source After Transaction Is Displayed
    Expand Email Details
    Validate Today And Yesterday Invoice Are Displayed    ${EXPECTED_DATE}
    Validate Filtered Cusomer Number In Displayed Invoice    ${CUSTOMER_NUMBER}
    Validate Financial Payment Details Are Displayed
    Select Tab In Invoice Details Page
    Send Email Invoice
    Validate Sent Date And Provider Response Message Is Displayed    ${EXPECTED_STATUS}
    Validate PayNOW Invoice Details Page Is Displayed
    Enable Toggle Button
    Validate Email Details Are Expanded
    Validate Toggle Button Is Enabled
    Validate Email Format Type Is Displayed
    Validate Email Details Are Collapsed
    Navigate To Details Page From Invoices
    Collapse Email Details
    Validate Email Address Is Displayed    ${EXPECTED_EMAIL}
    Validate Filtered Invoice Number In Displayed Invoice    ${INVOICE_NUMBER}
    Filter Invoice In Grid
    Validate Filtered Invoice Is Displayed    ${INVOICE_NUMBER}
    Filter Invoice Details With Invoice And Customer Number    ${INVOICE_NUMBER}    ${CUSTOMER_NUMBER}
    Validate PDF Attachment Status Is Displayed
    Validate Terms Amount Are Displayed In Financial Details
    Validate Invoices Date For Last 7 Days And 30 Days    ${EXPECTED_DATE}
    Validate Line Items Details Are Displayed
    Navigate To Transaction Details From Pending Payments
    Validate Invoice Details Are Displayed
    Validate Invoice
    Close Browser"""
    ],
    'Description': [
        "This test case checks the invoices functionalities for Sterlincooper service in a web application."
    ],
    'Testcase name': [
        "Test Invoices Functionality Of Sterlincooper Service"
    ]
})


# Creating a new dataframe in the desired format
settings = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the settings functionality of Sterlincooper service."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the settings functionality of Sterlincooper service web application
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/settings
${BROWSER}       chrome
${ACCOUNT_NUMBER}  account123
${INVOICE_NUMBER}  inv123
${EXPECTED_FILENAME}  document.pdf
${EXPECTED_MESSAGE}  success
${FILE_NAME}  upload.pdf
${ACTUAL_FILENAME}  uploaded.pdf
${EXPECTED_DOCUMENT_TYPE}  pdf

*** Test Cases ***
Test Settings Functionality Of Sterlincooper Service
    [Documentation]    Test case for the settings functionality of Sterlincooper service
    Launch Browser    ${BROWSER}    ${URL}
    Navigate To PayNOW    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}
    Validate PDF Document Is Displayed In PayNOW    ${EXPECTED_FILENAME}
    Validate PDF Is Deleted In Settings    ${EXPECTED_MESSAGE}
    Validate Message In Settings    ${EXPECTED_MESSAGE}
    Select Document Type In Settings
    Upload File In Settings Tab    ${FILE_NAME}
    Validate PDF Is Closed
    Close PDF Document
    Validate File Is Uploaded    ${ACTUAL_FILENAME}    ${EXPECTED_DOCUMENT_TYPE}
    Delete PDF Attachment
    Close Browser"""
    ],
    'Description': [
        "This test case checks the settings functionalities for Sterlincooper service in a web application."
    ],
    'Testcase name': [
        "Test Settings Functionality Of Sterlincooper Service"
    ]
})


all_transactions = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing all transactions functionality of Sterlincooper service."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing all transactions functionality of Sterlincooper service web application
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/transactions
${BROWSER}       chrome
${TRANSACTION_TAB}  details
${COUNT}  10
${AMOUNT}  1000
${TRANSACTION_TYPE}  ACH
${INVOICES_LIST}  [inv123, inv124]
${MONTH}  June
${EXPECTED_OPTION}  apply

*** Test Cases ***
Test All Transactions Functionality Of Sterlincooper Service
    [Documentation]    Test case for the transactions functionality of Sterlincooper service
    Launch Browser    ${BROWSER}    ${URL}
    Select Tab In Transaction Details Page    ${TRANSACTION_TAB}
    Validate Total Count And Amount Of ACH Transactions    ${COUNT}    ${AMOUNT}
    Select Transaction Type    ${TRANSACTION_TYPE}
    Select Confirm In Void Transaction Popup
    Validate Invoices Displayed On Invoice Detail Page    ${INVOICES_LIST}
    Validate Transactions Count In Previous Page
    Validate Sorted Transactions
    Validate Current And Previous Month Is Displayed    ${MONTH}
    Validate Payment Application Option    ${EXPECTED_OPTION}
    Login And Navigate To Transaction Details Page
    Close Browser"""
    ],
    'Description': [
        "This test case checks the transactions functionalities for Sterlincooper service in a web application."
    ],
    'Testcase name': [
        "Test All Transactions Functionality Of Sterlincooper Service"
    ]
})


payment_status = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the payment status functionality of Sterlincooper service."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the payment status functionality of Sterlincooper service web application
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/payment_status
${BROWSER}       chrome
${ACCOUNT_NUMBER}  account123
${DATE}  2024-06-14
${EXPECTED_STATUS}  scheduled
${EXPECTED_PAYMENT_DATE}  2024-06-15
${EXPECTED_PAYMENT_TYPE}  credit_card
${DAY}  7

*** Test Cases ***
Test Payment Status Functionality Of Sterlincooper Service
    [Documentation]    Test case for the payment status functionality of Sterlincooper service
    Launch Browser    ${BROWSER}    ${URL}
    Validate Last 7 Days And 30 Days Scheduled Payments    ${DAY}
    Validate Today And Yesterday Scheduled Payments    ${DATE}
    Create Scheduled Payment    ${ACCOUNT_NUMBER}
    Select Payment Date    ${DATE}
    Validate Last Month And This Month Date Scheduled Payments    ${DAY}
    Validate Status In Scheduled Payments    ${EXPECTED_STATUS}
    Validate Scheduled Payment Details Are Displayed    ${EXPECTED_PAYMENT_DATE}    ${EXPECTED_STATUS}    ${EXPECTED_PAYMENT_TYPE}
    Cancel Scheduled Payment
    Close Browser"""
    ],
    'Description': [
        "This test case checks the payment status functionalities for Sterlincooper service in a web application."
    ],
    'Testcase name': [
        "Test Payment Status Functionality Of Sterlincooper Service"
    ]
})


virtual_terminal = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the virtual terminal functionality of Sterlincooper service."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the virtual terminal functionality of Sterlincooper service web application
Library          SeleniumLibrary

*** Variables ***
${URL}           https://example.com/virtual_terminal
${BROWSER}       chrome
${ACCOUNT_NUMBER}  account123
${CUSTOMER_NUMBER}  customer123
${SAVED_PAYMENT_METHOD}  credit_card
${EXPECTED_SURCHARGE}  10
${STATE}  NY
${EXPECTED_SURCHARGE_ZERO}  0
${OPTION}  confirm

*** Test Cases ***
Test Virtual Terminal Functionality Of Sterlincooper Service
    [Documentation]    Test case for the virtual terminal functionality of Sterlincooper service
    Launch Browser    ${BROWSER}    ${URL}
    Search Customer In Virtual Terminal    ${ACCOUNT_NUMBER}
    Validate Searched Customer Number Is Displayed    ${CUSTOMER_NUMBER}
    Process Transacton With Saved Payment Method    ${ACCOUNT_NUMBER}    ${SAVED_PAYMENT_METHOD}
    Validate Surcharge    ${EXPECTED_SURCHARGE}
    Select Multiple Invoices
    Validate Surchage Exempt Is Applied
    Select State In PayNOW    ${STATE}
    Select State In Virtual Terminal    ${STATE}
    Validate Surcharge Is Not Applied For Zero Surcharge    ${EXPECTED_SURCHARGE_ZERO}
    Select Over Payment Confirmation    ${OPTION}
    Navigate To PayNOW And Select State    ${STATE}
    Close Browser"""
    ],
    'Description': [
        "This test case checks the virtual terminal functionalities for Sterlincooper service in a web application."
    ],
    'Testcase name': [
        "Test Virtual Terminal Functionality Of Sterlincooper Service"
    ]
})


common_api = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the general common API functionality of clients."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the general common API functionality of clients
Library          RequestsLibrary

*** Variables ***
${BASE_URL}      https://api.example.com
${MERCHANT}      merchant123
${BODY}          {"key": "value"}

*** Test Cases ***
Test General Common API Functionality Of Clients
    [Documentation]    Test case for the general common API functionality of clients
    Create Session    api_session    ${BASE_URL}
    ${headers}=    Get JSON Headers    ${MERCHANT}
    ${json_body}=    Convert To JSON    ${BODY}
    ${response}=    Post Request    api_session    /endpoint    headers=${headers}    data=${json_body}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}"""
    ],
    'Description': [
        "This test case checks the general common API functionalities for clients."
    ],
    'Testcase name': [
        "Test General Common API Functionality Of Clients"
    ]
})


customer_api_ = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the general customer functionality of an API."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the general customer functionality of an API
Library          RequestsLibrary

*** Variables ***
${BASE_URL}        https://api.example.com
${MERCHANT_ID}     merchant123
${MERCHANT_KEY}    key123
${UNIQUE_VALUE}    unique456

*** Test Cases ***
Test General Customer Functionality Of An API
    [Documentation]    Test case for the general customer functionality of an API
    Create Session    api_session    ${BASE_URL}
    ${billing_address}=    Create Billing Address Body    ${UNIQUE_VALUE}    ${MERCHANT_ID}
    ${json_body}=    Create Customer Body    ${UNIQUE_VALUE}    ${MERCHANT_KEY}    ${MERCHANT_ID}
    ${unique_value}=    Send Request To Create On Credit Hold Customer    ${MERCHANT_ID}
    ${shipping_address}=    Create Shipping Address Body    ${UNIQUE_VALUE}    ${MERCHANT_ID}
    ${unique_value}=    Send Request To Create Customer    ${MERCHANT_KEY}    ${MERCHANT_ID}
    ${json_body}=    Create On Credit Hold Customer Body    ${UNIQUE_VALUE}    ${MERCHANT_KEY}    ${MERCHANT_ID}
    ${response}=    Post Request    api_session    /customers    headers=${headers}    data=${json_body}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}"""
    ],
    'Description': [
        "This test case checks the general customer functionalities for an API."
    ],
    'Testcase name': [
        "Test General Customer Functionality Of An API"
    ]
})


invoice_api = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the invoice services functionality of an API."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the invoice services functionality of an API
Library          RequestsLibrary

*** Variables ***
${BASE_URL}          https://api.example.com
${MERCHANT}          merchant123
${UNIQUE_VALUE}      unique456
${INVOICE_NUMBER}    inv789
${DUE_AMOUNT}        1000
${INVOICE_DUE_DATE}  2024-06-15

*** Test Cases ***
Test Invoice Services Functionality Of An API
    [Documentation]    Test case for the invoice services functionality of an API
    Create Session    api_session    ${BASE_URL}
    ${json_body}=    Create Invoice Body    ${UNIQUE_VALUE}    ${INVOICE_NUMBER}    ${DUE_AMOUNT}    ${INVOICE_DUE_DATE}
    ${response}=    Post Request    api_session    /invoices    headers=${headers}    data=${json_body}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
    ${json_body}=    Create Disputed Invoice Body    ${UNIQUE_VALUE}    ${INVOICE_NUMBER}    ${DUE_AMOUNT}    ${INVOICE_DUE_DATE}
    ${response}=    Post Request    api_session    /disputed_invoices    headers=${headers}    data=${json_body}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
    ${company_details}=    Create Company Details Body
    ${product_details}=    Create Product Details Body
    ${ship_to_address}=    Create Ship To Address Body
    ${bill_to_address}=    Create Bill To Address Body
    ${response}=    Post Request    api_session    /invoices    headers=${headers}    data=${json_body}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
    @{invoices_list}=    Create Multiple Invoices Through API    ${MERCHANT}    ${UNIQUE_VALUE}    ${INVOICE_DUE_DATE}
    FOR    ${invoice}    IN    @{invoices_list}
        Log    ${invoice}
    END"""
    ],
    'Description': [
        "This test case checks the invoice services functionalities for an API."
    ],
    'Testcase name': [
        "Test Invoice Services Functionality Of An API"
    ]
})


process_payment_api = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the process payment services functionality of an API."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the process payment services functionality of an API
Library          RequestsLibrary

*** Variables ***
${BASE_URL}          https://api.example.com
${MERCHANT}          merchant123
${ACCOUNT_NUMBER}    account456
${INVOICE_NUMBER}    inv789
${CARD_NUMBER}       4111111111111111
${AMOUNT}            1000
${ROUTING_NUMBER}    123456789
${REASON}            "Payment for invoice"

*** Test Cases ***
Test Process Payment Services Functionality Of An API
    [Documentation]    Test case for the process payment services functionality of an API
    Create Session    api_session    ${BASE_URL}
    ${json_body}=    Create Process Invoice Payment Body For Credit Card    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    ${CARD_NUMBER}    ${AMOUNT}
    ${response}=    Post Request    api_session    /process_payment    headers=${headers}    data=${json_body}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
    ${response_details}=    Get Response Details    ${response}
    ${gateway_id}=    Get Gatewayid    ${response}
    ${billing_address}=    Get Billing Information    ${response}
    ${response}=    Send Request To Process Transaction For Multiple Invoices    ${MERCHANT}    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    ${CARD_NUMBER}    ${AMOUNT}
    Should Be Equal As Strings    ${response.status_code}    200
    ${response}=    Send Request To Process Payment Through ACH/Echeck    ${MERCHANT}    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    ${CARD_NUMBER}    ${ROUTING_NUMBER}    ${AMOUNT}
    Should Be Equal As Strings    ${response.status_code}    200
    ${response}=    Send Request To Process Payment For Credit Card    ${MERCHANT}    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    ${CARD_NUMBER}    ${AMOUNT}
    Should Be Equal As Strings    ${response.status_code}    200
    ${headers}=    Get JSON Header For Credit Card Token
    ${card_details}=    Get Card Details    ${CARD_NUMBER}
    ${json_body}=    Create Process Invoice Payment Body For ACH/Echeck    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    ${CARD_NUMBER}    ${ROUTING_NUMBER}    ${AMOUNT}
    ${response}=    Post Request    api_session    /process_payment    headers=${headers}    data=${json_body}
    Should Be Equal As Strings    ${response.status_code}    200
    ${amount}=    Get Amount    ${response}
    ${json_body}=    Create Request For Credit Card Token    ${card_details}
    ${invoice_body}=    Create Invoice For Processing Payment    ${INVOICE_NUMBER}    ${REASON}
    ${transaction_id}=    Get Id After Processing Transaction    ${response}
    ${json_body}=    Create Process Invoice Body For Multiple Transactions    ${ACCOUNT_NUMBER}    ${INVOICE_NUMBER}    ${CARD_NUMBER}    ${ROUTING_NUMBER}    ${AMOUNT}
    ${response}=    Send Request To Get Credit Card Token    ${CARD_NUMBER}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}"""
    ],
    'Description': [
        "This test case checks the process payment services functionalities for an API."
    ],
    'Testcase name': [
        "Test Process Payment Services Functionality Of An API"
    ]
})


token_api = pd.DataFrame({
    'Prompt': [
        "Generate a Robot Framework test case for testing the token service functionality of an API."
    ],
    'Response': [
        """*** Settings ***
Documentation    Test cases for testing the token service functionality of an API
Library          RequestsLibrary

*** Variables ***
${BASE_URL}          https://api.example.com
${INVOICE_LOCATION}  invoice_location
${CUSTOMER_NUMBER}   customer_number

*** Test Cases ***
Test Token Service Functionality Of An API
    [Documentation]    Test case for the token service functionality of an API
    Create Session    api_session    ${BASE_URL}
    ${invoice_token}=    Send Request To Get Invoice Token    ${INVOICE_LOCATION}
    ${headers}=    Get Token Header
    ${json_body}=    Create Body To Get PayNowSession Id    ${CUSTOMER_NUMBER}
    ${header_value}=    Get Invoice Location    ${response}
    ${response}=    Send Request To Get PayNowSession Id    ${CUSTOMER_NUMBER}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
    ${headers}=    Get Headers For PayNowSession Id
    ${session_id}=    Get PayNowSession Id From Request Body    ${response}"""
    ],
    'Description': [
        "This test case checks the token service functionalities for an API."
    ],
    'Testcase name': [
        "Test Token Service Functionality Of An API"
    ]
})



# Adding dataframes to the pipeline
pipeline.add_dataframe(common_web)
pipeline.add_dataframe(homepage)
pipeline.add_dataframe(web_tokens)
pipeline.add_dataframe(web_autopay)
pipeline.add_dataframe(scheduled_payments)
pipeline.add_dataframe(web_customers)
pipeline.add_dataframe(failed_login_attempts)
pipeline.add_dataframe(web_dashboard)
pipeline.add_dataframe(web_invoices)
pipeline.add_dataframe(settings)
pipeline.add_dataframe(all_transactions)
pipeline.add_dataframe(payment_status)
pipeline.add_dataframe(virtual_terminal)
pipeline.add_dataframe(common_api)
pipeline.add_dataframe(customer_api_)
pipeline.add_dataframe(invoice_api)
pipeline.add_dataframe(process_payment_api)
pipeline.add_dataframe(token_api)

# Combine dataframes
combined_df = pipeline.combine_dataframes()

# Save combined dataframe to JSON
json_filepath = '../json/clientCentral_apiWeb.json'
json_file = pipeline.to_json(combined_df, json_filepath)

# Converting JSON to CSV
csv_filepath = '../csv/clientCentral_apiWeb.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")