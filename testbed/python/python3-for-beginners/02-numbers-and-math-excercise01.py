#!/usr/bin/env python3
# Numbers and Math - Excercise 01:
#
# Let's assume you are planning to use your Python skills to build a social networking service.
# You decide to host your application on servers running in the cloud. You pick a hosting provider
# that charges $0.51 per hour. You will launch your service using one server and want to know
# how much it will cost to operate per day and per month.
#
# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per month?
#
# Created: 2020-09-06
# Updated: 2020-09-06
# By:      Matthias Koterski

# Object definition
hosting_charge_hourly = 0.51
server_qty = 1

daily_hours = 24
weekly_hours = daily_hours * 7
monthly_hours = daily_hours * 30
annual_hours = daily_hours * 365

opex_day = daily_hours * hosting_charge_hourly
opex_week = weekly_hours * hosting_charge_hourly
opex_month = monthly_hours * hosting_charge_hourly
opex_year = annual_hours * hosting_charge_hourly

print("-" * 30)
print(" The Social Network")
print("-" * 30)
print("Server(s) : {}".format(str(server_qty)))
print("Charge/hour : {}".format(str(hosting_charge_hourly)))
print("=" * 30)
print("OPEX / day : {}".format(str(opex_day)))
print("OPEX / week : {}".format(str(opex_week)))
print("OPEX / month : {}".format(str(opex_month)))
print("OPEX / year : {}".format(str(opex_year)))
print("-" * 30)