# Usage Examples and Query Patterns

This guide provides comprehensive examples of natural language queries you can ask the Tasty Bytes Cortex Analyst agent, organized by use case and complexity.

## Table of Contents
1. [Basic Queries](#basic-queries)
2. [Customer Analytics](#customer-analytics)
3. [Geographic Analysis](#geographic-analysis)
4. [Sales Insights](#sales-insights)
5. [Advanced Patterns](#advanced-patterns)
6. [Query Best Practices](#query-best-practices)

---

## Basic Queries

### Simple Counts

**Query:** "How many customers are in our loyalty program?"
```sql
-- Generated SQL
SELECT COUNT(DISTINCT customer_id)
FROM customer_loyalty_metrics_v
```
**Result:** 11,420 customers

---

**Query:** "How many countries do we operate in?"
```sql
-- Generated SQL
SELECT COUNT(DISTINCT country)
FROM customer_loyalty_metrics_v
```
**Result:** 30+ countries

---

### Simple Filters

**Query:** "Show me customers from Boston"
```sql
-- Generated SQL
SELECT 
  customer_id,
  first_name,
  last_name,
  e_mail,
  total_sales
FROM customer_loyalty_metrics_v
WHERE city = 'Boston'
```

---

**Query:** "List all customers from India"
```sql
-- Generated SQL
SELECT 
  customer_id,
  first_name,
  last_name,
  city,
  total_sales
FROM customer_loyalty_metrics_v
WHERE country = 'India'
```

---

## Customer Analytics

### Top Performers

**Query:** "Who are our top 10 customers by total sales?"
```sql
-- Generated SQL
SELECT 
  customer_id,
  first_name,
  last_name,
  city,
  country,
  ROUND(total_sales, 2) as total_sales
FROM customer_loyalty_metrics_v
ORDER BY total_sales DESC
LIMIT 10
```

**Sample Results:**
| Customer ID | Name | City | Country | Total Sales |
|-------------|------|------|---------|-------------|
| 110913 | Anna Sanchez | Boston | United States | $3,302.00 |
| 130576 | Grace Kline | Mumbai | India | $2,809.50 |
| 90298 | Dahlia Buchanan | Cairo | Egypt | $1,745.75 |

---

**Query:** "Show me the bottom 10 customers by sales"
```sql
-- Generated SQL
SELECT 
  customer_id,
  first_name,
  last_name,
  city,
  country,
  ROUND(total_sales, 2) as total_sales
FROM customer_loyalty_metrics_v
ORDER BY total_sales ASC
LIMIT 10
```

---

### Customer Segments

**Query:** "How many customers have spent more than $2000?"
```sql
-- Generated SQL
SELECT COUNT(DISTINCT customer_id)
FROM customer_loyalty_metrics_v
WHERE total_sales > 2000
```

---

**Query:** "Show me customers who have visited more than 50 locations"
```sql
-- Generated SQL
SELECT 
  customer_id,
  first_name,
  last_name,
  city,
  country,
  ARRAY_SIZE(visited_location_ids_array) as location_count,
  ROUND(total_sales, 2) as total_sales
FROM customer_loyalty_metrics_v
WHERE ARRAY_SIZE(visited_location_ids_array) > 50
ORDER BY location_count DESC
```

---

### Customer Details

**Query:** "What's the contact information for customer 110913?"
```sql
-- Generated SQL
SELECT 
  customer_id,
  first_name,
  last_name,
  e_mail,
  phone_number,
  city,
  country
FROM customer_loyalty_metrics_v
WHERE customer_id = 110913
```

---

**Query:** "Find all customers with email addresses from gmail.com"
```sql
-- Generated SQL
SELECT 
  customer_id,
  first_name,
  last_name,
  e_mail,
  city,
  country
FROM customer_loyalty_metrics_v
WHERE e_mail LIKE '%@gmail.com'
```

---

## Geographic Analysis

### Country-Level Analysis

**Query:** "Which countries have the highest number of customers?"
```sql
-- Generated SQL
SELECT
  country,
  COUNT(DISTINCT customer_id) as customer_count
FROM customer_loyalty_metrics_v
GROUP BY country
ORDER BY customer_count DESC
```

**Results:**
| Country | Customer Count |
|---------|----------------|
| United States | 5,420 |
| India | 3,890 |
| Egypt | 2,110 |
| Brazil | 1,840 |
| Canada | 1,320 |

---

**Query:** "What's the total sales by country?"
```sql
-- Generated SQL
SELECT
  country,
  ROUND(SUM(total_sales), 2) as total_revenue
FROM customer_loyalty_metrics_v
GROUP BY country
ORDER BY total_revenue DESC
```

---

**Query:** "Compare customer counts between United States and India"
```sql
-- Generated SQL
SELECT
  country,
  COUNT(DISTINCT customer_id) as customer_count,
  ROUND(SUM(total_sales), 2) as total_revenue
FROM customer_loyalty_metrics_v
WHERE country IN ('United States', 'India')
GROUP BY country
```

---

### City-Level Analysis

**Query:** "Which cities have the most customers?"
```sql
-- Generated SQL
SELECT
  city,
  country,
  COUNT(DISTINCT customer_id) as customer_count
FROM customer_loyalty_metrics_v
GROUP BY city, country
ORDER BY customer_count DESC
LIMIT 20
```

---

**Query:** "Show me all cities in the United States with our customers"
```sql
-- Generated SQL
SELECT DISTINCT
  city,
  COUNT(DISTINCT customer_id) as customer_count
FROM customer_loyalty_metrics_v
WHERE country = 'United States'
GROUP BY city
ORDER BY customer_count DESC
```

---

**Query:** "What's the average sales per customer by city?"
```sql
-- Generated SQL
SELECT
  city,
  country,
  COUNT(DISTINCT customer_id) as customer_count,
  ROUND(AVG(total_sales), 2) as avg_sales_per_customer
FROM customer_loyalty_metrics_v
GROUP BY city, country
HAVING COUNT(DISTINCT customer_id) >= 10
ORDER BY avg_sales_per_customer DESC
```

---

## Sales Insights

### Revenue Analysis

**Query:** "What's the total revenue across all customers?"
```sql
-- Generated SQL
SELECT ROUND(SUM(total_sales), 2) as total_revenue
FROM customer_loyalty_metrics_v
```

---

**Query:** "What's the average sales per customer?"
```sql
-- Generated SQL
SELECT ROUND(AVG(total_sales), 2) as average_sales
FROM customer_loyalty_metrics_v
```

---

**Query:** "Show me revenue distribution: min, max, average"
```sql
-- Generated SQL
SELECT
  ROUND(MIN(total_sales), 2) as min_sales,
  ROUND(MAX(total_sales), 2) as max_sales,
  ROUND(AVG(total_sales), 2) as avg_sales,
  ROUND(MEDIAN(total_sales), 2) as median_sales
FROM customer_loyalty_metrics_v
```

---

### Sales Rankings

**Query:** "Rank countries by total revenue"
```sql
-- Generated SQL
SELECT
  country,
  ROUND(SUM(total_sales), 2) as total_revenue,
  COUNT(DISTINCT customer_id) as customer_count,
  ROUND(AVG(total_sales), 2) as avg_customer_value
FROM customer_loyalty_metrics_v
GROUP BY country
ORDER BY total_revenue DESC
```

---

**Query:** "Which countries generate the least to most total sales revenue?"
```sql
-- Generated SQL
SELECT
  country,
  ROUND(SUM(total_sales), 2) as total_revenue
FROM customer_loyalty_metrics_v
GROUP BY country
ORDER BY total_revenue ASC
```

---

### Customer Value Segments

**Query:** "How many customers fall into different spending tiers?"
```sql
-- Generated SQL
SELECT
  CASE 
    WHEN total_sales < 500 THEN 'Low ($0-$499)'
    WHEN total_sales < 1000 THEN 'Medium ($500-$999)'
    WHEN total_sales < 2000 THEN 'High ($1000-$1999)'
    ELSE 'Premium ($2000+)'
  END as spending_tier,
  COUNT(DISTINCT customer_id) as customer_count,
  ROUND(AVG(total_sales), 2) as avg_sales
FROM customer_loyalty_metrics_v
GROUP BY 
  CASE 
    WHEN total_sales < 500 THEN 'Low ($0-$499)'
    WHEN total_sales < 1000 THEN 'Medium ($500-$999)'
    WHEN total_sales < 2000 THEN 'High ($1000-$1999)'
    ELSE 'Premium ($2000+)'
  END
ORDER BY avg_sales
```

---

## Advanced Patterns

### Multi-Dimensional Analysis

**Query:** "Show me customer distribution and revenue by country and city"
```sql
-- Generated SQL
SELECT
  country,
  city,
  COUNT(DISTINCT customer_id) as customer_count,
  ROUND(SUM(total_sales), 2) as total_revenue,
  ROUND(AVG(total_sales), 2) as avg_customer_value
FROM customer_loyalty_metrics_v
GROUP BY country, city
HAVING COUNT(DISTINCT customer_id) >= 5
ORDER BY total_revenue DESC
```

---

### Comparative Analysis

**Query:** "Compare top 5 cities by customer count vs top 5 by revenue"
```sql
-- Generated SQL
WITH top_by_customers AS (
  SELECT city, country, COUNT(DISTINCT customer_id) as cust_count
  FROM customer_loyalty_metrics_v
  GROUP BY city, country
  ORDER BY cust_count DESC
  LIMIT 5
),
top_by_revenue AS (
  SELECT city, country, ROUND(SUM(total_sales), 2) as revenue
  FROM customer_loyalty_metrics_v
  GROUP BY city, country
  ORDER BY revenue DESC
  LIMIT 5
)
SELECT * FROM top_by_customers
UNION ALL
SELECT * FROM top_by_revenue
```

---

### Location Visit Analysis

**Query:** "Who has visited the most unique locations?"
```sql
-- Generated SQL
SELECT
  customer_id,
  first_name,
  last_name,
  city,
  country,
  ARRAY_SIZE(visited_location_ids_array) as unique_locations_visited,
  ROUND(total_sales, 2) as total_sales
FROM customer_loyalty_metrics_v
ORDER BY unique_locations_visited DESC
LIMIT 20
```

---

**Query:** "What's the average number of locations visited per customer by country?"
```sql
-- Generated SQL
SELECT
  country,
  COUNT(DISTINCT customer_id) as customer_count,
  ROUND(AVG(ARRAY_SIZE(visited_location_ids_array)), 2) as avg_locations_visited
FROM customer_loyalty_metrics_v
GROUP BY country
ORDER BY avg_locations_visited DESC
```

---

### Customer Profile Queries

**Query:** "Find high-value customers (over $2000) from major cities"
```sql
-- Generated SQL
SELECT
  customer_id,
  first_name,
  last_name,
  city,
  country,
  e_mail,
  phone_number,
  ROUND(total_sales, 2) as total_sales
FROM customer_loyalty_metrics_v
WHERE 
  total_sales > 2000
  AND city IN ('Boston', 'Mumbai', 'Cairo', 'Tokyo', 'London')
ORDER BY total_sales DESC
```

---

**Query:** "Show me customers from India with sales above average"
```sql
-- Generated SQL
WITH avg_sales AS (
  SELECT AVG(total_sales) as country_avg
  FROM customer_loyalty_metrics_v
  WHERE country = 'India'
)
SELECT
  c.customer_id,
  c.first_name,
  c.last_name,
  c.city,
  ROUND(c.total_sales, 2) as total_sales,
  ROUND(a.country_avg, 2) as country_average
FROM customer_loyalty_metrics_v c
CROSS JOIN avg_sales a
WHERE 
  c.country = 'India'
  AND c.total_sales > a.country_avg
ORDER BY c.total_sales DESC
```

---

## Query Best Practices

### Tips for Effective Queries

1. **Be Specific**
   - ✅ "Show me customers from Boston with sales over $1000"
   - ❌ "Show me customers"

2. **Use Business Terms**
   - ✅ "Which countries have the most customers?"
   - ❌ "SELECT country, count(*) FROM table GROUP BY country"

3. **Start Simple, Then Refine**
   - First: "Show me customer counts by country"
   - Then: "Now show only countries with more than 1000 customers"
   - Finally: "Add total revenue for each"

4. **Reference Known Values**
   - ✅ "Compare sales between United States and India"
   - ✅ "Show me customer 110913's details"

5. **Use Natural Language**
   - ✅ "Who are our top 10 customers?"
   - ✅ "What's the average sales per customer in Egypt?"

### What Works Well

**Aggregations:**
- "Total", "sum", "average", "count"
- "How many", "What's the total"

**Comparisons:**
- "More than", "less than", "between"
- "Top", "bottom", "highest", "lowest"

**Filters:**
- "From [location]", "in [country]"
- "Where [condition]"

**Sorting:**
- "Ranked by", "ordered by", "sorted by"
- "Top 10", "bottom 5"

### Common Patterns

**Pattern 1: Count + Group By**
```
"How many [entities] are there by [dimension]?"
→ SELECT dimension, COUNT(*) FROM table GROUP BY dimension
```

**Pattern 2: Top N**
```
"Show me the top [N] [entities] by [metric]"
→ SELECT * FROM table ORDER BY metric DESC LIMIT N
```

**Pattern 3: Filter + Aggregate**
```
"What's the [metric] for [entities] in [location]?"
→ SELECT metric FROM table WHERE location = 'X'
```

**Pattern 4: Compare Groups**
```
"Compare [metric] between [group1] and [group2]"
→ SELECT group, metric FROM table WHERE group IN (...)
```

---

## Limitations and Workarounds

### Current Limitations

1. **No Time-Series Analysis**
   - The semantic view doesn't include date dimensions
   - Workaround: Add date dimensions to semantic view

2. **No Multi-Table Joins**
   - Based on single aggregated view
   - Workaround: Create additional semantic views

3. **Array Operations Limited**
   - VISITED_LOCATION_IDS_ARRAY requires specific SQL
   - Workaround: Use ARRAY_SIZE() for counts

### Future Enhancements

Consider adding to semantic view:
- Signup date dimension
- Birthday/age dimension
- Loyalty tier (derived)
- Customer lifetime calculation
- Relationships to order details

---

## Getting Creative

### Interesting Questions to Explore

1. "What percentage of customers have visited more than 20 locations?"
2. "Which cities have customers with above-average spending?"
3. "Show me the distribution of customers across countries"
4. "Find customers who might be traveling (visited many locations)"
5. "What's the geographic concentration of our customer base?"
6. "Compare customer value between major metro areas"
7. "Which countries have the highest customer engagement?"

### Building on Results

After getting initial results:
- "Now show only [subset]"
- "Can you rank these by [different metric]?"
- "What about [different dimension]?"
- "Show me the details for [specific item]"

---

**Pro Tip:** The more you use the agent, the better it understands your patterns and terminology. Start with verified queries and gradually expand to more complex analyses!

For more examples, check the [GitHub repository](https://github.com/yourusername/tasty-bytes-cortex-analyst) or open an issue with your use case.
