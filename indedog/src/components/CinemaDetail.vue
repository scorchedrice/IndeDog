<template>
    <div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="now_in" @click="searchNowInTheater">
            <label class="form-check-label" for="now_in">
                상영중인 영화를 기준으로 상영관 검색
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked @click="searchRegion">
            <label class="form-check-label" for="flexRadioDefault2">
                지역을 기준으로 상영관 검색
            </label>
        </div>
        <div v-if="searchMethod">
            <CinemaDetail_NowInTheater/>
        </div>
        <div v-else-if = "searchMethod==false">
            <CinemaDetail_Region/>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import CinemaDetail_NowInTheater from '@/components/CinemaDetail-NowInTheater.vue'
import CinemaDetail_Region from '@/components/CinemaDetail-Region.vue'
// Event
const searchMethod = ref(null) // true: nowintheater, false: searchRegion

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