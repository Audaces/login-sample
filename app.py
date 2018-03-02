import uuid
import urllib.parse
from bottle import redirect, get, post, run, request, template

CLIENT_ID = '<YOUR_CLIENT_ID>'


@get('/')
def index():
    return '<form action="/login" method="get"> <input type="submit" name="login" value="Login"> </form> <br>' \
           '<form action="/login_form_post" method="get"> <input type="submit" name="login" value="Login Form Post"> </form>'


@get('/login')
def login():
    return redirect(_login_url(False))


@get('/login_form_post')
def login_form_post():
    return redirect(_login_url(True))


def _login_url(by_form_post):
    authorization_url = 'https://login.audaces.com/core/connect/authorize'
    client_id = CLIENT_ID
    redirect_uri = urllib.parse.quote('http://localhost:8080/login/redirect', safe='')
    response_type = 'id_token token'
    scope = 'openid profile email'
    state = str(uuid.uuid4())
    nonce = str(uuid.uuid4())
    url_params_format = 'client_id={0}&redirect_uri={1}&response_type={2}&scope={3}&nonce={4}&state={5}'
    url_params = url_params_format.format(client_id, redirect_uri, response_type, scope, nonce, state)
    if by_form_post:
        url_params += '&response_mode=form_post'
    return redirect('{0}?{1}'.format(authorization_url, url_params))


@get('/login/redirect')
def get_login_redirect():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <script type="text/javascript">//<![CDATA[
            window.onload=function(){
            new Vue({
              el: '#app',
              data: {
                 url: new URL(window.location.href)
              },
              computed: {
                params: function() {
                    var hash = this.url.hash;
                    var query = {};
                    var pairs = (hash[0] === '#' ? hash.substr(1) : hash).split('&');
                    for (var i = 0; i < pairs.length; i++) {
                        var pair = pairs[i].split('=');
                        query[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1] || '');
                    }
                    return query;
                }
              }
            })
            }//]]>
        </script>
    </head>    
    <body>
        <script src="https://unpkg.com/vue"></script>    
        <div id="app">
          <ul v-for="(value, key, index) in params">
              <li>{{ key }}: {{ value }}</li>
          </ul>
        </div>
    </body>
    </html>
    """


@post('/login/redirect')
def post_login_redirect():
    page = """
        <ul> 
            % for key, value in data.items():
                <li>{{ key }}: {{ value }} </li>
            % end
        </ul>
    """
    return template(page, data=request.forms)


run(port=8080)
