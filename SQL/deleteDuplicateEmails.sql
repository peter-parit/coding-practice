delete from Person p
using Person q
where p.id > q.id and p.email = q.email;