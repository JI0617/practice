create user 'playdata'@'localhost' identified by '1111';
create user 'playdata'@'%' identified by '1111';


-- 생성된 계정을 확인
select user, host from mysql.user;

-- SQL문 작성 : 한 명령문이 끝나면 ; 으로 종료
-- 실행 : control + enter

-- 계정에 권한을 부여
-- grant 부여할 권한 on 대상 테이블 to 권한부여할 계정
grant all privileges on *.* to playdata@localhost; -- *:DB .*:Table
grant all privileges on *.* to playdata@'%';