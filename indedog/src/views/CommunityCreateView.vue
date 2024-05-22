<template>
    <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div v-if="!movieId">
        <label for="category">카테고리 : </label>
        <select name="category" id="category" v-model="category">
        <option value="영화">영화</option>
        <option value="상영관">상영관</option>
        <option value="자유">자유</option>
        <option v-if="store.isStaff" value="공지">공지</option>
      </select>
      </div>
      <div v-if="movieName">
        영화 : {{ movieName }}
      </div>
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
      <br>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()
const route = useRoute()
const isNotice = ref(false)
const category = ref(null)
const movieId = ref(null)
const movieName = ref(null)

// 영화 평론에서 넘어왔다면 실행
if (history.state.movie_id) {
  console.log(history.state.movie_id)
  console.log(history.state.movie_name)
  console.log('영화 평론')
  movieId.value = history.state.movie_id
  movieName.value = history.state.movie_name
  category.value = '영화'
}

const createArticle = function () {
    if(category.value === '공지') {
      isNotice.value = true
    }
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/create/`,
      data: {
        title: title.value,
        content: content.value,
        is_notice: isNotice.value,
        category: category.value,
        movie: movieId.value
      },
      headers: {
        Authorization : `Token ${store.token}`
      }
    })
      .then(response => {
        console.log(response.data)
        if(isNotice.value) {
          router.replace({ name: 'notice'})
        } else if(movieId.value){
          router.push({ name: 'movie_detail', params: { 'id': movieId.value }})
        } else {
          router.replace({ name: 'community'})
        }
        movieId.value = null
      })
      .catch(error => {
        console.log(error)
      })
  }

</script>

<style lang="scss" scoped>

</style>