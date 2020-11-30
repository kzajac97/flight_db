from pyramid.view import notfound_view_config


@notfound_view_config(renderer="../templates/404.pt")
def not_found_view(request):
    """View for 404 http error"""
    request.response.status = 404
    return {}
