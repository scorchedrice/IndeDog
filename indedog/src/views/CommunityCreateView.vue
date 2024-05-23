<template>
    <div>
    <h1>게시글 작성</h1>
    <hr>
    <form @submit.prevent="createArticle">
      <div v-if="!movieId">
        <label for="category"><h2>카테고리</h2></label>
        <div class="form-floating">
          <select class="form-select form-select-lg mb-3" name="category" id="category" v-model="category">
            <option value="영화">영화</option>
            <option value="상영관">상영관</option>
            <option value="자유">자유</option>
            <option v-if="store.isStaff" value="공지">공지</option>
          </select>
          <label for="category">카테고리를 선택해주세요.</label>
        </div>
        
      </div>
      <div v-if="movieName">
        영화 : {{ movieName }}
      </div>
      <div v-if="back == '/job'">
        구인공고를 작성해주세요.
      </div>
      <div>
        <label for="title"><h2>제목</h2></label>
        <br>
        <div class="input-group input-group-lg">
          <input class="form-control" area-describedby="inputGroup-sizing-lg" type="text" v-model.trim="title" id="title">
        </div>
      </div>
      <br>
      <div>
        <label for="content"><h4>내용 :</h4> </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <div v-if="category == '구인공고'">
        <label for="job">모집부문 : </label>
        <input type="text" v-model.trim="job" id="job">
        <label for="by">지원 마감기한 : </label>
        <input type="date" v-model="by" id="by">
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
const by = ref(null)
const job = ref(null)
const applicant = ref([])
const back = ref(history.state.back)


// 영화 평론에서 넘어왔다면 실행
if (history.state.movie_id) {
  console.log('영화 평론')
  movieId.value = history.state.movie_id
  movieName.value = history.state.movie_name
  category.value = '영화'
} else if (back.value == '/job') {
  category.value = '구인공고'
  movieId.value = 1
}

const createArticle = function () {
  console.log(category.value)
    if(category.value === '공지') {
      isNotice.value = true
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
        
        router.replace({ name: 'community'})
      })
      .catch(error => {
        console.log(error)
      })
      
    return
    } else if(category.value != '구인공고'){
      console.log('###')
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
        return
    }
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/job/create/`,
      data: {
        title: title.value,
        content: content.value,
        job: job.value,
        by: by.value,
        applicant: applicant.value
      },
      headers: {
        Authorization : `Token ${store.token}`
      }
    })
      .then(response => {
        console.log(response.data)
        router.replace({ name: 'job'})
      })
      .catch(error => {
        console.log(error)
      })
  }

</script>

<style lang="scss" scoped>

</style>