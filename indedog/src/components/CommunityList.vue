<template>
    <div>
        <h3>게시글 목록</h3>
        <article v-for="article in store.articles"
        :key="article.id">
            <h3>[{{ article.category }}]</h3>
            <RouterLink :to="{ name: 'CommunityDetailView', params: { id: article.id }}">
                <h3>{{ article.title }}</h3>
            </RouterLink>
        </article>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'

const store = useCounterStore()
</script>

<style scoped>
article {
    display: flex;
}
</style>