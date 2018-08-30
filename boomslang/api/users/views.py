""""""
from django.contrib.auth import LoginUserForm
from django.core.exceptions import PermissionDenied
from djangorestframework import Response


def activate(request):
    pass
    # request.logout()
    # check_activation_token(token)


def setup_two_factor(request):
    pass


def check_second_factor(request):
    pass


def login(request):
    """"""
    pass


@allowed_methods(["POST"])
def signup(request):
    """"""
    if request.user.is_authenticated:
        raise PermissionDenied("You are already logged in.")
    user_form = LoginUserForm(request.POST)
    if not user_form.is_valid():
        return Response(data=errors, status)
    user = user_form.save()
    # handle_activation_link()
    return Response()


class UserProfileAPIView():
    pass
