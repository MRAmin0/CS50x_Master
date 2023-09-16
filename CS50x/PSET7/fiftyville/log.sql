-- Keep a log of any SQL queries you execute as you solve the mystery.

-- checking the events on the given date and street
select description
from crime_scene_reports
where year = 2021
and month = 7
and day = 28
and street = 'Humphrey Street'