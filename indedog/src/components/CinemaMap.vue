<template>
    <div ref="mapContainer" style="width: 100%; height: 400px; font-family: euljiro;"></div>
    <div style="text-align: center;"></div>
    <div>
    <b-form-rating v-model="value"></b-form-rating>
    <p class="mt-2">Value: {{ value }}</p>
    <p style="text-align: right; font-family: euljiro;">test</p>
  </div>
</template>

<script setup>
import {ref,onMounted} from 'vue'
import { useCounterStore } from '@/stores/counter.js'
import {useRoute,useRouter} from 'vue-router'
const router = useRouter()


// 1. Data
const store = useCounterStore()
store.getCoord()
const cinemas = store.cinemas

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
                center: new window.kakao.maps.LatLng(37.5984617,127.0916835),
                level: 3,
                maxLevel: 8,
            }
                const mapInstance = new window.kakao.maps.Map(container, options)
                // 여기까지 지도 생성 과정

                // - Marker -
                for (let i = 0; i < cinemas.length; i++) {
                    const markerPosition = new kakao.maps.LatLng(cinemas[i].latitude, cinemas[i].longitude)
                        // - Marker Image -
                        // const imageSrc = "../src/assets/icon/marker_icon.jpg"
                        const imageSrc = "../src/assets/icon/dog_marker.png"
                        const imageSize = new kakao.maps.Size(50,50)
                        const imageOption = {offset: new kakao.maps.Point(27,69)}
                        const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)
                    const marker = new kakao.maps.Marker({
                        position: markerPosition,
                        image: markerImage,
                        title: cinemas[i].address,
                    }) // 마커를 생성
                    marker.setMap(mapInstance) // 마커 표시

                    // - Custom Overlay -
                    const content = '<div style:"text-align: center;"><strong>' + cinemas[i].address + '</strong></div>'
                    const infowindow = new kakao.maps.CustomOverlay({
                            content: content,
                            map: mapInstance,
                            position: marker.getPosition(),
                            clickable: true
                        })
                    infowindow.setMap(null)
                    // - Marker Event | mouse over -
                    {
                        kakao.maps.event.addListener(marker,'mouseover',function() {
                            infowindow.setMap(mapInstance);
                        });
                    };
                    {
                        kakao.maps.event.addListener(marker,'mouseout',function() {
                            infowindow.setMap(null);
                        });
                    };
                    // - Marker Event | click -
                    {
                        kakao.maps.event.addListener(marker,'click',function () {
                            router.push({name: "cinema_info", params: {'address': event.target.title}})
                        });
                    }
                }
        })
    }
}
</script>

<style scoped>
@import '@/assets/font/font.css';
#cinemaName {
  font-family: 'euljiro';
}
</style>