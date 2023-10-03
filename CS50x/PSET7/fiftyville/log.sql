-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Checking the events on the given date and street
SELECT
  description
FROM
  crime_scene_reports
WHERE
  YEAR = 2021
  AND MONTH = 7
  AND DAY = 28
  AND street = 'Humphrey Street';

-- Checking the interviews with people
SELECT
  name,
  transcript
FROM
  interviews
WHERE
  YEAR = 2021
  AND MONTH = 7
  AND DAY = 28;

--We found two transcripts with name 'Eugene' , So lets check how many Eugene do we have
SELECT
  name
FROM
  people
WHERE
  name = 'Eugene'
  -- Found out we have one Eugene
  -- So lets find out the name of three witnesses that hvae talken about 'bakery' on July 28, 2021
  --and also sort it by a-z
SELECT
  name,
  transcript
FROM
  interviews
WHERE
  YEAR = 2021
  AND MONTH = 7
  AND DAY = 28
  AND transcript LIKE '%bakery%'
ORDER BY
  name;

-- Witnesses are Eugene , Raymond , and Ruth.
--Find the people that have withdraw transaction on Leggett Street
SELECT
  account_number,
  amount
FROM
  atm_transactions
WHERE
  YEAR = 2021
  AND MONTH = 7
  AND DAY = 28
  AND atm_location = 'Legget Street'
  AND transaction_type = 'withdraw';

--