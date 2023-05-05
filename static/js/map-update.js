const place_input = document.getElementById('place_input')
const place_field = document.getElementById('place-field')
const placeId = document.getElementById('place-id')
const placeKeyword = document.getElementById('place-keyword')
const region_field = document.getElementById('region-field')
const modalButton = document.getElementById('modal-button')
const centerButton = document.getElementById('current-location')

const getAddress = (e) => {
  e.preventDefault()
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
      const places = response.data.documents
      let lst = []
      for (let i = 0; i < places.length; i++) {
        lst.push({
          'place_name': places[i].place_name,
          'address_name': places[i].address_name,
          'place_id': places[i].id,
        })
      }
      printAddress(lst)
    })
    .catch(function (error) {
      console.log(error)
    })
}
const printAddress = (lst) => {
  const addressList = document.querySelector('ol')
  addressList.textContent = ""
  for (let i = 0; i < lst.length; i++) {
    const element = lst[i]

    const liTag = document.createElement('li')
    liTag.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-start',)
    liTag.style.cursor = 'pointer'

    const wrap = document.createElement('div')
    wrap.classList.add('d-flex', 'align-items-center')

    const divTag1 = document.createElement('div')
    divTag1.classList.add('ms-2', 'me-auto')
    divTag1.textContent = element['place_name']

    const divTag2 = document.createElement('div')
    divTag2.classList.add('fw-bold')
    divTag2.setAttribute('id', 'place')
    divTag2.textContent = element['address_name']

    const spanTag1 = document.createElement('span')
    spanTag1.classList.add('hidden')
    spanTag1.setAttribute('id', 'place_id_value')
    spanTag1.textContent = element['place_id']

    const spanTag2 = document.createElement('span')
    spanTag2.classList.add('hidden')
    spanTag2.setAttribute('id', 'place_keyword_value')
    spanTag2.textContent = element['place_name']

    divTag1.appendChild(divTag2)
    divTag1.appendChild(spanTag1)
    divTag1.appendChild(spanTag2)
    liTag.appendChild(divTag1)
    addressList.appendChild(liTag)
  }

  // 해당하는 주소를 누를 때
  const addresses = addressList.querySelectorAll('li')
  addresses.forEach(address => {
    address.addEventListener('click', (e) => {
      const place = address.querySelector('#place')
      const region = place.textContent.split(' ')[0]

      const id = address.querySelector('#place_id_value')
      const keyword = address.querySelector('#place_keyword_value')

      const mapModalHeader = document.querySelector('#modal-place')
      const mapModalSpan = document.querySelector('#modal-address')

      mapModalHeader.textContent = address.querySelector('li div').firstChild.textContent
      mapModalSpan.textContent =  `(${place.textContent})`

      place_field.value = place.textContent
      region_field.value = region
      placeId.value = id.textContent
      placeKeyword.value = keyword.textContent
      
      const modal = document.querySelector('#addressList')
      const modalInstance = bootstrap.Modal.getInstance(modal)
      modalInstance.hide()
      
      const mapContainer = document.getElementById('map')
      const mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
      }
      const map = new kakao.maps.Map(mapContainer, mapOption)
      const geocoder = new kakao.maps.services.Geocoder()
      geocoder.addressSearch(place.textContent, function(result, status) {
        if (status === kakao.maps.services.Status.OK) {
          const coords = new kakao.maps.LatLng(result[0].y, result[0].x)
          const marker = new kakao.maps.Marker({
            map: map,
            position: coords
          })
          map.setCenter(coords)
        }
      })

      
      modalButton.classList.remove('hidden')
    })
  })

  // 해당하는 주소에 mouseover 할 때 지도를 보여줌
  addresses.forEach(address => {
    const place = address.querySelector('#place').textContent
    address.addEventListener('mouseover', () => {
      const mapContainer = document.getElementById('map-modal')
      const mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
      }
      const map = new kakao.maps.Map(mapContainer, mapOption)
      const geocoder = new kakao.maps.services.Geocoder()

      geocoder.addressSearch(place, function(result, status) {
        if (status === kakao.maps.services.Status.OK) {
          const coordsInput = new kakao.maps.LatLng(result[0].y, result[0].x)
          const marker = new kakao.maps.Marker({
            map: map,
            position: coordsInput
          })
          map.setCenter(coordsInput)
        }
      })
    })
  });
}

const modal = document.querySelector('#addressList')
modal.addEventListener('shown.bs.modal', function () {
  const place_input = document.querySelector('#place_input')
  place_input.focus()
})

place_input.addEventListener('keyup', getAddress);

// 상단 맵
const mapContainer = document.getElementById("map")
mapOption = {
		center: new kakao.maps.LatLng(33.450701, 126.570667),
		level: 3
};

// 지도를 생성합니다
const map = new kakao.maps.Map(mapContainer, mapOption)

// 주소-좌표 변환 객체를 생성합니다
const geocoder = new kakao.maps.services.Geocoder();
// 주소로 좌표를 검색합니다
geocoder.addressSearch(place_field.value, function(result, status) {

	// 정상적으로 검색이 완료됐으면 
	if (status === kakao.maps.services.Status.OK) {

		const coords = new kakao.maps.LatLng(result[0].y, result[0].x);

		// 결과값으로 받은 위치를 마커로 표시합니다
		const marker = new kakao.maps.Marker({
			map: map,
			position: coords
		});

		// 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
		map.setCenter(coords);
	}
});


modalButton.classList.remove('hidden')