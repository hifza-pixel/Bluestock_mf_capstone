-- 1 Top 5 fund houses by AUM
SELECT fund_house, aum_crore
FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) AS avg_nav
FROM nav_history;

-- 3 Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state;

-- 4 Expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 5 Average return by category
SELECT category, AVG(return_3yr_pct)
FROM scheme_performance
GROUP BY category;

-- 6 Total AUM by fund house
SELECT fund_house, SUM(aum_crore)
FROM aum_by_fund_house
GROUP BY fund_house;

-- 7 Top performing funds
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 8 Transactions by gender
SELECT gender, COUNT(*)
FROM investor_transactions
GROUP BY gender;

-- 9 Average investment amount
SELECT AVG(amount_inr)
FROM investor_transactions;

-- 10 Most active states
SELECT state, SUM(amount_inr)
FROM investor_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;