use sakila;

-- 1. film 테이블에서 영화 제목과 대여 요금을 조회하시오.
desc film;
select f.title, f.rental_rate from film f;
-- 2. actor 테이블에서 이름이 'JOHN'인 배우를 조회하시오.
desc actor;
select a.*
from actor a
where A.first_name='JOHN';
-- 3. category 테이블의 모든 카테고리 이름을 조회하시오.
desc category;
select C.* from category C;
-- 4. film 테이블에서 rental_rate가 3.99보다 큰 영화의 제목과 요금을 조회하시오.
desc film;
select title, rental_rate
from film
where rental_rate>3.99;
-- 5. customer 테이블에서 이메일 주소에 'gmail'이 포함된 고객을 조회하시오.
desc customer;
select email from customer limit 10; 
select *
from customer
where email like "%sakil%";
-- 6. film 테이블에서 길이가 120분 이하인 영화의 제목과 길이를 조회하시오.
desc film;
select title, length
from film
where length <= 120;
-- 7. language 테이블에서 언어 이름이 'English'인 행을 조회하시오.
desc language;
select name from language limit 10;
select *
from language A
where A.name = 'English';
-- 8. actor 테이블에서 성(last_name)이 'SMITH'인 배우의 이름과 성을 조회하시오.
desc actor;
select last_name, first_name
from actor
where last_name='SMITH';
-- 9. customer 테이블에서 first_name이 'A'로 시작하는 고객을 조회하시오.
desc customer;
select *
from customer c 
where first_name like '%A';
-- 10. film 테이블에서 2006년에 개봉한 영화만 조회하시오.
select *
from film f
where f.release_year=2006;

-- 11. 배우번호가 10, 21, 34, 56, 87, 89, 90인 사람들 정보만 출력
desc actor;
select * from actor a where a.actor_id in(10,21,34,56,87,89,90);  
-- 12. customer 테이블중 store_ID=1이고 회원 customer_id 562, 580, 470, 471, 363, 364
desc customer;
select *
from customer c
where c.store_id = 1 and c.customer_id in (
562,580,470,471,363,364
);