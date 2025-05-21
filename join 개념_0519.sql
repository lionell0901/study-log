use mydb;

-- emp 테이블의 정보를 확인하고 primary key가 존재하면삭제하려고 한다.

DESC emp; -- empno가 primary인지 확인

-- Primary Key 삭제 (올바른 구문으로 수정)
ALTER TABLE emp DROP PRIMARY KEY;

-- 중복 데이터 입력 테스트
INSERT INTO emp(empno, ename) VALUES(8000, '장길산');
INSERT INTO emp(empno, ename) VALUES(8000, '장길산');

-- 테이블 확인
SELECT * FROM emp;

-- 중복 데이터 삭제
DELETE FROM emp WHERE empno = 8000 LIMIT 2;

-- Primary Key 다시 설정
ALTER TABLE emp ADD CONSTRAINT pk_empno PRIMARY KEY(empno);

-- 결과 확인
DESC emp;

-- foreign key(외부키)
desc dept;
/*
alter TABLE 테이블
add constraint 외부키이
foreign key(필드명)
references 참조테이블명(참조필드명)
on delecte cascade 부모레코트 삭제시 자신도 삭
on update cascade 부모키값 변경시 자식도 자동으로 변
*/

-- 1. 참조하는 테이블(dept)의 deptno가 반드시 primary거나 unique조건을 만족해야한다.
-- 2. 데이터 타입이 동일해야한다.

alter table emp add constraint fk_emp_dept
foreign key(deptno)
references dept(deptno); -- 테이블 상호간 제약조건이 발생한다.
select * from dept;
show index from emp; -- 외래키 확인
delete from dept where deptno=10; -- 외래키때문에 삭제 불가
select * from emp;
-- 홍길동한테 부서번호가 없다.
update emp set deptno=50 where empno=8000;


-- join은 inner, outer, full - ansi 표준
-- emp 테이블에는 부서번호
-- dept 테이블에는 부서번호와 부서명
-- 두개 이상의 테이블을 하나로 묶어서 새로운 정보를 창출한다
-- 아래는 표준 아니라 다른 DBMS에서 에러 날 수 있
select A.empno, A.ename,A.deptno, B.dname
from emp A, emp B
where A.deptno=B.deptno; -- join 조건이 동등조건(equl조)

-- 표준조
select A.empno, A.ename,A.deptno, B.dname
from emp A
inner join dept B on A.deptno = B.deptno;

-- 회원번호가 7369, 7892, 8000 등
select A.empno, A.ename,A.deptno, B.dname
from emp A, emp B
where A.deptno=B.deptno and
A.empno in(7369,7892, 8000)

-- 단점 : 조인 조건과 검색 조건이 구분이 안간다.그래서 조인이 여러번
-- 이뤄질 경우에 보기 안좋다.

select A.empno, A.ename,A.deptno, B.dname
from emp A
right join dept B on A.deptno = B.deptno;

-- 중복성 배
select distinct deptno from emp;