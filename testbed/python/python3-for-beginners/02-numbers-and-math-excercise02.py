#!/usr/bin/env python3
# Numbers and Math - Excercise 02:
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
# Building on the previous example, let's also assume that you have saved $918 to fund your new
# adventure. You wonder how many days you can keep one server running before your money
# runs out. Of course, you hope your social network becomes popular and requires 20 servers to
# keep up with the demand. How much will it cost to operate at that point?
# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per month?
# How much does it cost to operate twenty servers per day?
# How much does it cost to operate twenty servers per month?
# How many days can I operate one server with $918?
#
# Created: 2020-09-06
# Updated: 2020-09-06
# By:      Matthias Koterski

# Object definition
hosting_charge_hourly = 0.51

daily_hours = 24
weekly_hours = daily_hours * 7
monthly_hours = daily_hours * 30
annual_hours = daily_hours * 365

opex_day = daily_hours * hosting_charge_hourly
opex_week = weekly_hours * hosting_charge_hourly
opex_month = monthly_hours * hosting_charge_hourly
opex_year = annual_hours * hosting_charge_hourly

runtime = 918 % opex_day

print("-" * 70)
print("\n{0:^70}\n".format("The Sillycube Network"))
print("-" * 70)
# print("OPEX - 1 server / day : {}".format(str(opex_day)))
# print("OPEX - 1 server / week : {}".format(str(opex_week)))
# print("OPEX - 1 server / month : {}".format(str(opex_month)))
# print("OPEX - 1 server / year : {}".format(str(opex_year)))
# print("-" * 30)
# print("OPEX - 1 server / day : {}".format(str(opex_day)))
# print("OPEX - 1 server / week : {}".format(str(opex_week)))
# print("OPEX - 1 server / month : {}".format(str(opex_month)))
# print("OPEX - 1 server / year : {}".format(str(opex_year)))
# print("-" * 30)

print("{0:^9} | {1:^9} | {2:^9} | {3:^9} | {4:^9} | {5:^9}".format("server", "hourly", "daily", "weekly", "monthly", "annual"))
print("{0:^9} | {1:^9} | {1:^9} | {1:^9} | {1:^9} | {1:^9}".format("qty", "costs"))
print("=" * 70)
print("{0:>9} | {1:>9.2} | {2:>9.2} | {3:>9.2} | {4:^9.2} | {5:^9.2}".format("1", hosting_charge_hourly, opex_day, opex_week, opex_month, opex_year))
print("{0:>9} | {1:>9.2} | {1:>9.2} | {1:>9.2} | {1:^9.2} | {1:^9.2}".format("20", hosting_charge_hourly * 20, opex_day * 20, opex_week * 20, opex_month * 20, opex_year * 20))
print("-" * 70)
print("\nOne server can be run with EUR 981.00 for {.0} days.".format(runtime))

# print("{0:9} | {1:<8.2}".format("Apples", 0.87123))
# print("{0:9} | {1:<8.2}".format("Oranges", 1))



# OPEX 

# Server | hourly  | etc.
# qty    | costs   |
# ----------------------------------
#      1 |    0.51 |
#     20 |   10.20 |

# One server can be operated with EUR 981 for X months

# Output
# ------------------------------
#  The Social Network
# ------------------------------
# Server(s) : 1
# Charge/hour : 0.51
# ==============================
# OPEX / day : 12.24
# OPEX / week : 85.68
# OPEX / month : 367.2
# OPEX / year : 4467.6
# ------------------------------