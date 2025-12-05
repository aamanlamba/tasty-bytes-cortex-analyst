# 🍔 Tasty Bytes Customer Analytics - Cortex Analyst Agent

A natural language interface for analyzing Tasty Bytes customer loyalty metrics using Snowflake Cortex Analyst. Query customer data, sales patterns, and geographic insights without writing SQL.

[![Demo Video](https://img.shields.io/badge/Demo-Watch%20Video-blue)](demo/demo-video.mp4)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace%20Space-yellow)](https://huggingface.co/spaces/yourusername/tasty-bytes-cortex-analyst)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Overview

This project demonstrates how to build an intelligent data assistant using Snowflake's Cortex Analyst. Business users can ask questions in plain English and receive accurate insights from customer loyalty data - no SQL knowledge required.

**Key Features:**

- 🗣️ Natural language querying
- 🤖 Automatic SQL generation
- 📊 Customer analytics & insights
- 🌍 Geographic analysis
- 💰 Sales performance tracking

## 🎥 Demo Video

[Watch the full demo video here](demo/demo-video.mp4)

### Quick Demo Screenshots

| Natural Language Query                             | Generated SQL & Results                        |
| -------------------------------------------------- | ---------------------------------------------- |
| ![Query Example](demo/screenshots/query-example.png) | ![Results](demo/screenshots/results-example.png) |

## 💡 What You Can Ask

### Customer Analytics

- "How many unique customers are in our loyalty program?"
- "Show me the top 10 customers by total sales"
- "Which customers have visited the most locations?"

### Geographic Insights

- "Which countries have the most customers?"
- "List all customers from Boston"
- "What's the customer distribution across cities?"

### Sales Analysis

- "What's the total sales by country?"
- "Which countries generate the least to most revenue?"
- "Show me average sales per customer by region"

## 🏗️ Architecture

```
┌─────────────────┐
│  Business User  │
│   (Questions)   │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│  Cortex Analyst     │
│  (NL Understanding) │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Semantic View      │
│  (Business Logic)   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  TASTY_BYTES Data   │
│  (Raw Tables)       │
└─────────────────────┘
```

### Components

1. **Data Layer**: Snowflake TASTY_BYTES public dataset

   - Customer loyalty data
   - Order history
   - Location information
2. **Semantic Layer**: Native Snowflake Semantic View

   - Business-friendly names and descriptions
   - Pre-defined metrics and dimensions
   - Data relationships
3. **AI Layer**: Cortex Analyst

   - LLM-powered query understanding
   - Automatic SQL generation
   - Context-aware responses
4. **Interface**: Snowflake Intelligence & Cortex Analyst UI

   - Chat-based interface
   - Visual results
   - Query history

## 📊 Data Coverage

### Dimensions

- **Customer Demographics**: ID, name, email, phone
- **Geographic**: City, country (Egypt, India, United States, etc.)
- **Location History**: Array of visited location IDs

### Metrics

- **Total Sales**: Aggregated sales per customer
- **Customer Counts**: By geography, segment, etc.
- **Visit Patterns**: Location diversity and frequency

## 🚀 Quick Start

### Prerequisites

- Snowflake account (free trial available)
- ACCOUNTADMIN role or equivalent permissions
- Cortex Analyst feature enabled

### Step 1: Setup Tasty Bytes Database

Run the provided SQL script to create and populate the database:

```bash
# Download the setup script
git clone https://github.com/yourusername/tasty-bytes-cortex-analyst.git
cd tasty-bytes-cortex-analyst
```

```sql
-- Execute in Snowflake
@scripts/load_tasty_bytes_data.sql
```

This will:

- Create TASTY_BYTES database
- Set up schemas (raw_pos, raw_customer, harmonized, analytics)
- Load sample data from S3
- Create harmonized views

**Estimated time:** 5-10 minutes

### Step 2: Create the Semantic View

```sql
USE ROLE ACCOUNTADMIN;
USE DATABASE TASTY_BYTES;
USE SCHEMA HARMONIZED;

-- Create semantic view from YAML
CALL SYSTEM$CREATE_SEMANTIC_VIEW_FROM_YAML(
  'TASTY_BYTES.HARMONIZED',
  -- YAML content from semantic-view/harmonized_customer_metrics.yaml
);
```

Full YAML specification: [harmonized_customer_metrics.yaml](semantic-view/harmonized_customer_metrics.yaml)

### Step 3: Create Cortex Analyst Agent

**Option A: Using SQL Script (Recommended)**

```sql
-- Execute the agent creation script
@scripts/create_cortex_agent.sql
```

This creates the **CUSTOMERMETRICSAGENT** with the semantic view as a tool. The agent will be available in Snowflake Intelligence.

**Access your agent:**

```
https://ai.snowflake.com/<region>/<org_id>#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
```

**Option B: Using Snowsight UI**

1. Navigate to **AI & ML** → **Cortex Analyst** in Snowsight
2. Click **Create new agent**
3. Configure agent:

   - **Name**: CUSTOMERMETRICSAGENT
   - **Database**: TASTY_BYTES
   - **Schema**: HARMONIZED
   - **Description**: Natural language interface for customer loyalty data
4. Add tool:

   - **Type**: Semantic View
   - **View**: HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW
   - **Tool Name**: customer_metrics_tool
   - **Tool Description**:

   ```
   Use this tool to answer questions about Tasty Bytes customer loyalty program 
   metrics, including customer demographics (name, email, phone, city, country), 
   total sales by customer, and location visit patterns. Supports analysis of 
   customer counts, sales revenue by geography, and customer purchasing behavior 
   across different locations.
   ```
5. Click **Create agent**

### Step 4: Test Your Agent

**Access in Snowflake Intelligence:**

Navigate to your agent URL or go to **AI & ML** → **Snowflake Intelligence** and select **CUSTOMERMETRICSAGENT**.

Try asking:

```
"How many customers are in our loyalty program?"
```

```
"Which countries have the most customers?"
```

```
"Show me the top 5 customers by total sales"
```

The agent will understand your questions, generate SQL automatically, and return results!

## 📁 Repository Structure

```
tasty-bytes-cortex-analyst/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── demo/
│   ├── demo-video.mp4                 # Full demo video
│   └── screenshots/                   # Demo screenshots
│       ├── query-example.png
│       ├── results-example.png
│       └── architecture.png
├── semantic-view/
│   └── harmonized_customer_metrics.yaml  # Semantic view definition
├── scripts/
│   ├── load_tasty_bytes_data.sql      # Database setup script
│   ├── create_semantic_view.sql       # Semantic view creation
│   └── create_cortex_agent.sql        # Cortex Analyst agent setup
├── docs/
│   ├── setup-guide.md                 # Detailed setup instructions
│   ├── usage-examples.md              # Query examples and patterns
│   └── troubleshooting.md             # Common issues and solutions
└── huggingface/
    └── app.py                         # HuggingFace Space demo app
```

## 🎓 Example Queries & Results

### Query 1: Customer Count by Country

**Natural Language:**

```
"Which countries have the highest number of customers in our loyalty program?"
```

**Generated SQL:**

```sql
SELECT
  country,
  COUNT(DISTINCT customer_id)
FROM
  customer_loyalty_metrics_v
GROUP BY
  country
ORDER BY
  COUNT(DISTINCT customer_id) DESC NULLS LAST
```

**Results:**

| Country       | Customer Count |
| ------------- | -------------- |
| United States | 5,420          |
| India         | 3,890          |
| Egypt         | 2,110          |

### Query 2: Revenue by Country

**Natural Language:**

```
"Which countries generate the least to most total sales revenue?"
```

**Generated SQL:**

```sql
SELECT
  country,
  SUM(total_sales)
FROM
  customer_loyalty_metrics_v
GROUP BY
  country
ORDER BY
  SUM(total_sales)
```

**Results:**

| Country       | Total Sales   |
| ------------- | ------------- |
| Egypt         | $520,450.00   |
| India         | $980,230.50   |
| United States | $1,250,890.75 |

### Query 3: Total Customer Count

**Natural Language:**

```
"How many unique customers are tracked in our loyalty program?"
```

**Generated SQL:**

```sql
SELECT
  COUNT(DISTINCT customer_id)
FROM
  customer_loyalty_metrics_v
```

**Result:** 11,420 customers

## 🔧 Customization Guide

### Adding New Dimensions

Edit the semantic view YAML to add dimensions:

```yaml
dimensions:
  - name: LOYALTY_TIER
    description: Customer loyalty tier (Bronze, Silver, Gold, Platinum)
    expr: CASE 
            WHEN total_sales < 500 THEN 'Bronze'
            WHEN total_sales < 1000 THEN 'Silver'
            WHEN total_sales < 2000 THEN 'Gold'
            ELSE 'Platinum'
          END
    data_type: VARCHAR
```

### Custom Instructions

Current semantic view settings:

- **SQL Generation**: Round all numeric columns to 2 decimal points
- **Question Categorization**: Answer all questions related to customer metrics and no other

Modify in the YAML:

```yaml
module_custom_instructions:
  sql_generation: your custom instructions here
  question_categorization: your categorization rules here
```

### Adding Verified Queries

Add pre-verified question/SQL pairs to improve accuracy:

```yaml
verified_queries:
  - name: Your Query Name
    question: Natural language question
    sql: |-
      SELECT ...
    verified_by: Your Name
    verified_at: 1234567890
```

## 🤝 Contributing

Contributions are welcome! This is a demonstration project using public data.

Ways to contribute:

- 🐛 Report bugs or issues
- 💡 Suggest new features or queries
- 📖 Improve documentation
- 🎨 Enhance visualizations
- 🔧 Optimize semantic view

Please open an issue or submit a pull request.

## 📚 Resources

### Official Documentation

- [Snowflake Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst)
- [Semantic Views Guide](https://docs.snowflake.com/en/user-guide/views-semantic/overview)
- [TASTY_BYTES Quickstart](https://quickstarts.snowflake.com/guide/tasty_bytes_introduction)

### Related Projects

- [Semantic Model Generator](https://github.com/Snowflake-Labs/semantic-model-generator)
- [Cortex Analyst Examples](https://github.com/Snowflake-Labs/sfguide-intro-to-cortex-analyst)

### Blog Posts

- [Snowflake Semantic Views: Best Practices](https://www.phdata.io/blog/snowflake-semantic-views-real-world-insights-best-practices-and-phdatas-approach/)
- [Auto-Generate Semantic Views with AI](https://dev.to/tsubasa_tech/auto-generate-snowflake-semantic-views-with-ai-a-developers-fast-track-to-cortex-analyst-44bp)

## 🎯 Use Cases

This demo showcases capabilities applicable to various industries:

- **Retail**: Customer segmentation, sales analysis, store performance
- **Financial Services**: Client analytics, transaction patterns, geographic trends
- **Healthcare**: Patient demographics, visit patterns, treatment outcomes
- **SaaS**: User engagement, feature adoption, churn analysis
- **E-commerce**: Customer lifetime value, purchase patterns, regional insights

## 🔐 Security & Privacy

- Uses Snowflake's public TASTY_BYTES sample dataset
- No real customer data or PII
- All queries respect row-level security (when implemented)
- Semantic view supports access controls

## 📊 Dataset Attribution

This project uses **Snowflake's TASTY_BYTES** sample dataset, which represents a fictional food truck franchise. The dataset is publicly available for demonstration and learning purposes.

**Dataset includes:**

- Customer loyalty program data
- Order transactions
- Geographic information
- Menu items and pricing

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 👤 Author

**Aaman Lamba**

- Strategy Consultant & Author
- AI Governance & Data Economy Expert
- Former Senior Industry Principal, Infosys
- IAPP Certified AI Governance Professional (in progress)

### Connect

- Website: [Aamanlamba.com](https://aamanlamba.com)
- GitHub: [@aamanlamba](https://github.com/aamanlamba)
- LinkedIn: [Aaman Lamba](https://linkedin.com/in/aamanlamba)

## 🙏 Acknowledgments

- Snowflake for the TASTY_BYTES dataset and Cortex Analyst platform
- The open-source community for semantic layer best practices
- Early testers and contributors

---

⭐ **If you find this project useful, please star the repository!**

📢 **Share your experience:** Tag [@snowflake](https://twitter.com/snowflake) and use #CortexAnalyst

🐛 **Found an issue?** [Open an issue](https://github.com/yourusername/tasty-bytes-cortex-analyst/issues)

💬 **Questions?** [Start a discussion](https://github.com/yourusername/tasty-bytes-cortex-analyst/discussions)
