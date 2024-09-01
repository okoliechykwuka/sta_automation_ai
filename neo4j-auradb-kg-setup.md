# Setting Up Neo4j AuraDB, Uploading Data, and Inspecting Data Relationships

This documentation provides a step-by-step guide to setting up a Neo4j AuraDB instance, uploading data into the database, and checking data relationships, nodes, and properties. This is essential for integrating a knowledge graph into the STA Automation Chatbot applicatio

## Prerequisites?

**NONE!**

## 1. Setting Up a Neo4j AuraDB Instance

1. **Step 1: Sign Up or Log In to Neo4j AuraDB**

    Visit the Neo4j AuraDB website "<https://neo4j.com/product/auradb/>", and sign up for an account if you don't have one. If you already have an account, log in.

2. **Step 2: Create a New Database**

    * Once logged in, navigate to the Neo4j AuraDB dashboard.
    * Click on the "`Create a Database`" button.
    * Choose a name for your database, select the region closest to you, and choose the "Aura Free" plan if you're using the free tier.
    * Click "`Create`" to start the database creation process. This may take a few minutes.

3. **Step 3: Access the Database**

    * Once the database is ready, you'll be provided with connection details, including a Bolt URL, username, and password.
    * Keep these details secure as they will be needed to connect to the database from your application or tools like Neo4j Browser or Neo4j Desktop.

## 2. Uploading Data to Neo4j AuraDB

1. **Step 1: Prepare Your Streamlit Application for Data Upload**

    Ensure your Streamlit application is configured to allow users to upload test case data. Typically, this data will be in CSV or JSON format.

2. **Step 2: Connect to Your Database**

    * Use the neo4j Python driver to connect your Streamlit application to Neo4j AuraDB. You will use the Bolt URL, username, and password obtained during the database setup.

3. **Step 3: Upload Data via the Streamlit Interface**

    * Within your Streamlit app, implement functionality to handle file uploads and process the uploaded data into nodes and relationships for Neo4j.

## 3. Checking Data Relationships, Nodes, and Properties

After uploading data, you can query Neo4j Auradb directly using cypher queries

e.g

```cypher
    MATCH (t:TestCase)-[r:TESTS]->(f:Feature)
    RETURN t, r, f
```

