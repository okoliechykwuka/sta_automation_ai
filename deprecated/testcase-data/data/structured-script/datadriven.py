# Recreate the CSV data manually
import pandas as pd

# Data for the CSV
data = {
    "Prompt": [
        "Create a data-driven testcase that validates TC_11 Validate Customer Is Unable To Process Payment By A Declined Card",
        "Create a data-driven testcase that validates TC_08 Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week",
        "Create a data-driven testcase that validates TC_05 Validate Merchant Is Able To Schedule Payment With Master Credit Card",
        "Create a data-driven testcase that validates TC_04 Validate Merchant Is Able To View First And Last Login Failed Attempt",
        "Create a data-driven testcase that validates TC_02 Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts",
        "Create a data-driven testcase that validates TC_03 Validate Merchant Is Able To Filter Auto Pay Details"
    ],
    "Testcase Type": [
        "Data-driven",
        "Data-driven",
        "Data-driven",
        "Data-driven",
        "Data-driven",
        "Data-driven",

    ],
    "Testcase Name": [
        "TC_11 Validate Customer Is Unable To Process Payment By A Declined Card",
        "TC_08 Validate Customer Is Able To Schedule AutoPay Payments On A Sunday Of The Week",
        "TC_05 Validate Merchant Is Able To Schedule Payment With Master Credit Card",
        "TC_04 Validate Merchant Is Able To View First And Last Login Failed Attempt",
        "TC_02 Validate Merchant Is Able To View Number Of Recent And Total Login Failed Attempts",
        "TC_03 Validate Merchant Is Able To Filter Auto Pay Details",

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
        Validate AutoPay Details Are Displayed    ${account_number}    All Invoices Due    Each Day    41111"""        
    ]
}

fulldata = pd.DataFrame(data)

csv_file = fulldata.to_csv('../csv/datadriven.csv', index=False)

print(f"CSV data saved to: {csv_file}")

