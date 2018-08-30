
from django.conf import settings
from django.db.models import Prefetch
from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from auths.backends import TokenBasedBasicAuthentication

from core.utils import check_pkg_download_permission, serve_file
from packages.models import Package, Version, Build
from stats.models import DownloadHistory


def check_pkg_consistency():
    """Check that all protected branches are a single index
    - unicity of name
    - version must be increased
    - `force` option ignored
    """
    pass


class BuildPermission:
    """"""
    pass


class PackageAPIView(APIView):
    """APIView returning same Pypi response with the packages of the repo."""

    authentication_classes = (TokenBasedBasicAuthentication,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'pip_index.html'

    def get(self, request, pkg_name):
        user = request.user
        print(f'processing {pkg_name} from user {user}')
        version_prefetch = Prefetch(
            "version_set",
            queryset=Version.objects.prefetch_related("build_set").filter(active=True)
        )
        try:
            package = Package.objects.prefetch_related(version_prefetch).get(name=pkg_name)
        except Package.DoesNotExist:
            raise Http404("The package {pkg_name} does not exist")
        if not check_pkg_download_permission(user, package):
            raise PermissionDenied(
                "You do not have access to this package."
                "Please check your username and token."
            )
        return Response({'package': package}, template_name='pip_index.html')


class DownloadBuildAPIView(APIView):
    authentication_classes = (TokenBasedBasicAuthentication,)

    def get(self, request, pk, filename):
        user = request.user
        print("\n\nCOOL, this is user ", user)
        build = Build.objects.get(id=pk)
        from django.core.files import File
        file = File(build.file)
        extension = file.name.split('.')[-1]
        response = HttpResponse(file, content_type=f'application/{extension}')
        response['Content-Disposition'] = f'attachment; filename={build.filename}'
        return response
        serve_file(response=Response(), file=build.file)
        return response


class UploadPypiAPIView(APIView):
    authentication_classes = (TokenBasedBasicAuthentication,)

    @csrf_exempt
    def post(self, request):
        from pprint import pprint
        pprint(request.POST)
        print(request.FILES)
        user = request.user
        print("\n\nCOOL, this is user ", user)
        return Response()


class PackageAdminListAPIView(APIView):
    def get(self, request, pkg_name):
        return Response()


class PackageAdminUpdateAPIView(APIView):

    def get(self, request, pkg_name):
        return Response()


class QualityCheckEditAPIView(APIView):
    pass


class CondaRepodataAPIView(APIView):
    authentication_classes = (TokenBasedBasicAuthentication,)

    def get(self, request, arch):
        user = request.user
        file_path = f"conda_pkgs/conda/{arch}/repodata.json"
        return serve_file(response=Response(), file_path=file_path)


@csrf_exempt
@api_view(['POST'])
def initialize(request):
    from pprint import pprint
    pprint(request.__dict__)
    return Response()
