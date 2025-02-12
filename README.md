# FIT-FROM-HOME
Project Overview:
This project revolves around bringing a gym-like experience at home and managing a gym online in the most efficient way to achieve optimal results.

Features:
The online gym mode will assign trainees workout tasks that can be done at home based on their individual requirements.
Workouts will be tailored according to BMI, personal goals, and available home equipment (such as skipping rope, cycle, dumbbells, etc.).
A progress tracker will help trainees monitor their durability, consistency, and improvements over time.
Trainees will also have the opportunity to consult professional trainers for guidance and personalized advice.

1. CALCULATOR MODULE
This module focuses on calculating various health metrics for the trainee.

Calculations Included:

BMI (Body Mass Index)
BMR (Body Metabolic Rate)
Fat percentage
Total calorie content in a given amount of food
Data Flow:

Uses information stored in the BASIC module
Outputs data for the Progress_Tracker module

2. DIET MAKER MODULE
This module helps trainees plan their diet based on statistical and user-specific data.
Uses data from the BASIC module
Outputs data for the EXERCISE module


3. Exercise Module
Assigns tasks and exercises based on trainee requirements, using data from the DIET module.
Generates custom workout sessions based on data stored in Exercises.csv.
Covers all 12 body parts like forearms, biceps, calves, chest, etc.
Personalizes workouts by calculating calories burned per minute for each exercise.


4. Workout Assistant Module
Manages workout sessions by tracking the trainee’s activities in real-time.
Remains active until all workout tasks are completed within the given time slot.
Uses data from the EXERCISE module for scheduling and tracking.


5. Progress Tracker Module
Aggregates trainee data such as fat percentage, weight changes, and other key metrics.
Maintains a daily progress record to assess overall fitness improvement.
Uses data from both BASIC and EXERCISE modules for tracking growth and results.
