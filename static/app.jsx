// function APP() {
    // const [movies, setMovies] = React.userState({});

    // React.useEffect(() => {
    //     fetch('/createdsearch')
    //     .then((response) => response.json())
    //     .then((movieData) => {
    //         setMovies(movieData);

    //     });
    // }, []);

// ReactDOM.render(<App />, document.querySelector('#root'))

    const get_movies = document.querySelector('#get-movies');

    get_movies.addEventListener('submit', (evt) => {
        evt.preventDefault();

        const genre = document.querySelector('#genre-id').value;
        const result_type = document.querySelector('#result_type').value;
        const selectedOptions = document.querySelectorAll("#service option:checked");
        const service = [...selectedOptions].map(s=>s.value);
        // console.log(selectedOptions);
        document.querySelector('#title').innerHTML = "";
        fetch(`/createdsearch?genre-id=${genre}&service=${service}&result_type=${result_type}`)
        .then((response) => response.text())
        .then((data) => { const dataJson = JSON.parse(data)  
            const keys = Object.keys(dataJson);
            for (const key of keys) {
                // console.log(dataJson);
                // console.log(Object.keys(dataJson));
                 const keyTitle = dataJson[key]["title"]
                 const streamingsite = dataJson[key]['streaming']
                 const link = dataJson[key]["link"]
                 const keyPoster = ("https://image.tmdb.org/t/p/original" + dataJson[key]["poster_path"])
                 const keyRender = ("<li>" + keyTitle + "  on " + streamingsite + "<br>" + '<br></br>' 
                 + '<form action="/addtowatchlist"><input type="submit" value="Add to Watchlist"></form>' + "</li>" + "<a href=" + '"' + link + '">' +
                 "<img src=" + '"' + keyPoster + '"' 
                 + " " + 'width="300"' + " " + 'height="400"></a>');

                document.querySelector('#title').insertAdjacentHTML('beforeend', keyRender)};
                // innerHTML = dataJson["1922"]["title"];
            });   
    });
    