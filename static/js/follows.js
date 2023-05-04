const form = document.querySelector("#follow-form")
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value

form.addEventListener("submit", function (event) {
  event.preventDefault()

  const userId = event.target.dataset.userId;

  axios({
    method: "post",
    url: `/accounts/${userId}/follow/`,
    headers: { "X-CSRFToken": csrftoken },
  }).then((response) => {
    const isFollowed = response.data.is_followed
    const followBtn = document.querySelector('#follow-form > input[type=submit]')

    if(isFollowed){
      followBtn.value='팔로잉'
    } else{
      followBtn.value='팔로우'
    }
  });
});