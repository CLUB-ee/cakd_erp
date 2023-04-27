-- DB 선택 
use cakd7_erp;

alter table cakd7_erp.manager AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.manager set manager.manId = @count:=@count+1;

alter table cakd7_erp.menu AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.menu set menu.menuId = @count:=@count+1;

alter table cakd7_erp.material AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.material set material.mateId = @count:=@count+1;

alter table cakd7_erp.recipe AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.recipe set recipe.id = @count:=@count+1;

alter table cakd7_erp.cusOrd AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.cusOrd set cusOrd.cusOrdNum = @count:=@count+1;

alter table cakd7_erp.inStock AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.inStock set inStock.inNum = @count:=@count+1;

alter table cakd7_erp.ord AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.ord set ord.ordNum = @count:=@count+1;

alter table cakd7_erp.outStock AUTO_INCREMENT=1;
set @count=0;
update cakd7_erp.outStock set outStock.outNum  = @count:=@count+1;

-- manager Table
INSERT INTO manager VALUES (null,'중앙정보처리가든','1234','02-313-1711','서울특별시 마포구 신촌로 176 중앙빌','infoprotect@choongang.co.kr',1.2,'105-91-95789');

-- menu Table
INSERT INTO menu VALUES (null,null,'소불고기 덮밥',10000,0,0);
INSERT INTO menu VALUES (null,null,'제육볶음',10000,0,0);
INSERT INTO menu VALUES (null,null,'비빔밥',10000,0,0);
INSERT INTO menu VALUES (null,null,'떡갈비',15000,0,0);
INSERT INTO menu VALUES (null,null,'보쌈',30000,0,0);

-- material Table
INSERT INTO material VALUES (null,'소고기','축산물',null,null,300,0);
INSERT INTO material VALUES (null,'돼지고기','축산물',null,null,170,0);
INSERT INTO material VALUES (null,'양파','농산물',null,null,30,0);
INSERT INTO material VALUES (null,'파','농산물',null,null,50,0);
INSERT INTO material VALUES (null,'버섯','농산물',null,null,40,0);
INSERT INTO material VALUES (null,'당근','농산물',null,null,50,0);
INSERT INTO material VALUES (null,'마늘','농산물',null,null,100,0);
INSERT INTO material VALUES (null,'청양고추','농산물',null,null,170,0);
INSERT INTO material VALUES (null,'애호박','농산물',null,null,80,0);
INSERT INTO material VALUES (null,'계란','축산물',null,null,40,0);
INSERT INTO material VALUES (null,'무','농산물',null,null,30,0);

-- recipe Table
-- 소불고기 덮밥
INSERT INTO recipe VALUES (null,150,1,1);
INSERT INTO recipe VALUES (null,100,3,1);
INSERT INTO recipe VALUES (null,50,4,1);
INSERT INTO recipe VALUES (null,50,5,1);
INSERT INTO recipe VALUES (null,30,6,1);
INSERT INTO recipe VALUES (null,10,7,1);
-- 제육 볶음
INSERT INTO recipe VALUES (null,150,2,2);
INSERT INTO recipe VALUES (null,100,3,2);
INSERT INTO recipe VALUES (null,50,4,2);
INSERT INTO recipe VALUES (null,10,8,2);
INSERT INTO recipe VALUES (null,10,7,2);
-- 비빔밥
INSERT INTO recipe VALUES (null,100,2,3);
INSERT INTO recipe VALUES (null,50,3,3);
INSERT INTO recipe VALUES (null,30,6,3);
INSERT INTO recipe VALUES (null,20,9,3);
INSERT INTO recipe VALUES (null,100,10,3);
-- 떡갈비
INSERT INTO recipe VALUES (null,200,1,4);
INSERT INTO recipe VALUES (null,200,2,4);
INSERT INTO recipe VALUES (null,20,7,4);
INSERT INTO recipe VALUES (null,30,4,4);
INSERT INTO recipe VALUES (null,20,6,4);
-- 보쌈
INSERT INTO recipe VALUES (null,500,2,5);
INSERT INTO recipe VALUES (null,100,3,5);
INSERT INTO recipe VALUES (null,50,4,5);
INSERT INTO recipe VALUES (null,300,11,5);
INSERT INTO recipe VALUES (null,30,7,5);