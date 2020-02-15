-- lathremBot.sql
--
-- This SQL creates the database structure required for the lathremBot.
--
-- Install the mariaDB database server:
--     sudo apt-get install mariadb-server
--
-- Useful links:
--     https://mariadb.com/kb/en/documentation/

-------------------------------------------------------------------------------
---- lathremBot Database ------------------------------------------------------
-------------------------------------------------------------------------------

drop database lathremBot;
drop user lathrem;

create database lathremBot;
create user 'lathrem' identified by 'poros';
grant select, insert, update, delete, execute on lathremBot.* to 'lathrem';

use lathremBot;

-------------------------------------------------------------------------------
---- lathremBot Tables --------------------------------------------------------
-------------------------------------------------------------------------------

create table config (
    configKey varchar(255) not null,
    configValue varchar(255) not null,
    primary key (configKey)
);

create table serverConfig (
    serverId varchar(255) not null,
    configKey varchar(255) not null,
    configValue varchar(255) not null,
    primary key (serverId, configKey)
);

create table memberConfig (
    memberId varchar(255) not null,
    configKey varchar(255) not null,
    configValue varchar(255) not null,
    primary key (memberId, configKey)
);

-------------------------------------------------------------------------------
---- lathremBot Procedures ----------------------------------------------------
-------------------------------------------------------------------------------

delimiter //

-- none yet

delimiter ;

-------------------------------------------------------------------------------
---- lathremBot Triggers ------------------------------------------------------
-------------------------------------------------------------------------------

delimiter //

-- none yet

delimiter ;

-------------------------------------------------------------------------------
---- lathremBot Data  ---------------------------------------------------------
-------------------------------------------------------------------------------

insert into config (configKey, configValue)
values ('token', 'your bot token goes here'),
       ('admin', '274244725848932352'),
       ('prefix', '[]');
