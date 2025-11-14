CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT a.salary AS getNthHighestSalary
    FROM 
    (
        SELECT
            e.salary AS salary,
            dense_rank() OVER --repeats rank     if same value unlike rank()
            (ORDER BY e.salary DESC) as r
        FROM Employee e
    ) a
    WHERE a.r = N LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;