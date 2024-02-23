SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & 256 <> 0  -- Python 스킬을 가진 개발자
   OR SKILL_CODE & 1024 <> 0 -- C# 스킬을 가진 개발자
ORDER BY ID ASC;
