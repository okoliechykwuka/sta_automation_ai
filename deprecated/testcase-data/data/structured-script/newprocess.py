# Recreate the CSV data manually
import pandas as pd

# Data for the CSV
data = {
    "Prompt": [
        "Create a data-driven testcase that validates TC_11 Validate Customer Is Unable To Process Payment By A Declined Card",
        "Create a data-driven testcase that validates TC_08 Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week",
        "Create a data-driven testcase that validates TC_05 Validate Merchant Is Able To Schedule Payment With Master Credit Card",
        "Create a keyword-driven testcase that handles common open invoices",
        "Create a keyword-driven testcase that handles integrated open invoices",
        "Create a data-driven testcase that validates TC_04 Validate Merchant Is Able To View First And Last Login Failed Attempt",
        "Create a data-driven testcase that validates TC_02 Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts",
        "Create a data-driven testcase that validates TC_03 Validate Merchant Is Able To Filter Auto Pay Details",
        "Create a keyword-driven testcase that handles virtual terminal operations",
        "Create a keyword-driven testcase that handles dashboard operations",

    ],
    "Testcase Type": [
        "Data-driven",
        "Data-driven",
        "Data-driven",
        "Keyword-driven",
        "Keyword-driven",
        "Data-driven",
        "Data-driven",
        "Data-driven",
        "Keyword-driven",
        "Keyword-driven",

    ],
    "Testcase Name": [
        "TC_11 Validate Customer Is Unable To Process Payment By A Declined Card",
        "TC_08 Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week",
        "TC_05 Validate Merchant Is Able To Schedule Payment With Master Credit Card",
        "Common Open Invoices",
        "Integrated Open Invoices",
        "TC_04 Validate Merchant Is Able To View First And Last Login Failed Attempt",
        "TC_02 Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts",
        "TC_03 Validate Merchant Is Able To Filter Auto Pay Details",
        "Virtual Terminal Operations",
        "Dashboard Operations",

    ],
    "Response": [
    """*** Settings ***\n
        Documentation    Suite contains test cases for validating Customer Is Unable To Process Payment By A Declined Card
        Test Template    Validate Customer Is Unable To Process Payment By A Declined Card
        Test Tags        Priority1    test:retry(1)
        Resource         ../../../Config/super.resource
        Library          DataDriver    ${TESTDATA_FOLDER}    sheet_name=DeclinedCardPayment
        
        *** Test Cases ***
        ${test_case_name}
        
        *** Keywords ***
        Validate Customer Is Unable To Process Payment By A Declined Card
            [Arguments]     ${test_case_name}
            [Documentation]     Validate Customer Is Unable To Process Payment By A Declined Card
            ${card_details}    Read TestData From Excel    ${TESTDATA_FOLDER}    ${test_case_name}    DeclinedCardPayment
            ${customer_details}     Generate Random Customer Details
            Launch PayNow Application    ${NON_INTEGRATED_MERCHANT}    
            Enter Customer Details      ${customer_details}    ${NON_INTEGRATED_MERCHANT}  
            Select Payment Type      Lump Sum
            Enter Lumpsum Amount      1
            Select Payment Method     Credit Card
            Enter Credit Card Values   ${card_details}
            Validate Errors After Clicking On Process Invoice    ${card_details.Error_Message}""",
    """*** Settings ***
    Documentation    Suite contains test cases for validating Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week
    Test Template    Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week
    Test Tags     Priority1    test:retry(1)
    Resource   ../../../Config/super.resource
    Library    DataDriver    ${TESTDATA_FOLDER}    sheet_name=AutoPaySunday
    
    *** Test Cases ***
    ${test_case_name}
    
    *** Keywords ***
    Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week
        [Arguments]    ${test_case_name}
        [Documentation]     Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week  
        ${Payment_details}    Read TestData From Excel    ${TESTDATA_FOLDER}    ${test_case_name}    AutoPaySunday    
        ${account_number}    Send Request To Create Customer    ${OMNICORP_MERCHANT}    3
        ${invoice_number}   Send Request To Create Invoice For Customer    ${account_number}    ${OMNICORP_MERCHANT}
        Login To PayNOW And Navigate To Autopay   ${account_number}    ${invoice_number}
        Select Specific Day Of The Week   ${Payment_details.Day}
        Select Invoices Due For The Payment
        Enter Customer And Credit Card Details For AutoPay   4111111111111111
        Validate Created AutoPay Details For Specific Day Of Week       Days of Week    All Invoices Due    ${Payment_details.Day}    
        Send Request To Create AutoPay For Specific Day Of The Week   ${account_number}    4111111111111111    ${Payment_details.Day}    
        Validate Created AutoPay Details For Specific Day Of Week       Days of Week    All Invoices Due    ${Payment_details.Day}   
        Validate AutoPay Origin In Scheduled Payments   ${account_number}    ${invoice_number}    AutoPay""",
    """*** Settings ***
    Documentation    Suite contains test cases for validating Merchant Is Able To Schedule Payment With Master Credit Card
    Test Template    Validate Merchant Is Able To Schedule Payment With Master Credit Card
    Test Tags        Priority1    test:retry(1)
    Resource         ../../../Config/super.resource
    Library          DataDriver    ${TESTDATA_FOLDER}    sheet_name=SchedulePaymentMasterCard
    
    *** Test Cases ***
    ${test_case_name}
    
    *** Keywords ***
    Validate Merchant Is Able To Schedule Payment With Master Credit Card
        [Arguments]    ${test_case_name}
        [Documentation]    Validate Merchant Is Able To Schedule Payment With Master Credit Card  
        ${Scheduled_Payments}    Read TestData From Excel    ${TESTDATA_FOLDER}    ${test_case_name}    SchedulePaymentMasterCard 
        ${customer_details}    Generate Random Customer Details
        ${account_number}    Set Variable    ${Scheduled_Payments.Account_Number}
        ${invoice_number}    Set Variable    ${Scheduled_Payments.Invoice_Number}   
        Launch PayNow Application    ${OMNICORP_MERCHANT}
        Enter Account Number And Invoice    ${account_number}    ${invoice_number}   
        Enter Customer Details    ${customer_details}    ${OMNICORP_MERCHANT} 
        Select Payment Method    Credit Card
        Enter Credit Card Details    ${Scheduled_Payments.Creditcard_Number}    ${Scheduled_Payments.Expiry_Date}    ${Scheduled_Payments.CVV}    
        Select Payment Date    today+1
        Create Schedule Payment    
        Send Event To Process Schedule Payment    ${account_number}    ${invoice_number}    
        Validate Scheduled Payment Status    ${account_number}    ${invoice_number}    ${Scheduled_Payments.Status}""",
    """
    Common Open Invoices    
    [Documentation]    Handling common open invoices operations  
    Select Payment Method    Credit Card
    Enter ACH/ECheck Values    ${echeck_details}
    Navigate To Window
    Process Payment Without Payment Authorization   
    Validate Payment Method And Total Amount    ${expected_payment_method}    ${expected_amount}  
    Enter Customer Details    ${customer_details}    ${merchant}
    Validate Payment Authorization Is Unchecked By Default
    Click On Close Button
    Signout From Payment Receipt Page   
    Navigate To Contact Unified Payments Group For More Information   
    Validate Surcharge Amount Is Displayed
    Validate Total Charges Under Summary Of Payment    ${expected_charges}  
    Validate Payment Authorization Screen Is Closed
    Validate Customer Invoice Referral Page Is Visible   
    Validate Details In Generated Payment Receipt    ${payment_type}    ${account_number}    ${payment_method}    ${amount}   
    Validate Surcharge Percentage Should Be Equal    ${exp_percentage}
    Validate Checkboxes Are Selected By Default
    Add Reason For Less Than Due Amount    ${invoice}    ${reason}
    Validate Errors After Clicking On Process Invoice    ${error_message}
    Enter Zip Code    ${zip_code}
    Wait Till Loading Text Is Invisible
    Validate Invoice Receipt Is Received In Email    ${transaction_id}
    ${transaction_id}    Get Transaction ID
    Validate Find Routing Number Popover Is Displayed
    ${customer_details}    Generate Random Customer Details
    Select Specific Invoice And Enter Amount    ${invoice_number}    ${amount} 
    Select Account Type In ACH/ECheck    ${account_type}
    Validate Send EMail Receipt Is Checked By Default   
    Navigate To Payment Authorization And Validate Title    
    Enter Lumpsum Amount    ${amount}
    Validate Payment Type And Account Number    ${expected_payment_method}    ${expected_account_number} 
    Select State    ${state}
    Enter Credit Card Details    ${card_number}    ${expired_data}    ${cvv_number}
    Validate Terms Conditions And Privacy Policy Page Is Closed
    Validate Future Payment Details In Scheduled Payments Page    ${future_date}
    Select Payment Type    ${payment_type}   
    Process Invoice Payment
    Navigate To Terms Conditions And Privacy Policy Page   
    Validate Terms Conditions And Privacy Policy Page Is Displayed   
    Validate Payment Receipt Is Generated
    Enter ACH/ECheck Details    ${account_number}    ${routing_number}""",
    """
    Integrated Open Invoices
    [Documentation]    Handling integrated open invoices operations
    Expand All Line Items
    Save Payment Method With Nickname    ${payment_method}    ${nickname}
    Validate Unpaid Invoices Are Displayed    ${invoice}
    Validate Invoice Status Is Paid    ${invoice_number}
    Select Multiple Invoices    ${invoice_list}
    Click On Total Amount Link
    Validate Customer PO Number From The Specific Invoice Grid    ${invoice_number}
    Choose Filter Type    ${filter_name}
    Collapse Specific Line Item
    Click On Days Past Due Amount Link    ${due_date}
    Validate Selected Date Is Displayed In Date Range    ${increment}
    Validate Date Range Is Displayed In Payment History Tab
    Validate Multiple Invoices Check Box Should Be Checked By Default    ${invoice}
    Enter Amount And Pay Invoice    ${amount}
    Cancel Login With Invoice Popup
    Select Date Range From Calendar    ${start_date}    ${end_date}
    Validate All Invoices Are Checked
    Collapse All Line Items
    Select All Due Invoices
    Navigate To Menu Tab    ${tab_name}
    Validate Line Item Is Expanded
    Pay Invoice From Invoice Screen    ${invoice_number}
    Unselect Invoice Checkboxes
    Validate Total Amount After Selecting State
    Use Valid Check And Pay The Amount    ${amount}    ${account_type}    ${account_number}    ${routing_number}
    Select Any Saved Payment Method    ${cardno_or_checkno}
    Validate Discount Applied For Early Payment Before Due Date    ${invoice_number}
    Validate Invoice Checkbox Should Be Unselected
    Filter Invoice By Using Logical Operator    ${logical_operator}    ${filter_option""",
    """*** Settings ***
    Documentation    Suite contains test cases for validating Merchant Is Able To View First And Last Login Failed Attempt
    Test Template    Validate Merchant Is Able To View First And Last Login Failed Attempt
    Test Tags        Priority1    test:retry(1)
    Resource         ../../../Config/super.resource
    Library          DataDriver    ${TESTDATA_FOLDER}    sheet_name=LoginFailedAttempt

    *** Test Cases ***
    ${test_case_name}

    *** Keywords ***
    Validate Merchant Is Able To View First And Last Login Failed Attempt
        [Arguments]    ${test_case_name}
        [Documentation]    Validate Merchant Is Able To View First And Last Login Failed Attempt
        ${account_number}    Send Request To Create Customer    STERLING_COOPER
        ${invoice_number}    Send Request To Create Invoice For Customer    STERLING_COOPER    ${account_number}
        Send Request To Process Payment Through ACH/Echeck Card    STERLING_COOPER    ${account_number}    ${invoice_number}    ${ACH_ECHECK_DETAILS}
        Login To PayNOW With Invalid Credentials    ${account_number}    12345
        Select Module    Failed PayNOW Logins
        Filter With Customer Number In Failed PayNOW Logins    ${account_number}
        Validate First Login Failed Attempt Is Displayed    ${account_number}    today
        Validate Last Login Failed Attempt Is Displayed    ${account_number}    today""",
    """*** Settings ***
    Documentation    Suite contains test cases for validating Merchant Is Able To View Number Of Recent And Total Login Failed Attempts
    Test Template    Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts
    Test Tags        Priority1    test:retry(1)
    Resource         ../../../Config/super.resource
    Library          DataDriver    ${TESTDATA_FOLDER}    sheet_name=LoginFailedAttempts

    *** Test Cases ***
    ${test_case_name}

    *** Keywords ***
    Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts
        [Arguments]    ${test_case_name}
        [Documentation]    Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts
        ${account_number}    Send Request To Create Customer    STERLING_COOPER
        ${invoice_number}    Send Request To Create Invoice For Customer    STERLING_COOPER    ${account_number}
        Send Request To Process Payment Through ACH/Echeck Card    STERLING_COOPER    ${account_number}    ${invoice_number}    ${ACH_ECHECK_DETAILS}
        Login To PayNOW With Invalid Credentials    ${account_number}    12345
        Select Module    Failed PayNOW Logins
        Filter With Customer Number In Failed PayNOW Logins    ${account_number}
        Validate Number Of Recent Login Failed Attempts    ${account_number}    1
        Validate Total Number Of Login Failed Attempts    ${account_number}    1""",
    """*** Settings ***
    Documentation    Suite contains test cases for validating Merchant Is Able To Filter Auto Pay Details
    Test Template    Validate Merchant Is Able To Filter Auto Pay Details
    Test Tags        Priority1    test:retry(1)
    Resource         ../../../Config/super.resource
    Library          DataDriver    ${TESTDATA_FOLDER}    sheet_name=AutoPayDetails

    *** Test Cases ***
    ${test_case_name}

    *** Keywords ***
    Validate Merchant Is Able To Filter Auto Pay Details
        [Arguments]    ${test_case_name}
        [Documentation]    Validate Merchant Is Able To Filter Auto Pay Details
        ${account_number}    Send Request To Create Customer    omnicorp    3
        ${invoice_number}    Send Request To Create Invoice For Customer    omnicorp    ${account_number}
        ${customer_details}    Generate Random Customer Details
        Select Merchant    Omnicorp
        Select Module    Customers
        Filter With Customer Number    ${account_number}
        Navigate To Details Page From Invoices    ${account_number}
        Save Credit Card Payment    4111111111111111    Credit Card
        Create AutoPay    ${customer_details}    Credit Card
        Select Module    AutoPay
        Filter Customer In AutoPay    ${account_number}
        Validate AutoPay Details Are Displayed    ${account_number}    All Invoices Due    Each Day    41111""",
    """Virtual Terminal Operations
        [Documentation]    Handling virtual terminal operations
        Search Customer In Virtual Terminal    ${account_number}
        Validate Searched Customer Number Is Displayed    ${customer_number}
        Process Transacton With Saved Payment Method    ${account_number}    ${saved_payment_method}
        Validate Surcharge    ${expected_surcharge}
        Select Multiple Invoices
        Validate Surchage Exempt Is Appliedtestcase-data/data/structured-script/newprocess.py
        Select State In PayNOW    ${state}
        Select State In Virtual Terminal    ${state}
        Validate Surcharge Is Not Applied For Zero Surcharge State    ${expected_surcharge}
        Select Over Payment Confirmation    ${option}
        Navigate To PayNOW And Select State    ${state}""",
    """Dashboard Operations
        [Documentation]    Handling dashboard operations
        Validate Details Are Displayed In Last Page
        Validate Details Are Displayed In First Page
        Send Invoice Email And Navigate To Email Summary    ${account_number}
        Expand Details In Email Summary
        Validate Email Summary Page Is Displayed    ${date}
        Filter With Customer Number In Email Details    ${filter_with}    ${customer_number}
        Validate Details Are Displayed In Next And Previous Page    ${expected_count}
        Validate Email Format In Email Details    ${expected_emailformat}
        Navigate To Customer Details Page From Email Details    ${customer}
        Validate Email Details Are Displayed    ${expected_email}    ${expected_date}    ${expected_subject}
        Reset Filter
        Validate Email Details Are Expanded In Email Summary
        Navigate To Customer Details Page From Email Summary
        Collapse Details In Email Summary
        Validate Email Details Are Collapsed In Email Summary
        Navigate To Pages    ${page}
        Validate Reset Filter Details Are Displayed
        Validate Email Sent Date And Subject    ${expected_subject}    ${expected_emailaddress}
        Validate Email PDF Attachment Status    ${expected_pdfstatus}
        Navigate To Email Summary Page    ${day}""",
        
    ]
}

fulldata = pd.DataFrame(data)

csv_file = fulldata.to_csv('../csv/aligned_data.csv', index=False)

print(f"CSV data saved to: {csv_file}")

