from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, get_object_or_404

from churchsettings.models import ChurchSetup


def only_manager(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 1:
                return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('401 Unauthorized: You are not authorised to view this page.', status=401)

    return wrapper_func


def allowed_roles(permitted_roles=[]):
    def decorator(request_view):
        def wrapper_func(request, *args, **kwargs):
            if request.user.role in permitted_roles:
                return request_view(request, *args, **kwargs)
            else:
                return HttpResponse('401 Unauthorized: You are not authorised to view this')

        return wrapper_func

    return decorator


def login_not_required(view_func):
    def not_required(request, *args, **kwargs):
        if request.user.id is None:
            return view_func(request, *args, **kwargs)
    return not_required


def check_if_setup(request_view):
    def wrapper_func(request, *args, **kwargs):
        try:
            setup = ChurchSetup.objects.filter(user=request.user).get()
            return request_view(request, *args, **kwargs)
        except ChurchSetup.DoesNotExist:
            return redirect('setup-church', user=request.user.id)

    return wrapper_func

# def allowed_groups(permitted_groups=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#                 if group in permitted_groups:
#                     return view_func(request, *args, **kwargs)
#                 if group == 'qasa':
#                     return redirect('analytic_dashboard')
#                 elif group == 'student':
#                     return redirect('evaluations')
#                 else:
#                     return HttpResponse('401 Unauthorized: You are not authorised to view this page.', status=401)
#             else:
#                 return HttpResponse('401 Unauthorized: You are not authorised to view this page.', status=401)
#
#         return wrapper_func
#
#     return decorator