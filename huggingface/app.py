"""
Tasty Bytes Cortex Analyst - Demo Space
========================================
An interactive showcase of the Tasty Bytes Customer Analytics Cortex Analyst agent.

This Gradio app demonstrates:
- Natural language querying capabilities
- Example queries and results
- Architecture and setup instructions
- Live demo video

Note: This is a demo/showcase space. The actual Cortex Analyst runs on Snowflake infrastructure.
To try it yourself, follow the setup instructions in the GitHub repository.
"""

import gradio as gr
import pandas as pd

# Sample data for demonstration
sample_customer_counts = pd.DataFrame([
    {"Rank": 1, "Country": "United States", "Customers": 5420, "Total Sales": "$1,250,890.75"},
    {"Rank": 2, "Country": "India", "Customers": 3890, "Total Sales": "$980,230.50"},
    {"Rank": 3, "Country": "Egypt", "Customers": 2110, "Total Sales": "$520,450.00"},
])

sample_top_customers = pd.DataFrame([
    {"Customer ID": 110913, "Name": "Anna Sanchez", "City": "Boston", "Total Sales": "$3,302.00"},
    {"Customer ID": 130576, "Name": "Grace Kline", "City": "Mumbai", "Total Sales": "$2,809.50"},
    {"Customer ID": 90298, "Name": "Dahlia Buchanan", "City": "Cairo", "Total Sales": "$1,745.75"},
])

example_queries = [
    ("How many customers are in our loyalty program?", "SELECT COUNT(DISTINCT customer_id) FROM customer_loyalty_metrics_v", "11,420 customers"),
    ("Which countries have the most customers?", "SELECT country, COUNT(DISTINCT customer_id) FROM customer_loyalty_metrics_v GROUP BY country ORDER BY COUNT(DISTINCT customer_id) DESC", "See table below"),
    ("Show me the top 5 customers by total sales", "SELECT customer_id, first_name, last_name, city, total_sales FROM customer_loyalty_metrics_v ORDER BY total_sales DESC LIMIT 5", "See table below"),
    ("What's the total sales by country?", "SELECT country, SUM(total_sales) FROM customer_loyalty_metrics_v GROUP BY country ORDER BY SUM(total_sales)", "See results in table"),
]

def create_demo():
    with gr.Blocks(theme=gr.themes.Soft(), title="Tasty Bytes Cortex Analyst Demo") as demo:
        gr.Markdown("""
        # 🍔 Tasty Bytes Customer Analytics - Cortex Analyst Demo
        
        **Natural Language Interface for Customer Loyalty Data**
        
        This demo showcases a Snowflake Cortex Analyst agent built on the TASTY_BYTES public dataset.
        Ask questions in plain English and get instant insights - no SQL knowledge required!
        
        ⚠️ **Note**: This is a demonstration space. To try the actual agent, follow the setup instructions in the GitHub repository.
        """)
        
        # Main demo section
        with gr.Tab("🎥 Demo Video"):
            gr.Markdown("""
            ## Watch the Full Demo
            
            See Cortex Analyst in action: natural language queries, automatic SQL generation, and instant results.
            """)
            
            # Placeholder for video (you'll upload your actual demo video)
            gr.Markdown("""
            📹 **Demo video coming soon!**
            
            The video will demonstrate:
            - Asking questions in natural language
            - Automatic SQL generation by Cortex Analyst
            - Real-time results and insights
            - Various query types (counts, aggregations, rankings)
            
            **Until then, explore the other tabs to see example queries and results!**
            """)
            
        # Example queries tab
        with gr.Tab("💡 Example Queries"):
            gr.Markdown("""
            ## Try These Questions
            
            Here are some examples of natural language queries you can ask the Cortex Analyst agent:
            """)
            
            for i, (question, sql, result) in enumerate(example_queries, 1):
                with gr.Accordion(f"Example {i}: {question}", open=(i==1)):
                    gr.Markdown(f"**Natural Language Query:**")
                    gr.Code(question, language=None)
                    
                    gr.Markdown(f"**Generated SQL:**")
                    gr.Code(sql, language="sql")
                    
                    gr.Markdown(f"**Result:**")
                    gr.Markdown(f"`{result}`")
            
            gr.Markdown("""
            ### More Example Questions:
            
            **Customer Analytics:**
            - "How many customers do we have in total?"
            - "Show me all customers from Boston"
            - "Which customer has the highest total sales?"
            - "List customers who have visited more than 50 locations"
            
            **Geographic Analysis:**
            - "What cities have the most customers?"
            - "Compare customer counts across countries"
            - "Show me the geographic distribution of our customers"
            
            **Sales Insights:**
            - "What's the average sales per customer?"
            - "Which country generates the most revenue?"
            - "Show me total sales by city"
            - "Who are our top 10 customers by spend?"
            """)
            
        # Sample results tab
        with gr.Tab("📊 Sample Results"):
            gr.Markdown("""
            ## Example Query Results
            
            Here's what the actual results look like when you query the agent:
            """)
            
            gr.Markdown("### Query: 'Which countries have the highest number of customers?'")
            gr.Dataframe(sample_customer_counts, label="Customer Count by Country")
            
            gr.Markdown("---")
            
            gr.Markdown("### Query: 'Show me the top 3 customers by total sales'")
            gr.Dataframe(sample_top_customers, label="Top Customers")
            
            gr.Markdown("""
            ---
            💡 **Tip**: All numeric values are automatically rounded to 2 decimal places as specified 
            in the semantic view's custom instructions.
            """)
            
        # Architecture tab
        with gr.Tab("🏗️ Architecture"):
            gr.Markdown("""
            ## System Architecture
            
            The Cortex Analyst agent uses a layered architecture to transform natural language 
            into actionable insights:
            """)
            
            gr.Markdown("""
            ```
            ┌─────────────────────────────────────────┐
            │         Business User                    │
            │    (Natural Language Questions)          │
            └──────────────┬──────────────────────────┘
                           │
                           ▼
            ┌─────────────────────────────────────────┐
            │       Cortex Analyst (AI Layer)          │
            │  • Understands natural language          │
            │  • Maps questions to business concepts   │
            │  • Generates SQL queries                 │
            └──────────────┬──────────────────────────┘
                           │
                           ▼
            ┌─────────────────────────────────────────┐
            │   Semantic View (Business Logic)        │
            │  • Business-friendly names               │
            │  • Metrics & dimensions                  │
            │  • Pre-verified queries                  │
            │  • Custom instructions                   │
            └──────────────┬──────────────────────────┘
                           │
                           ▼
            ┌─────────────────────────────────────────┐
            │    TASTY_BYTES Dataset                   │
            │  • Customer loyalty data                 │
            │  • Order history                         │
            │  • Geographic information                │
            └─────────────────────────────────────────┘
            ```
            """)
            
            gr.Markdown("""
            ### Key Components:
            
            **1. Data Layer** - Snowflake TASTY_BYTES public dataset
            - Customer loyalty program data
            - Order transactions
            - Location and geographic information
            
            **2. Semantic Layer** - Native Snowflake Semantic View
            - Translates technical column names to business terms
            - Defines metrics (e.g., "total sales") and dimensions (e.g., "country")
            - Includes verified query examples
            - Enforces data access controls
            
            **3. AI Layer** - Cortex Analyst
            - Powered by LLM (Large Language Model)
            - Understands natural language intent
            - Automatically generates SQL queries
            - Returns results in business-friendly format
            
            **4. Interface** - Snowflake Intelligence & Cortex Analyst UI
            - Chat-based interaction
            - Visual result presentation
            - Query history and refinement
            """)
            
        # Setup guide tab
        with gr.Tab("🚀 Setup Guide"):
            gr.Markdown("""
            ## How to Set This Up Yourself
            
            Follow these steps to create your own Cortex Analyst agent with the TASTY_BYTES dataset:
            
            ### Prerequisites
            - Snowflake account (free trial available at [signup.snowflake.com](https://signup.snowflake.com))
            - ACCOUNTADMIN role or equivalent permissions
            - Cortex Analyst feature enabled (available in most regions)
            
            ### Step 1: Clone the Repository
            ```bash
            git clone https://github.com/yourusername/tasty-bytes-cortex-analyst.git
            cd tasty-bytes-cortex-analyst
            ```
            
            ### Step 2: Load the TASTY_BYTES Dataset
            ```sql
            -- Execute in Snowflake Snowsight or your SQL client
            -- This creates the database, schemas, and loads sample data
            @scripts/load_tasty_bytes_data.sql
            ```
            ⏱️ Takes approximately 5-10 minutes
            
            ### Step 3: Create the Semantic View
            ```sql
            -- Execute the semantic view creation script
            @scripts/create_semantic_view.sql
            ```
            ⏱️ Takes less than 1 minute
            
            ### Step 4: Create the Cortex Analyst Agent
            
            1. Navigate to **AI & ML** → **Cortex Analyst** in Snowsight
            2. Click **Create new agent**
            3. Configure:
               - **Name**: Tasty Bytes Customer Analytics
               - **Description**: Natural language interface for customer data
            4. Add Tool:
               - **Type**: Semantic View
               - **View**: `HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW`
               - **Description**: 
                 ```
                 Use this tool to answer questions about Tasty Bytes customer 
                 loyalty program metrics, including customer demographics, 
                 total sales, and location visit patterns.
                 ```
            5. Click **Create agent**
            
            ### Step 5: Test Your Agent
            
            Try asking:
            - "How many customers are in our loyalty program?"
            - "Which countries have the most customers?"
            - "Show me the top 10 customers by sales"
            
            ### 📚 Full Documentation
            
            For detailed instructions, troubleshooting, and advanced customization:
            - [GitHub Repository](https://github.com/yourusername/tasty-bytes-cortex-analyst)
            - [Snowflake Cortex Analyst Docs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst)
            - [Semantic Views Guide](https://docs.snowflake.com/en/user-guide/views-semantic/overview)
            """)
            
        # About tab
        with gr.Tab("ℹ️ About"):
            gr.Markdown("""
            ## About This Project
            
            This demo showcases **Snowflake Cortex Analyst**, an AI-powered natural language 
            interface for querying structured data. The project uses the publicly available 
            TASTY_BYTES sample dataset from Snowflake.
            
            ### Dataset
            **TASTY_BYTES** represents a fictional global food truck franchise with:
            - 11,420+ customer loyalty program members
            - Order transaction history
            - Multiple countries and cities
            - Customer demographics and preferences
            
            ### Features Demonstrated
            - ✅ Natural language to SQL translation
            - ✅ Automatic query generation
            - ✅ Business-friendly semantic layer
            - ✅ Pre-verified query examples
            - ✅ Custom SQL generation instructions
            
            ### Use Cases
            This pattern applies to many industries:
            - **Retail**: Customer segmentation, sales analysis
            - **Finance**: Client analytics, transaction patterns
            - **Healthcare**: Patient demographics, visit patterns
            - **SaaS**: User engagement, feature adoption
            - **E-commerce**: Customer lifetime value, purchase behavior
            
            ### Author
            **Aaman Lamba**
            - Strategy Consultant & Author
            - AI Governance & Data Economy Expert
            - Former Senior Industry Principal, Infosys
            - IAPP Certified AI Governance Professional (in progress)
            
            ### Resources
            - 📦 [GitHub Repository](https://github.com/yourusername/tasty-bytes-cortex-analyst)
            - 📖 [Snowflake Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst)
            - 💼 [LinkedIn](https://linkedin.com/in/aamanlamba)
            
            ### License
            MIT License - Open source and free to use
            
            ---
            
            ⭐ **Like this project?** Star it on [GitHub](https://github.com/yourusername/tasty-bytes-cortex-analyst)!
            
            🐛 **Found an issue?** [Report it here](https://github.com/yourusername/tasty-bytes-cortex-analyst/issues)
            """)
    
    return demo

# Launch the app
if __name__ == "__main__":
    demo = create_demo()
    demo.launch()
