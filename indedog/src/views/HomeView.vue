<template>
    <header v-if="isDeskTop">
        <h1>오늘은 무슨 재미있는 것들이 있을까?</h1>
        <div class="row align-items-center" style="border-bottom: solid black 2px; border-top: solid black 2px;">
            <div class="col-6" style="border-right: solid black 2px;">
                <TodayRecommend />
            </div>
            <div class="col-6">
                <div style="height: 100px; border-bottom: solid black 2px">
                    <AIRecommend/>
                </div>
                <div style="height: 400px;">
                    <!-- <h1>여기에 베스트 게시물을 전시해볼까용</h1> -->
                    <BestArticle/>
                </div>
            </div>
        </div>
        <br>
        <div>
            <NowInTheater/>
        </div>
        <br>
        <div>
            <Notice/>
        </div>
        
        
    </header>
    <header v-else-if="!isDeskTop" class="row align-items-center container">
        <div class="col" style="background-color: green; margin-bottom: 15px;">
            <MobileTodayRecommend/>
        </div>
        <hr>
        <div class="col" style="background-color: bisque; margin-bottom: 15px;">
            <MobileNowInTheater/>
        </div>
        <hr>
        <div class="col" style="background-color: blueviolet;">
            <MobileNotice/>
        </div>

    </header>
</template>

<script setup>
import TodayRecommend from "@/components/TodayRecommend.vue"
import MobileTodayRecommend from "@/components/mobile/home/MobileTodayRecommend.vue"
import NowInTheater from "@/components/NowInTheater.vue"
import MobileNowInTheater from "@/components/mobile/home/MobileNowInTheater.vue"
import Notice from "@/components/Notice.vue"
import MobileNotice from "@/components/mobile/home/MobileNotice.vue"
import AIRecommend from "@/components/AIRecommend.vue"
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'
import { FwbAvatar } from "flowbite-vue"
import BestArticle from '@/components/community/BestArticle.vue'

const store = useCounterStore()

const mobileWidth = ref(576)

onMounted(() => {

  console.log(window.innerWidth)
  if (window.innerWidth < 576) {
    isDeskTop.value = false
    mobileWidth.value = window.innerWidth
  } else {
    isDeskTop.value = true
  }
})

const isDeskTop = ref(true);
window.onresize = function () {
    if (window.innerWidth < 576) {
        isDeskTop.value = false
        mobileWidth.value = window.innerWidth
    } else {
        isDeskTop.value = true
    }
}
</script>

<style scoped>
@import '@/assets/font/font.css';
h1,h2 {
    font-family: "hanna";
    text-align: center;
}
* {
    font-family: "hanna_air"
}
</style>