""""""

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import ListAPIView, RetrieveAPIView

from Package.models import Package


class CanSeePackage(IsAuthenticated):
    """Permission class checking that the user can see the package."""

    def has_object_permission(self, request, view, obj):
        """Check the object belongs to the bank user."""
        user = request.user
        same_user = obj.user_owner == request.user
        is_public = obj.visibility == Package.VisibilityChoices.PUBLIC
        same_team = (
            obj.visibility == Package.VisibilityChoices.TEAM
            and obj.team_owner in user.team_set.all()
        )
        whitelisted = (
            obj.visibility == Package.VisibilityChoices.TEAM
            and obj.team_owner in user.team_set.all()
        )


class PublicPackageListAPIView(ListAPIView):
    """"""
    queryset = Package.objects.filter(is_public=True)


class OrganizationPackageListAPIView(ListAPIView):
    """"""
    def get_queryset(request):
        user = request.user
        zzz = Q()

        queryset = Package.objects.filter(
            organization=user.organization,
        )

class PackageRetrieveAPIView(RetrieveAPIView):
    """"""
    def retrieve():
        """"""
        pass
