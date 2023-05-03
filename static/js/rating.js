// rating
const rating = document.getElementById('rating')
rating.style.cursor = 'pointer'
const stars = rating.querySelectorAll('input')
stars.forEach(star => {
  star.addEventListener('click', () => {
    const selectedRate = star.value
    const tmp = rating.querySelectorAll('label')
    const children = Array.from(tmp)
    const selectedChildren = children.slice(0, selectedRate)
    children.forEach(star => {
      star.textContent = "☆"
    })
    selectedChildren.forEach(star => {
      star.textContent = "★"
    });
  })
});