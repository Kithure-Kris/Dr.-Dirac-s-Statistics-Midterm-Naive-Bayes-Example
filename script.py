import numpy as np
'''
Dr. Dirac is administering a statistics midterm exam and wants to use Bayes’ Theorem to help him understand the following:

Given that a student answered a question correctly, what is the probability that she really knows the material?
Dr. Dirac knows the following probabilities based on many years of teaching:

1. There is a question on the exam that 60% of students know the correct answer to.
2. Given that a student knows the correct answer, there is still a 15% chance that the student picked the wrong answer.
3. Given that a student does not know the answer, there is still a 20% chance that the student picks the correct answer by guessing.

Using these probabilities, we can answer the question.
'''

#Using Bayes Theorem to find P(knows the material | answers correctly)

#What is the probability that the student knows the material?
P(knows the material) = 0.60

#Given that the student knows the material, what is the probability that she answers correctly?
P(answers correctly | knows material) = 1 - 0.15

#What is the probability of any student answering correctly?
P(answers correctly| doesnt know material) = 0.20

P(doesnt know material) = 0.40

P(answers correctly) = (P(answers correctly | knows material) * P(knows material) + (P(answers correctly| doesnt know material) * P(doesnt know material))

#Using the three probabilities and Bayes’ Theorem, calculate P(knows material | answers correctly)
P(knows material | answers correctly) = (P(answers correctly | knows material) * P(answers correctly)) / P(knows material)

#https://youtu.be/20S36x0MtzQ
