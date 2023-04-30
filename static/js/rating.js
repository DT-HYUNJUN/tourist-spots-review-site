const stars = document.querySelectorAll('.star-rating input');
const ratingInput = document.querySelector('input[name="rating"]');

stars.forEach((star, index) => {
  star.addEventListener('click', () => {
    ratingInput.value = index + 1
    for (let i = 0; i < stars.length; i++) {
      if (i <= index) {
        stars[i].nextElementSibling.textContent = '★'
      } else {
        stars[i].nextElementSibling.textContent = '☆'
      }
    }
  })
})
