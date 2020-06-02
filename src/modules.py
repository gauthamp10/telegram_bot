import json
import random
import requests
from bs4 import BeautifulSoup
from faker import Faker
fake = Faker()

#----------------------------------------------------------------
def print_help():
    text='-------Services Offered--------\n'
    commands=['HD Wallpaper: /wallpaper\n','Random Gif: /gif\n','Random Meme: /meme\n','Random Joke: /joke\n','Random Video: /video\n','Random Quote: /quote\n','Random Profile: /profile\n','Currency Rates: /currency\n','Bitcoin Price: /bitcoin\n']
    for command in commands:
        text=text+command+"\n"
    return text+"\n       OR You can simply chat....."

def flag(code):
    code = code.upper()
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

#-----------------------------------------------------------------

def get_quote():
    data = requests.get('http://api.quotable.io/random').json()
    return data


def get_fake_data():
    try:
        license=fake.license_plate()
        ccno=fake.credit_card_number(card_type=None)
        profile=fake.profile(fields=None, sex=None)
        b_date=str(profile['birthdate'])
        latitude=str(profile['current_location'][0])
        longitude=str(profile['current_location'][1])
        dat="------------------------\n"
        dat=dat+"Name: "+profile['name']+"\n"
        dat=dat+"Sex:"+profile['sex']+"\n"
        dat=dat+"Birth date:"+b_date+"\n"
        dat=dat+"Blood Group: "+profile['blood_group']+"\n"
        dat=dat+"--------Address---------\n"
        dat=dat+profile['address']+"\n"
        dat=dat+"------------------------\n"
        dat=dat+"Residence: "+profile['residence']+"\n"
        dat=dat+"Job: "+profile['job']+"\n"
        dat=dat+"Email: "+profile['mail']+"\n"
        dat=dat+"Credit card: "+ccno+"\n"
        dat=dat+"License no: "+license+"\n"
        dat=dat+"Company:"+profile['company']+"\n"
        dat=dat+"Website:"+profile['website'][0]+"\n"
        dat=dat+"-------Current location-------\n[Lat:"+latitude+" "+"Long: "+longitude+"]\n"
        return dat
    except Exception as e:
        return "Service down temporarily! Please don't be upset."
        print("An error occured - ",str(e))

def get_image():
    try:
        xres=str(random.randint(1000,1440))+"/"
        yres=str(random.randint(650,1080))
        res=yres+xres
        image_data='https://source.unsplash.com/random/'+res
        return image_data
    except Exception as e:
        return "https://pbs.twimg.com/profile_images/562212925717241857/346KXLGh.png"
        print("An Error occured - ",str(e))
        pass

def get_bitcoin():
    try:
        bitcoin=requests.get('https://api.coindesk.com/v1/bpi/currentprice/INR.json',timeout=30).json()
        text="Bitcoin Live Price\n"+"-"*28
        text=text+"\n1 BTC ="+u"\u20B9"+bitcoin['bpi']['INR']['rate']
        text=text+"\n1 BTC ="+	u"\u0024"+bitcoin['bpi']['USD']['rate']
        return text
    except Exception as e:
        return "Service down temporarily! Please don't be upset."
        print("An Error occured- ",str(e))
        pass


def get_currency():
    tmp=list()
    s=''
    try:
        currency=requests.get('https://api.exchangeratesapi.io/latest?base=INR').json()
        for code,rates in currency['rates'].items():
            tmp.append("1 INR = "+str(round(rates,2))+str(" "+code))
        for item in tmp:
            s=s+item+"\n"
        return s
    except Exception as e:
        return "Service down temporarily! Please don't be upset."
        print("An Error occured - ",str(e))
        pass

def get_joke():
    try:
        joke=requests.get("https://official-joke-api.appspot.com/random_joke").json()
        joke=joke['setup']+"\n"+joke['punchline']
        return joke
    except Exception as e:
        return "Service down temporarily! Please don't be upset.\nThat's not a joke."
        print("An Error occured - ",str(e))
        pass
        

def get_meme():
    try:
        meme=requests.get("https://meme-api.herokuapp.com/gimme").json()
        return meme['url']
    except Exception as e:
        return "https://pbs.twimg.com/profile_images/562212925717241857/346KXLGh.png"
        print("An Error occured - ",str(e))
        pass

def get_gif():
    try:
        while True:
            gif=requests.get("https://api.giphy.com/v1/gifs/random?api_key=ZczhuGHOz7HDoDM4tUkRAdvyILcuR3RW&tag=&rating=G").json()
            gif_image=gif['data']['image_url']
            thumb=gif['data']['images']['480w_still']['url']
            caption=gif['data']['title']
            if gif_image.endswith(".gif"):
                return gif_image,thumb,caption
            else:
                pass
    except Exception as e:
        gif="http://s3.favim.com/orig/160123/black-and-white-error-grunge-Favim.com-3923949.gif"
        thumb="https://www.google.com/images/errors/robot.png"
        caption="Internal Server Error!"
        return gif,thumb,caption
        print("An Error occured - ",str(e))
        pass
def get_youtube():
    try:
        data=requests.get("https://www.randomyoutubevideos.com/")
        soup = BeautifulSoup(data.text,'html.parser')
        vid=soup.find('meta',attrs={'name':'og:url'})
        vid=vid['content'].split('?video=')[1]
        link="www.youtube.com/watch?v="+str(vid)
        return link
    except Exception as e:
        return "https://www.youtube.com/watch?v=TQSaPsKHPqs"
        print("An Error occured - ",str(e))
        pass



def search(query): 
    try:  
        address = "http://www.bing.com/search?q="+query

        htmlResult = requests.get(address,{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})

        soup = BeautifulSoup(htmlResult.text,'html.parser')

        [s.extract() for s in soup('span')]
        unwantedTags = ['a', 'strong', 'cite']
        for tag in unwantedTags:
            for match in soup.findAll(tag):
                match.replaceWithChildren()

        results = soup.findAll('li', { "class" : "b_algo" })
        
        title=str(results[0].find('h2')).replace(" ", " ")
        ret=str(results[0].find('p')).replace(" ", " ")
        ret=ret[3:]
        ret=ret[:-4]
        dat="Title -"+title+"\n "+"------------\n"+ret
        if ret== None:
            ret="Server Error!....Please retry..."
        return ret 
    except Exception as e:
        print("An Error occured- ",str(e))
        pass        

def get_book_data(query):
    i=0
    data=requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:'+query).json()
    title=data['items'][0]['volumeInfo']['title']
    subtitle=data['items'][0]['volumeInfo']['subtitle']
    publisher=data['items'][0]['volumeInfo']['publisher']
    publishedDate=data['items'][0]['volumeInfo']['publishedDate']
    author_no=len(data['items'][0]['volumeInfo']['authors'])
    category_no=len(data['items'][0]['volumeInfo']['categories'])
    pageCount=data['items'][0]['volumeInfo']['pageCount']
    maturityRating=data['items'][0]['volumeInfo']['maturityRating']
    imageLinks=data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    book_data=''
    book_data=book_data+"-----------------------------\n"
    book_data=book_data+"Title: "+title
    book_data=book_data+"\nSubtitle: "+subtitle
    book_data=book_data+"\nPublisher: "+publisher
    book_data=book_data+"\nPublished Date: "+publishedDate
    book_data=book_data+"\n------Authors------\n"
    while i<author_no:
        book_data=book_data+data['items'][0]['volumeInfo']['authors'][i]
        i=i+1
    i=0
    while i<category_no:
        book_data=book_data+data['items'][0]['volumeInfo']['categories'][i]
        i=i+1
    book_data=book_data+"\nPage count: "+str(pageCount)
    book_data=book_data+"\nMaturity Rating: "+maturityRating
    return book_data,imageLinks




def get_ist():
    ist=requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata').json()
    return ist["datetime"]
