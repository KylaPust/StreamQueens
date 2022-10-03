import requests, users, os
from flask import jsonify

genres_dict = {"1":"Biography",
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


def get_api_results(genre, type, service):

	url = "https://streaming-availability.p.rapidapi.com/search/basic"

	#querystring = {"country":"us","service":"netflix","type":"movie","genre":"28","page":"1","output_language":"en","language":"en"}
	querystring = {"country":"us","service":{service},"type":{type},"genre":{genre}, "page":"1", "output_language":"en","language":"en"}

	headers = {
	"X-RapidAPI-Key": "secrets.sh",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	data = response.json()

	results = data['results']

	api_results = []

	for movie in results:
		
		title = movie['originalTitle']
		genre = movie['genres']
		overview = movie['overview']
		poster_path = movie['posterPath']
		#streaminginfo, net, us only used to get to link
		streaminginfo = movie['streamingInfo']
		#not returned
		net = streaminginfo[service]
		#not returned
		us = net['us']
		link = us['link']
		streaming = service
		movie_obj = users.create_movie(title, overview, poster_path, link, streaming)
		api_results.append(movie_obj)

	#return jsonify({movie.movie_id: movie.to_dict() for movie in api_results})
	return api_results