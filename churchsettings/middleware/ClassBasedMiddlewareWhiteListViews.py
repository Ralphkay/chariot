from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, resolve
from django.http import HttpResponse


class ChurchAuthMiddlewareWhiteList:
    def __init__(self, get_response):
        self.whitelisted_urls = list([reverse('run-view')])
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path not in self.whitelisted_urls:
                return self.utilityfunc(request.path)
        response = self.get_response(request)
        return response

    def utilityfunc(self, path):
        if path in self.whitelisted_urls:
            return redirect(path)
        else:
            return redirect('login')