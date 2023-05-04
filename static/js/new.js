const newPosts = document.querySelectorAll('.new')
newPosts.forEach(newPost => {
  setInterval(() => {
    newPost.classList.toggle('text-danger')
  }, 800)
});