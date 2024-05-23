<template>
    <div>
        <div class="row align-items-md-stretch">
      <div class="col-md-6">
        <div class="h-100" style="border: solid black 2px;" >
          <BestArticle/>
        </div>
      </div>
      <div class="col-md-6">
        <div class="h-100 p-5 bg-body-tertiary border rounded-3">
          <h2>커뮤니티 게시판 이용 규칙</h2>
          <p>더 유익하고, 즐거운 커뮤니티를 위해 다음의 규칙을 준수해주세요.</p>
        </div>
      </div>
    </div>
    </div>
    <br>
    <div style="border: solid black 5px;">
        <MovieCommunity/>
    </div>
    <br>
    <div style="border: solid black 5px">
        <TheaterCommunity/>
    </div>
    <br>
    <div style="border: solid black 4px;">
        <FreeCommunity/>
    </div>
    <div>
        <RouterLink :to="{ name: 'CommunityCreateView'}">
            <h1>게시글 작성</h1>
        </RouterLink>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import BestArticle from '@/components/community/BestArticle.vue'
import MovieCommunity from '@/components/community/MovieCommunity.vue'
import TheaterCommunity from '@/components/community/TheaterCommunity.vue'
import FreeCommunity from '@/components/community/FreeCommunity.vue'
const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>