const postImgs = document.querySelectorAll('.card-img-top')


postImgs.forEach((postImg) => {
  postImg.addEventListener("mouseenter", () => {
    const postBottom = postImg.nextElementSibling
    postBottom.classList.remove('card-bottom-hidden')
    });

  postImg.addEventListener("mouseleave", () => {
    const postBottom = postImg.nextElementSibling
    postBottom.classList.add('card-bottom-hidden')
    });

})