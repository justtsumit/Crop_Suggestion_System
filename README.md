# CROP SUGGESTION SYSTEM

# Project Overview
This is a simple Python-based project that recommends suitable crops based on:
- Soil type  
- Season (Kharif / Rabi / Zaid)
- budget 

# Problem Statement
Farmers often get confused about which crop to grow in which season for their specific soil type and budget 
Wrong crop selection can reduce productivity and increase cost.

This project provides a simple solution and information that suggests crops based on soil and season and accordig to their budget

# Objectives
- To identify the best crops for a given soil type and season and budget
- To create a simple Python program using conditional logic.
- To make an easy-to-use recommendation system for basic agricultural planning.


# Top-Down Design

1. Main Function
	.	Take input from the user: soil type, season, budget
	.	Check if inputs are valid
	.	Call suggest_crop function
	.	Print the suggested crop or an error message

2. suggest_crop Function
	.	Store crops for each soil type and season
	.	Store affordable crops for each budget
	.	Find crops that match both soil/season and budget
	.	If no crop matches --> return “No suitable crop”
	.	Otherwise --> return one crop randomly

3. Input Validation
	.	Soil type must be: black, alluvial, red
	.	Season must be: kharif, rabi, zaid
	.	Budget must be: low, medium, high

4. Data
	.	Crops stored in dictionaries by soil type and season
	.	Affordable crops stored in dictionaries by budget

5. (Flowchart image is  added )

---

# Algorithm
Step 1: Start the program.

Step 2: Take input from the user:
	.	Soil type (black, alluvial, red)
	.	Season (kharif, rabi, zaid)
	.	Budget (low, medium, high)

Step 3: Convert all inputs to lowercase to standardize.

Step 4: Validate inputs:
	>	If soil type, season, or budget is invalid → display error message and stop.

Step 5: Get the list of crops suitable for the given soil and season.

Step 6: Get the list of crops affordable for the given budget.

Step 7: Find the intersection of the two lists (crops suitable and affordable).

Step 8: Check if the filtered list is empty:
	.	If yes → display "Sorry! No suitable crop found for the given conditions"
	.	If no → select a random crop from the list and display it

Step 9: End the program.
---

#  Code
The source code is available in main.py.


# Output
Screenshots of the program output are available in the /screenshots


# Project Structure
Crop_Suggestion_System
|--main.py
|--README.md
|--statement.md
|--screenshots/
