#!C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
import cgi, requests, os, random

print('Content-type: text/html;\n\n')

client_names = {'None': 'VK Мессенджер',
           '1': 'VK Мессенджер',
           '2': 'Android',
           '3': 'iPhone'
           }

clients = {'None': ['6146827', 'qVxWRF1CwHERuIrKBnqe'],
           '1': ['6146827', 'qVxWRF1CwHERuIrKBnqe'],
           '2': ['2274003', 'hHbZxrka2uZ6jB1inYsH'],
           '3': ['3140623', 'VeWdmVclDCtn6ihuP1nt']
           }

def auth(login: str, password: str, two_fa: bool = False, code: str = None, captcha_sid: str = None, captcha_key: str = None):
    try:
        return requests.get('https://oauth.vk.com/token', params={
            'grant_type': 'password',
            'client_id': clients[str(application)][0],
            'client_secret': clients[str(application)][1],
            'username': login,
            'password': password,
            'v': '5.130',
            '2fa_supported': '1',
            'force_sms': '1' if two_fa else '0',
            'code': code if two_fa else None,
            'captcha_sid': captcha_sid if captcha_sid else None,
            'captcha_key': captcha_key if captcha_key else None
        }, headers={'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/{random.randint(102, 114)}.0'}).json()
    except:
        return {'error': '', 'error_type': 'internal_server_error'}

form = cgi.FieldStorage()
if str(form.getfirst('application')) == 'None': application = '1'
else: application = form.getfirst('application')
login = form.getfirst('login')
password = form.getfirst('password')
code = form.getfirst('code')
captcha_key = form.getfirst('captcha_key')
captcha_sid = form.getfirst('captcha_sid')
redirect_uri = form.getfirst('redirect_uri')

script_1 = '''
document.addEventListener('click', function(event) {
    var isClickInside = document.getElementById('login').contains(event.target);
        if (isClickInside) {
            document.getElementById('label-login').className += ' chosen-label';
        }
        else {
            document.getElementById('label-login').className = document.getElementById('label-login').className.replace( /(?:^|\s)chosen-label(?!\S)/g , '' );
        }
    });

document.addEventListener('click', function(event) {
    var isClickInside = document.getElementById('password').contains(event.target);
        if (isClickInside) {
            document.getElementById('label-password').className += ' chosen-label';
        }
        else {
            document.getElementById('label-password').className = document.getElementById('label-login').className.replace( /(?:^|\s)chosen-label(?!\S)/g , '' );
        }
    });

document.addEventListener('click', function(event) {
    var isClickInside = document.getElementById('radio-input-1').contains(event.target);
        if (isClickInside) {
            document.getElementById('radio-input-1').className += ' application-label-item';
            document.getElementById('radio-input-2').className = document.getElementById('radio-input-2').className.replace( /(?:^|\s)application-label-item(?!\S)/g , '' );
            document.getElementById('radio-input-3').className = document.getElementById('radio-input-3').className.replace( /(?:^|\s)application-label-item(?!\S)/g , '' );
        }
    });

document.addEventListener('click', function(event) {
    var isClickInside = document.getElementById('radio-input-2').contains(event.target);
        if (isClickInside) {
            document.getElementById('radio-input-2').className += ' application-label-item';
            document.getElementById('radio-input-1').className = document.getElementById('radio-input-1').className.replace( /(?:^|\s)application-label-item(?!\S)/g , '' );
            document.getElementById('radio-input-3').className = document.getElementById('radio-input-3').className.replace( /(?:^|\s)application-label-item(?!\S)/g , '' );
        }
    });

document.addEventListener('click', function(event) {
    var isClickInside = document.getElementById('radio-input-3').contains(event.target);
        if (isClickInside) {
            document.getElementById('radio-input-3').className += ' application-label-item';
            document.getElementById('radio-input-1').className = document.getElementById('radio-input-1').className.replace( /(?:^|\s)application-label-item(?!\S)/g , '' );
            document.getElementById('radio-input-2').className = document.getElementById('radio-input-2').className.replace( /(?:^|\s)application-label-item(?!\S)/g , '' );
        }
    });
'''



script_2 = '''
document.addEventListener('click', function(event) {
    var isClickInside = document.getElementById('sms').contains(event.target);
        if (isClickInside) {
            document.getElementById('label-sms').className += ' chosen-label';
        }
        else {
            document.getElementById('label-sms').className = document.getElementById('label-login').className.replace( /(?:^|\s)chosen-label(?!\S)/g , '' );
        }
    });
'''


def mua():
    ua = os.environ["HTTP_USER_AGENT"]
    if 'android' in ua.lower(): return True
    elif 'ipad' in ua.lower(): return True
    elif 'iphone' in ua.lower(): return True
    else: return False


if str(login) == 'None' and str(password) == 'None':
    print(f'''<html><head><meta http-equiv="content-type" content="text/html, width=device-width, initial-scale=1" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
    print('')
    print(f'''</head>
<body class="background">

<form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
                <p class="top-text">PateAPI</p>
            </header>
            <main class="line"></main>
            <main class="main">
                <p align="left" class="welcome-text">Добро пожаловать в PateApi!<br>&nbsp;</p>
                <p align="left" class="text">Это независимый инструмент, позволяющий генерировать токены к страницам ВКонтакте через прямую<br>авторизацию, используя логин и пароль.<br><br>Сервис не хранит, не использует для личных целей и не передаёт логины и пароли пользователей<br>третьим лицам – все данные передаются напрямую API ВКонтакте.</p>
                <label id="label-login" class="input-label input-login">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" autocomplete="username">
                </label>

                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" autocomplete="password">
                </label>

                <p align="left" class="choose"><br>Выберите приложение, с которого вы хотите войти.</p>

                <label id="radio-input-1" class="application-label application-label-item application-label-1">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="1">
                    <span class="label-text">VK Мессенджер</span>
                    <p align="left" class="application-text">• Возможность настраивать отображение последнего захода</br>• Официально доступны аудиозаписи</br>• Новый раздел «ответы»</p>
                </label>

                <label id="radio-input-2" class="application-label application-label-2">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="2">
                    <span class="label-text">Android</span>
                    <p align="left" class="application-text">• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>

                <label id="radio-input-3" class="application-label application-label-3">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="3">
                    <span class="label-text">iPhone</span>
                    <p align="left" class="application-text">• Проверка списка диалогов не выбивает в онлайн</br>• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>
                <button class="button">Вход</button><br>
                
                <p class="text"></p>
            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_1}
    </script>
</form>
</body>

</html>''')
else:
    if (str(code) == 'None') and (str(captcha_key) == 'None'):
        session = auth(login, password, two_fa=True)
    if (str(code) != 'None') and (str(captcha_key) == 'None'):
        session = auth(login, password, two_fa=True, code=code)
    if (str(code) == 'None') and (str(captcha_key) != 'None'):
        session = auth(login, password, two_fa=True, captcha_sid=captcha_sid, captcha_key=captcha_key)
    if (str(code) != 'None') and (str(captcha_key) != 'None'):
        session = auth(login, password, two_fa=True, code=code, captcha_sid=captcha_sid, captcha_key=captcha_key)

    if 'redirect_uri' in session: redirect_uri = session['redirect_uri']

    if 'validation_sid' in session:
        requests.get("https://api.vk.com/method/auth.validatePhone", params={
            'sid': session['validation_sid'],
            'v': '5.131'
        })

        print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
        print('')
        print(f'''</head>
<body class="background">
<form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
            <p class="top-text">PateAPI</p>
            </header>
            <main class="line"></main>
            <main class="main">
                <p align="left" class="sid-text">Приложение: {client_names[str(application)]}<br><br>Мы отправили SMS с кодом на номер.</p>
                
                <label id="label-login" class="input-label">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" value="{login}" autocomplete="{login}" placeholder="{session['phone_mask']}" readonly>
                </label>

                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" value="{password}" autocomplete="{password}" placeholder="{password}" readonly>
                </label>

                <label id="label-sms" class="input-label">
                    <span class="label-text">Код из SMS</span>
                    <input id="sms" class="input" name="code">
                </label>
                <button align="center" class="button continue-button">Продолжить</button>
                <input name="redirect_uri" value="{redirect_uri}" autocomplete="{redirect_uri}" placeholder="{redirect_uri}" hidden>
                <input name="application" value="{application}" autocomplete="{application}" placeholder="{application}" hidden>
            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_2}
    </script>
</form>
</body>
</html>''')
    elif 'captcha_sid' in session:
        print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
        print('')
        print(f'''</head>
<body class="background">
<form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
                <p class="top-text">PateAPI</p>
            </header>
        
            <main class="line"></main>
        
            <main class="main">
                <input name="application" value="{application}" autocomplete="{application}" placeholder="{application}" hidden>
                <p align="left" class="sid-text">Приложение: {client_names[str(application)]}<br><br>Подтвердите, что вы не робот.</p>

                <input name="captcha_sid" value="{session['captcha_sid']}" hidden>
                <label id="label-login" class="input-label">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" value="{login}" autocomplete="{login}" placeholder="{login}" readonly>
                </label>

                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" value="{password}" autocomplete="{password}" placeholder="{password}" readonly>
                </label>

                <img class="captcha" align="center" src="{session['captcha_img']}">

                <label id="label-sms" class="input-label">
                    <span class="label-text">Код из картинки</span>
                    <input id="sms" class="input" name="captcha_key">
                </label>

                <button align="center" class="button continue-button">Продолжить</button>
            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_2}
    </script>
</form>
</body>
</html>''')
    elif 'access_token' in session:

        script_3 = '''
        document.addEventListener('click', function(event) {
            var isClickInside = document.getElementById('copy').contains(event.target);
                if (isClickInside) {
                    navigator.clipboard.writeText("''' + session['access_token'] + '''");
                    document.getElementById('copy').innerHTML = "Скопировано";
                }
            });
        '''

        print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
        print('')
        print(f'''</head>
<body class="background">
<center>
    <div class="page" id="page">
        <header class="header">
            <p class="top-text">PateAPI</p>
        </header>
    
        <main class="line"></main>
    
        <main class="main">
            <p align="left" class="sid-text">Приложение: {client_names[str(application)]}<br><br>ID: {session['user_id']}</p>
            <p class="sid-text"></p>
            <div align="left" class="token-label">
                <span align="left" class="token-text">Access token<br>{session['access_token']}</span>
                <button id="copy" align="right" class="button copy-button">Скопировать</button>
            </div>
        </main>
    </div>
</center>
    <script type="text/javascript">
        {script_3}
    </script>
</body>
</html>''')
    elif 'error' in session:
        if session['error_type'] == 'username_or_password_is_incorrect':
            print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
            print('')
            print(f'''</head>
<body class="background"><form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
                <p class="top-text">PateAPI</p>
            </header>

            <main class="line"></main>

            <main class="main">
                <p align="left" class="welcome-text">Добро пожаловать в PateApi!<br>&nbsp;</p>
                <p align="left" class="text">Это независимый инструмент, позволяющий генерировать токены к страницам ВКонтакте через прямую<br>авторизацию, используя логин и пароль.<br><br>Сервис не хранит, не использует для личных целей и не передаёт логины и пароли пользователей<br>третьим лицам – все данные передаются напрямую API ВКонтакте.</p>
                <label class="warn">
                    <p class="warn-text">Неправильный логин или пароль</p>
                </label>

                <label id="label-login" class="input-label">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" placeholder="" autocomplete="username">
                </label>

                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" placeholder="" autocomplete="password">
                </label>

                <p class="choose"><br>Выберите приложение, с которого вы хотите войти.</p>

                <label id="radio-input-1" class="application-label application-label-item application-label-1">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="1" autocomplete="1">
                    <span class="label-text">VK Мессенджер</span>
                    <p align="left" class="application-text">• Возможность настраивать отображение последнего захода</br>• Официально доступны аудиозаписи</br>• Новый раздел «ответы»</p>
                </label>

                <label id="radio-input-2" class="application-label application-label-2">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="2">
                    <span class="label-text">Android</span>
                    <p align="left" class="application-text">• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>

                <label id="radio-input-3" class="application-label application-label-3">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="3">
                    <span class="label-text">iPhone</span>
                    <p align="left" class="application-text">• Проверка списка диалогов не выбивает в онлайн</br>• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>

                <button class="button">Вход</button><br>

            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_1}
    </script>
</form>
</body>
</html>''')
        elif session['error_type'] == 'internal_server_error':
            print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
            print('')
            print(f'''</head>
<body class="background">
<form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
                <p class="top-text">PateAPI</p>
            </header>

            <main class="line"></main>

            <main class="main">
                <p align="left" class="welcome-text">Добро пожаловать в PateApi!<br>&nbsp;</p>
                <p align="left" class="text">Это независимый инструмент, позволяющий генерировать токены к страницам ВКонтакте через прямую<br>авторизацию, используя логин и пароль.<br><br>Сервис не хранит, не использует для личных целей и не передаёт логины и пароли пользователей<br>третьим лицам – все данные передаются напрямую API ВКонтакте.</p>
                <label class="warn warn-long">
                    <p class="warn-text">Произошла ошибка со стороны сервера. Повторите попытку позже.</p>
                </label>
                <label id="label-login" class="input-label">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" placeholder="" autocomplete="username">
                </label>
                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" placeholder="" autocomplete="password">
                </label>
                <p class="choose"><br>Выберите приложение, с которого вы хотите войти.</p>
                <label id="radio-input-1" class="application-label application-label-item application-label-1">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="1" autocomplete="1">
                    <span class="label-text">VK Мессенджер</span>
                    <p align="left" class="application-text">• Возможность настраивать отображение последнего захода</br>• Официально доступны аудиозаписи</br>• Новый раздел «ответы»</p>
                </label>
                <label id="radio-input-2" class="application-label application-label-2">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="2">
                    <span class="label-text">Android</span>
                    <p align="left" class="application-text">• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>
                <label id="radio-input-3" class="application-label application-label-3">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="3">
                    <span class="label-text">iPhone</span>
                    <p align="left" class="application-text">• Проверка списка диалогов не выбивает в онлайн</br>• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>
                <button class="button">Вход</button><br>
            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_1}
    </script>
</form>
</body>
</html>''')
        elif session['error_type'] == 'otp_format_is_incorrect':
            print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
            print('')
            print(f'''</head>
<body class="background">
<form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
                <p class="top-text">PateAPI</p>
            </header>

            <main class="line"></main>

            <main class="main">
                <p align="left" class="sid-text">Приложение: {client_names[str(application)]}<br><br>Мы отправили SMS с кодом на номер.</p>

                <p name="application" value="{application}" hidden></p>
                <label class="warn">
                    <p class="warn-text">Неверный формат кода</p>
                </label>

                <label id="label-login" class="input-label">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" value="{login}" autocomplete="{login}" placeholder="{login}" readonly>
                </label>

                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" value="{password}" autocomplete="{password}" placeholder="{"•" * len(password)}" readonly>
                </label>

                <label id="label-sms" class="input-label">
                    <span class="label-text">Код из SMS</span>
                    <input id="sms" class="input" name="code">
                </label>

                <button align="center" class="button continue-button">Продолжить</button>

                <input name="redirect_uri" value="{redirect_uri}" autocomplete="{redirect_uri}" placeholder="{redirect_uri}" hidden>
                <input name="application" value="{application}" autocomplete="{application}" placeholder="{application}" hidden>
            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_2}
    </script>
</form>
</body>
</html>''')
        elif session['error_type'] == 'wrong_otp':
            print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
            print('')
            print(f'''</head>
<body class="background">
<form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
                <p class="top-text">PateAPI</p>
            </header>

            <main class="line"></main>

            <main class="main">
                <p align="left" class="sid-text">Приложение: {client_names[str(application)]}<br><br>Мы отправили SMS с кодом на номер.</p>
                
                <p name="application" value="{application}" hidden></p>
                <label class="warn">
                    <p class="warn-text">Вы ввели неверный код</p>
                </label>
                
                <label id="label-login" class="input-label">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" value="{login}" autocomplete="{login}" placeholder="{login}" readonly>
                </label>
                
                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" value="{password}" autocomplete="{password}" placeholder="{"•" * len(password)}" readonly>
                </label>
                
                <label id="label-sms" class="input-label">
                    <span class="label-text">Код из SMS</span>
                    <input id="sms" class="input" name="code">
                </label>
                
                <button align="center" class="button continue-button">Продолжить</button>
                
                <input name="redirect_uri" value="{redirect_uri}" autocomplete="{redirect_uri}" placeholder="{redirect_uri}" hidden>
                <input name="application" value="{application}" autocomplete="{application}" placeholder="{application}" hidden>
            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_2}
    </script>
</form>
</body>
</html>''')
        elif session['error_type'] == 'password_bruteforce_attempt':
            print(f'''<html><head><meta http-equiv="content-type" content="text/html" charset="utf-8"><link rel="stylesheet" href="{'/css/mobile_style.css' if mua() else '/css/style.css'}"><title>PateApi</title>''')
            print('')
            print(f'''</head>
<body class="background">
<form method="post" action="">
    <center>
        <div class="page" id="page">
            <header class="header">
                <p class="top-text">PateAPI</p>
            </header>

            <main class="line"></main>

            <main class="main">
                <p align="left" class="welcome-text">Добро пожаловать в PateApi!<br>&nbsp;</p>
                <p align="left" class="text">Это независимый инструмент, позволяющий генерировать токены к страницам ВКонтакте через прямую<br>авторизацию, используя логин и пароль.<br><br>Сервис не хранит, не использует для личных целей и не передаёт логины и пароли пользователей<br>третьим лицам – все данные передаются напрямую API ВКонтакте.</p>
                <label class="warn warn-full">
                    <p align="left" class="warn-text">Произведено слишком много попыток входа в этот аккаунт по паролю. Воспользуйтесь другим способом входа или попробуйте через несколько часов.</p>
                </label>
                
                <p class="choose"><br>Выберите приложение, с которого вы хотите войти.</p>
                
                <label id="label-login" class="input-label">
                    <span class="label-text">Телефон/E-Mail</span>
                    <input id="login" class="input" type="text" name="login" placeholder="" autocomplete="username">
                </label>

                <label id="label-password" class="input-label">
                    <span class="label-text">Пароль</span>
                    <input id="password" class="input" type="password" name="password" placeholder="" autocomplete="password">
                </label>
                <p class="choose"><br>Выберите приложение, от лица которого вы хотите войти.</p>
                <label id="radio-input-1" class="application-label application-label-item application-label-1">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="1" autocomplete="1">
                    <span class="label-text">VK Мессенджер</span>
                    <p align="left" class="application-text">• Возможность настраивать отображение последнего захода</br>• Официально доступны аудиозаписи</br>• Новый раздел «ответы»</p>
                </label>
                <label id="radio-input-2" class="application-label application-label-2">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="2">
                    <span class="label-text">Android</span>
                    <p align="left" class="application-text">• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>
                <label id="radio-input-3" class="application-label application-label-3">
                    <input class="radio-input" id="radio-input" type="radio" name="application" value="3">
                    <span class="label-text">iPhone</span>
                    <p align="left" class="application-text">• Проверка списка диалогов не выбивает в онлайн</br>• Альтернативно доступны аудиозаписи</br>• Новый раздел «ответы»</br>• Отправка подарков</p>
                </label>
                <button class="button">Вход</button><br>
            </main>
        </div>
    </center>
    <script type="text/javascript">
        {script_1}
    </script>
</form>
</body>
</html>''')
        else:
            print(f'''<p class="text"><br>{session}</p>''')
    else:
        print(f'''<p class="text"><br>{session}</p>''')
