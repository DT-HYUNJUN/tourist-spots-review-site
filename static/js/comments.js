const comments = document.querySelectorAll('#comments')
const commentSubmit = document.getElementById('comment-submit')
const commentField = document.getElementById('comment-field')
const commentCount = document.getElementById('comment-count')
const commentArea = document.getElementById('comment-area')
const max = commentField.dataset.maxLength

comments.forEach(comment => {
  const deleteBtn = comment.querySelector('#comment_delete')

  comment.addEventListener('mouseover', () => {
    deleteBtn.classList.remove('hidden')
  })

  comment.addEventListener('mouseout', () => {
    deleteBtn.classList.add('hidden')
  })
})

if (commentField.value.length === 0) {
  commentCount.textContent = ''
}

commentField.addEventListener('input', (e) => {
  const count = commentField.value.length
  commentCount.textContent = `${count} / ${max}`
  if (count >= max) {
    commentCount.textContent = `${max} / ${max}`
  }
})

commentArea.addEventListener('click', () => {
  commentField.focus()
})

function resize(obj) {
  obj.style.height = ( obj.scrollHeight) + 'px';
} 

// const form = document.getElementById('comment-form')
// const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
// form.addEventListener('submit', function (e) {
//   e.preventDefault()
//   const userId = e.target.dataset.userId
//   axios({
//     method: 'POST',
//     url: `/posts/${userId}/comment/`,
//     headers: {'X-CSFRToken': csrftoken}
//   })
// })


// const commentForm = document.querySelector('#comment-form');
// const commentList = document.querySelector('#comment-list');
// const commentContent = document.querySelector('#comment-content')
// commentForm.addEventListener('submit', (event) => {
//   event.preventDefault();

//   const formData = new FormData(commentForm);
//   const xhr = new XMLHttpRequest();

//   xhr.onreadystatechange = function() {
//     if (xhr.readyState === XMLHttpRequest.DONE) {
//       if (xhr.status === 200) {
//         const newComment = document.createElement('li');
//         newComment.innerText = formData.get('content');
//         commentList.appendChild(newComment);
//         // commentForm.reset();
//       } else {
//         console.error(xhr.responseText);
//       }
//     }
//   };

//   xhr.open(commentForm.method, commentForm.action);
//   xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
//   xhr.send(formData);
// });

