<template>
    <h1>KakaoMap Render</h1>
    <div ref="mapContainer" style="width: 100%; height: 400px;"></div>
    <div style="text-align: center;"></div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import {useCounterStore} from '@/stores/counter.js'
// 1. Data
const props = defineProps({cinemaName: String})
const store = useCounterStore()
store.getCoord()
const cinemas = store.cinemas
const cinema_lat = ref('')
const cinema_lng = ref('')

for(let i = 0; i < cinemas.length; i++) {
    if (cinemas[i].address == props.cinemaName) {
        cinema_lat.value = cinemas[i].latitude
        cinema_lng.value = cinemas[i].longitude
        console.log(cinema_lat.value)
        break
    }
}
// 2. setting KakaoMap
const mapContainer = ref(null)

onMounted(() => {
    loadKakaoMap(mapContainer.value)
})
const loadKakaoMap = (container) => {
    const script = document.createElement('script')
    script.src = 'https://dapi.kakao.com/v2/maps/sdk.js?appkey=2a1d54c8291415ac437b2532d4f11171'
    document.head.appendChild(script)
    script.onload= () => {
        window.kakao.maps.load(() => {
            const options = {
                center: new window.kakao.maps.LatLng(cinema_lat.value,cinema_lng.value),
                level: 3,
                maxLevel: 8,
            }
                const mapInstance = new window.kakao.maps.Map(container, options)
                // 여기까지 지도 생성 과정

                // - Marker -
                const markerPosition = new kakao.maps.LatLng(cinema_lat.value, cinema_lng.value)
                const imageSrc = "../../src/assets/icon/marker_icon.jpg"
                const imageSize = new kakao.maps.Size(30,30)
                const imageOption = {offset: new kakao.maps.Point(27,69)}
                const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)        
                const marker = new kakao.maps.Marker({
                    position: markerPosition,
                    image: markerImage,
                    title: props.cinemaName,
                    }) // 마커를 생성
                    marker.setMap(mapInstance) // 마커 표시

                // - Marker Custom Overlay -
                   // 커스텀 오버레이에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
                   const content = '<div class="wrap" style="background-color: aqua;">' + 
                        '    <div class="info">' + 
                        '        <div class="title">' + 
                        props.cinemaName + 
                        '        </div>' + 
                        '        <div class="body">' + 
                        '            <div class="img">' +
                        '                <img src="https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/thumnail.png" width="73" height="70">' +
                        '           </div>' + 
                        '            <div class="desc">' + 
                        '                <div class="ellipsis">해당 영화관의 주소를 입력합니다.</div>' + 
                        '                <div class="jibun ellipsis">화곡로 999길 999</div>' + 
                        '                <div><a href="' + 'https://map.kakao.com/link/to/'+props.cinemaName+','+cinema_lat.value+','+cinema_lng.value +'" target="_blank" class="link">길찾기</a></div>' + 
                        '            </div>' + 
                        '        </div>' + 
                        '    </div>' +    
                        '</div>';

                    // 커스텀 오버레이를 생성합니다
                    const overlay = new kakao.maps.CustomOverlay({
                        content: content,
                        map: mapInstance,
                        position: marker.getPosition(),
                        clickable: true    
                    });

                    // - Marker Event -
                    {
                        kakao.maps.event.addListener(marker,'click',function() {
                            overlay.setMap(mapInstance)
                        });
                    };
                    {
                        kakao.maps.event.addListener(mapInstance,'click',function () {
                            overlay.setMap(null)
                        })
                    }
                
        })
    }
}
</script>

<style scoped>

</style>