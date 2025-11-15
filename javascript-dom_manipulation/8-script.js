document. add EventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.com/api?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.querySelector('#hello').textContent = data.hello;
        });
});
