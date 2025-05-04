select 
    concat('1','Q') as QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM
    ECOLI_DATA
WHERE 
    quarter(DIFFERENTIATION_DATE)=1
UNION
select 
    concat('2','Q') as QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM
    ECOLI_DATA
WHERE 
    quarter(DIFFERENTIATION_DATE)=2
UNION
select 
    concat('3','Q') as QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM
    ECOLI_DATA
WHERE 
    quarter(DIFFERENTIATION_DATE)=3
UNION
select 
    concat('4','Q') as QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM
    ECOLI_DATA
WHERE 
    quarter(DIFFERENTIATION_DATE)=4;

    