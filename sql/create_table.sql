create table `user_barrage` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `room` VARCHAR (16) NOT NULL DEFAULT '' COMMENT '房间号',
    `user_name` varchar(64) NOT NULL DEFAULT '' COMMENT '用户昵称',
    `barrage_content` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '弹幕内容',
    `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
    `expired` tinyint(4) DEFAULT '0' COMMENT '删除标志0 正常 1删除',
    PRIMARY KEY (`id`),
    KEY `idx_room_create_time` (`room`, `create_time`)
) ENGINE=InnoDB COMMENT='用户弹幕表';