use sakila;


select * from actor limit 10;
select * from film limit 10;
-- 어떤 배우가 어떤 영화에 출연했는지 알고싶다.
select * from film_actor limit 10;

-- 영화 필름 기준으로 join

SELECT title, description, B.actor_id, C.first_name
FROM film A
LEFT OUTER JOIN film_actor B ON A.film_id = B.film_id
LEFT OUTER JOIN actor C ON B.actor_id = C.actor_id;


SELECT title, description, B.actor_id,
CONCAT(C.last_name, " ", C.first_name) AS actor_name
FROM film A
LEFT OUTER JOIN film_actor B ON A.film_id = B.film_id
LEFT OUTER JOIN actor C ON B.actor_id = C.actor_id;

-- catogory가 comedy인 영화 목록만 
-- film, category, film_category
select title
from film A
left outer join film_category B on A.film_id=B.film_id
left outer join category c on B.category_id=C.category_id
where C.name = 'comedy';

-- 고객의 이름과 고객의 대여한 영화 제목을 모두 출력하자
-- customer, rental, inventory, film, 
-- inventory_id, film_id, stroe_id
select * from inventory i  limit 10;
select * from customer c  limit 10;
select * from rental limit 10;
select * from film limit 10;

-- 문제1. 서브쿼리를 활용해서 title 가져오기
select concat(A.last_name, A.first_name)name, D.title
from customer A
left outer join rental B on A.customer_id = B.customer_id
left outer join inventory C on B.inventory_id = C.inventory_id
LEFT OUTER JOIN film D ON D.film_id=C.film_id;



-- 문제2. NICK WAHLBERG 라는 배우가 출연한 영화의 제목 조회하기
select title
from actor A
inner join film_actor B on actor_id=B.actor_id
inner join film c on B.film_id = C.film_id
where A.first_name='NICK' and A.last_name='WAHLBERG';

-- 'London' 도시의 고객 이름 

SELECT A.first_name
FROM customer A
JOIN address B ON A.address_id = B.address_id
JOIN city C ON B.city_id = C.city_id
WHERE C.city = 'London'

select * from customer limit 10;
select * from address limit 10;
select * from city limit 10;


-- join 속도를 빠르게 하려면, join 필드에 인덱스를 만들어야한다.
-- 서브쿼리 : 서브쿼리는 주쿼리 옆에서 주쿼리보다 먼저 실해오디서 결과를
-- 가져온 다음에 주쿼리가 실행된다.
-- 서브쿼리는 select 절, from 절, where, order by 등 가능
-- select절 : 스칼라서브 쿼리, 결과값이 null이거나 한개만 가져오는 쿼리
-- join을 대체할 수 있다 우리가 볼때 편해보임, 조인이 더 빠르다
-- 가급적 join으로 해결하고 join이 안될때 서브쿼리를 사용하자

use mydb;
-- 사원번호, 사원이름, 부서명을 가져오려고 한다.
select empno, ename, deptno -- 서브쿼리를 이용해 부서필드 가져오기
from emp;

select dname from dept where deptno=10;

select empno, ename, deptno,
(select dname from dept where dept.deptno=emp.deptno) as dname
from emp;

use sakila;

select first_name, last_name, B.film_id
from actor A
left outer join film_actor B on A.actor_id =B.actor_id;

select first_name, last_name,
(select title from film C where B.film_id=C.film_id) as title
,(select length from film C where B.film_id=C.film_id) as length
from actor A
left outer join film_actor B on A.actor_id =B.actor_id;


-- from 절에서 : 다중행을 반환한다. 다중행 서브쿼리, 인라인
use mydb;

-- select * from emp where deptno in(10, 20) 에서 사원이름, 부서명

select A.ename, dname
from (
	select * from emp where deptno in (10,20)
) as A
join dept B on A.deptno=B.deptno;


use sakila;

-- film_id : ambigous 오류가 뜨면 명확하게 A. 붙여주
select A.film_id, title, length, actor_id
from film A
left outer join film_actor B on A.film_id=B.film_id;

select first_name, last_name, title
from actor A
left outer join(
	select A.film_id, title, length, actor_id
	from film A
	left outer join film_actor B on A.film_id=B.film_id
	-- inline view
) B on A.actor_id=B.actor_id;

-- where절
use mydb;

-- emp 테이블에 smith 라 사람의 부서와 같은 부서에 있는 사람들 정보
select deptno from emp where ename='SMITH';
-- where 조건절에 오는 서브쿼리가 데이터가 여러개일
-- 단일행인경우와 다중행인 경우 처리방법이 다르다
select * from emp where deptno=20;

select * from emp
where deptno=(select deptno from emp where ename='정지우');

SELECT * FROM emp
WHERE ename='정지우';

-- 정지우가 근무하는 부서의 급여 평균보다 급여를 받는 사람들 정보를 확인하고자 한다.
SELECT AVG(sal) 
FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE ename='정지우');

SELECT * 
FROM emp 
WHERE sal > (
    SELECT AVG(sal) 
    FROM emp 
    WHERE deptno = (
        SELECT deptno 
        FROM emp 
        WHERE ename='정지우'
    )
);


-- 부서 평균 급여보다 급여가 많은 사원 조회
select * from emp
where sal > (select avg(sal) from emp);

-- 가장 높은 급여를 받는 사원 정보 조회하기
select ename
from emp
where sal = (select max(sal) from emp);


-- 매니저가 존재하는 사원만 조회
select ename
from emp
where job = (select job from emp where job='매니저');

select ename
from emp
where job = '매니저';

-- 매니저(상사)가 존재하는 사원만 조회
select * from emp where mgr in (select empno from emp);

SELECT *
FROM emp
WHERE mgr IS NOT NULL;

-- 상관쿼리 : 외부쿼리의 값을 내부쿼리에서 참조하는 서브쿼리를 말한다.
-- 외부쿼리의 각 행마다 내부쿼리가 실행되는 구조
-- exists, any, all, in 등이 있다.
-- exists - 서브쿼리의 실행결과가 하나라도 있으면 True 없으면 Fasle
--		    서브쿼리의 실행 결과가 한건이라도 있으면 실행된다.
-- any	  - 조건을 만족하는 것이 하나라도 있으면 수
-- 		부등호 or 부등호 or 부등호 부등호 or 부등호 or 부등호
-- All 	  - 모든 조건을 만족하는
--		부등호 and 부등호 and 부등호 and 부등호
-- in 	  - 등호 or 등호 or 등호 or

-- 부서별 평균 급여보다 높은 사원조회
-- 부서별 평균값이 필요
use mydb;
select avg(sal) from emp where deptno=10;
select avg(sal) from emp where deptno=20;
select avg(sal) from emp where deptno=30;

-- 부서번호 10이 서브쿼리의 외부 쿼리에서 가져와야 한

-- 외부의 A의 deptno 와 서브쿼리(내부쿼리)의 deptno가 서로 관계가 있다.
-- 상관쿼
select empno, sal, deptno from emp A
where sal > (select avg(sal) from emp B where B.deptno=A.deptno);

-- exists - 매니저가 존재하는 사원만 조회
select empno, ename, mgr from emp;
select ename from emp where mgr=7902;
-- 서브쿼리의 실행결과가 하나라도 있으면 외부쿼리를 실행한다
-- 서브쿼리의 결과 유무만 따진다.
-- select * from emp where exists (서브쿼리)

select empno, ename, mgr from emp A
where exists (
	select 1 from emp B where A.mgr=B.empno
);


use w3schools;

-- 주문내역, 고객이름, 판매자이름
-- orderdetails에서 orderdetaild에서 끌어오고 
-- order Iddlrh
-- order id에서 customers id
desc orders;
desc customers;


select A.*, B.CustomerName,
concat(C.lastName, " ", C.FirstName) as EmployeeName
from orders A
join customers B on A.customerId=B.customerID
join employees C on A.employeeId=C.employeeId;

-- 주의사항, linux mysql은 필드명이나 테이블명의 대소문자 구분함

-- 그룹함수, avg, max, min, count, sum 등
use mydb;
-- ename, sal필드는 데이터 개수만큼, avg(sal)-1개=> 개수안맞
-- select ename, sal, avg(sal) from emp;

select ename, sal, (select avg(sal) FROM emp) avg_sal
from emp;

-- 부분합,그룹별로 묶느게 가능하다.
-- 각 부서별로 급여평균을 확인하고 싶다.
-- 그룹함수는 group by절에 온 필드는 사용가
select deptno, avg(sal)
from emp
group by deptno;

-- 이름과 부서번호 급여 부서별 평균을 확인하고 싶다.
select ename, deptno, 
	(select avg(sal) from emp B where A.deptno=B.deptno)
	dept_sal
from emp A;

-- 서브쿼리와 join 합치기
select ename, A.deptno, dept_sal, sum_sal, max_sal, min_sal
from emp A
left outer join(
	select deptno, avg(sal) dept_sal, sum(sal) sum_sal, 
	max(sal) max_sal, min(sal) min_sal
	from emp
	GROUP by deptno) B
on A.deptno=B.deptno;

use w3schools;

-- orders 테이블에서 고객별 주문 개수구하고 정렬은 주문수가 많은 고객부터 내림차순
-- 고객이름, 주문 카운트

select customerid, count(customerid)
from orders
group by customerid
having count(customerid) >=5
order by count(customerid) desc;

-- 오늘의 과제(0519)
-- 1. 주문이 한번도 없는 고객의 이름을 조회하기
desc customers; -- customerid, custemrName
desc orders; -- customerid, orderid
desc orderdetails; -- orderid, quantity

select c.customerName
from customers c
left join orders o on c.customerid = o.customerid
where o.customerid is null;


-- 2. 주문 건수가 가장 많은 판매자 이름 구하기
select
	concat(e.lastName, " ", e.FirstName) as EmployeeName,
	count(o.orderID) as OrderCount
from employees e
join orders o on o.EmployeeID=e.EmployeeID
group by e.employeeid, employeeName
order by OrderCount DESC
LIMIT 1;


-- 3. 판매건수가 5건 이상인 판매자 인원 수
desc employees; -- EmployeeID
desc orders; -- OrderID
desc orderDetails; -- OrderID, Quantity

SELECT COUNT(*) AS EmployeeCount
FROM (
    -- 여기서 각 판매자별 판매건수를 계산하고 5건 이상인 판매자만 필터링
    SELECT e.employeeID
    FROM employees e
    JOIN orders o ON e.employeeID = o.employeeID -- 적절한 JOIN 조건
    GROUP BY employeeID -- 적절한 그룹화
    HAVING count(orderID) >= 5 -- 적절한 조건
) AS EmployeesWithMoreThan5Sales;
