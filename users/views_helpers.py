"""

View helpers contain functionality shared between several view partials.
None of these classes provide full view functionality.

"""
from django.contrib.auth import authenticate

def look_user(email_user, password_user):
    user = authenticate(email = email_user, password = password_user)
    if user is not None:
        return True

    return False
