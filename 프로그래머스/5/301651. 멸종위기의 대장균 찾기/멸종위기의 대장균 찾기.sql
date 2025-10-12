-- 코드를 작성해주세요

-- 세대 작성하기
with recursive 
generation_ as(
    select id, parent_id, 1 as level
    from ECOLI_DATA
    where parent_id is null
    
    union all
    
    select c.id, c.parent_id, d.level+1
    from ECOLI_DATA as c 
    join generation_ as d on c.parent_id=d.id
    
)

select count(*) as COUNT,  level as GENERATION
from generation_
where id not in (select DISTINCT parent_id from ECOLI_DATA WHERE parent_id is not null)
group by level
order by 2;
