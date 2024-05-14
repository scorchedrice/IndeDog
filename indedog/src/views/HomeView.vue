<template>
    <header class = "row align-items-center">
        <div class="col" style="margin-top: 15px; margin-bottom: 15px; background-color: green;">
            <TodayRecommend />
        </div>
        <hr>
        <div style="background-color: bisque;">
            <NowInTheater/>
        </div>
    </header>
</template>

<script setup>
import TodayRecommend from "@/components/TodayRecommend.vue"
import NowInTheater from "@/components/NowInTheater.vue"
</script>

<style scoped>

</style>