const btnp = document.querySelector('#plus');
const dropdownContent = document.querySelector('#dropdownContent');

btnp.addEventListener('click', (e) => {
    e.preventDefault();
    if (dropdownContent.style.display === 'none' || dropdownContent.style.display === '') {
        dropdownContent.style.display = 'flex';
    } else {
        dropdownContent.style.display = 'none';
    }
});