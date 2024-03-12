-- 코드를 입력하세요
-- DATE_FORMAT 함수!!
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER="W" and MONTH(DATE_OF_BIRTH)=3 and TLNO IS NOT NULL -- 문자에 "" 붙여야 함
ORDER BY MEMBER_ID;