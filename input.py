'''
name = input('Your name:')
tweet = input('Tweet your day:')
print('{} tweeted {}'.format(name, tweet))  # String formatting replaces {} with variable values
# print(f'{name} tweeted {tweet}')  # New string formatting added on Python3.6
'''


""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

# Build your code below
total_bill = input('How much is your total bill? ')
payment = input('How much is your payment? ')
change = int(payment) - int(total_bill)
print ('Hi! Your change is {}'.format(change))
