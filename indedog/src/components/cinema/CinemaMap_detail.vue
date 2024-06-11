<template>
    <h1>KakaoMap Render</h1>
    <div ref="mapContainer" style="width: 100%; height: 400px;"></div>
    <div style="text-align: center;"></div>
    <Rating :address="address"/>
    <hr>
    <!-- <div v-for="comment in comments">

    </div> -->
</template>

<script setup>
import {ref, onMounted} from 'vue'
import { useRoute } from 'vue-router'
import {useCounterStore} from '@/stores/counter.js'
import Rating from '@/components/Rating.vue'
// 1. Data
const props = defineProps({cinemaName: String})
const store = useCounterStore()
store.getCoord()
const cinemas = store.cinemas
const cinema_lat = ref('')
const cinema_lng = ref('')
const route = useRoute()
const address = ref(null)

address.value = route.params.address

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
    script.src = 'https://dapi.kakao.com/v2/maps/sdk.js?appkey='
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
                // const imageSrc = "../../src/assets/icon/marker_icon.jpg"
                const imageSrc = "../src/assets/icon/dog_marker.png"
                const imageSize = new kakao.maps.Size(50,50)
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
                   const content = '<div class="wrap" style="background-color: white; border: 3px solid black">' + 
                        '    <div class="info">' + 
                        '        <div class="title">' + 
                        props.cinemaName + 
                        '        </div>' + 
                        '        <div class="body">' + 
                        '            <div class="img">' +
                        '                ' +
                        '           </div>' + 
                        '            <div class="desc">' + 
                        '                <div><a href="' + 'https://map.kakao.com/link/to/'+props.cinemaName+','+cinema_lat.value+','+cinema_lng.value +'" target="_blank" class="link">'+props.cinemaName+'로 가는 길 카카오 맵으로 알아보기</a></div>' + 
                        '            </div>' + 
                        '        </div>' + 
                        '    </div>' +    
                        '</div>';

                    // 커스텀 오버레이를 생성합니다
                    const overlay = new kakao.maps.CustomOverlay({
                        content: content,
                        map: mapInstance,
                        position: marker.getPosition(),
                        clickable: true,
                        yAnchor: -0.01,
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