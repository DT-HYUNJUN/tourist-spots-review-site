const forms = document.querySelectorAll(".like-form")
const csrftokenLike = document.querySelector("[name=csrfmiddlewaretoken]").value

forms.forEach((form) => {
  form.addEventListener('submit', function(e) {
    e.preventDefault()
    const postId = e.target.dataset.postId
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/posts/${postId}/likes/`,
      headers: { "X-CSRFToken": csrftokenLike},
    }).then((response) => {
      const isLiked = response.data.is_liked
      const likeBtn = document.querySelector(`#like-${postId}`)
      if (isLiked){
        likeBtn.className = 'bi bi-heart-fill'
      } else{
        likeBtn.className = 'bi bi-heart'
      }

      const likeCountTag = document.querySelector('#like-count')
      const likeCountData = response.data.like_count
      likeCountTag.textContent = likeCountData
    })
    .catch((error) => {
      console.log(error.response)
    })
  })
})