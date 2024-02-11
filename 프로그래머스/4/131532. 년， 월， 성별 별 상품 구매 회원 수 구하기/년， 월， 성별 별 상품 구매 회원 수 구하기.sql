SELECT YEAR(S.SALES_DATE) AS YEAR ,MONTH(S.SALES_DATE) AS MONTH ,GENDER,COUNT(DISTINCT S.USER_ID) AS USERS
FROM USER_INFO I
JOIN ONLINE_SALE S ON I.USER_ID = S.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR,MONTH,GENDER
ORDER BY YEAR ASC,MONTH ASC,GENDER ASC;
