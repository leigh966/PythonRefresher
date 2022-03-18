import functools


user = {"username": "dog", "access_level": "guest"}
#user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func) # Function keeps its name and documentation
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"{user['username']} does not have admin privledges"
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())