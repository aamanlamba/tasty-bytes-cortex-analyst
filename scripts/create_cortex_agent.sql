-- ============================================================================
-- Tasty Bytes - Cortex Analyst Agent Creation
-- ============================================================================
-- This script creates a Cortex Analyst agent with the semantic view as a tool.
-- The agent will be available in Snowflake Intelligence for natural language
-- queries about customer loyalty metrics.
--
-- Prerequisites:
-- 1. Semantic view HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW must be created
--    (Run create_semantic_view.sql first)
-- 2. ACCOUNTADMIN role or equivalent permissions
-- 3. Cortex Analyst feature enabled in your Snowflake account
-- ============================================================================

USE ROLE ACCOUNTADMIN;
USE DATABASE TASTY_BYTES;
USE SCHEMA HARMONIZED;

-- ============================================================================
-- Step 1: Verify the semantic view exists
-- ============================================================================

SHOW SEMANTIC VIEWS IN SCHEMA TASTY_BYTES.HARMONIZED;

-- You should see HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW in the results
-- If not, run create_semantic_view.sql first

-- ============================================================================
-- Step 2: Create the Cortex Analyst Agent
-- ============================================================================

-- Create the agent with the semantic view as a tool
CREATE OR REPLACE CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT
  COMMENT = 'Natural language interface for Tasty Bytes customer loyalty analytics. Ask questions about customer demographics, sales, and geographic distribution without writing SQL.'
  AS
    SYSTEM$ADD_SEMANTIC_VIEW_TOOL(
      'TASTY_BYTES.HARMONIZED.HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW',
      '{
        "name": "customer_metrics_tool",
        "description": "Use this tool to answer questions about Tasty Bytes customer loyalty program metrics, including customer demographics (name, email, phone, city, country), total sales by customer, and location visit patterns. Supports analysis of customer counts, sales revenue by geography, and customer purchasing behavior across different locations.",
        "parameters": {}
      }'
    );

-- ============================================================================
-- Step 3: Verify the agent was created successfully
-- ============================================================================

SHOW CORTEX ANALYST AGENTS IN SCHEMA TASTY_BYTES.HARMONIZED;

-- You should see CUSTOMERMETRICSAGENT in the results

-- ============================================================================
-- Step 4: Get agent details and configuration
-- ============================================================================

DESCRIBE CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT;

-- ============================================================================
-- Step 5: Grant access to other roles (optional)
-- ============================================================================

-- Grant usage to specific roles if needed
-- Example: Grant to a business analyst role
-- GRANT USAGE ON CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT 
--   TO ROLE BUSINESS_ANALYST_ROLE;

-- Grant to all roles that should have access
-- GRANT USAGE ON CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT 
--   TO ROLE PUBLIC;

-- ============================================================================
-- Step 6: Access the Agent in Snowflake Intelligence
-- ============================================================================

-- The agent is now available at:
-- https://ai.snowflake.com/<region>/<org_id>#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
--
-- Or navigate manually:
-- 1. Go to AI & ML in Snowsight navigation
-- 2. Click "Snowflake Intelligence"
-- 3. Select the CUSTOMERMETRICSAGENT from the agent dropdown
-- 4. Start asking questions!

-- ============================================================================
-- Example Queries to Test the Agent
-- ============================================================================

/*
Try asking these questions in Snowflake Intelligence:

Basic Queries:
- "How many customers are in our loyalty program?"
- "Which countries have the most customers?"
- "Show me customers from Boston"

Sales Analysis:
- "What's the total sales by country?"
- "Show me the top 10 customers by total sales"
- "Which country generates the most revenue?"

Geographic Analysis:
- "Compare customer counts between United States and India"
- "What cities have the most customers?"
- "Show me the geographic distribution of our customers"

Advanced Queries:
- "What's the average sales per customer by country?"
- "Which customers have visited more than 50 locations?"
- "Find high-value customers from major cities"
*/

-- ============================================================================
-- Agent Configuration Details
-- ============================================================================

/*
Agent Name: CUSTOMERMETRICSAGENT
Database: TASTY_BYTES
Schema: HARMONIZED
Tool: customer_metrics_tool (semantic view)

Capabilities:
- Natural language understanding
- Automatic SQL generation
- Customer demographic queries
- Sales analysis
- Geographic insights
- Location visit patterns

Limitations:
- Focused on customer metrics only (by design)
- No time-series analysis (no date dimensions)
- Single table/view scope
- English language only

Custom Instructions (from semantic view):
- Round all numeric columns to 2 decimal points
- Answer all questions related to customer metrics and no other
*/

-- ============================================================================
-- Updating the Agent (if needed)
-- ============================================================================

-- To update the agent's configuration, use ALTER:
/*
ALTER CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT
  SET COMMENT = 'Updated description';
*/

-- To update the tool description:
/*
ALTER CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT
  REPLACE TOOLS WITH
    SYSTEM$ADD_SEMANTIC_VIEW_TOOL(
      'TASTY_BYTES.HARMONIZED.HARMONIZEDCUSTOMERMETRICSSEMANTICVIEW',
      '{
        "name": "customer_metrics_tool",
        "description": "Updated tool description here",
        "parameters": {}
      }'
    );
*/

-- ============================================================================
-- Troubleshooting
-- ============================================================================

/*
Issue: Agent not visible in Snowflake Intelligence
Solution: 
1. Verify agent exists: SHOW CORTEX ANALYST AGENTS;
2. Check permissions: Ensure your role has USAGE on the agent
3. Refresh Snowsight interface
4. Check you're in the correct database/schema context

Issue: Agent can't access semantic view
Solution:
1. Verify semantic view exists: SHOW SEMANTIC VIEWS;
2. Grant USAGE on semantic view to agent's role
3. Verify base table permissions

Issue: Agent gives incorrect results
Solution:
1. Test queries directly against semantic view
2. Add more verified queries to semantic view
3. Refine semantic view descriptions
4. Update custom instructions

Issue: "Agent not available in this region"
Solution:
1. Check if Cortex Analyst is available in your region
2. Contact Snowflake support to enable the feature
3. Try a different region if possible
*/

-- ============================================================================
-- Monitoring and Analytics
-- ============================================================================

-- View agent usage (requires appropriate privileges)
/*
SELECT 
    query_text,
    execution_status,
    total_elapsed_time,
    rows_produced
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
WHERE query_text ILIKE '%CUSTOMERMETRICSAGENT%'
ORDER BY start_time DESC
LIMIT 100;
*/

-- ============================================================================
-- Clean Up (Optional - use only if you want to remove the agent)
-- ============================================================================

-- To remove the agent (WARNING: This will delete the agent)
-- DROP CORTEX ANALYST AGENT IF EXISTS TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT;

-- ============================================================================
-- Next Steps
-- ============================================================================

/*
1. Access Snowflake Intelligence at the URL above
2. Select the CUSTOMERMETRICSAGENT
3. Try the example queries
4. Share the agent URL with your team
5. Gather feedback and iterate on the semantic view
6. Add more verified queries based on common questions
7. Monitor usage and optimize performance

For more information:
- Documentation: See docs/setup-guide.md
- Examples: See docs/usage-examples.md  
- GitHub: https://github.com/yourusername/tasty-bytes-cortex-analyst
- HuggingFace: https://huggingface.co/spaces/yourusername/tasty-bytes-cortex-analyst
*/

-- ============================================================================
-- Agent URL for Easy Access
-- ============================================================================

-- Direct link to your agent (replace <region> and <org_id> with your values):
-- https://ai.snowflake.com/<region>/<org_id>#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT

-- Example:
-- https://ai.snowflake.com/us-east-1/ogc69807#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT

SELECT 'Agent created successfully! Access it in Snowflake Intelligence.' AS status;
