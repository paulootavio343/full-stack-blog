(function () {
    const slide = document.querySelector('.trending-container');
    const article = document.querySelectorAll('.trending-container article');
    const buttonLeft = document.querySelector('.button-left');
    const buttonRight = document.querySelector('.button-right');

    let articleWidth = article[0].offsetWidth + 20;
    let counter = 0;

    function resetSlide() {
        window.addEventListener('resize', () => {
            articleWidth = article[0].offsetWidth + 20;
            counter = 0;
            slide.scrollLeft = 0;
        });
    }

    function moveSlide() {
        if (counter === article.length - 1) {
            counter = 0;
            slide.scrollLeft = 0;
        } else {
            counter++;
            slide.scrollLeft += articleWidth;
        }
    }

    function activateButtons() {
        buttonLeft.addEventListener('click', () => {
            if (counter === 0) {
                counter = article.length - 1;
                slide.scrollLeft += articleWidth * (article.length - 1);
            } else {
                counter--;
                slide.scrollLeft -= articleWidth;
            }
            clearInterval(slideInterval);
            slideInterval = setInterval(moveSlide, 10000);
        })

        buttonRight.addEventListener('click', () => {
            if (counter === article.length - 1) {
                counter = 0;
                slide.scrollLeft = 0;
            } else {
                counter++;
                slide.scrollLeft += articleWidth;
            }
            clearInterval(slideInterval);
            slideInterval = setInterval(moveSlide, 10000);
        })
    }

    resetSlide();
    activateButtons();
    let slideInterval = setInterval(moveSlide, 10000);
})()