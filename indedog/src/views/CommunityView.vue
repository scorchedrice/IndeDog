<template>
    <div v-if="store.token">
        <h1>이곳에는 커뮤니티가 렌더링 될 예정입니다. 로그인한 회원만 접속 가능합니다.</h1>
        <RouterLink :to="{ name: 'CommunityCreateView' }">
            게시글 작성하기
        </RouterLink>
        <CommunityList />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import CommunityList from '@/components/CommunityList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>

</style>