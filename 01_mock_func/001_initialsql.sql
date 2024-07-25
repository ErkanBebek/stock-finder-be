-- users tablosu
CREATE TABLE users (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    password VARCHAR(14) NOT NULL,
    role VARCHAR(10) NOT NULL,
    email VARCHAR(20) NOT NULL,
    phone VARCHAR(20),
    hash VARCHAR(255)
);

-- us_stock tablosu
CREATE TABLE us_stock (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(20) NOT NULL
);

-- tr_stock tablosu
CREATE TABLE tr_stock (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(20) NOT NULL
);

-- global_coins tablosu
CREATE TABLE global_coins (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(20) NOT NULL
);

-- tr_stock_fundamentals tablosu
CREATE TABLE tr_stock_fundamentals (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    stock_name VARCHAR(100) NOT NULL,
    last_price DOUBLE,
    profit_change DOUBLE,
    last_period_profit DOUBLE,
    last_year_profit DOUBLE,
    last_period TEXT,
    ev_ebitda DOUBLE,
    sector_ev_ebitda_average DOUBLE,
    ev_sales DOUBLE,
    sector_ev_sales_average DOUBLE,
    pe_ratio DOUBLE,
    sector_pe_ratio_average DOUBLE,
    pbv_ratio DOUBLE,
    sector_pbv_ratio_average DOUBLE,
    sector TEXT
);


-- us_stock_fundamentals tablosu
CREATE TABLE us_stock_fundamentals (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    stock_name VARCHAR(100) NOT NULL,
    last_price DOUBLE,
    profit_change DOUBLE,
    last_period_profit DOUBLE,
    last_year_profit DOUBLE,
    last_period TEXT,
    ev_ebitda DOUBLE,
    sector_ev_ebitda_average DOUBLE,
    ev_sales DOUBLE,
    sector_ev_sales_average DOUBLE,
    pe_ratio DOUBLE,
    sector_pe_ratio_average DOUBLE,
    pbv_ratio DOUBLE,
    sector_pbv_ratio_average DOUBLE,
    sector TEXT
);

-- comments tablosu
CREATE TABLE comments (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    stock_id INT NOT NULL,
    stock_locale INT NOT NULL,
    user_id INT NOT NULL,
    comment TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME
);

-- contact_message tablosu
CREATE TABLE contact_message (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    reciever_id INT NOT NULL,
    message TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME
);

-- user_stock_entry tablosu
CREATE TABLE user_stock_entry (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    stock_id INT NOT NULL,
    stock_locale VARCHAR(255) NOT NULL,
    snapshot_price DOUBLE,
    sold_price DOUBLE,
    buy_date DATETIME,
    sell_date DATETIME
);

CREATE TABLE watch_list (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    stock_id INT NOT NULL,
    stock_locale VARCHAR(255) NOT NULL,
    watched_price DECIMAL(10, 2) NOT NULL,
    watch_date DATETIME NOT NULL
);

CREATE TABLE basket (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    stock_id INT NOT NULL,
    stock_locale VARCHAR(255) NOT NULL,
    taken_price DECIMAL(10, 2) NOT NULL,
    taken_date DATETIME NOT NULL,
    sold_date DATETIME NOT NULL,
    sold_price DECIMAL(10, 2) NOT NULL
    );