from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from auths.backends import TokenBasedBasicAuthentication

from core.utils import serve_file


class PackageAPIView(APIView):
    authentication_classes = (TokenBasedBasicAuthentication,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'pip_index.html'

    def get(self, request, pkg_name):
        user = request.user
        print(f'processing {pkg_name} from user {user}')
        return Response()


class CondaRepodataAPIView(APIView):
    authentication_classes = (TokenBasedBasicAuthentication,)

    def get(self, request, arch):
        user = request.user
        file_path = f"conda/{arch}/repodata.json"

        print(f'processing {file_path} from user {user}')
        return serve_file(response=Response(), file_path=file_path)


# https://github.com/balzss/yip/blob/master/yip

@csrf_exempt
@api_view(['POST'])
def initialize(request):
    from pprint import pprint
    pprint(request.__dict__)
    return Response()
