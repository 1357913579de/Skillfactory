CREATE
TABLE
ORDERS(
    order_id
INT
AUTO_INCREMENT
NOT
NULL,
time_in
DATETIME
NOT
NULL,
time_out
DATETIME,
cost
FLOAT
NOT
NULL,
pickup
INT
NOT
NULL,

PRIMARY
KEY( order_id )
);