<template>
    <div v-if="article">
        <h1>제목 : {{ article.title }}</h1>
        <h3>작성자 : {{ article.user }}</h3>
        <p>내용 : {{ article.content }}</p>
        <p>작성된 날짜 : {{ article.created_at }}</p>
        <p>수정된 날짜 : {{ article.updated_at }}</p>
        <div v-if="store.loginUser === article.user">
          <div v-if="store.loginUser == article.user">
          <RouterLink :to="{ name: 'CommunityUpdate', params: { 'id': article.id }}">
            <button>
              게시글 수정
            </button>
          </RouterLink>
          <hr>
            <button @click="articleDelete(article.id)">
              게시글 삭제
            </button>
        </div>
      </div>
      <RouterLink :to="{name: 'community'}">
        [BACK]
      </RouterLink>
        <hr>
        <footer v-if="article.category != '공지'">
          <h1>코멘트</h1>
          <hr>
          <form @submit.prevent="createComment(article.id)">
            <input type="text" v-model="content">
            <input type="submit" value="댓글달기">
          </form>
          <div v-for="comment in article.comment_set" style="display: flex;">
            <h4>{{ comment.user }}</h4>
            <p>{{ comment.content }}</p>
          </div>
        </footer>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const router = useRouter()
const content = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((response) => {
      console.log(response.data)
      article.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})

const articleDelete = function(article_pk) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${article_pk}/update/`,
    headers: {
        Authorization : `Token ${store.token}`
    }
  })
    .then(res => {
      console.log('게시글 삭제 완료')
      window.alert('게시글이 삭제되었습니다.')
      router.replace({ name: 'community'})
    })
    .catch(err => {
      console.log(err)
    })
  }

const createComment = function(article_id) {
  if(!store.loginUser){
        window.alert('로그인을 하셔야 댓글등록이 가능해요!')
        return
    }
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${article_id}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization : `Token ${store.token}`
    }
  })
    .then(res => {
      console.log('댓글 생성')
      window.location.reload()
    })
    .catch(err => {
      console.log(err)
      window.alert('댓글을 적어주세요')
    })
}



</script>

<style scoped>

</style>