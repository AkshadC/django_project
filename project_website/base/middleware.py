# middleware.py
from django.shortcuts import redirect

class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Redirect to auto-login for admin pages
        if not request.user.is_authenticated and request.path.startswith('/admin/'):
            return redirect('auto_login')
        response = self.get_response(request)
        return response
