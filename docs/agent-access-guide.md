# Accessing Your Cortex Analyst Agent

This guide explains how to access and use the CUSTOMERMETRICSAGENT in Snowflake Intelligence.

## Quick Access

### Direct URL Method (Fastest)

Your agent is available at:
```
https://ai.snowflake.com/<region>/<org_id>#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
```

**Example URL:**
```
https://ai.snowflake.com/us-east-1/ogc69807#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
```

**To find your URL:**
1. Log into Snowflake
2. Look at your browser address bar
3. Extract the region (e.g., `us-east-1`) and org ID (e.g., `ogc69807`)
4. Replace in the URL template above

### Snowsight Navigation Method

1. **Log into Snowflake Snowsight**
   - Go to your Snowflake account URL
   - Sign in with your credentials

2. **Navigate to Snowflake Intelligence**
   - Click **"AI & ML"** in the left navigation menu
   - Select **"Snowflake Intelligence"**

3. **Select Your Agent**
   - In the agent dropdown (top of page)
   - Choose **"CUSTOMERMETRICSAGENT"**

4. **Start Asking Questions!**
   - Type your question in natural language
   - Press Enter or click Send
   - View the generated SQL and results

## Using the Agent

### Basic Interaction

**1. Ask a Question**
```
Type: "How many customers are in our loyalty program?"
```

**2. Review Generated SQL**
The agent will show you the SQL it generated:
```sql
SELECT COUNT(DISTINCT customer_id)
FROM customer_loyalty_metrics_v
```

**3. View Results**
See the answer displayed in a clear format:
```
Result: 11,420 customers
```

### Query Types

**Customer Counts**
- "How many customers are in our loyalty program?"
- "How many customers do we have in Egypt?"
- "Count customers by country"

**Geographic Analysis**
- "Which countries have the most customers?"
- "Show me cities with more than 100 customers"
- "Compare customer counts between United States and India"

**Sales Analysis**
- "What's the total sales by country?"
- "Show me the top 10 customers by total sales"
- "What's the average sales per customer?"

**Customer Details**
- "Show me customer 110913's information"
- "Find all customers from Boston"
- "List customers with sales over $2000"

**Advanced Queries**
- "What's the average sales per customer by country?"
- "Which customers have visited more than 50 locations?"
- "Show me high-value customers from major cities"

## Agent Features

### What the Agent Can Do

✅ **Understand Natural Language**
- Ask questions in plain English
- No SQL knowledge required
- Conversational interface

✅ **Generate Accurate SQL**
- Automatically creates optimized queries
- Shows you the SQL for transparency
- Follows best practices

✅ **Provide Business Context**
- Uses business-friendly terminology
- Returns formatted results
- Includes relevant metadata

✅ **Support Complex Analysis**
- Aggregations (COUNT, SUM, AVG)
- Filtering and comparisons
- Sorting and ranking
- Multi-dimensional analysis

### Agent Limitations

❌ **Scope Limited to Customer Metrics**
- By design, only answers customer-related questions
- Won't answer questions about orders, menu items, etc.
- This ensures focused, high-quality responses

❌ **No Time-Series Analysis**
- Current semantic view doesn't include date dimensions
- Can't answer "show me sales trends over time"
- Can be added by extending the semantic view

❌ **Single View Scope**
- Based on CUSTOMER_LOYALTY_METRICS_V
- Can't join with other tables
- Create additional agents for other datasets

❌ **English Language Only**
- Currently supports English queries only
- May add other languages in future

## Tips for Best Results

### 1. Be Specific
✅ Good: "Show me customers from Boston with sales over $1000"
❌ Vague: "Show me some customers"

### 2. Use Business Terms
✅ Good: "Which countries have the most customers?"
❌ Technical: "SELECT country, COUNT(*) FROM table GROUP BY country"

### 3. Start Simple, Then Refine
1. First: "Show me customer counts by country"
2. Then: "Now show only countries with more than 1000 customers"
3. Finally: "Add total revenue for each"

### 4. Reference Known Values
✅ "Compare sales between United States and India"
✅ "Show me customer 110913's details"

### 5. Ask Follow-up Questions
The agent maintains context within a conversation:
- "Now sort by sales ascending"
- "Show me just the top 5"
- "What about Egypt?"

## Common Patterns

### Pattern 1: Counting
```
Template: "How many [entities] are there [filter]?"
Example: "How many customers are there in India?"
```

### Pattern 2: Top N
```
Template: "Show me the top [N] [entities] by [metric]"
Example: "Show me the top 10 customers by total sales"
```

### Pattern 3: Comparisons
```
Template: "Compare [metric] between [group1] and [group2]"
Example: "Compare customer counts between United States and India"
```

### Pattern 4: Aggregations
```
Template: "What's the [aggregate] [metric] by [dimension]?"
Example: "What's the total sales by country?"
```

## Sharing Your Agent

### Share with Team Members

**Option 1: Share Direct URL**
```
Send teammates: https://ai.snowflake.com/<region>/<org_id>#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
```

**Option 2: Grant Access**
```sql
GRANT USAGE ON CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT 
  TO ROLE BUSINESS_ANALYST_ROLE;
```

**Option 3: Provide Instructions**
1. Go to AI & ML → Snowflake Intelligence
2. Select CUSTOMERMETRICSAGENT from dropdown
3. Start asking questions

### Training Your Team

**Quick Training Session (15 minutes):**

1. **Demo (5 min)**: Show 3-5 example queries
2. **Try It (5 min)**: Let them ask questions
3. **Review (5 min)**: Discuss SQL and results

**Example Questions for Training:**
- Start: "How many customers do we have?"
- Medium: "Which countries have the most customers?"
- Advanced: "What's the average sales per customer by country?"

## Troubleshooting

### Issue: Agent Not Found

**Symptom:** Can't find CUSTOMERMETRICSAGENT in dropdown

**Solutions:**
1. Verify agent exists:
   ```sql
   SHOW CORTEX ANALYST AGENTS IN SCHEMA TASTY_BYTES.HARMONIZED;
   ```
2. Check you're in correct database/schema context
3. Verify you have USAGE permission on the agent
4. Refresh your browser

### Issue: Permission Denied

**Symptom:** "You don't have permission to use this agent"

**Solutions:**
1. Ask admin to grant access:
   ```sql
   GRANT USAGE ON CORTEX ANALYST AGENT TASTY_BYTES.HARMONIZED.CUSTOMERMETRICSAGENT 
     TO ROLE YOUR_ROLE;
   ```
2. Switch to a role that has access
3. Contact your Snowflake administrator

### Issue: Agent Gives "I Don't Know" Response

**Symptom:** Agent can't answer your question

**Reasons:**
1. Question is outside scope (not customer metrics)
2. Question is ambiguous or unclear
3. Required data not in semantic view

**Solutions:**
1. Rephrase question more clearly
2. Use terms from verified queries
3. Start with simpler question
4. Ask "What can you tell me about...?"

### Issue: Incorrect Results

**Symptom:** SQL generated but results seem wrong

**Solutions:**
1. Review the generated SQL
2. Verify question was understood correctly
3. Rephrase question for clarity
4. Check if data matches expectations
5. Report issue for semantic view improvement

## Advanced Usage

### Creating Custom Views

If you need to ask questions beyond current scope:

1. Create additional semantic views for other data
2. Create new agents for different use cases
3. Combine multiple agents in workflow

### Monitoring Usage

Track how your team uses the agent:

```sql
SELECT 
    query_text,
    execution_status,
    total_elapsed_time
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
WHERE query_text ILIKE '%CUSTOMERMETRICSAGENT%'
ORDER BY start_time DESC
LIMIT 100;
```

### Improving Accuracy

Add verified queries to semantic view:

1. Identify common questions
2. Write and test SQL
3. Add to semantic view as verified queries
4. Agent accuracy improves automatically

## Support Resources

### Documentation
- Setup Guide: `docs/setup-guide.md`
- Usage Examples: `docs/usage-examples.md`
- GitHub: [Project Repository](https://github.com/yourusername/tasty-bytes-cortex-analyst)

### Getting Help
1. Check documentation first
2. Review example queries
3. Open GitHub issue
4. Contact Snowflake support

### Feedback
Help improve the agent by:
- Sharing questions it handles well
- Reporting incorrect responses
- Suggesting new features
- Contributing verified queries

---

## Quick Reference

**Agent Name:** CUSTOMERMETRICSAGENT
**Database:** TASTY_BYTES
**Schema:** HARMONIZED
**Tool:** customer_metrics_tool (semantic view)

**Access URL Template:**
```
https://ai.snowflake.com/<region>/<org_id>#/ai/chat/new?db=TASTY_BYTES&schema=HARMONIZED&agent=CUSTOMERMETRICSAGENT
```

**Example Questions:**
- "How many customers are in our loyalty program?"
- "Which countries have the most customers?"
- "Show me the top 10 customers by total sales"
- "What's the average sales per customer by country?"

**Support:**
- Docs: `docs/` directory
- GitHub: Issues and discussions
- Snowflake: Support portal

---

**Now go explore your data with natural language! 🚀**
