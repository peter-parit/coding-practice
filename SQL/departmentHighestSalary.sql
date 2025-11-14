-- with window functions
with ranks as (
    select 
        d.name as Department, 
        e.name as Employee, 
        e.salary as Salary,
        rank() over (partition by d.id order by e.salary desc) as rnk
    from Employee e
    join Department d on e.departmentId = d.id
)
select 
    r.Department as Department, 
    r.Employee as Employee,
    r.Salary as Salary
from ranks r
where r.rnk = 1

-- with selects
select 
    d.name as Department, 
    e.name as Employee,
    max(e.salary) as Salary
from Department d join Employee e
on d.id = e.departmentId
where e.salary = (
    select max(m.salary)
    from Employee m
    where m.departmentId = e.departmentId
)
group by d.name, e.name;