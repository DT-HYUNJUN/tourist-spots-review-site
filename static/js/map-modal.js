const place_field2 = document.getElementById('place-field')
const modalContent = document.querySelector('#modal-content')
// 모달 버튼 요소를 가져옵니다.
const modalButton2 = document.getElementById("modal-button");

// 모달 요소를 가져옵니다.
const mymodal = document.getElementById("my-modal");

// 모달에서 닫기 버튼 요소를 가져옵니다.
const close = mymodal.querySelector(".close");

let kakaoMap;
let coordsModal;
let maps

// 모달 버튼에 클릭 이벤트 핸들러를 추가합니다.
modalButton2.addEventListener("click", function() {
  mymodal.style.display = "block";

  kakaoMap = document.createElement('div')
  kakaoMap.setAttribute('id', 'map-modal-select')
  kakaoMap.classList.add('map-select')

  modalContent.appendChild(kakaoMap)

  // 지도 생성
  const mapModalContainer = document.getElementById('map-modal-select')
  
  const mapModalOption = {
    center: new kakao.maps.LatLng(33.450701, 126.570667),
    level: 3
  }
  maps = new kakao.maps.Map(mapModalContainer, mapModalOption)
  
  const geocoderModal = new kakao.maps.services.Geocoder()
  geocoderModal.addressSearch(place_field2.value, function(result, status) {
    if (status === kakao.maps.services.Status.OK) {
      coordsModal = new kakao.maps.LatLng(result[0].y, result[0].x)
      const markerModal = new kakao.maps.Marker({
        map: maps,
        position: coordsModal
      })
      maps.setCenter(coordsModal)
    }
  })
});

// 모달에서 닫기 버튼에 클릭 이벤트 핸들러를 추가합니다.
close.addEventListener("click", function() {
  // modalContent.removeChild(kakaoMap)
  kakaoMap.remove()
  mymodal.style.display = "none";
});

// 모달 이외의 영역을 클릭하면 모달이 닫힙니다.
window.addEventListener("click", function(event) {
  if (event.target == mymodal) {
    // modalContent.removeChild(kakaoMap)
    kakaoMap.remove()
    mymodal.style.display = "none";
  }
});

function panTo() {
  maps.panTo(coordsModal);
}