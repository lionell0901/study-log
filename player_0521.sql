use mydb2;
show tables;
/*
player
schedule
stadium
team
*/

select * from team; -- 팀이 15개 있다.

-- 1. team_id = K01 인 선수들의 명단 확인
select * from player where team_id='k01';
-- 2. K01팀 선수 중, 백번호 → 입단연도 → 이름 순으로 정렬
SELECT player_name, join_yyyy, posit
FROM PLAYER
WHERE team_id = 'K01'
ORDER BY back_no ASC, join_yyyy ASC, player_name ASC;

-- 3. 고객이 null값 선수 3명을 따로 처리하기를 원한다면?
select player_name, join_yyyy, posit
from PLAYER p 
where TEAM_ID = 'K01' and JOIN_YYYY is NULL 
UNION all
select player_name, join_yyyy, posit
from PLAYER p 
where TEAM_ID = 'K01' and JOIN_YYYY is not null
order by JOIN_YYYY, player_name;

-- 울산지역에 있는 모든 팀과 각 팀에 속한 선수이름과 우편번호 주소를 출력하자
-- join
select * from team;
-- 필요한 것은 team_id, player_name, Zip_code1+Zip_code2
-- Team_id 가 조인필드로 엮인다.

select B.TEAM_NAME, A.PLAYER_NAME , B.REGION_NAME,
	   concat(B.ZIP_CODE1,"-",B.zip_code2) zipncode,
	   B.ADDRESS
from player A
inner join team B on A.team_id=B.team_id
where region_name='울산';

-- team_id 가 K01 이거나 K03인 선수의 팀이름 팀주소, 선수이름
select B.TEAM_NAME, A.PLAYER_NAME , B.ADDRESS
from player A
inner join team B on A.team_id=B.team_id
where A.TEAM_ID in('K01','K03');

-- 서브쿼리
-- select 절에서 사용하는 서브쿼리는 스칼라 서브쿼리만 된다.
-- 스칼라 -> 쿼리 실행결과가 달랑 값 하나
-- select count(*) from team;
select A.player_name
from player A
where A.team_id in('K01','K03');
-- 서브쿼리로 2개를 합친다.
select team_name from team where team_id in ('k01','k03')

-- player이름, 팀이름, 경기장 이름 K05, K07, K12 구단
-- 팀이름으로 정렬, 백넘버로 정렬

select A.PLAYER_NAME, B.TEAM_NAME,C.STADIUM_NAME
from PLAYER A
join team B on A.team_id=B.team_id
join STADIUM C on B.STADIUM_ID =C.STADIUM_ID
where A.TEAM_ID in('K05','K07','K12')
ORDER BY B.TEAM_NAME, A.BACK_NO;