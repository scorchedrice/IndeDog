<template>
    <div>
        <h3>영화평점 최신순 정렬 (MovieComment)</h3>
    </div>
</template> 

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

const category = ref('전체')
const store = useCounterStore()
</script>

<style scoped>
</style>