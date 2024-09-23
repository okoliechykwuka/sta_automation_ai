# baseline_data.py
import os
import streamlit as st
import pandas as pd
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = st.secrets.get('NEO4J_URI')
NEO4J_USER = st.secrets.get('NEO4J_USER')
NEO4J_PASSWORD = st.secrets.get('NEO4J_PASSWORD')

st.write(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

def insert_data(tx, row):
    tx.run('''
    MERGE (tc:TestCase {
        prompt: $prompt,
        testcase_name: $testcase_name,
        response: $response,
        documentation: $documentation
    })

    MERGE (tt:TestcaseType {name: $testcase_type})
    MERGE (tc)-[:HAS_TYPE]->(tt)

    WITH tc, $response AS resp

    FOREACH (lib IN [lib IN split(resp, '\n') WHERE lib CONTAINS 'Library' | trim(split(lib, ' ')[1])] |
        MERGE (l:Library {name: lib})
        MERGE (tc)-[:USES_LIBRARY]->(l)
    )

    FOREACH (varLine IN [line IN split(resp, '\n') WHERE line CONTAINS '${' | 
        trim(split(line, '}')[0] + '}')
    ] |
        MERGE (v:Variable {name: varLine})
        MERGE (tc)-[:USES_VARIABLE]->(v)
    )

    FOREACH (validatedCase IN [line IN split(resp, '\n') WHERE toLower(line) CONTAINS 'validate' | 
        trim(split(line, ' ')[1])
    ] |
        MERGE (vtc:ValidatedCase {name: validatedCase})
        MERGE (tc)-[:VALIDATES]->(vtc)
    )
    ''', row)

def process_dataframe(driver, df):
    with driver.session() as session:
        for index, row in df.iterrows():
            session.execute_write(insert_data, row.to_dict())
            print(f"Processed row {index}")

def load_baseline_data(file_path):
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df = df.fillna("Unknown")
    
    AUTH = (NEO4J_USER, NEO4J_PASSWORD)
    driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH)
    
    process_dataframe(driver, df)
    
    driver.close()
    print("Baseline data loaded successfully.")

# if __name__ == "__main__":
#     baseline_file_path = "combineddata.csv"  # Update this path as needed
#     load_baseline_data(baseline_file_path)
