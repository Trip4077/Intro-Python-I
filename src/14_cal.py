"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Ensures arguments are formatted correctly based on string length
def argCheck(arg1, arg2):

  if( len( arg1 ) > 2 or len( arg2 ) > 4):
    return False

  else:
    return True

# Generates a calendar based on number of inputs
def generate_calendar( input ):
  if input == 3:
    # Check Format
    if not argCheck( sys.argv[1], sys.argv[2] ):
      return "Please enter format MM YYYY"

    # Full User Input
    monthly = calendar.month( int( sys.argv[2] ), int( sys.argv[1] ), 2, 1 )
    return monthly

  elif input == 2 :
    #Check Format
    if not argCheck( sys.argv[1], "2019" ):
      return "Please enter format MM YYYY"

    # Default To This year
    year = datetime.today().year
    monthly = calendar.month( year, int( sys.argv[1] ), 2, 1 )
    return monthly

  else:
    # Default To Today
    year = datetime.today().year
    month = datetime.today().month

    monthly = calendar.month( year, month, 2, 1 )
    return monthly

# Get arguments passed
argLength = len( sys.argv )

print( generate_calendar( argLength ) )