from django.conf import settings
from django.shortcuts import Http404


def serve_file(response, file=None, file_path=None, file_name=None):
    """"""

    if not settings.DEBUG:
        file_name = file_name or file.name
        response['X-Accel-Redirect'] = f'/protected/{file_name}'
        return response

    if file:
        response.content = file.read()
        return response

    try:
        with open(settings.MEDIA_ROOT + file_path) as file:
            response.content = file.read()
            return response
    except Exception as e:
        print(e)
        raise Http404
