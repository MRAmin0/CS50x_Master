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

-- 