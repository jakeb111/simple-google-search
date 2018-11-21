import requests
from bs4 import BeautifulSoup
import os
import webbrowser

while True:
    start = 0
    os.system('cls')
    query = input("Google Search: ")
    os.system('cls')
    option = 'n'
    while option == 'n' or option == 'l':
        print("Loading...")
        r = requests.get('https://www.google.com/search?q=' + query + "&start=" + str(start))
        os.system('cls')

        if r.status_code != 200:
            print("Request was not made with error code: " + r.status_code)
            break

        soup = BeautifulSoup(r.text, 'lxml')
        arr = soup.find_all(attrs={"class": "r"})
        print("Page " + str(int(start/10)+1) + ": " + query)
        for x in range(len(arr)):
            print(str(x+1+start) + ": " + arr[x].a.get_text())

        option = input("Next page(n), last page(l) or choose a link to open in your browser: ")

        os.system('cls')
        
        if option == 'n':
            start += 10
        elif option == 'l':
            if start != 0:
                start -= 10
        else:
            try:
                option = int(option)
            except:
                break
            if option > 0 and option <= len(arr):
                webbrowser.open_new_tab("https://www.google.com" + arr[int(option)-1].a.get('href'))
                input("Link opened in a new tab! Press enter to make another query.")