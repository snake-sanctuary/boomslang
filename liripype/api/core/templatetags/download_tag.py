from django import template

register = template.Library()


@register.simple_tag
def get_download_url(build, user):
    return build.get_download_url(user)
