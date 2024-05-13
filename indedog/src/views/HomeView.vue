<template>
    <header class = "row align-items-center" style="width: 1600px;">
        <div class="col-9">
            <TodayRecommend />
        </div>
        <div class = "col-3">
            <Menu />
        </div>
    </header>
</template>

<script setup>
import TodayRecommend from "@/components/TodayRecommend.vue"
import Menu from "@/components/Menu.vue"
</script>

<style scoped>

</style>