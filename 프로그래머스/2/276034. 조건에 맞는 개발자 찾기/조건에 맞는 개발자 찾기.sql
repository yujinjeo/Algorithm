# with codes as (
#     select code
#     from SKILLCODES
#     where name='C#' or name='Python'
# )
# select d.id, d.email, d.first_name, d.last_name 
# from developers as d
# join codes as c on (d.skill_code & c.code) != 0
# order by id asc;

SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S
  ON D.SKILL_CODE & S.CODE != 0
WHERE S.NAME IN ('Python', 'C#')
ORDER BY D.ID ASC;
