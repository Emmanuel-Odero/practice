from requests_html import HTML

with open('../siteToScrape.html') as html_file:
	source = html_file.read()
	html =  HTML(html=source)


print(html.html)

#we can alternatively type the text as follows
print(html.text)