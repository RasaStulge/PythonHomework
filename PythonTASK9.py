# Task 9
# Decoration

def greeting(func):
    def wrapper(*args, **kwargs):
        return f" merry christmas , {func(*args, **kwargs)}"
    return wrapper

@greeting
def kiss():
    return ":*"

@greeting
def personalization(name):
    return f" dear {name}"


if __name__ == '__main__':
   decorated_kiss_func = greeting(kiss)   #sudekoravom funkcija
   print(kiss())
   print(decorated_kiss_func())
   decorated_personalization_fun = greeting(personalization)
   print(decorated_personalization_fun("John"))
   print(kiss())
   print(personalization(name="Smith"))


