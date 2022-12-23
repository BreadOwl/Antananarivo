create database devopsroles;
use devopsroles;

CREATE TABLE test_table (
  book VARCHAR(20),
  author VARCHAR(20)
);

INSERT INTO test_table
  (book, author)
VALUES
  ('DevOps', 'Name1'),
  ('Dev', 'Name2');
