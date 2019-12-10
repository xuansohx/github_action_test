# actions/update_lotto.py

import requests
# url = 'http://localhost:8000'
url = 'http://ec716171.ngrok.io' # ngrok에서 받아 온 주소
requests.get(url + '/board/fetch_lotto')