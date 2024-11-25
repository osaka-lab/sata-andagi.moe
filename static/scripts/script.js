document.getElementById('search').addEventListener('submit', function(event) {
    event.preventDefault();
    const value = document.getElementById('input-search').value;
    window.location.href = `/memes?q=${encodeURIComponent(value)}`;
});