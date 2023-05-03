// rating
const rating = document.getElementById('rating')
const stars = rating.querySelectorAll('input')
const postRate = document.getElementById('rating').dataset.rating

const tmp = rating.querySelectorAll('label')
const children = Array.from(tmp)

const update = document.getElementById('update')

const printCurrentRate = () => {
  const selectedChildren = children.slice(0, postRate)
  selectedChildren.forEach(star => {
    star.textContent = "★"
  });
}

const cancelUpdate = () => {
  const selectedChildren = children.slice(0, postRate)
  children.forEach(star => {
    star.textContent = "☆"
  })
  selectedChildren.forEach(star => {
    star.textContent = "★"
  });
  update.classList.add('hidden')
}

stars.forEach(star => {
  // 기존 rating
  printCurrentRate()

  // rating 클릭 이벤트
  star.addEventListener('click', () => {
    update.classList.remove('hidden')
    const selectedRate = star.value
    const selectedChildren = children.slice(0, selectedRate)
    children.forEach(star => {
      star.textContent = "☆"
    })
    selectedChildren.forEach(star => {
      star.textContent = "★"
    });
    checkSame()
  })
});

// rating update 취소
update.addEventListener('click', () => {
  cancelUpdate()
})

const checkSame = () => {
  const labels = document.querySelectorAll('label')
  const countArray = Array.from(labels)
  const count = countArray.filter(label => label.textContent === '★').length

  if (count == postRate) {
    update.classList.add('hidden')
  }
}