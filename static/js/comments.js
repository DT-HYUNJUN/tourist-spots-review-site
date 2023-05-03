const comments = document.querySelectorAll('#comments')

comments.forEach(comment => {
  const deleteBtn = comment.querySelector('#comment_delete')

  comment.addEventListener('mouseover', () => {
    deleteBtn.classList.remove('hidden')
  })

  comment.addEventListener('mouseout', () => {
    deleteBtn.classList.add('hidden')
  })
});