//  좋아요 ajax 
const forms = document.querySelectorAll('.like_forms')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
forms.forEach(form => {
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const articleId = event.target.dataset.articleId
    axios({
      method: 'post',
      url: `/articles/${articleId}/likes/`,
      headers: {'X-CSRFToken': csrftoken},
    })
      .then((response) => {
        const isLiked = response.data.is_liked
        const likeBnt = document.querySelector(`#like-${articleId}`)
        // if (isLiked === true) {
        //   likeBnt.value = '좋아요 취소'
        // } else {
        //   likeBnt.value = '좋아요'
        // }
        const likesCountData = response.data.likes_count
        const likesCountTag = document.querySelector(`#likes-count`)
        likesCountTag.textContent = likesCountData
      })
  })
})

// 북마크 ajax 
const bookmark_forms = document.querySelectorAll('.bookmark_forms')
const bm_csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
bookmark_forms.forEach(form => {
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const articleId = event.target.dataset.articleId
    axios({
      method: 'post',
      url: `/articles/${articleId}/bookmark/`,
      headers: {'X-CSRFToken':bm_csrftoken},
    })
      .then((response) => {
        const isbookmarked = response.data.isbookmarked
        const bookmarkBnt = document.querySelector(`#bookmark-${articleId}`)
        // if (isbookmarked === true) {
        //   bookmarkBnt.value = 'bookmark 취소'
        // } else {
        //   bookmarkBnt.value = 'bookmark'
        // }
        const bookmarkCountData = response.data.bookmark_count
        const bookmarkCountTag = document.querySelector(`#bookmark-count`)
        bookmarkCountTag.textContent = bookmarkCountData
      })
  })
})

// comment 좋아요 ajax 
const commentforms = document.querySelectorAll('.comment_like_forms')
const r_csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
commentforms.forEach(form => {
  form.addEventListener('submit', function (event) {  
    event.preventDefault()
    const articleId = event.target.dataset.articleId;
    const commentId = event.target.dataset.commentId;
    axios({
      method: 'post',
      url: `/articles/${articleId}/comments/${commentId}/likes/`,
      headers: {'X-CSRFToken': r_csrfToken},
    })
    .then((response) => {
      const isLiked = response.data.r_is_liked
      const likeBnt = document.querySelector(`#like-${commentId}`)
      const likesCountData = response.data.r_likes_count
      const likesCountTag = document.querySelector(`#r_likes_count_${commentId}`)
      likesCountTag.textContent = likesCountData

      location.reload();
    })
    .catch((error) => {
      console.error(error);
    });
  });
});

// comment 싫어요 ajax 
const dis_commentforms = document.querySelectorAll('.comment_dislike_forms')
const dis_csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
dis_commentforms.forEach(form => {
  form.addEventListener('submit', function (event) {  
    event.preventDefault()
    const articleId = event.target.dataset.articleId;
    const commentId = event.target.dataset.commentId;
    axios({
      method: 'post',
      url: `/articles/${articleId}/comments/${commentId}/dislikes/`,
      headers: {'X-CSRFToken': dis_csrfToken},
    })
    .then((response) => {
      const isLiked = response.data.dis_is_liked
      const likeBnt = document.querySelector(`#dislike-${commentId}`)

      const likesCountData = response.data.dislikes_count
      const likesCountTag = document.querySelector(`#dislikes_count_${commentId}`)
      likesCountTag.textContent = likesCountData

      location.reload();
    })
    .catch((error) => {
      console.error(error);3
    });
  });
});





// // 댓글 ajax 
// // 새로운 댓글을 화면에 추가합니다.
// const commentForm = document.querySelector('#comment_form');
// commentForm.addEventListener('submit', (event) => {
//   event.preventDefault(); // 폼 전송을 취소합니다.

//   const formData = new FormData(commentForm);
//   const url = `/articles/${articleId}/comments/`;
//   fetch(commentForm.action, {
//     method: 'post',
//     body: formData,
//   })
//   .then(response => response.json())
//   .then(data => {
//     // 새로운 댓글을 화면에 추가합니다.
//     const commentList = document.querySelector('#comment-list');
//     const newComment = document.createElement('li');
//     newComment.innerHTML = `
//       <div class="comment-info">
//         <span class="comment-author">${data.author}</span>
//         <span class="comment-created">${data.created}</span>
//       </div>
//       <div class="comment-content">${data.content}</div>
//     `;
//     if (commentList) {
//       console.log('commentList exists');
//     }
//     commentList.appendChild(newComment);
    
//     // 폼을 초기화합니다.
//     commentForm.reset();
//   })
//   .catch(error => console.error(error));
// });

