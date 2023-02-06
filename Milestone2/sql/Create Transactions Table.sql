CREATE TABLE Transactions (
    id INT NOT NULL AUTO_INCREMENT,
    account_src INT NOT NULL,
    account_dest INT NOT NULL,
    balance_change DECIMAL(10,2) NOT NULL,
    transaction_type VARCHAR(255) NOT NULL,
    memo VARCHAR(255),
    expected_total DECIMAL(10,2) NOT NULL,
    created DATETIME NOT NULL,
    modified DATETIME,
    PRIMARY KEY (id)
);