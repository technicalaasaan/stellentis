from django.shortcuts import redirect, resolve_url

class StellentisMiddleWare:
    def __init__(self, resp):
        self.get_response = resp

    def __call__(self, req):
        resp = self.get_response(req)
        return resp
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('request', request)
        # return redirect('/admin')
