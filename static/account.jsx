const accountWatchlist = document.querySelectorAll('#removemovie');

for (let i = 0; i < accountWatchlist.length; i++){
        accountWatchlist[i].addEventListener('submit', (evt) => {
            evt.preventDefault();
            const choice = accountWatchlist[i]
            const movie = choice.querySelector('#movie').value;
            console.log(choice);
            console.log(movie);

            fetch(`/removefromwatchlist?movie=${movie}`)
            .then((response) => response.text())
            .then((data) => {const flashmessage = data
                
                console.log(flashmessage)
                location.reload()
            })}
            )}; 

const RateMovie = document.querySelectorAll('#ratemovie');

for (let i = 0; i < RateMovie.length; i++){
    RateMovie[i].addEventListener('submit', (evt) => {
            evt.preventDefault();
            const choice = RateMovie[i]
            const rating = choice.querySelector('#rating').value;
            const movie = choice.querySelector('#movie_id').value;
            console.log(choice);
            console.log("rating:", rating);
            console.log("movie:", movie);
            
            
            fetch(`/ratemovie?rating=${rating}&movie=${movie}`)
            .then((response) => response.text())
            .then((data) => {const flashmessage = data
                            
                console.log(flashmessage)
                location.reload()
                })}
                )}; 
            