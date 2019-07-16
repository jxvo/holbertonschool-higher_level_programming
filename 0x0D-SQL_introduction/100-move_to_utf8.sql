-- converts a database to a UTF8 text file
USE hbtn_0c_0;
ALTER DATABASE CHARACTER SET utf8mb4;
ALTER DATABASE COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
