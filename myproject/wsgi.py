from wsgiref.simple_server import make_server

class Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        for lists in self.app(environ, start_response):
            text = lists
            if text.find('<body') > 0:
                r = text.encode()
                yield r
                r = "<div class='top'>Middleware TOP</div>".encode()
                yield r
            elif text.find('</body>') > 0:
                r = "<div class='botton'>Middleware BOTTOM</div>".encode()
                yield r
                r = text.encode()
                yield r
            else:
                r = text.encode()
                yield r

def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/HTML')])
    file = open(environ['PATH_INFO'], 'r')
    Page_result = []
    for line in file:
        Page_result.append(line)
    return Page_result

make_server('localhost', 8000, Middleware(app)).serve_forever()