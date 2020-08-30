import urllib.request, urllib.error, urllib.parse
import json

import requests

'''Created by Nanthakumar J J U can use this code and modify but dont forgot to give credits to me
My website: http://jjnanthakumar.github.io/
'''
__author__ = "jjnanthakumar477@gmail.com"


def agifyapi(serviceurl):
    print('-----------------------------To predict your age using name------------------------------------')
    name = input("Enter your name: ->")
    print("Retrieving: => " + serviceurl + name)
    data = urllib.request.urlopen(serviceurl + name).read().decode()
    js = json.loads(data)
    print("Predicted age is : " + str(js['age']))


def genderizeapi(serviceurl):
    print('-----------------------------To predict your gender using name------------------------------------')
    name = input("Enter your name: ->")
    print("Retrieving: => " + serviceurl + name)
    data = urllib.request.urlopen(serviceurl + name).read().decode()
    js = json.loads(data)
    print("Predicted gender is : " + str(js['gender']))
    return js['gender']  # use if it is required based on your program


def ipifyapi(serviceurl):
    print('-----------------------------To find your public IP------------------------------------')
    print("Retrieving: => " + serviceurl)
    data = urllib.request.urlopen(serviceurl).read().decode()
    js = json.loads(data)
    print("Your public IP is : " + str(js['ip']))
    return js['ip']  # use if it is required based on your program


def geoipapi(serviceurl):
    print('-----------------------------To find locations based on IP------------------------------------')
    print("Retrieving: => " + serviceurl)
    data = urllib.request.urlopen(serviceurl + ipifyapi(serviceurl='https://api.ipify.org?format=json')).read().decode()
    js = json.loads(data)
    print("Your IP Country is : " + js['country_name'])
    print("Your IP Region is : " + js['region_name'])
    print("Your IP city is : " + js['city'])
    print("Your Time zone is : " + js['time_zone'])
    # more datas u can print based on the json format like latitude, longitude etc..


def itunessearchapi(serviceurl):
    # have fun with ITUNES API
    print('-----------------------------To get songs URL etc..------------------------------------')
    print("Retrieving: => " + serviceurl)
    address = input("Enter Author name: -> ")
    songs_limit = input("Enter songs Limits: -> ")  # if needed u can give limits but sometimes ir results in a error
    serviceurl = serviceurl + urllib.parse.urlencode({'term': address, 'limit': songs_limit})
    print(serviceurl)
    data = urllib.request.urlretrieve(serviceurl, '/users/drda/projects/sample/songs.json')
    with open('songs.json', 'r') as f:
        datas = f.read()
        js = json.loads(datas)
        js = js['results']
        for ele in js:
            if ele['primaryGenreName'] == 'Tamil' or ele['primaryGenreName'] == 'tamil':
                print('Go to this url: -> ' + ele['trackViewUrl'])
                print('Preview URL only 30 seconds sample audio: -> ' + ele['previewUrl'])
                print("Collection Name: -> " + ele['collectionCensoredName'])
                print("Collection Release date: -> " + ele['releaseDate'].split('T')[0])
                print("Track Name: -> " + ele['trackCensoredName'])


def jokeapi(serviceurl):
    print('-----------------------------To print Jokes------------------------------------')
    from urllib.request import Request, urlopen
    print("Retrieving: => " + serviceurl)
    req = Request(serviceurl, headers={'User-Agent': 'Mozilla/5.0'})
    data = urlopen(req).read().decode()
    js = json.loads(data)
    ''' These try and except blocks are used because the jokes key may vary in respected api '''
    try:
        print(js['setup'])
        print(js['delivery'])
    except:
        print(js['joke'])


def nationalizeapi(serviceurl):
    print('-----------------------------To check Country id------------------------------------')
    name = input("Enter your name: ->")
    print("Retrieving: => " + serviceurl + name)
    data = urllib.request.urlopen(serviceurl + name).read().decode()
    js = json.loads(data)
    ''' The api is not much good.. its just for reference  '''
    try:
        print("Your predicted Country id is: " + js['country'][0]['country_id'])
    except:
        print("Sorry I cant predict...")
    # print("Predicted nationality is : " + str(js['nationality']))
    # return js['nationality']  # use if it is required based on your program


def showpublicapis(serviceurl):
    # this is main function where u can find bunch of freee api links and u can make use of it any projects
    print('----------------------------To get Free API links-------------------------------')
    print("Retrieving: -> " + serviceurl)
    data = urllib.request.urlopen(serviceurl).read().decode()
    js = json.loads(data)
    # print(js)
    for data in js['entries']:
        print(data['Description'] + " url is: " + data['Link'])


def ocr_space_url(overlay=False, api_key='must specify your own apikey', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7 Register here to get free api key: -> https://ocr.space/ocrapi
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """
    print("------------------------------To convert Image to text-----------------------------")
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    filename = input("Enter file path: -> ")
    try:
        with open(filename, 'rb') as f:
            print("Parsing data: -> https://api.ocr.space/parse/image")
            r = requests.post('https://api.ocr.space/parse/image',
                              files={filename: f},
                              data=payload,
                              )
    except:
        r = 0
        print("Oops! File not found.. Provide a valid path")
    # for posting data to webserver urllib is difficult compared to this requests module
    # in other functions even u can use this requests module but iam doing course based on urllib so i prefered to use that..
    if r != 0:
        js = json.loads(r.content.decode())
        return js['ParsedResults'][0]['ParsedText']


def openweathermap(serviceurl, api_key='paste your api keys or u can give ur keys in a function call also'):
    import datetime
    # get your api key here https://home.openweathermap.org/ and paste in that function
    print('----------------------------To show Current weather in your city--------------------------------')
    city = input("Enter City name: -> ")
    payload = {'q': city, 'appid': api_key}
    url = 'https://' + serviceurl + urllib.parse.urlencode(payload)
    print("Retrieving: -> " + url)
    d = urllib.request.urlopen(url).read().decode()
    js = json.loads(d)
    print(js)
    print("Your city Current weather status : " + js['weather'][0]['description'])
    print("Your city Current Tempearture    : " + str(js['main']['temp']))
    print("Your city Current Pressure       : " + str(js['main']['pressure']))
    print("Your city Current wind speed     : " + str(js['wind']['speed']))
    print("Sunrise  :     {:>25}".format(str(datetime.datetime.fromtimestamp(js['sys']['sunrise']))))
    print("Sunset   :     {:>25}".format(str(datetime.datetime.fromtimestamp(js['sys']['sunset']))))


def omdbapi(serviceurl, api_key='f2faaef3'):
    print('----------------------------To get movies related data from web-------------------------------')
    type = input("Enter type whether movie, series or episode : -> ")
    title = input(
        "Enter movie/series/episode title : -> ")  # if needed u can get release year as input from the user and pass it to payload like {'y': year}
    payload = {'apikey': api_key, 'type': type, 't': title}
    url = serviceurl + urllib.parse.urlencode(payload)
    print("Retrieving: -> " + url)
    d = urllib.request.urlopen(url).read().decode()
    js = json.loads(d)

    print(title.capitalize() + ' ' + type.capitalize() + " Poster URL  : -> " + str(js['Poster']))
    print(title.capitalize() + ' ' + type.capitalize() + " Released on : -> " + str(js['Released']))
    print(title.capitalize() + ' ' + type.capitalize() + " Runtime     : -> " + str(js['Runtime']))
    print(title.capitalize() + ' ' + type.capitalize() + " Director    : -> " + str(js['Director']))
    print(title.capitalize() + ' ' + type.capitalize() + " Writer      : -> " + str(js['Writer']))
    print(title.capitalize() + ' ' + type.capitalize() + " Actors      : -> " + str(js['Actors']))
    print(title.capitalize() + ' ' + type.capitalize() + " Description : -> " + str(js['Plot']))


def meetupapi(serviceurl):
    print(
        '----------------------here u can see how many meetings are currently running throughout the world--------------')
    topic_name = input("Enter any topic name: -> ")
    payload = {'query': topic_name}
    url = serviceurl + urllib.parse.urlencode(payload)
    print("Retrieving: => " + url)
    d = urllib.request.urlopen(url).read().decode()
    js = json.loads(d)
    count = 0
    for ele in js:
        # print(ele) #if u need u can un comment and see urlkey and all kinds of stuffs as a key value pairs
        count += 1
    print("Totally " + str(count) + ' meetings happening in topic of ' + topic_name)


def calendarapi(serviceurl, apikey='f96fcb013f4367955723f5a5fbe3e990e2055299'):
    ''' Even more u can do with these apis u can get type as input from user and add it to payload dictionary'''
    print('-------------------------Here u can get public holidays date--------------------------')
    year = int(input("Enter Year : ->  "))
    # month = int(input("Enter Month[1-12] : ->  ")) # optional u can uncomment and use it
    # day = int(input("Enter Date[1-31] : ->  ")) # optional u can uncomment and use it
    country_code = input(
        "Enter Your Country code : -> ")  # u can refer here for list of country codes  Link: https://calendarific.com/supported-countries
    payload = {'api_key': apikey, 'country': country_code, 'year': year}  # , 'month': month, 'day': day}
    url = serviceurl + urllib.parse.urlencode(payload)
    print("Retrieving: => " + url)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read().decode()
    js = json.loads(data)
    # print(js)
    if js['meta']['code'] == 200:
        holidays = js['response']['holidays']
        print("*****************Holidays******************")
        if holidays != []:
            for ele in holidays:
                print('--------------------------------------------')
                print("Holiday Date: " + ele['date']['iso'])
                print("Holiday Name: " + ele['name'])
                print("Holiday Description: " + ele['description'])
                print("Holiday Type: " + ''.join(ele['type']))
        else:
            print("Sorry No holidays found")
    else:
        print("Argh! some error in your inputs...")


def faceplusapi(serviceurl, apikey='Paste your respective apikey here',
                apisecret='paste your api secret key u can find in below link'):
    # Link: -> https://console.faceplusplus.com/register ( register here and get respective api keys and secrets
    print("------------------------------To detect face-----------------------------")
    payload = {'api_secret': apisecret,
               'api_key': apikey,
               'return_attributes': 'gender,smiling,age,headpose,facequality,emotion,beauty,skinstatus,mouthstatus'
               }
    filename = input("Enter file path: -> ")
    try:
        with open(filename, 'rb') as f:
            print("Parsing data: -> " + serviceurl)
            r = requests.post(serviceurl,
                              files={'image_file': f},
                              data=payload,
                              )
    except:
        r = 0
        print("File Not Found Provide correct path! ")
    # for posting data to webserver urllib is difficult compared to this requests module
    # in other functions even u can use this requests module but iam doing course based on urllib so i prefered to use that..
    if r != 0:
        js = json.loads(r.content.decode())
        for ele in js['faces']:  # even u can parse more datas from api by giving extra aruments in payload respectively
            print("Predicted Gender from the image: -> " + ele['attributes']['gender']['value'])
            print("Predicted Age from the image: -> " + str(ele['attributes']['age']['value']))
            print("Predicted Emotions from the image: -> " + str(ele['attributes']['emotion']))
            print("Predicted Face beauty MaleScore from the image: -> " + str(
                ele['attributes']['beauty']['male_score']))
            print("Predicted Face beauty FemaleScore from the image: -> " + str(
                ele['attributes']['beauty']['female_score']))


def clashofclansapi(serviceurl,
                    apikey='''paste your api key here'''):
    # get coc api key from here Link: -> https://developer.clashofclans.com/#/register
    """
    Search for clans with specific criteria
    params: {
      "name": 'SomeClanName',
      "warFrequency": ['always', 'moreThanOncePerWeek','oncePerWeek','lessThenOncePerWeek','never','Unknown'],
      "locationId": 1,
      "minMembers": 20,
      "minClanPoints": 1200,
      "minClanLevel": 1-10,
      "limit": 5,
      "after": 2,
      "before": 100
    }
    """
    print("-----------------------------To get Clash of Clans game data---------------------------------------"
    clantag = input("Enter Any Clan Tag: -> ")
    url = serviceurl + clantag[1:]
    print("Retreiving : => " + url)
    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer " + apikey
    }

    req = requests.get(url, headers=headers)

    r = req.content.decode()
    js = json.loads(r)
    try:
        print("Clan Tag             : " + js['tag'])
        print("Clan Name            : " + js['name'])
        print("Clan Type            : " + js['type'])
        print("Clan Description     : " + js['description'])
        print("Clan Location        : " + js['location']['name'])
        print("Clan Level           : " + str(js['clanLevel']))
        print("Clan Points          : " + str(js['clanPoints']))
        print("Clan VersusPoints    : " + str(js['clanVersusPoints']))
        print("Clan Req. Trophies   : " + str(js['requiredTrophies']))
        print("Clan WarFrequency    : " + js['warFrequency'])
        print("Clan War Win Streak  : " + str(js['warWinStreak']))
        print("Clan Total War wins  : " + str(js['warWins']))
        print("Clan War League      : " + js['warLeague']['name'])
        print("Total Clan Members   : " + str(js['members']))
        print("Clan Members List with Name and Tag: -> ")
        print(
            '-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' {:<18}  {:<18}  {:<18}  {:<18}  {:<18}  {:<18}  {:<18}  {:<18} '.format('Clan Rank', 'Name', 'Tag',
                                                                                        'Role', 'ExpLevel',
                                                                                        'CurrentLeague', 'Trophies',
                                                                                        'Troops Donated'))
        print(
            '-------------------------------------------------------------------------------------------------------------------------------------------------------------')
        for ele in js['memberList']:
            print("{:^18}  {:<18}  {:<18}  {:<18}  {:^18}  {:<18}  {:^18}  {:^18}".format(ele['clanRank'],
                                                                                          ele['name'], ele['tag'],
                                                                                          ele['role'], ele['expLevel'],
                                                                                          ele['league']['name'],
                                                                                          ele['trophies'],
                                                                                          ele['donations']))


    except KeyError:
        print("Clan tag is invalid! try different one")


def fetchpokemonapi(serviceurl):
    limit = input("Enter pokemon Limit : -> ")
    payload = {'limit': limit}
    print("Retrieving: => " + serviceurl)
    r = requests.get(serviceurl, params=payload)
    js = r.json()
    pokes = []
    for ele in js['results']:
        pokes.append(ele['name'])
    for poke in sorted(pokes):
        # here u can start sorting based on pokemon firstletter or lastletter and print(js) it will give more data about pokemons
        print(poke)


def covid19api(serviceurl):
    # state = input("Enter State Name : -> ")
    print("-------------------------------------To get coivid19 cases in India--------------------------------------------"
    print("Retrieving: => " + serviceurl)
    r = requests.get(serviceurl)
    js = r.json()
    # print(js)
    '''statelst = []
    for i in js:
        statelst.append(i['state'])'''
    for ele in js:
        print("-----------------------" + ele['state'] + '----------------------')
        print("Total number of cases    : " + str(ele['noOfCases']))
        print("Active cases             : " + str(ele['active']))
        print("Recovered cases          : " + str(ele['cured']))
        print("Death cases              : " + str(ele['deaths']))
def nandyflames(serviceurl):
    # This is my own website created using Django and deployed using heroku
    # The website link is: -> https://nandy-flamesgame.herokuapp.com/
    # In your virtual environment you must have installed this external module or use this line in your terminal " pip install bs4"
    from bs4 import BeautifulSoup  # here i have used bs4 module to parse html data
    name1 = input("Enter Your Name: ")
    name2 = input("Enter Another Name: ")
    print("Retrieving: -> https://nandy-flamesgame.herokuapp.com/")
    post_request = requests.session()
    post_request.get(serviceurl)
    csrftoken = post_request.cookies['csrftoken']
    # now the csrftoken cookie is stored in csrftoken
    r = post_request.post(serviceurl, data={'n1': name1, 'n2': name2, 'csrfmiddlewaretoken': csrftoken},
                          headers=dict(Referer=serviceurl))
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    data = soup('h2')
    for d in data:
        print(d.text)


# agifyapi(serviceurl='https://api.agify.io/?name=')
# genderizeapi(serviceurl='https://api.genderize.io/?name=')
# ipifyapi(serviceurl='https://api.ipify.org?format=json')  # for ipv4
# ipifyapi(serviceurl='https://api6.ipify.org?format=json')  # for ipv6
# geoipapi(serviceurl='https://freegeoip.app/json/')
# itunessearchapi(serviceurl='https://itunes.apple.com/search?')
# jokeapi(serviceurl='https://sv443.net/jokeapi/v2/joke/Any')
# nationalizeapi(serviceurl='https://api.nationalize.io?name=')
# showpublicapis(serviceurl='https://api.publicapis.org/entries')
# print(ocr_space_url())
# openweathermap(serviceurl='api.openweathermap.org/data/2.5/weather?')
# omdbapi('http://www.omdbapi.com/?')
# meetupapi(serviceurl='https://api.meetup.com/find/topics?')
# calendarapi('https://calendarific.com/api/v2/holidays?')
# print(get_domains().content.decode())
# faceplusapi(serviceurl='https://api-us.faceplusplus.com/facepp/v3/detect')
# clashofclansapi('https://api.clashofclans.com/v1/clans/%23')
# fetchpokemonapi('https://pokeapi.co/api/v2/pokemon')
# covid19api('https://api.covid19api.com/live/country/')
# covid19api('https://covid-india-cases.herokuapp.com/states')
# nandyflames(serviceurl='https://nandy-flamesgame.herokuapp.com/')

print("Created by " + __author__)
