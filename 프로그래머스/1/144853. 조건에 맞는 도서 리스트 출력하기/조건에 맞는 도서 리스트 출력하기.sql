SELECT BOOK_ID, substring(published_date, 1, 10) as PUBLISHED_DATE from book
where PUBLISHED_DATE like '2021%'
and category = '인문'
order by PUBLISHED_DATE