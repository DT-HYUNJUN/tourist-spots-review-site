const place_input = document.getElementById('place_input')
const place_field = document.getElementById('place_field')
const getAddress = (e) => {
  e.preventDefault();
  const searching = e.target.value;
  axios.get('https://dapi.kakao.com/v2/local/search/keyword.json', {
    params: {
      query: searching,
    },
    headers: {
      Authorization: 'KakaoAK 2caddc4f25bdd55869865a211f7d13bb',
    }
  })
    .then(function (response) {
      const places = response.data.documents;
      let lst = []
      for (let i = 0; i < places.length; i++) {
        lst.push({
          'place_name': places[i].place_name,
          'address_name': places[i].address_name,
        })
      }
      // console.log(lst);
      printAddress(lst)
    })
    .catch(function (error) {
      console.log(error);
    });
}
const printAddress = (lst) => {
  const addressList = document.querySelector('ol')
  addressList.textContent = ""
  for (let i = 0; i < lst.length; i++) {
    const element = lst[i];

    const liTag = document.createElement('li')
    liTag.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-start',)
    liTag.style.cursor = 'pointer'

    const divTag1 = document.createElement('div')
    divTag1.classList.add('ms-2', 'me-auto')
    divTag1.textContent = element['place_name']

    const divTag2 = document.createElement('div')
    divTag2.classList.add('fw-bold')
    divTag2.setAttribute('id', 'place')
    divTag2.textContent = element['address_name']

    divTag1.appendChild(divTag2)
    liTag.appendChild(divTag1)
    addressList.appendChild(liTag)
  }
  const addresses = addressList.querySelectorAll('li')
  addresses.forEach(address => {
    address.addEventListener('click', (e) => {
      const place = address.querySelector('#place')
      // console.log(address.textContent)
      place_field.value = place.textContent
      const modal = document.querySelector('.modal')
      const modalInstance = bootstrap.Modal.getInstance(modal)
      modalInstance.hide()
    })
  });
}
place_input.addEventListener('keyup', getAddress);