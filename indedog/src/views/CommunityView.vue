<template>
    <template v-if="isLoading">
    </template>
    <div v-if="!isLoading">
        <div class="row align-items-md-stretch">
      <div class="col-md-6">
        <div class="h-100" style="border: solid black 2px;" >
          <BestArticle/>
        </div>
      </div>
      <div class="col-md-6">
        <div class="h-100 p-5" style="border: solid black 2px;">
          <h2>커뮤니티 게시판입니다.</h2>
          <p>더 유익하고, 즐거운 커뮤니티를 위해 규칙을 준수해주세요.</p>
          <hr>
          <hr>
          <div class="row">
            <div class="col-md-6">
              <RouterLink :to="{ name: 'CommunityCreateView'}">
                <h3>게시글 작성하기</h3>
              </RouterLink>
            </div>
            <div class="col-md-6">
              <RouterLink :to="{ name: 'community_notice'}">
                <h3>커뮤니티 규칙 확인하기</h3>
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3">
      </div>
    </div>
    </div>
    <br>
    <div style="border: solid black 2px;">
        <MovieCommunity/>
    </div>
    <br>
    <br>
    <div style="border: solid black 2px;">
        <FreeCommunity/>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import BestArticle from '@/components/community/BestArticle.vue'
import MovieCommunity from '@/components/community/MovieCommunity.vue'
import TheaterCommunity from '@/components/community/TheaterCommunity.vue'
import FreeCommunity from '@/components/community/FreeCommunity.vue'
const store = useCounterStore()
const isLoading = ref(true)

onMounted(() => {
  store.getArticles()
  setTimeout(() => {
    isLoading.value = false
  }, 500);
})
</script>

<style scoped>

</style>