# Optimization: Azure SQL Database

**Domain:** Azure
**Subdomain:** Azure SQL Database
**Incident Type:** Optimization

## Scenario / Query
An Azure SQL Database is experiencing high DTU consumption due to inefficient query plans. How can I identify and resolve the top resource-consuming queries to optimize performance?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure SQL Database with DTU-based purchasing model, standard tier

## Symptoms
- High DTU usage consistently above 80%
- Slow application response times
- Increased query duration for specific workloads

## Error Codes
N/A

## Root Causes
1. Missing or outdated indexes
2. Suboptimal query execution plans
3. High volume of read/write operations on specific tables

## Remediation Steps
1. Use the Azure portal to navigate to the SQL database and open Query Performance Insight to identify top queries by DTU consumption.
2. Review the query details and recommendations for index creation or query tuning provided by the Azure SQL Database Advisor.
3. Apply index recommendations by using the Azure portal or T-SQL commands such as CREATE INDEX.
4. Optionally, use the Database Engine Tuning Advisor to analyze a workload and generate tuning recommendations.

## Validation
Monitor DTU usage in the Azure portal after applying index changes. Verify that DTU consumption drops below 70% and query durations improve.

## Rollback
Drop any newly created indexes using DROP INDEX <index_name> ON <table_name>; or revert query changes to previous execution plan using plan guides.

## References
- <https://learn.microsoft.com/en-us/azure/azure-sql/database/query-performance-insight-usage>
- <https://learn.microsoft.com/en-us/azure/azure-sql/database/database-advisor-implement-performance-recommendations>
