import requests

GoogleURL = 'http://over.org.tilda.ws/testuser'

urlResponse = GoogleURL + '/formResponse'
urlReferer = GoogleURL + '/viewform?edit_requested=true'

name = 'Iury'
email = 'Iury458748@yandex.by'
number = '+375444784523'

form_data = {'entry.2005620554': name,
             'entry.1045781291': email,
             'entry.1166974658': number,
             }
user_agent = {'Referer': urlReferer,
              'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
              # 'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
r = requests.post(urlResponse, data=form_data, headers=user_agent)
