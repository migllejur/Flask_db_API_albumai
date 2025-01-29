// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/albumai')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('albumai-body');
            tbody.innerHTML = '';

            data.forEach(albumas => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${album.id}</td>
                    <td>${album.atlikejas}</td>
                    <td>${album.pavadinimas}</td>
                    <td>${album.metai}</td>
                    <td>${album.zanras}</td>
                    <td>${album.kainu_vidurkis}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

