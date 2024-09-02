# Calorie Tracker

A calorie tracker app utilizing microservices communicating through ZeroMQ to help a user meet their fitness goals.

## Table of Contents

1. [Overview](#overview)
2. [Microservices](#Microservices)
3. [Reflection](#Reflection)

## Overview

In this portfolio project for my Software Engineering I course, I created a calorie tracker app that a user operates via command line interface. The main program completes various tasks such as calculating calories consumed or burned and preparing reports for the user by communicating with microservices through ZeroMQ. The user navigates the command line interface by entering selections and prompts, which the program uses to prepare the desired outputs.

## Microservices

* calculate_calories_burned - Upon receiving a request, this microservice calculates the calories burned by a user's exercise using the provided weight, duration of the exercise, and metabolic equivalents. It then sends the calculation back to the main program.
* prepare_log - When this microservice receives a request, it generates a list of the foods and the total number of calories a user has consumed for the day. This microservice also prepares a list of all exercises the user has performed for the day and the calories burned from such exercise. These lists are sent back to to the main program, which displays the compiled report for the user.
* exercise_duration_tracker - This microservice generates a report of the progress a user has made toward reaching a daily goal of 30 minutes of exercise. Upon receiving a request, the microservice totals the total time a user has exercised for the day then subtracts that time from the 30-minute exercise goal recommended by the Mayo Clinic. The user's progress toward that goal is sent back to the main program, which is then displayed for the user.
* rng_quote_gen_microservce - As part of this portfolio project, every student was required to create one microservice requested by another classmate. I requested a random quotation generator so that I could add motivational and supportive quotes throughout the interface for the user. My partner created this microservice for my project.

## Reflection

This was my first attempt at creating a program using microservices that interact through a communication pipe. In addition to honing some of my Python skills, I learned about the benefits of using microservices, which--given their more "decentralized" nature--allows for easier maintenance of an overall program and more flexibility for team productivity and deployment during development.

