<template>
    <header class = "row align-items-center">
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
</template>

<script setup>
import TodayRecommend from "@/components/TodayRecommend.vue"
import NowInTheater from "@/components/NowInTheater.vue"
import Notice from "@/components/Notice.vue"
</script>

<style scoped>

</style>