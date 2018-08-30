import base64

from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied


User = get_user_model()


class TokenBackend:
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):

        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class TokenBasedBasicAuthentication(BasicAuthentication):
    """
    HTTP Basic authentication against username/password.
    """

    def authenticate_credentials(self, userid, password, request=None):
        """
        Authenticate the userid and password against username and token
        with optional request for context.
        """
        credentials = {
            User.USERNAME_FIELD: userid,
            'token': password
        }
        print("TRYING AUTH WITH CREDENTIALS", credentials)
        try:
            user = User.objects.get(**credentials)
        except (User.DoesNotExist, ValidationError):
            raise AuthenticationFailed('Invalid username/password.')

        if not user.is_active:
            raise AuthenticationFailed('User inactive or deleted.')
        return (user, None)
