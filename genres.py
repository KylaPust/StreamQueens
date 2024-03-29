import requests

url = "https://streaming-availability.p.rapidapi.com/genres"

headers = {
	"X-RapidAPI-Key": "key",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

#Results:
{"1":"Biography",
"10402":"Music",
"10749":"Romance",
"10751":"Family",
"10752":"War",
"10763":"News",
"10764":"Reality",
"10767":"Talk Show",
"12":"Adventure",
"14":"Fantasy",
"16":"Animation",
"18":"Drama",
"2":"Film Noir",
"27":"Horror",
"28":"Action",
"3":"Game Show",
"35":"Comedy",
"36":"History",
"37":"Western",
"4":"Musical",
"5":"Sport",
"53":"Thriller",
"6":"Short",
"7":"Adult",
"80":"Crime",
"878":"Science Fiction",
"9648":"Mystery",
"99":"Documentary"}