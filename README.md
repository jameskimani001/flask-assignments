# flask-assignments
# Python Solutions to Algorithmic Problems

This repository contains Python solutions to several algorithmic problems, each designed to solve a unique problem with varying requirements and constraints.

## Table of Contents
1. [Email Generation](#email-generation)
2. [Palindrome Creation](#palindrome-creation)
3. [Longest Sentence](#longest-sentence)
4. [Asphalt Patches](#asphalt-patches)
5. [Different Letters Concatenation](#different-letters-concatenation)

---

## 1. Email Generation

### Problem

You are tasked with generating email addresses for employees based on their names. The email addresses are to be formatted as `FirstMiddleLast@Company.com`, with the option to add numbers to resolve duplicates. Each part of the name is used in the address, with the first name and middle name (if any) abbreviated to their initials, and the last name truncated to at most 8 characters.

The function processes a list of names and ensures the generated emails are unique by adding numeric suffixes to any duplicates.

---

## 2. Palindrome Creation

### Problem

Given a string `S` that contains lowercase letters and question marks (`?`), the task is to replace the question marks with lowercase letters to form a palindrome, if possible. If it's not possible to create a palindrome (because of conflicting characters), the function should return `"NO"`.

A palindrome is a word that reads the same forwards and backwards. The solution checks if it's feasible to replace the question marks to form a valid palindrome.

---

## 3. Longest Sentence

### Problem

Given a string `S` containing multiple sentences, which are separated by punctuation marks like periods (`.`), question marks (`?`), or exclamation marks (`!`), the task is to find the sentence with the maximum number of words.

Each sentence is split into words, and the function counts the number of words in each sentence. The function then returns the maximum number of words found in any sentence.

---

## 4. Asphalt Patches

### Problem

A road is represented by a string of segments, where each segment can either contain a pothole (`X`) or be in good condition (`.`). The task is to calculate the minimum number of patches required to cover all the potholes, where each patch can cover exactly three consecutive segments.

The solution iterates through the string, placing patches to cover potholes while ensuring that the patches cover three consecutive segments at once. It calculates and returns the minimum number of patches required.

---

## 5. Different Letters Concatenation

### Problem

Given an array of strings, the task is to calculate the length of the longest string that can be formed by concatenating some of the strings such that all the letters in the resulting string are unique.

The function first filters out any strings that contain duplicate letters. Then it checks all possible combinations of the strings and determines the longest combination that contains no duplicate letters.

---

## Installation

To run these solutions, you need Python installed on your machine.

1. Install Python from [python.org](https://www.python.org/downloads/) if it's not already installed.
2. Clone or download this repository to your local machine.

### Usage

1. Open a terminal or command prompt.
2. Navigate to the folder where the Python file is located:
   ```bash
   cd /path/to/your/folder
Run any Python file using Python 3:
bash
Copy
python3 <filename>.py
For example, to run the Email Generation solution:

bash
Copy
python3 email_generation.py
Example:
For Palindrome Creation, create a Python file (e.g., palindrome.py) and run:
bash
Copy
python3 palindrome.py
