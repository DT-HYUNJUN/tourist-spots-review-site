const place = document.getElementById('map').dataset.place

const mapContainer = document.getElementById('map') // 지도를 표시할 div 

mapOption = {
		center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
		level: 3 // 지도의 확대 레벨
};

// 지도를 생성합니다
const mapDetail = new kakao.maps.Map(mapContainer, mapOption);

// 주소-좌표 변환 객체를 생성합니다
const geocoder = new kakao.maps.services.Geocoder();
let coords
// 주소로 좌표를 검색합니다
geocoder.addressSearch(place, function(result, status) {

	// 정상적으로 검색이 완료됐으면 
	if (status === kakao.maps.services.Status.OK) {

		coords = new kakao.maps.LatLng(result[0].y, result[0].x);

		// 결과값으로 받은 위치를 마커로 표시합니다
		const marker = new kakao.maps.Marker({
			map: mapDetail,
			position: coords
		});

		// 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
		mapDetail.setCenter(coords);
	}
});

function panToDetail() {
  mapDetail.panTo(coords);
}