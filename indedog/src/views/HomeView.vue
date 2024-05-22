<template>
    <header v-if="isDeskTop">
        <div class="row">
            <div class="col-8"  style="border: solid black 5px;">
                <TodayRecommend />
            </div>
            <div class="col-4" style="border: solid black 5px;">
                <AIRecommend/>
            </div>
        </div>
        <br>
        <div>
            <NowInTheater/>
        </div>
        <br>
        <div style="border: solid black 5px;">
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