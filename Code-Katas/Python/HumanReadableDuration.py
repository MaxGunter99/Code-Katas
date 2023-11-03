
# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# RUN WITH: python3 code-katas/python/HumanReadableDuration.py

def format_duration(seconds):
    return_value = ""
    vals = {}

    # # IN SECONDS
    second = 1
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365

    for name, i in [ 
        ( "year", year ) ,
        ( "day",  day ), 
        ( "hour", hour ),
        ( "minute", minute ), 
        ( "second", second ), 
    ]:
        print( f"{name} - {seconds // i }" )
        for _ in range( seconds // i ):
            if name not in vals:
                vals[name] = 0
            vals[name] += 1
            seconds -= i

    new_arr = [ f"{v} {k}" if v < 2 else f"{v} {k}s" for k,v in vals.items() ] 

    if len( new_arr ) >= 2:
        and_thing = " and ".join(new_arr[-2:])
        everything_else = ", ".join( new_arr[:-2] + [ and_thing ] )
        return_value += everything_else
    elif len( new_arr ) == 1:
        return new_arr[0]
    else:
        return "now"
    
    print( f"returning: {return_value}" ) 
    return return_value


assert format_duration( 61 ) == "1 minute and 1 second"
assert format_duration( 59 ) == "59 seconds"
assert format_duration( 120 ) == "2 minutes"
assert format_duration( 60 ) == "1 minute"
assert format_duration( 90 ) == "1 minute and 30 seconds"
assert format_duration( 3662 ) == "1 hour, 1 minute and 2 seconds"
assert format_duration( 15731080 ) == '182 days, 1 hour, 44 minutes and 40 seconds'
assert format_duration( 132030240 ) == '4 years, 68 days, 3 hours and 4 minutes'