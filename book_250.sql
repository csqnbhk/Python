CREATE TABLE `book_250` (
  `name` varchar(40) NOT NULL COMMENT '书名',
  `grade` varchar(10) NOT NULL COMMENT '评分',
  `person` varchar(10) NOT NULL COMMENT '评价人数',
  `book_250_pk` int(4) NOT NULL AUTO_INCREMENT COMMENT '主键，自增',
  PRIMARY KEY (`book_250_pk`)
) ENGINE=InnoDB AUTO_INCREMENT=251 DEFAULT CHARSET=utf8 COMMENT='保存豆瓣的推荐书';
