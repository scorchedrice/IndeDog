<template>
    <header v-if="isDeskTop" class = "row align-items-center">
        <div class="col" style="margin-bottom: 15px; border: 5px solid black">
            <TodayRecommend />
        </div>
       
        
            <NowInTheater/>
        
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

</style>