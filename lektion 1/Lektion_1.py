from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
#print(page)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
#print(html)

title_index = html.find("<title>")
#print(title_index) # Returns index of the opening <title> tag, 14

start_index = title_index + len("<title>")
# print(start_index) #returns index of the first letter in the titel, 21

end_index = html.find("</title>")
#print(end_index) #returns index of closing </title>, 39

title = html[start_index:end_index]
#print(title) #returns titel, Profile: Aphrodite

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
#print(title) #returns some html with the titel

