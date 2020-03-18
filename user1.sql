/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : user1

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2020-03-18 21:31:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `students`
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` bigint(30) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `heat` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `at_school` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `huobei` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `wuhan` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `at_huobei` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `at_wuhan` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `meet_disease_area_people` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `arrive_school` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `arrive_school_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=201771030116 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('201771030100', '李一', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '2020-03-16 12:26:52');
INSERT INTO `students` VALUES ('201771030101', '王二', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'Y', 'N', '2020-03-03 12:52:55');
INSERT INTO `students` VALUES ('201771030105', '张三', 'Y', 'N', 'Y', 'N', 'N', 'N', 'Y', 'N', '2020-03-03 12:52:59');
INSERT INTO `students` VALUES ('201771030106', '王五', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '2020-03-03 12:27:45');
INSERT INTO `students` VALUES ('201771030107', '刘正', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '2020-03-16 12:29:15');
INSERT INTO `students` VALUES ('201771030108', '李四', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '2020-03-03 12:27:12');
INSERT INTO `students` VALUES ('201771030109', '何欢', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '2020-03-03 12:29:32');
INSERT INTO `students` VALUES ('201771030110', '赵四', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'Y', 'N', '2020-03-03 12:53:03');
INSERT INTO `students` VALUES ('201771030115', '李一', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '2020-03-16 16:20:55');

-- ----------------------------
-- Table structure for `students table`
-- ----------------------------
DROP TABLE IF EXISTS `students table`;
CREATE TABLE `students table` (
  `id` bigint(30) NOT NULL,
  `name` char(10) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of students table
-- ----------------------------
INSERT INTO `students table` VALUES ('201771030100', 'ST001');

-- ----------------------------
-- Table structure for `students_t`
-- ----------------------------
DROP TABLE IF EXISTS `students_t`;
CREATE TABLE `students_t` (
  `id` bigint(30) NOT NULL,
  `name` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `heat` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `at_school` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `huobei` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `wuhan` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `at_huobei` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `at_wuhan` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `meet_disease_area_people` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `arrive_school` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'N',
  `arrive_school_time` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of students_t
-- ----------------------------
