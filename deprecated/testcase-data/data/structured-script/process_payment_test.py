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

validate_process_payment_with_visa_card = pd.DataFrame({
    'Prompt': [
        "Create a validate a data driven testcase that validates FTC_117 validate process payment with visa debit card"
    ],
    'Testcased Type': [
        "Data-driven"
    ],
    'Testcase Name': [
        "FTC_117 Validate Process Payment With Visa Debit Card"
    ],
    'Response': [
        """ *** Settings *** <br>
        Documentation suite contains test cases for validating Process Payment with Visa Debit Card with valid and invalid data<br>
        Test Template Validate Process Payment With Visa Debit Card<br>
        Test Tags Priority1 test (1)<br>
        Resource ../../../Config/super.resource<br>
        Library DataDriver ${TESTDATA_FOLDER} sheet_name=ProcessPayment<br> 
        
        *** Test Cases *** <br>
        ${test_case_name}<br> 
        
        *** Keywords ***<br>
        Validate Process Payment With Visa Debit Card<br>
            [Arguments]                     ${test_case_name}<br>
            [Documentation]                 Validate Process Payment with Visa Debit Card<br>
            ${creditcard_details}           <br>Read TestData From Excel    ${TESTDATA_FOLDER}  ${test_case_name}   ProcessPayment<br>
            ${customer_details}             <br>Generate Random Customer Details<br>
            Launch PayNow Application       ${NON_INTEGRATED_MERCHANT}<br>
            Enter Customer Details          ${customer_details} ${NON_INTEGRATED_MERCHANT}<br>
            Select Payment Type             Lump Sum<br>
            Enter Lumpsum Amount            1<br>
            Select Payment Method           Credit Card<br>
            Enter Credit Card Values        ${creditcard_details}<br>
            ${status}                       Run Keyword And Return Status   
            Dictionary Should Contain Key   ${creditcard_details}   Error_Message<br>
            IF '${status}'=='True' 
                Validate Errors After Clicking On Process Invoice   ${creditcard_details}[Error_Message]<br>
            ELSE 
                Process Invoice Payment 
                Validate Payment Receipt Is Generated<br>
            END
        """
    ]
})

non_integrated_open_invoices = pd.DataFrame({
    'Prompt': [
        "Create a keyword driven testcase that handles open invoices of non-integrated types"
    ],
    'Testcase Type': [
        "Keyword-driven"
    ],
    'Testcase Name': [
        'Non-integrated Open Invoices'
    ],
    'Response': [
        """
        Validate All Invoices Should Be Removed         [Documentation]     Validating all invoices are removed are not 
        Validate Filled-In Specific Invoice Data        ${invoice_number}, ${expected_dueamount}, ${expected_amounttopay}.             
        Click On Clear All Button                       [Documentation]     Click on clear all button                       
        Click On Add Invoice                            [Documentation]     scroll down and click on add invoice button
        Enter Credit Card Values                         ${creditcard_details} 
        Create Multiple Invoices                        [Documentation]     is will creates multiple invoices
        Enter Customer Details Without State            [Documentation]     Enter customer details without state
        Validate Filled-In Specific Invoice Data After Removing Other Invoice   ${invoice_no_to_unselect}, ${expected_invoicenumber}, ${expected_dueamount}.
        Validate Invoice Details With Invalid Data      ${test_case_validation}, ${specific_invoice}. 
        Enter Account Number                            ${account_number}. 
        Add Invoice Details                             ${invoice_number}, ${due_amount}, ${amount_to_pay}. 
        Validate Customer Can Navigate Back From Payment Methods    ${payment_method}. 
        Validate Selected Invoice Should Be Removed                 ${invoice_number}. 
        Validate Dundermifflin Wikipedia Screen Is Visible          [Documentation].    Validate Dundermifflin Wikipedia Screen Is Visible
        """
    ]
})

pipeline.add_dataframe(validate_process_payment_with_visa_card)
pipeline.add_dataframe(non_integrated_open_invoices)

# combine dataframes
combined_df = pipeline.combine_dataframes()

json_filepath = '../json/jsondatakeyword_omniinvoice.json'
json_file = pipeline.to_json(combined_df, json_filepath)
csv_filepath = '../csv/data_keyword_omni_invoice.csv'
csv_file = pipeline.json_to_csv(json_filepath, csv_filepath)

print(f"JSON data saved to: {json_file}")
print(f"CSV data saved to: {csv_file}")