# Detailed Setup Guide

This guide walks you through setting up the Tasty Bytes Cortex Analyst agent step by step.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Step 1: Get a Snowflake Account](#step-1-get-a-snowflake-account)
3. [Step 2: Load the TASTY_BYTES Dataset](#step-2-load-the-tasty_bytes-dataset)
4. [Step 3: Create the Semantic View](#step-3-create-the-semantic-view)
5. [Step 4: Create the Cortex Analyst Agent](#step-4-create-the-cortex-analyst-agent)
6. [Step 5: Test Your Agent](#step-5-test-your-agent)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required
- **Snowflake Account**: Free trial available (no credit card required for 30 days)
- **Role**: ACCOUNTADMIN or a role with:
  - CREATE DATABASE privilege
  - CREATE SEMANTIC VIEW privilege
  - USAGE on Cortex services
- **Cortex Analyst Enabled**: Available in most AWS and Azure regions

### Optional
- Git for cloning the repository
- SQL client (Snowflake Snowsight is included)

---

## Step 1: Get a Snowflake Account

### Option A: Free Trial (Recommended)

1. Go to [signup.snowflake.com](https://signup.snowflake.com)
2. Fill out the registration form
3. Choose your cloud provider (AWS or Azure)
4. Select a region close to you
5. Verify your email address
6. Complete the setup wizard

**Time required:** 5-10 minutes

### Option B: Use Existing Account

If you already have a Snowflake account:
1. Ensure Cortex Analyst is available in your region
2. Verify you have ACCOUNTADMIN access
3. Check that you have sufficient compute credits

---

## Step 2: Load the TASTY_BYTES Dataset

### Method 1: Using Snowsight (GUI)

1. **Log in to Snowflake**
   - Navigate to your Snowflake account URL
   - Sign in with your credentials

2. **Open Snowsight**
   - Click on "Snowsight" in the navigation menu
   - Or navigate directly to `https://<account>.snowflakecomputing.com/`

3. **Create a New Worksheet**
   - Click on "+ Worksheet" or "Projects" → "+ SQL Worksheet"
   - Name it "Tasty Bytes Setup"

4. **Execute the Setup Script**
   - Copy the contents of `scripts/load_tasty_bytes_data.sql`
   - Paste into the worksheet
   - Click "Run All" or press `Ctrl+Enter` (Windows) / `Cmd+Return` (Mac)

5. **Monitor Progress**
   - Watch the results panel for completion messages
   - All tables should be created and loaded successfully

**Expected output:**
```
Database TASTY_BYTES created.
Schema RAW_POS created.
Schema RAW_CUSTOMER created.
Schema HARMONIZED created.
Schema ANALYTICS created.
...
[Tables loaded successfully]
```

**Time required:** 5-10 minutes

### Method 2: Using Command Line (SnowSQL)

1. **Install SnowSQL** (if not already installed)
   ```bash
   # Mac/Linux
   curl -O https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/latest/snowsql-latest-darwin_x86_64.pkg
   
   # Windows
   # Download from https://developers.snowflake.com/snowsql/
   ```

2. **Connect to Snowflake**
   ```bash
   snowsql -a <account> -u <username>
   ```

3. **Execute the Setup Script**
   ```bash
   snowsql -a <account> -u <username> -f scripts/load_tasty_bytes_data.sql
   ```

**Time required:** 5-10 minutes

### Verification

Verify the data was loaded correctly:

```sql
-- Check database and schemas
SHOW DATABASES LIKE 'TASTY_BYTES';
SHOW SCHEMAS IN DATABASE TASTY_BYTES;

-- Check table row counts
SELECT 'customer_loyalty' as table_name, COUNT(*) as row_count 
FROM tasty_bytes.raw_customer.customer_loyalty
UNION ALL
SELECT 'order_header', COUNT(*) 
FROM tasty_bytes.raw_pos.order_header
UNION ALL
SELECT 'order_detail', COUNT(*) 
FROM tasty_bytes.raw_pos.order_detail;

-- Check the harmonized view
SELECT * FROM tasty_bytes.harmonized.customer_loyalty_metrics_v LIMIT 10;
```

**Expected results:**
- customer_loyalty: ~11,000+ rows
- order_header: ~100,000+ rows
- order_detail: ~300,000+ rows

---

## Step 3: Create the Semantic View

### Method 1: Using the SQL Script

1. **Open a New Worksheet in Snowsight**

2. **Execute the Semantic View Script**
   - Copy contents of `scripts/create_semantic_view.sql`
   - Paste into worksheet
   - Click "Run All"

3. **Verify Creation**
   ```sql
   SHOW SEMANTIC VIEWS IN SCHEMA TASTY_BYTES.HARMONIZED;
   ```

You should see `HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW` in the results.

**Time required:** 1-2 minutes

### Method 2: Manual Creation

If you prefer to understand each component:

1. **Review the YAML Specification**
   - Open `semantic-view/harmonized_customer_metrics.yaml`
   - Note the dimensions, facts, and verified queries

2. **Create Using Stored Procedure**
   ```sql
   USE ROLE ACCOUNTADMIN;
   USE DATABASE TASTY_BYTES;
   USE SCHEMA HARMONIZED;
   
   CALL SYSTEM$CREATE_SEMANTIC_VIEW_FROM_YAML(
     'TASTY_BYTES.HARMONIZED',
     -- Paste YAML content here between $$
   );
   ```

### Understanding the Semantic View

The semantic view defines:

**Dimensions** (attributes for filtering):
- CUSTOMER_ID: Unique customer identifier
- FIRST_NAME, LAST_NAME: Customer names
- E_MAIL, PHONE_NUMBER: Contact information
- CITY, COUNTRY: Geographic location
- VISITED_LOCATION_IDS_ARRAY: Location history

**Facts/Metrics** (measurable values):
- TOTAL_SALES: Aggregate sales per customer

**Verified Queries** (pre-tested examples):
1. Customer count in loyalty program
2. Revenue by country (ascending)
3. Customer count by country (descending)

**Custom Instructions**:
- Round numeric values to 2 decimal places
- Only answer customer metrics questions

---

## Step 4: Create the Cortex Analyst Agent

### Step-by-Step Instructions

**Method 1: Using SQL Script (Recommended)**

1. **Execute the Agent Creation Script**
   ```sql
   -- In Snowflake Snowsight
   @scripts/create_cortex_agent.sql
   ```

2. **Verify Agent Creation**
   ```sql
   SHOW CORTEX ANALYST AGENTS IN SCHEMA TASTY_BYTES.HARMONIZED;
   ```
   
   You should see **CUSTOMERMETRICSAGENT** in the results.

3. **Get Agent Details**
   ```sql
   DESCRIBE CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT;
   ```

**Time required:** 1-2 minutes

**Method 2: Using Snowsight UI**

1. **Navigate to Cortex Analyst**
   - In Snowsight, click on "AI & ML" in the left navigation
   - Select "Cortex Analyst"
   - You'll see the Cortex Analyst dashboard

2. **Create New Agent**
   - Click "Create new" button (top right)
   - Select "Create new agent"

3. **Configure Basic Settings**
   - **Agent Name**: `CUSTOMERMETRICSAGENT`
   - **Database**: `TASTY_BYTES`
   - **Schema**: `HARMONIZED`
   - **Description**: `Natural language interface for analyzing Tasty Bytes customer loyalty data`
   - Click "Next"

4. **Add Tools**
   - Click "+ Add Tool"
   - **Tool Type**: Select "Semantic View"
   - **Select Semantic View**: Choose `HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW`
   - **Tool Name**: `customer_metrics_tool`
   - **Tool Description**: 
     ```
     Use this tool to answer questions about Tasty Bytes customer loyalty 
     program metrics, including customer demographics (name, email, phone, 
     city, country), total sales by customer, and location visit patterns. 
     Supports analysis of customer counts, sales revenue by geography, and 
     customer purchasing behavior across different locations.
     ```
   - Click "Add Tool"

5. **Review and Create**
   - Review your agent configuration
   - Click "Create agent"

**Time required:** 2-3 minutes

### Agent URL

Your agent will be available at:
```
https://ai.snowflake.com/<region>/<org_id>#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
```

Replace `<region>` and `<org_id>` with your Snowflake account details.

Example:
```
https://ai.snowflake.com/us-east-1/ogc69807#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
```

### Alternative: Using Snowflake Intelligence

You can also access the agent directly in Snowflake Intelligence:

1. Navigate to "AI & ML" → "Snowflake Intelligence"
2. In the agent dropdown, select **CUSTOMERMETRICSAGENT**
3. The semantic view will be automatically available
4. Start asking questions directly

**Direct URL:** Use the agent URL from above for quick access.

---

## Step 5: Test Your Agent

### Basic Test Queries

Start with these simple queries to verify everything works:

#### Test 1: Customer Count
```
Question: "How many customers are in our loyalty program?"
Expected: A single number (around 11,000+)
```

#### Test 2: Geographic Distribution
```
Question: "Which countries have the most customers?"
Expected: A ranked list with United States, India, Egypt at the top
```

#### Test 3: Sales Analysis
```
Question: "What's the total sales by country?"
Expected: Aggregated sales figures by country
```

#### Test 4: Top Customers
```
Question: "Show me the top 10 customers by total sales"
Expected: A table with customer details and sales amounts
```

### Advanced Test Queries

Once basic queries work, try more complex ones:

```
"What's the average sales per customer in each country?"
"Which cities have more than 100 customers?"
"Show me customers from Boston who have spent over $1000"
"Compare customer counts between United States and India"
```

### Verifying SQL Generation

For each query:
1. Check the generated SQL in the response
2. Verify it matches expected patterns
3. Ensure results are accurate
4. Note any issues or unexpected behavior

### Testing in Different Interfaces

**Option A: Cortex Analyst UI**
- Direct chat interface
- Best for testing specific queries
- Shows SQL generation clearly

**Option B: Snowflake Intelligence**
- More conversational interface
- Better for exploratory analysis
- Integrates with other Snowflake features

---

## Troubleshooting

### Issue 1: Semantic View Not Visible

**Symptom:** Can't find the semantic view when adding tools to agent

**Solutions:**
1. Verify the view was created:
   ```sql
   SHOW SEMANTIC VIEWS IN SCHEMA TASTY_BYTES.HARMONIZED;
   ```

2. Check permissions:
   ```sql
   SHOW GRANTS ON SEMANTIC VIEW TASTY_BYTES.HARMONIZED.HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW;
   ```

3. Grant access if needed:
   ```sql
   GRANT USAGE ON SEMANTIC VIEW TASTY_BYTES.HARMONIZED.HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW 
     TO ROLE YOUR_ROLE;
   ```

### Issue 2: "Cortex Analyst Not Available"

**Symptom:** Feature not visible in Snowsight

**Solutions:**
1. Check your region supports Cortex Analyst
   - Most AWS regions: ✅
   - Most Azure regions: ✅
   - Some regions may be in preview

2. Verify account settings:
   - Contact Snowflake support to enable
   - Check if in preview and request access

### Issue 3: Data Load Failures

**Symptom:** Error messages during `load_tasty_bytes_data.sql` execution

**Solutions:**
1. Check warehouse is running:
   ```sql
   SHOW WAREHOUSES;
   ALTER WAREHOUSE demo_build_wh RESUME IF SUSPENDED;
   ```

2. Verify S3 access:
   ```sql
   LIST @tasty_bytes.public.s3load;
   ```

3. Check for network issues or quotas

### Issue 4: Agent Not Understanding Questions

**Symptom:** Agent returns "I don't know" or incorrect results

**Solutions:**
1. Start with verified queries (from YAML)
2. Be more specific in your questions
3. Use business terms defined in semantic view
4. Check if question is within scope (customer metrics only)

### Issue 5: Incorrect SQL Generation

**Symptom:** Generated SQL doesn't match expected logic

**Solutions:**
1. Review semantic view definition
2. Check custom instructions
3. Add more verified queries as examples
4. Refine dimension and fact descriptions

### Getting Help

If issues persist:

1. **GitHub Issues**
   - [Open an issue](https://github.com/yourusername/tasty-bytes-cortex-analyst/issues)
   - Include error messages and steps to reproduce

2. **Snowflake Support**
   - Access through your Snowflake account
   - Reference Cortex Analyst documentation

3. **Community**
   - [Snowflake Community Forums](https://community.snowflake.com/)
   - Tag questions with `cortex-analyst` and `semantic-views`

---

## Next Steps

Once your agent is working:

1. **Customize the Semantic View**
   - Add more dimensions
   - Create derived metrics
   - Add more verified queries

2. **Expand to Other Datasets**
   - Apply the same pattern to your own data
   - Create multiple semantic views
   - Build specialized agents

3. **Share Your Success**
   - Star the GitHub repository
   - Share on LinkedIn with #CortexAnalyst
   - Contribute improvements back

---

**Estimated Total Time:** 20-30 minutes for complete setup

**Questions?** Check the [main README](../README.md) or open an issue on GitHub.
