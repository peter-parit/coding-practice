select e.name
from Employee e
where (
    select count(c.managerId)
    from Employee c
    where c.managerId = e.id
) >= 5