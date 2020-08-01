from plyer import notification
# https://api.covid19india.org/state_district_wise.json
import requests
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

url = 'https://api.covid19india.org/state_district_wise.json'
data = requests.get(url).text
def notify(title, message):
    notification.notify(title=title, app_icon='D:\Projects\Python Projects\PycharmProjects\covid\icon.ico',
                        message=message, timeout=7)
speak('Made by Sachin')
if __name__ == '__main__':
    dict = json.loads(data)
    s = input('Enter State name for data access(Case sensitive):')
    i = input('Enter District name (Case Sensitive):')
    if len(s) < 1 and len(i) < 1:
        s = 'Uttar Pradesh'
        i = 'Lucknow'
    state = dict[s]
    dists = state['districtData']
    dist = dists[i]
    new = dist['delta']
    message = f'''
    Active Cases: {dist['active']}
    Confirmed Cases: {dist['confirmed']}
    Deceased Cases: {dist['deceased']}
    Recovered Cases: {dist['recovered']}
    '''
    newcases = f'''
    Confirmed: {new['confirmed']}
    Recovered: {new['recovered']}
    Deceased : {new['deceased']}'''
    print(message)
    notify(f'Covid{s, i}', message)
    speak(f'Cases in {i,s}{message}')

    print(newcases)
    notify(f'Covid{s, i}', newcases)
    speak(f'New cases in {i,s}{newcases}')
    time.sleep(2)
def repeat():
    speak('Next updates in one hour')
    time.sleep(3600)
    message = f'''
       Active Cases: {dist['active']}
       Confirmed Cases: {dist['confirmed']}
       Deceased Cases: {dist['deceased']}
       Recovered Cases: {dist['recovered']}
       '''
    newcases = f'''
       Confirmed: {new['confirmed']}
       Recovered: {new['recovered']}
       Deceased : {new['deceased']}'''
    print(message)
    notify(f'Covid{s, i}', message)
    speak(f'Cases in {i,s}{message}')
    time.sleep(7)
    notify(f'Covid{s, i}', newcases)
    print(newcases)
    speak(f'New Cases in {i,s}{newcases}')

    call()
def call():
    repeat()
repeat()




