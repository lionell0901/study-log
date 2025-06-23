use w3schools;
select * from customers;

-- 고객 이름이 Handel 이라는 사람이 있고 이 고객의 주문 내용 확인


select orderID, A.customerID, customername
from customers A
join orders B on A.customerID=B.customerID
where customername like '%Handel%';

desc orderdetails; -- orederID있
desc products;

select A.productid, quantity, productname, A.orderID
from orderdetails A
join products B on A.productID = B.productID
where orderid in (
	select orderID
	from customers A
	join orders B on A.customerID=B.customerID
	where customername like '%Handel%'
	);

-- inner join 의 경우에는 from 절 테이블과 join 절 테이블 구분 필요 없음
-- 데이터 개수가 작은 테이블이 앞쪽에 오는 것이 좀 좋다(권고사항)
-- 조인 - for문, nested loop join -> has join
-- where 조건절이 먼저 실행되서 우선 데이터를 거른 다음에 조인을 한다.

-- left outer join: from절에 가까운 테이블 내용이 다 나오길 원할때
-- right outer join : from절에서 먼 테이블 내용이 다 나오길 원할때
-- cross join

select A.customerID, B.orderID
from Customers A, orders B where 1;

-- selfjoin emp테이블의 mgr 필드가 자기 상사의 사원번호
-- 동일 테이블을 조인한다고 해서 self join -코드테이블 만들떄

use mydb;
show tables;
select * from emp;
select B.ename, B.mgr, C.ename
from emp B
self join emp B on B.mgr=B.empno;

SELECT A.ename AS employee,
       A.mgr AS manager_id,
       B.ename AS manager_name
FROM emp A
JOIN emp B ON A.mgr = B.empno;

-- join이 일반적으로 subquery보다 빠르다.

use w3schools;

-- Employees 테이블에 Lastname이 king임
-- 이사람이 판매한 내역 확인하고자 함
-- 주문번호, 고객이름, 배달업자, 제품명

desc employees; -- EmployeeID, firstName
desc orders; -- EmployeeID, custromerID, orderID, ShipperID
desc shippers; -- shipperID, ShipperName
desc orderDetails; -- orderID, ProductID
desc products; -- productID, ProductName
desc customers; -- customerID, CustomerName

SELECT 
    O.orderID,
    C.CustomerName,
    S.ShipperName,
    P.ProductName
FROM Employees E
JOIN Orders O ON E.EmployeeID = O.EmployeeID
JOIN Customers C ON O.CustomerID = C.CustomerID
JOIN Shippers S ON O.ShipperID = S.ShipperID
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
WHERE E.LastName = 'King';

-- union, union all 단순 합하기, 데이터 텃붙이기
-- union 의 경우 중복을 배제한다.
-- union all은 중복을 배제하지 않는다.
/*
 select column1, column2 from table1
 union all
 select column1, column2 from table2
필드 개수와 타입만 맞으면 된다.
행 => 열로 바꿔야할때 주로 사용
포털, 국가 기관 검색어로 검새하면 각 테이블로부터 검색한 내용을 전부
union해서 갖고 온다.
 */

use w3schools;
select empno, ename from emp
union all
select deptno, dname from dept;


-- count명에 null값이 있으면 출력하지 않는다. w3shcools 예제문제
select count(*)
from customer;

select country, count(*)
from customers
group by country
order by count(*) DESC;

-- 배달업체별로 주문개수
select shippername, count(*)
from orders A
join shippers B on A.shipperid=B.shipperid
group by shippername;

-- 주문번호, 배달업체, 배달업체 카운트
select orderid, shippername, count(*)
from orders A
join shippers B on A.shipperid=B.shipperid
group by shippername;

-- 주문번호, 배송업체번호, 카운트
select orderid
from orders A
inner join()


-- exists의 장점: 서브쿼리의 모든 수행을기다리지 않고
-- 뭔가 하나 찾으면 바로 끝
-- 서브쿼리의 수행 결과셋 존재유무만 파악

-- Any: 서브쿼리에서 오는 조건보다 하나라도 만족하는 항목이 있을 경우
--	   부등호 or 부등호 or 부등

SELECT SupplierName
FROM Suppliers
WHERE EXISTS (
	SELECT ProductName FROM Products
	WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20
);

-- 프로그래밍 언어 mysql script 가 있어서 함수도 프로시저도
-- 만들 수 있다. mysql 만들었던 언어가 함수와 프로시저
-- 함수는 반드시 반환값이 있다. 프로시저는 반환값이 없다.
-- mysql의 내장함수
-- 대부분의 dbms들은 select절은 from절 못빠짐
-- 오라클 같은 경우에는 dummy table이 있다. 가짜
-- select sysdata from dummy;

select now();

select now() from customers; -- customer 테이블 데이터 개수만큼

select * from customers
where customername like '%Around%';

select concat("tom ", "is", " a student") as sentence;
select concat(address, "-", postalcode, "-", city) address
from customers;

select ltrim("      hello      "), "***";
select rtrim("      hello      "), "***";
-- 대부분의 dbms가 문자열 인덱스를 0부터 시작하는데, sql은 1
select substr("Hello mysql", 7, 5);
select substr("2025-05-20",1,4) year,
	   substr("2025-05-20",6,2) month,
  	   substr("2025-05-20",9,2) day;

-- cell: 올림함수, 데이터개수가 231기->페이지 23.1
-- floor : 내림함
-- interval간격
select adddate("2018-07-23", interval 10 DAY);
select adddate("2025-12-27", interval 10 DAY);
select datediff("2016-08-25", "2018-06-29");

use mydb;
desc dept;
select * from dept;

-- 테이블구조가 간단한 경우에 필드명을 생략할 수 있다.
-- desc에 나온 필드 목록과 동일한 구조로 넣어야한다.(detpno, dname, loc)
insert into dept values(50, '개발1부', '서울');
insert into dept values(60, '개발2부', '부산');

insert into dept(deptno, dname) values(70, '개발3부');



insert into emp(empno) values(9000);
-- 규칙에 위배되는 데이터는 삭제해야 워크밴치에서 NOT NULL 설정 가능!
insert into emp(empno, ename, sal)
values(10000, '홍길동',3300);

delete from emp where sal is null;
-- null값 가지고 있는 데이터 삭제
delete from emp where mgr is null;

select * from emp;

-- 한번에 여러명 넣기
insert into emp(empno, ename, sal)
values(8500, '홍길순', 3200),
	  (8503, '홍길순', 3300),
	  (8505, '도우너', 3400);

-- 데이터에 ' 가 들어가야 할때 ==> ''
-- 'Tom''s family'
-- 'Jane' ==> '''Jane'''

insert into emp(empno, ename, sal)
values(8120, '''Jane''', 3200);

-- 서버와 클라이언트의 차이 정리

구분        서버                              클라이언트
---------------------------------------------------------------
역할        -- 요청을 받아 처리하고 응답을 보냄       -- 요청을 보내고 응답을 기다림
예시        -- 웹 서버, DB 서버, 파일 서버 등        -- 브라우저, DBeaver, 이메일 앱, 스마트폰 등
상태        -- 항상 켜져 있으며 대기 상태            -- 사용자가 필요할 때 실행됨
방향        -- 서비스를 제공하는 쪽                  -- 서비스를 받는 쪽 (사용자)
기능 위치    -- 백엔드(Back-end) 중심                 -- 프론트엔드(Front-end) 또는 사용자 단
상호작용    -- 클라이언트의 요청에 따라 응답 처리     -- 서버에 요청을 보내고 응답을 표시

-- 테이블을 만들기, 테이블 복사 명령어가 없음
-- create table 테이블명 (컬럼1 타입,컬럼2 타입 )
create table emp2 as select * from emp;
select * from emp2;
-- 서브쿼리를 써서 테이블을 복사할 수 있다.
-- primary, foreign key는 데려오지 않
desc emp2;
-- 구조만 복사하기(1=0은 맞지 않는)
create table emp3 as select * from emp where 1=0;
desc emp3;
select * from emp3;
-- 부분 구조 복사
create table emp4 as
select empno, ename, sal
from emp where deptno in (10,20);

desc emp4;
select * from emp4;

insert into emp3 (empno, ename, job, sal)
select empno, ename, sal
from emp;

use w3schools;
select * from customers;
-- 문제 1. customers 테이블의 구조를 복사한 후 customers2
-- 만들고 고객 아이디중에 3,23,21,45,67,89, 54 복사하기
create table customers2 as select * from customers where 1=0;
desc customers2;
select * from customers2;

insert into customers2 (CustomerID)
select customerID
from customers where CustomerID in(3,23,21,45,67,89,54);

DROP TABLE customers2;

create table customers2 as
select CustomerID from customers
where CustomerId in(3,23,21,45,67,89,54);

select * from customers2;

drop table customers2;

create table customers2 as
select customers (CustomerID) from customers
where CustomerId in(3,23,21,45,67,89,54);

-- 문제 2 고객 아이디중에 4,5,11,33,42,43,56,57,58을 이동하기
-- customers -> customers2로 이동하기

create table customers2
select *
from customers
where customerId in (4,5,11,33,42,43,56,57,58);


select * from customers2;

-- 문제3. 제품 가격이 100$를 넘는 제품을 구매한 고객 리스트
desc customers; -- customerID, customerName
desc orders; -- customerID, OrderID
desc orderDetails; -- OrderID, ProductID
desc products; -- productID, productname, price

select O.orderID,
	   C.customerName,
	   p.price
from customers C
join orders O on C.CustomerId = O.customerId
join orderDetails OD on O.orderid = OD.orderid
join products P on OD.productID = p.productID
where P.price > 100;

-- 문제4. orderdetails 테이블의 quantity가 제품을 구매한 수량이고
-- product테이블의 있는 price가 단가이다. 구매한 고객이름과 제품명 제품전체가액을 구하시오.
-- 예시) 홍길동 가구 quantity와 price가 곱해져야 한다.
-- 집가서 풀어보기

-- 문제5. 핀란드에 있는 공급자 리스트 가져오기(finland)
-- distinct 뒤에 나오는 필드값을 중복을 배제하는 명령
select distinct country, suppliername from suppliers;

select suppliername from suppliers where country='Finland';

-- 문제6. 카테고리 제품이 seafood인 제품의 구매자 리스트를 조회하시오.
from orders A
inner join orderdetails B 
-- 이거 한번 풀어보

-- --------오늘의 과제
select distinct country from customers;

-- 1. customers 테이블에서 나라가 Germany인 나라의 정보 전체
select * from customers where country = 'Germany';
-- 2. customers 테이블에서 나라가 Austria, USA, Poland, Denmark에 
-- 	사는 고객리스트
select * from customers;
select * from customers where country in('Austria', 'USA', 'Poland', 'Denmark');

-- 3. 각자 나라별로 고객이 몇명씩 있는지 확인
select * from customers limit 10;
select country, count(*) as Customer_count
from customers
group by country
order by customer_count desc;
-- 4. 나라별로 고객이 5명 이상인 나라 목록만 조회
select country, count(*) as Customer_count
from customers
group by Country
having customer_count >= 5
order by customer_count DESC;
5. 나라 이름이 B로 시작하는 나라들의 고객 전체 합
6. 나라는 UK 도시명은 London에 있는 고객들 이름 목록
7. 주문날짜가 '1996-07-01'~'1996-09-30' 까지 주문아이디와
	고객이름
8. 위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하
9. 배달자가 Federal Shipping 인 경우의 상푸명 가격 수량
