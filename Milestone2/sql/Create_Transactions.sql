create table UserAcc.Transactions
(
    id               int auto_increment
        primary key,
    account_src      int            not null,
    account_dest     int            not null,
    balance_change   decimal(10, 2) not null,
    transaction_type varchar(255)   not null,
    memo             varchar(255)   null,
    expected_total   decimal(10, 2) not null,
    created          datetime       not null,
    modified         datetime       null
);

