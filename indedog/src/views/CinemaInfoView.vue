<template>
    <div>
        <h1>{{ route.params.address }}!</h1>
        <CinemaMapDetail :cinema-name="route.params.address"/>
    </div>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {ref} from 'vue'

import CinemaMapDetail from '@/components/cinema/CinemaMap_detail.vue'
defineProps({
    cinemaName: String
})

const route = useRoute()
console.log(route.params)
</script>

<style lang="scss" scoped>

</style>