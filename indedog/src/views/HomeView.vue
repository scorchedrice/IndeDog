<template>
    <header v-if="isDeskTop" class = "row align-items-center">
        <div class="col" style="margin-bottom: 15px; background-color: green;">
            <TodayRecommend />
        </div>
        <hr>
        <div style="margin-bottom: 15px; background-color: bisque;">
            <NowInTheater/>
        </div>
        <hr>
        <div style="background-color: blueviolet;">
            <Notice/>
        </div>
    </header>
    <header v-else>
        <h1>sdads</h1>
    </header>
</template>

<script setup>
import TodayRecommend from "@/components/TodayRecommend.vue"
import NowInTheater from "@/components/NowInTheater.vue"
import Notice from "@/components/Notice.vue"
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'

const store = useCounterStore()

onMounted(() => {
  store.getMovies()
})

const isDeskTop = ref(true);
window.onresize = function () {
    if (window.innerWidth < 576) {
        isDeskTop.value = false
    } else {
        isDeskTop.value = true
    }
}
</script>

<style scoped>

</style>