const regionButton = document.querySelector('#region-button')
const regionList = document.querySelector('#region-list')
const regions = regionList.querySelectorAll('li')
const arrow = document.querySelector('#arrow')

regionButton.addEventListener('click', () => {
  regionList.classList.toggle('hidden')
  if (regionList.classList.length === 2) {
    arrow.classList.remove('bi-arrow-up-short')
    arrow.classList.add('bi-arrow-down-short')
  } else {
    arrow.classList.remove('bi-arrow-down-short')
    arrow.classList.add('bi-arrow-up-short')
  }
})