(function () {
    const header = document.querySelector('.header');
    const menu = document.querySelector('.mobile-menu');
    const listLink = document.querySelectorAll('.list-link');

    // Expands the mobile menu
    menu.addEventListener('click', () => {
        [header, menu].forEach(element => {
            element.classList.toggle('active');
        })
    })

    // Expands the mobile drop-down menu
    listLink.forEach(element => {
        element.addEventListener('click', () => {
            if (element.classList.contains('active')) {
                element.classList.remove('active');
                element.nextElementSibling.classList.remove('active');
            } else {
                listLink.forEach(element => {
                    element.classList.remove('active');
                    element.nextElementSibling.classList.remove('active');
                })

                element.classList.add('active');
                element.nextElementSibling.classList.add('active');
            }
        })
    })
})()