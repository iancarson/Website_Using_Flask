create table UserAcc.accounts
(
    id             int auto_increment
        primary key,
    account_number varchar(12)                 not null,
    user_id        int                         not null,
    balance        decimal(10, 2) default 0.00 null,
    account_type   varchar(10)                 not null,
    created        datetime                    not null,
    modified       datetime                    not null,
    constraint account_number
        unique (account_number)
);

