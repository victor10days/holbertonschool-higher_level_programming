fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        document.querySelector('#list_movies').appendChild(li);
    });
