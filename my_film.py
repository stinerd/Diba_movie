import requests
from inscriptis import get_text
import sys
from time import sleep
from bs4 import BeautifulSoup
import re
import wget
import os
from urlextract import URLExtract
def print_slow_3(words):
    str(words)
    for char in str(words):
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
        char.replace("%","")

def Points():
    link = requests.get("http://mydiba.link")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    link_movie_pints = soup.find_all('div' , class_="post-infos-index")
    for point in link_movie_pints:
        point = str(point)
        urls_point = get_text(point)
        sleep(1)
        print("About the movie\n\n","IMdb",urls_point,"\n\n")
# def movie():
#     link = requests.get("http://mydiba.link")
#     url = link.text
#     soup = BeautifulSoup(url, "html.parser")
#     link_movie_pints = soup.find_all('article' , class_="movie")
#     for point in link_movie_pints:
#         point = str(point)
#         urls_point = get_text(point)
#         sleep(1)
#         print("About the movie\n\n","IMdb",urls_point,"\n\n")

print_slow_3("Diba movie Download new film ;(  ")


def film():
    extractor = URLExtract()
    link = requests.get("http://mydiba.link")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    link_movie = soup.find_all('h2' , class_="post-titles")
    link_movie_pints = soup.find_all('div' , class_="post-infos-index")
    for point in link_movie_pints:
        point = str(point)
        urls_point = get_text(point)


    data = urls_point
    print(data)
    for name_movie in link_movie:
        string = str(name_movie)
        urls = extractor.find_urls(string)
        dl_url = str(urls)
        ddr = dl_url.replace("[","")
        ddr = ddr.replace("]","")
        ddr = ddr.replace("'","")
        string_txt = get_text(string)
        sleep(1)
        print("\n\n",string_txt,"\n\nurl -->",ddr, "\n\n")
def movie():

    link = requests.get("http://mydiba.link")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    link_movie_pints = soup.find_all('article' , class_="movie")
    for point in link_movie_pints:
        show_link = point.find_all('h2' , class_="post-titles")
        extractor = URLExtract()
        point = str(point)
        urls_point = get_text(point)
        urls_imdb = show_link
        str_url = str(urls_imdb)
        ext = extractor.find_urls(str_url)
        dl_url = str(ext)
        ddr = dl_url.replace("[","")
        ddr = ddr.replace("]","")
        ddr = ddr.replace("'","")
        d_tir = ddr
        sleep(1)

        print("\n\n","About the movie\n\n","Link :-->",ddr,"\n\n",urls_point,"\n")
    ##############################################################################3
        dl = input("Select iteme \n\n1-Download type(dl)\n2-Next_Movie type(n) \n3-exit type(exit)\n\n   Please Type : ")
        if dl == "dl":
            extractor_dl = URLExtract()
            url_dl = requests.get(ddr)
            url_new_dl = url_dl.text
            soup = BeautifulSoup(url_new_dl, "html.parser")
            link_movie_dl = soup.find_all('a' , class_="dublboxa")
            down = link_movie_dl
            for  a in down:
                if re.findall('http.*\.mkv', a['href']):
                    link_for_dl = a
                    string_for_dl = str(link_for_dl)
                    for_down = extractor.find_urls(string_for_dl)

                    downloader_db = str(for_down)
                    ddr_db = downloader_db.replace("[","")
                    ddr_db = ddr_db.replace("]","")
                    ddr_db = ddr_db.replace("'","")
                    print(ddr_db)
                    sleep(1)
                    os.system("mkdir  Diba_movie")
                    wget.download(ddr_db)
                    os.system("mv *.mkv /Diba_movie")
        if dl == "n":
            pass

        if dl == "exit":
            sys.exit()

        if dl == "tir":
            extractor_dl = URLExtract()
            tir = requests.get(d_tir)
            sleep(10)
            tir_text = tir.text

            soup = BeautifulSoup(tir_text, "html.parser")


            link_t =  soup.find_all('p', class_="text-justify")



            print(link_t)
            sleep(60)

    extractor = URLExtract()
    link = requests.get("http://mydiba.link/top-250-imdb/")
    url = link.text
    soup = BeautifulSoup(url, "html.parser")
    mydivs = soup.find_all('a', class_="bxof")
    my = str(mydivs)
    urls = extractor.find_urls(my)


movie()
