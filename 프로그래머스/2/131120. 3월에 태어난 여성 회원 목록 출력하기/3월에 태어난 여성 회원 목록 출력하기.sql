SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
substring(DATE_OF_BIRTH, 1, 10) as DATE_OF_BIRTH from MEMBER_PROFILE
where substring(DATE_OF_BIRTH, 6, 2) = '03'
and GENDER = 'W'
and TLNO is not null
order by MEMBER_ID
