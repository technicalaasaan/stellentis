from django.shortcuts import redirect, resolve_url

class StellentisMiddleWare:
    def __init__(self, resp):
        self.get_response = resp

    def __call__(self, req):
        resp = self.get_response(req)
        return resp
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('request', request.path_info, request.user.is_authenticated)
        pathinfo = request.path_info
        if request.user.is_authenticated:
            if pathinfo in ('/login/'):
                return redirect('/sample')
        else:
            print('pa', pathinfo)
            if pathinfo.startswith('/admin/'):
                return
            if pathinfo not in ('/login/', '/register/', '/admin/'):
                return redirect('/login/')
