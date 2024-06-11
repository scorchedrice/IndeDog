<template>
    <header>
        <h1>오늘은 무슨 재미있는 것들이 있을까?</h1>
        <div class="row align-items-center" style="border-bottom: solid black 2px; border-top: solid black 2px;">
            <div class="col-6" style="border-right: solid black 2px;">
                <TodayRecommend />
            </div>
            <div class="col-6">
                <div style="height: 100px;">
                    <AIRecommend/>
                </div>
                <div style="height: 400px; border-top: solid black 2px">
                    <BestArticle/>
                </div>
            </div>
        </div>
        <br>
        <div>
            <NowInTheater/>
        </div>
        <br>
        <div class="row">
            <div class="col-6">
                <Notice/>
            </div>
            <div  class="col-6">
                <div class="body-tertiary rounded-3">
                    <div class="container-fluid" style="text-align: center;">
                    <h3 class="display-5 fw-bold">함께할 사람을 찾고 계신가요?</h3>
                    <h4>IndeDog과 함께 찾아봐요!</h4>
                    <RouterLink :to="{name: 'job'}">
                        <h5>채용공고 바로가기</h5>
                    </RouterLink>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>

<script setup>
import TodayRecommend from "@/components/TodayRecommend.vue"
import NowInTheater from "@/components/NowInTheater.vue"
import Notice from "@/components/Notice.vue"
import AIRecommend from "@/components/ai/AIRecommend.vue"
import { useCounterStore } from '@/stores/counter'
import BestArticle from '@/components/community/BestArticle.vue'
import { RouterLink } from 'vue-router'


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