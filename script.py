from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup



# Extract Movie data from IMDB 
def extract(url):
    
    # Get page data 
    response = requests.get(url)

    # check request status
    if response.status_code != 200:
        print("URL got error: " + str(response.status_code))
        return None


    # file = open("../scrapping/imdb.data","r")
    # body = file.read()

    # Create valiables
    body = response.text

    # parse response HTML body
    html = BeautifulSoup(body, 'html.parser')


    #==============================+Extracting Data+==================================================================================================================================
    # ________________Name________________
    name = html.find('h1').text

    # ________________Get Roles(Directors, Writers, Stars)________________
    roles = html.find_all(attrs={"class" : "ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt"})

    # ________________Directors________________ => list
    directors_d = roles[0].find_all(attrs={"class" : "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
    directors = []
    for director in directors_d : 
        directors.append(director.text)

    # ________________Writers________________ => list
    writers_d = roles[1].find_all(attrs={"class" : "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
    writers = []
    for writer in writers_d : 
        writers.append(writer.text)

    # ________________Stars________________ => list
    
    stars_d = roles[2].find_all(attrs={"class" : "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
    stars = []
    for star in stars_d : 
        stars.append(star.text)

    # ________________Tags________________ => list
    tags = []
    tags_d = html.find(attrs={"class" : "ipc-chip-list__scroller"})
    tags_d = tags_d.find_all("a")
    for tag in tags_d : 
        tags.append(tag.text)   

    # ________________Year________________ => int
    year = html.find(attrs={"class" : "ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"})
    year = int(year.text)

    # ________________Rate________________ => float
    rate = html.find(attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"})
    rate = float(rate.text.split("/")[0])

    # ________________Popularity________________ => up,down
    popu = html.find_all(attrs={"class": "ipc-icon"})



    #===============================================================================================================================================================================

    result = """
    Name: {name}
    Directors: {directors}
    Writers: {writers} 
    Stars: {stars} 
    Rate: {rate} 
    Year: {year}
    Tags: {tags}
    """
    #-------------------------------------+Extra Code+-------------------------------------|

    # #=============+Create Object+=============+

    # class Movie:
    #     def __init__(self, name, year, rate, writers, directors, stars, tags):
    #         self.name = name
    #         self.year = year
    #         self.rate = rate
    #         self.writers = writers
    #         self.directors = directors
    #         self.stars = stars
    #         self.tags = tags
            
    # obj = Movie(name, year, rate, writers, directors, stars, tags)
    # return obj

    # #=========================+Array+======================================
    
    # array_data = {"name" : name , "writers" : writers, "stars" : stars, "tags" : tags, "directors" : directors, "year" : year, "rate" : rate}
    # return = array_data
    #--------------------------------------------------------------------------------------|

    return result.format(name = name, directors = str(directors), writers = str(writers), stars = str(stars), rate = str(rate) , year = str(year), tags = str(tags))




#  Usage : 
url = "https://www.imdb.com/title/tt11671006/"

print(extract(url))

# Or

urls = [
    "https://www.imdb.com/title/tt0111161/",
    "https://www.imdb.com/title/tt0468562/",
    "https://www.imdb.com/title/tt0468563/", 
    "https://www.imdb.com/title/tt0073486/",
    "https://www.imdb.com/title/tt0114369/",
    "https://www.imdb.com/title/tt0047478/",
    "https://www.imdb.com/title/tt0038650/",
    "https://www.imdb.com/title/tt0102926/",
    "https://www.imdb.com/title/tt0317248/",       
        ]

for url in urls: 
    print(extract(url))


































