import random
import openai
import anthropic
import pandas as pd
import os
import glob
import re
import time
from google.colab import userdata

# Verify and set the API key
openai_api_key = userdata.get('OPENAI_API_KEY')
if openai_api_key is None or openai_api_key.strip() == "":
    raise ValueError("OpenAI API key is not set. Please set it in Colab secrets.")

openai.api_key = openai_api_key
print("OpenAI API key set successfully.")

def generate_documentation_and_prompt(test_case_name, test_case_type, file_path):
    # Extract application and directory context from the file path
    parts = file_path.split('/')
    application_name = parts[-3]  # Adjust the index based on your specific path structure
    directory_name = parts[-2]

    # Define actions and types for variability in the prompt
    actions = ['Generate', 'Create', 'Build', 'Validate']
    types = ['keyword-driven', 'data-driven']

    # Select a random action
    action = random.choice(actions)
    type_phrase = 'keyword-driven' if 'Keyword' in directory_name else 'data-driven'

    # Construct the full prompt using the extracted context
    prompt = f"{action} {type_phrase} {application_name.lower()} for {directory_name.replace('_', ' ')} {test_case_name}"

    # Generate documentation
    documentation_template = f"Provide a summary for the test case '{test_case_name}' explaining its purpose"
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": documentation_template}],
            max_tokens=150
        )
        documentation = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating documentation for {test_case_name}: {str(e)}")
        documentation = f"Documentation for {test_case_name} could not be generated due to an error."

    return prompt, documentation

def infer_return_type(keyword_name, args):
    keyword_name = keyword_name.lower()
    args = str(args).lower()

    if keyword_name.startswith("validate") or "is displayed" in keyword_name:
        return "${boolean}"

    if any(word in keyword_name for word in ["count", "number", "total", "sum", "calculate"]):
        if "float" in args or "." in args:
            return "${float}"
        else:
            return "${integer}"

    if any(word in keyword_name for word in ["list", "array", "multiple", "all"]):
        return "@{list}"

    if any(word in keyword_name for word in ["dict", "map", "hash", "object"]):
        return "&{dictionary}"

    return "${string}"

def process_keyword_driven_test_case(file_path):
    test_case_name = os.path.splitext(os.path.basename(file_path))[0]
    test_case_data = pd.read_csv(file_path)

    keywords = test_case_data['KeywordName'].tolist()
    if 'Arguments' in test_case_data.columns:
        args_list = test_case_data['Arguments'].tolist()
    else:
        args_list = test_case_data[['Argument1', 'Argument2', 'Argument3']].fillna('').apply(
            lambda row: '    '.join(filter(None, row)), axis=1).tolist()

    # prompt, documentation = generate_documentation_and_prompt(test_case_name)
    # Get dynamic prompt and documentation based on file path
    prompt, documentation = generate_documentation_and_prompt(test_case_name, 'keyword-driven', file_path)

    settings = (
        "*** Settings ***\n"
        f"Documentation    Validate {test_case_name}\n"
        "Test Setup       Initialize Environment\n"
        "Test Teardown    Cleanup Environment\n"
        "Suite Setup      Open Application\n"
        "Suite Teardown   Close Application\n"
        "Resource         resource_file.robot\n\n"
    )
    variables = (
        "*** Variables ***\n"
        "${VALID_USER}       testuser\n"
        "${VALID_PASSWORD}   secret\n\n"
    )
    test_cases = f"*** Test Cases ***\n{test_case_name}\n    [Documentation]    Validate {test_case_name} using the following steps\n"
    test_cases += '    \n    '.join(f"{kw}    {args}" for kw, args in zip(keywords, args_list)) + "\n\n"

    keywords_section = "*** Keywords ***\n"
    for keyword, args in zip(keywords, args_list):
        return_type = infer_return_type(keyword, args)
        keywords_section += (
            f"{keyword}\n"
            f"    [Arguments]    {args}\n"
            f"    [Return]    {return_type}\n"
            "    [Documentation]    Keyword description\n"
            f"    Log    {args}\n\n"
        )

    refined_response = settings + variables + test_cases + keywords_section

    return [{"prompt": prompt, "testcase_type": "keyword-driven", "testcase_name": test_case_name, "response": refined_response, "documentation": documentation}]

def process_data_driven_test_case(file_path):
    test_case_name = os.path.splitext(os.path.basename(file_path))[0]
    test_case_data = pd.read_csv(file_path)

    args1 = test_case_data['Argument1'].tolist() if 'Argument1' in test_case_data.columns else [''] * len(test_case_data)
    args2 = test_case_data['Argument2'].tolist() if 'Argument2' in test_case_data.columns else [''] * len(test_case_data)
    args3 = test_case_data['Argument3'].tolist() if 'Argument3' in test_case_data.columns else [''] * len(test_case_data)

    keywords = test_case_data['KeywordName'].tolist()

    all_arguments = [
        '    '.join(filter(None, [f"${{{arg}}}" for arg in [a1, a2, a3]]))
        for a1, a2, a3 in zip(args1, args2, args3)
    ]

    prompt, documentation = generate_documentation_and_prompt(test_case_name, 'data-driven', file_path)
    # prompt, documentation = generate_documentation_and_prompt(test_case_name)

    settings = (
        "*** Settings ***\n"
        f"Documentation    Validate {test_case_name}\n"
        "Test Template    Test Execution\n"
        "Resource         resource_file.robot\n\n"
    )
    variables = (
        "*** Variables ***\n"
        "${VALID_USER}       testuser\n"
        "${VALID_PASSWORD}   secret\n\n"
    )
    test_cases = f"*** Test Cases ***\n{test_case_name}\n    [Documentation]    Validate {test_case_name} using the following steps\n"
    test_cases += '    \n    '.join(f"{keywords[i]}    {all_arguments[i]}" for i in range(len(keywords))) + "\n\n"

    keywords_section = "*** Keywords ***\n"
    for i, keyword in enumerate(keywords):
        return_type = infer_return_type(keyword, all_arguments[i])
        keywords_section += (
            f"{keyword}\n"
            f"    [Arguments]    {all_arguments[i]}\n"
            f"    [Return]    {return_type}\n"
            "    [Documentation]    Keyword description\n"
            f"    Log    {all_arguments[i]}\n\n"
        )

    refined_response = settings + variables + test_cases + keywords_section

    return [{"prompt": prompt, "testcase_type": "data-driven", "testcase_name": test_case_name, "response": refined_response, "documentation": documentation}]

def find_csv_files(root_directories):
    csv_files = []
    for root_directory in root_directories:
        for subdir, dirs, files in os.walk(root_directory):
            for file in glob.glob(os.path.join(subdir, '*.csv')):
                csv_files.append(file)
    return csv_files

def process_files(file_paths, process_function):
    results = []
    start_time = time.time()
    for file_path in file_paths:
        try:
            result = process_function(file_path)
            results.extend(result)  # Flatten the list of results
        except Exception as e:
            print(f"Failed to process {file_path}: {str(e)}")
    end_time = time.time()
    print(f"Processed {len(file_paths)} files in {end_time - start_time:.2f} seconds")
    return results

# Root directories for keyword-driven and data-driven test cases
roots_keyword_driven = [
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/API',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/CommonKeywordsForAllMerchants',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/Omnicorp/Customers',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/SterlingCooper/Customers',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/SterlingCooper/Dashboard',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/SterlingCooper/Invoices',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/SterlingCooper/Settings',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/SterlingCooper/Transactions',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Keywords Ram/ClientCentral_Keywords/Web/SterlingCooper/Virtual_Terminal',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW_Keywords Ramashanker/PayNOW_Keywords/API',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW_Keywords Ramashanker/PayNOW_Keywords/Web',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW_Keywords Ramashanker/PayNOW_Keywords/Web/PayNOW',
]

roots_data_driven = [
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW Test Cases Ramashanker/PayNOW Test Cases/Autopay Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW Test Cases Ramashanker/PayNOW Test Cases/Omnicorp Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW Test Cases Ramashanker/PayNOW Test Cases/SchedulePayment Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW Test Cases Ramashanker/PayNOW Test Cases/Sterlingcooper Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW Test Cases Ramashanker/PayNOW Test Cases/non integrated Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/PayNOW Datadriver Testcases Ramashanker',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/all_transactions_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/autopay_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/customers_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/dashboard_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/failed_login_attempts_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/invoices_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/payment_status_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/scheduled_payments_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/settings_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/tokens_Testcases',
    '/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/SDT UAR Test Cases/ClientCentral_Testcases Ram/ClientCentral_Testcases/virtual_terminal_Testcases'
]

# Collect all relevant CSV files
keyword_driven_files = find_csv_files(roots_keyword_driven)
data_driven_files = find_csv_files(roots_data_driven)

print(f"Found {len(keyword_driven_files)} keyword-driven test cases")
print(f"Found {len(data_driven_files)} data-driven test cases")

# Process keyword-driven and data-driven test cases
refined_KD_data_openai = process_files(keyword_driven_files, process_keyword_driven_test_case)
refined_DD_data_openai = process_files(data_driven_files, process_data_driven_test_case)

# Convert to DataFrame and Save refined data to CSV
keydriven_df = pd.DataFrame(refined_KD_data_openai)
ddriven_df = pd.DataFrame(refined_DD_data_openai)
keydriven_df.to_csv('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/newKeyword_driven_testcases.csv', index=False)
ddriven_df.to_csv('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/newData_driven_testcases.csv', index=False)

# print("Keyword-driven test cases saved to keydriven_df.csv")
# print("Data-driven test cases saved to ddriven_df.csv")

keydriven_df.shape

ddriven_df.shape

keydriven_df.head()

ddriven_df.head()

keydriven_df.to_excel('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/newKeyword_driven_testcases.xlsx', index=False)
ddriven_df.to_excel('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/newData_driven_testcases.xlsx', index=False)

print("done!!!")

