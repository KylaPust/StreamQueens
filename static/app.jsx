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
        // const service = document.querySelector('#service').value;
        console.log(genre);
        document.querySelector('#title').innerHTML = "";
        fetch(`/createdsearch?genre-id=${genre}`)
        .then((response) => response.text())
        .then((data) => { const dataJson = JSON.parse(data)  
            const keys = Object.keys(dataJson);
            for (const key of keys) {
                // console.log(dataJson);
                // console.log(Object.keys(dataJson));
                 const keyTitle = dataJson[key]["title"]
                 const keyPoster = ("https://image.tmdb.org/t/p/original" + dataJson[key]["poster_path"])
                 console.log(keyTitle, keyPoster);
                 const keyRender = ("<li>" + keyTitle + "<br>" + "<img src=" + '"' + keyPoster + '"' 
                 + " " + 'width="300"' + " " + 'height="400">' + "</li>");

                document.querySelector('#title').insertAdjacentHTML('beforeend', keyRender)};
                // innerHTML = dataJson["1922"]["title"];
            });   
    });
    
