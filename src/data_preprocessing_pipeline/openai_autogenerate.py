import openai
import pandas as pd
from tqdm import tqdm
import time

import os
from google.colab import userdata

# Verify and set the API key
openai_api_key = userdata.get('OPENAI_API_KEY')
if openai_api_key is None or openai_api_key.strip() == "":
    raise ValueError("OpenAI API key is not set. Please set it in Colab secrets.")

openai.api_key = openai_api_key
print("OpenAI API key set successfully.")

# Load existing data
keyword_driven_df = pd.read_csv('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/newKeyword_driven_testcases.csv')
data_driven_df = pd.read_csv('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/newData_driven_testcases.csv')

def get_examples(df, n=3):
    return df.sample(n).to_dict('records')

def create_prompt(examples, test_type):
    prompt = f"Generate a new {test_type} test case following EXACTLY the structure and style of these examples:\n\n"
    for i, example in enumerate(examples, 1):
        prompt += f"Example {i}:\n"
        for key, value in example.items():
            prompt += f"{key}: {value}\n"
        prompt += "\n"
    prompt += f"Now, create a new {test_type} test case following this EXACT structure and style. Ensure all fields are filled correctly and the content is relevant to {test_type} testing."
    return prompt

def generate_test_case(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a test case generator that precisely follows given examples and instructions."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating test case: {e}")
        return None

def parse_generated_case(content):
    lines = content.split('\n')
    parsed_case = {}
    current_key = None
    for line in lines:
        if ': ' in line:
            key, value = line.split(': ', 1)
            current_key = key.strip()
            parsed_case[current_key] = value.strip()
        elif current_key:
            parsed_case[current_key] += '\n' + line.strip()
    return parsed_case

def generate_new_test_cases(df, test_type, count):
    new_test_cases = []
    for _ in tqdm(range(count)):
        examples = get_examples(df)
        prompt = create_prompt(examples, test_type)
        generated_content = generate_test_case(prompt)
        if generated_content:
            parsed_case = parse_generated_case(generated_content)
            new_test_cases.append(parsed_case)
        time.sleep(1)  # To avoid rate limiting
    return new_test_cases

# Generate new test cases
new_keyword_cases = generate_new_test_cases(keyword_driven_df, 'keyword-driven', 350)
new_data_cases = generate_new_test_cases(data_driven_df, 'data-driven', 350)

# Convert to DataFrames
new_keyword_df = pd.DataFrame(new_keyword_cases)
new_data_df = pd.DataFrame(new_data_cases)

new_keyword_df.head()

new_data_df.head()

# # Save the combined datasets
# new_keyword_df.to_excel('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/test_keyword_generated.xlsx', index=False)
# new_data_df.to_csv('/content/drive/MyDrive/WORKS/SOFTWARE-DRIVEN-TEST AUTOMATION/dataset & info/test_data_generated.xlsx', index=False)

# # Combine with existing data
# combined_keyword_df = pd.concat([keyword_driven_df, new_keyword_df], ignore_index=True)
# combined_data_df = pd.concat([data_driven_df, new_data_df], ignore_index=True)

# # Save the combined datasets
# combined_keyword_df.to_csv('combined_keyword_driven.csv', index=False)
# combined_data_df.to_csv('combined_data_driven.csv', index=False)