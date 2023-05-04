const regionButton = document.querySelector('#region-button')
const regionArrow = regionButton.querySelector('span')
const regionList = document.querySelector('#region-list')
const regions = regionList.querySelectorAll('li')
regionButton.addEventListener('click', () => {
  regionArrow.textContent = '<'
  regionList.classList.toggle('hidden')
  
  regions.forEach(region => {
    region.animate
  });
})

