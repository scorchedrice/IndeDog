<template>
    <div>
        <CinemaDetail_NowInTheater/>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import CinemaDetail_NowInTheater from '@/components/CinemaDetail-NowInTheater.vue'
import CinemaDetail_Region from '@/components/CinemaDetail-Region.vue'
// Event

const searchNowInTheater = function () {
    console.log('NOWINTHEATER')
    searchMethod.value=true
    console.log(searchMethod)
}

const searchRegion = function () {
    console.log('REGION')
    searchMethod.value=false
    console.log(searchMethod)
}
</script>

<style scoped>

</style>