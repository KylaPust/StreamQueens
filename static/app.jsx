const get_movies = document.querySelector('#get-movies');

    get_movies.addEventListener('submit', (evt) => {
        evt.preventDefault();

        const genre = document.querySelector('#genre-id').value;
        const exclude_watchlist = document.querySelector('#exclude_watchlist').value;
        const result_type = document.querySelector('#result_type').value;
        const selectedOptions = document.querySelectorAll("#service option:checked");
        const service = [...selectedOptions].map(s=>s.value);
        // console.log(selectedOptions);
        document.querySelector('#title').innerHTML = "";
        fetch(`/createdsearch?genre-id=${genre}&service=${service}&result_type=${result_type}&exclude_watchlist=${exclude_watchlist}`)
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
                 const keyRender = ('<div id="searchpad" class="col-4 d-flex align-items-stretch""><div class="card card-block" style="width: 20rem;"><img class="card-img-top" src='
                 + '"' + keyPoster + '"' + 'alt=' + '“' + keyTitle + '“' + 
                 '> <div class="card-body"><h5 class="card-title”>' + keyTitle + 
                 '</h5><p class="card-text”>' + keyTitle + '</p><a class="header-center" href=' +  link + ' ' + 'class="btn btn-success">Go to ' + streamingsite 
                 + '</a><p><form action="/addtowatchlist" id="rendered_list"'+
                 'value="'+dataJson[key]+'"><button class="btn btn-outline-light" type="submit" id="movie" value="'+
                 dataJson[key]['movie_id'] +'">Add to Watchlist</button></form></div></div>');

                document.querySelector('#title').insertAdjacentHTML('beforeend', keyRender)};
                // innerHTML = dataJson["1922"]["title"];

                const watchlist = document.querySelectorAll('#rendered_list');

                for (let i = 0; i < watchlist.length; i++){
                watchlist[i].addEventListener('submit', (evt) => {
                    evt.preventDefault();
                    const choice = watchlist[i]
                    const movie = choice.querySelector('#movie').value;
                    console.log(choice);
                    console.log(movie);

                    fetch(`/addtowatchlist?movie=${movie}`)
                    .then((response) => response.text())
                    .then((data) => {const flashmessage = data
                        
                        console.log(flashmessage)
                        

                    
                    
                    
                    })}
                )};
            });   
    });
    
