from django.shortcuts import redirect
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

class PreventBackMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        protected_views = [
            'post_food',
            'edit_post',
            'delete_post',
        ]

        current_view = resolve(request.path_info).url_name

        if current_view in protected_views and not request.user.is_authenticated:
            return redirect('home')  # Change 'home' if your homepage has a different URL name

        return None

    def process_response(self, request, response):
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
