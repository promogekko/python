def funny_division(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 vous etes chanceux")
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "entrer un nombre different de zero"

for val in (0, "hello", 50.0, 13):
    print("Testing {}:".format(val), end=" ")
    print(funny_division(val))


#---------------------------------------------------------------

import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" % e.__class__.__name__)
else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")

#-------------------------------------------------------------
