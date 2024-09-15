import os
from neo4j import GraphDatabase
import pandas as pd

path = "combineddata.csv"
df = pd.read_csv(path, encoding='ISO-8859-1')  # Ignore invalid bytes


from dotenv import load_dotenv
load_dotenv('.env', override=True)
NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

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
            
            
#drop null rows
df["documentation"] = df["documentation"].replace({pd.NA:"Unknown"})
df["prompt"] = df["prompt"].replace({pd.NA:"Unknown"})
df["testcase_type"] = df["testcase_type"].replace({pd.NA:"Unknown"})
df["testcase_name"] = df["testcase_name"].replace({pd.NA:"Unknown"})
df["response"] = df["response"].replace({pd.NA:"Unknown"})

AUTH = (NEO4J_USERNAME, NEO4J_PASSWORD)
# Create a driver instance
driver = GraphDatabase.driver(NEO4J_URI, auth=AUTH)

# Process the DataFrame
process_dataframe(driver, df)

# Close the driver connection
driver.close()