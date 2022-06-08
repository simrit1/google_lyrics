from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
# COPYRIGHT 2022 Nathan Koliha released under the MIT license
# superpotato9.com 
 
#  _______________           ______________          __________________________          ___________________
# |               |         |              |        |                          |        |                   |         _______
# | url from user |  ===>   | request sent |  ===>  | data from request turned |  ===>  |  text between two |  ====> | DONE! |
# |               |         |  to google   |        |  into plain text via bs4 |        |  points extracted |        |_______|
# |_______________|         |______________|        |__________________________|        |___________________|



# those two points are "/" and source: or if that raises error the second one is replaced with "/" 



def between(one, two, string):  # finds the text between two strings used to get the lyrics
         
    # getting index of substrings
        idx1 = string.index(one)
        idx2 = string.index(two)
      
    # length of substring 1 is added to
    # get string from next character
        res = string[idx1 + len(one) + 1: idx2]
        return res



def tag_visible(element): #tags all text areas that are visible 
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True


def text_from_html(body):  #extracts only stuff correspond to the func above
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)




class song: # main class for the package 
  def __init__(self, title, check_ssl): #title is the title of the song reccomended that you include artist name, check ssl is a bool true means it checks ssl certifs
    song = title.title()
    url = 'https://www.google.com/search/static?q=' + song.replace(' ','+') + '+lyrics' # makes a url for the song 
    html = requests.get(url, verify=check_ssl).content # requests the page
    all_data = text_from_html(html) #gets the html from the pae
    try:  # is this spaghetti code? ...yes does it work... yes 
        lyrics = between('/', ' Source:', all_data) # tries to get data from between / and source
    except ValueError: # if it is one of the few pages with wacky formatting it tries using / for both 
        try:
         lyrics = between('/', '/', all_data)
        except ValueError:
             lyrics = None
    self.lyrics = lyrics 

# the two lines below this are an example of how to use it 
#as_it_was = song("as it was", False)
#print(as_it_was.lyrics)



