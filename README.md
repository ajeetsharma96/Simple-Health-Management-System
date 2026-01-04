#  Health Management System (Python)

A simple Health Management System built using Python, designed to practice core Python concepts like file handling, dictionaries, functions, and conditional logic — without using OOP or external libraries.

# Project Overview

This project allows users to store and retrieve health-related data (Food & Exercise) for multiple people.
Each user has separate files for food intake and exercise activities, and every entry is stored with a timestamp.

The project is intentionally kept simple and beginner-friendly.

# Features

 1.Stores data in text files
 2.Supports multiple users
 3.Tracks Food intake
 4.Tracks Exercise activities
 5.Automatically records date & time
 6.Retrieve previously stored data
 7.Handles missing files gracefully

# Concepts Used

1.Python File Handling (open, read, write)

2.Dictionaries for data mapping and control flow

3.Functions

4.Conditional statements

5.datetime module for timestamps

6.os.path.exists() for file existence check

❌ No Object-Oriented Programming
❌ No external libraries
❌ No advanced frameworks

# File Structure
healthManagementSystem.py
ajeet_food.txt
ajeet_exercise.txt
rahul_food.txt
rahul_exercise.txt
akash_food.txt
akash_exercise.txt
rudra_food.txt
rudra_exercise.txt
rakesh_food.txt
rakesh_exercise.txt


(Files are created automatically when data is stored.)

# How the Program Works

User selects:

Store data

Retrieve data

User chooses a profile

User selects category:

Food

Exercise

Program performs the selected operation using dictionary-driven logic

# Sample Output
----------HEALTH MANAGEMENT SYSTEM----------
1. Store the data
2. Retrieve the data

Enter your choice: 1
Enter the Profile: Ajeet
Enter the categories: 1
Good! What did you eat ? Rice and vegetables
Data stored into your Profile successfully!

# Why This Project?

This project was created to:

Strengthen understanding of basic Python

Learn real-world file handling

Practice clean logic without OOP

Build confidence in structuring Python programs
