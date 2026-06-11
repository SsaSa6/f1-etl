CREATE DATABASE IF NOT EXISTS f1;
USE f1;

CREATE TABLE `f1_2025_drivers` (
  `meeting_key` int,
  `session_key` int,
  `driver_number` int,
  `broadcast_name` varchar(30),
  `full_name` varchar(30),
  `name_acronym` varchar(30),
  `team_name` varchar(30),
  `team_colour` varchar(30),
  `first_name` varchar(30),
  `last_name` varchar(30),
  `headshot_url` varchar(300),
  `country_code` varchar(100),
  PRIMARY KEY (`session_key`, `driver_number`)
);

CREATE TABLE `f1_2025_sessions` (
  `session_key` int PRIMARY KEY,
  `session_type` varchar(30),
  `session_name` varchar(30),
  `date_start` datetime,
  `date_end` datetime,
  `meeting_key` int,
  `circuit_key` int,
  `circuit_short_name` varchar(30),
  `country_key` int,
  `country_code` varchar(30),
  `country_name` varchar(30),
  `location` varchar(30),
  `gmt_offset` varchar(30),
  `year` int,
  `is_cancelled` boolean
);

CREATE TABLE `f1_2025_meetings` (
  `meeting_key` int PRIMARY KEY,
  `meeting_name` varchar(100),
  `meeting_official_name` varchar(100),
  `location` varchar(30),
  `country_key` int,
  `country_code` varchar(30),
  `country_name` varchar(30),
  `country_flag` varchar(200),
  `circuit_key` int,
  `circuit_short_name` varchar(30),
  `circuit_type` varchar(30),
  `circuit_info_url` varchar(200),
  `circuit_image` varchar(200),
  `gmt_offset` varchar(30),
  `date_start` datetime,
  `date_end` datetime,
  `year` int,
  `is_cancelled` boolean
);

CREATE TABLE `f1_2025_laps` (
  `meeting_key` int,
  `session_key` int,
  `driver_number` int,
  `lap_number` int,
  `date_start` datetime,
  `duration_sector_1` float,
  `duration_sector_2` float,
  `duration_sector_3` float,
  `i1_speed` int,
  `i2_speed` int,
  `is_pit_out_lap` bool,
  `lap_duration` float,
  `st_speed` float,
  PRIMARY KEY (`session_key`, `driver_number`, `lap_number`)
);

CREATE TABLE `f1_2025_session_result` (
  `position` int,
  `driver_number` int,
  `number_of_laps` int,
  `dnf` bool,
  `dns` bool,
  `dsq` bool,
  `duration` float,
  `gap_to_leader` float,
  `meeting_key` int,
  `session_key` int,
  PRIMARY KEY (`driver_number`, `session_key`)
);

CREATE TABLE `f1_2025_pit` (
  `date` datetime,
  `session_key` int,
  `lane_duration` float,
  `driver_number` int,
  `meeting_key` int,
  `lap_number` int,
  `stop_duration` float,
  PRIMARY KEY (`date`, `session_key`, `driver_number`, `lap_number`)
);

CREATE TABLE `f1_2025_championship_teams` (
  `meeting_key` int,
  `session_key` int,
  `team_name` varchar(30),
  `position_start` int,
  `position_current` int,
  `points_start` int,
  `points_current` int,
  PRIMARY KEY (`session_key`, `team_name`)
);

CREATE TABLE `f1_2025_championship_drivers` (
  `meeting_key` int,
  `session_key` int,
  `driver_number` int,
  `position_start` int,
  `position_current` int,
  `points_start` int,
  `points_current` int,
  PRIMARY KEY (`session_key`, `driver_number`)
);

CREATE TABLE `f1_2025_starting_grid` (
  `position` int,
  `driver_number` int,
  `lap_duration` float,
  `meeting_key` int,
  `session_key` int,
  PRIMARY KEY (`driver_number`, `session_key`)
);

CREATE TABLE `f1_2025_stints` (
  `meeting_key` int,
  `session_key` int,
  `stint_number` int,
  `driver_number` int,
  `lap_start` int,
  `lap_end` int,
  `compound` varchar(30),
  `tyre_age_at_start` int,
  PRIMARY KEY (`session_key`, `stint_number`, `driver_number`)
);

ALTER TABLE `f1_2025_drivers` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_drivers` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_sessions` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_laps` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_laps` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_session_result` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_session_result` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_pit` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_pit` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_championship_teams` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_championship_drivers` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_stints` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_starting_grid` ADD FOREIGN KEY (`session_key`) REFERENCES `f1_2025_sessions` (`session_key`);

ALTER TABLE `f1_2025_starting_grid` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_stints` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_championship_teams` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);

ALTER TABLE `f1_2025_championship_drivers` ADD FOREIGN KEY (`meeting_key`) REFERENCES `f1_2025_meetings` (`meeting_key`);