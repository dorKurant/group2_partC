const btns = document.querySelectorAll('.imgButton');
btns.forEach(btn => {
    btn.addEventListener('mouseover', (e) => {
        e.preventDefault();
        console.log('click');
        if(e.target.id!=='house'){
            e.target.style.width = '200px';
            e.target.style.height = '250px';
        }

    });
    btn.addEventListener('mouseout', (e) => {
        e.preventDefault();

        if (e.target.id!=='house'){
             e.target.style.width = '170px';
             e.target.style.height = '210px';
        }
    })


});

