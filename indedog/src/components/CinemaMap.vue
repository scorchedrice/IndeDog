<template>
    <div ref="mapContainer" style="width: 100%; height: 400px;"></div>
    <div style="text-align: center;"></div>
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
                        const imageSrc = "https://cdn4.iconfinder.com/data/icons/dog-breed-minimal-outline/512/Pomeranian-1024.png"
                        const imageSize = new kakao.maps.Size(30,30)
                        const imageOption = {offset: new kakao.maps.Point(27,69)}
                        const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)
                    const marker = new kakao.maps.Marker({
                        position: markerPosition,
                        image: markerImage,
                        title: cinemas[i].address,
                    }) // 마커를 생성
                    marker.setMap(mapInstance) // 마커 표시

                    // - Marker Window -
                    const infowindow = new kakao.maps.InfoWindow({
                            content: '<div style="font-family: euljiro"; margin:7px 22px 7px 12px;>' + cinemas[i].address + '</div>'
                        })
                    // - Marker Event | mouse over -
                    {
                        kakao.maps.event.addListener(marker,'mouseover',function() {
                            infowindow.open(mapInstance,marker);
                        });
                    };
                    {
                        kakao.maps.event.addListener(marker,'mouseout',function() {
                            infowindow.close();
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