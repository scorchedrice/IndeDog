<template>
    <div v-if="article">
        <h1>제목 : {{ article.title }}</h1>
        <h3>작성자 : {{ article.user }}</h3>
        <p>내용 : {{ article.content }}</p>
        <p>작성된 날짜 : {{ article.created_at }}</p>
        <div v-if="store.loginUser == article.user || store.isStaff">
        <RouterLink :to="{ name: 'CommunityUpdate', params: { 'id': article.id }}">
          <button>
            게시글 수정
          </button>
        </RouterLink>
        <hr>
          <button @click.prevent="articleDelete(article.id)">
            게시글 삭제
          </button>
        </div>
        <div v-if="store.loginUser">
          <button v-if="!isLike" @click.prevent="upLike(article.id, 1)">
                좋아요
          </button>
          <button v-else @click.prevent="upLike(article.id, 2)">
              좋아요 취소
          </button>
        </div>
      <RouterLink :to="{name: 'community'}">
        뒤로가기
      </RouterLink>
        <hr>
        <footer v-if="article.category != '공지'">
          <h1>코멘트</h1>
          <hr>
          <form @submit.prevent="createComment(article.id)">
            <input type="text" v-model="content">
            <input type="submit" value="댓글달기">
          </form>
          <div v-for="(comment, index) in article.comment_set">
            <p>{{ comment.user }} |
              <input type="button" v-if="store.loginUser == comment.user && !updateNow" @click.prevent="commentUpdate(comment.id, comment.content)" value="수정">
              <input type="button" v-if="store.loginUser == comment.user && updateNow" @click.prevent="commentUpdatePush(comment.id, index)" value="수정완료">
              <span> | </span>
              <a v-if="store.loginUser == comment.user || store.isStaff" @click.prevent="commentDelete(comment.id, index)">
                  [삭제]
              </a>
            </p>
            <h4 v-if="!(updateNow && comment.id == currentIdx)">{{ comment.content }}</h4>
            <input v-if="updateNow && comment.id == currentIdx" type="text" v-model="contentUpdate">
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
const isLike = ref(false)
const likeusersList = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((response) => {
      console.log(response.data)
      article.value = response.data
      likeusersList.value = response.data.like_users
      if (likeusersList.value.includes(store.loginPk)) {
        isLike.value = true
      }
    })
    .catch((error) => {
      console.log(error)
    })
})

const fetchData = async () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((response) => {
      likeusersList.value = response.data.like_users
      article.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

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
      content.value = null
      fetchData()
    })
    .catch(err => {
      console.log(err)
      window.alert('댓글을 적어주세요')
    })
}


const upLike = function(article_pk, type) {
        if (type === 1) {
            likeusersList.value.push(store.loginPk)
            console.log(likeusersList.value)
            isLike.value = !isLike.value
        } else {
            likeusersList.value = likeusersList.value.filter(user => user !== store.loginPk)
            isLike.value = !isLike.value
        }
        axios({
            method: 'put',
            url: `${store.API_URL}/api/v1/articles/${article_pk}/like/`,
            data: {
                like_users: likeusersList.value
            },
            headers: {
                Authorization : `Token ${store.token}`
            }
        })
        .then(res => {
            console.log('좋아요 수정완료')
            console.log(res.data)
            fetchData()
        })
        .catch(err => {
            console.log(err)
        })
    }
    
  const length = ref(null)

  const commentDelete = function (comment_id, idx) {
  axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/articles/${comment_id}/comments/update/`,
      headers: {
          Authorization : `Token ${store.token}`
      }
  })
    .then(res => {
      console.log(article.value.comment_set.length)
      length.value = article.value.comment_set.length
      article.value.comment_set.splice(length.value-1-idx, 1)
      console.log('삭제완료')
      fetchData()
    })
    .catch(err => {
      console.log(err)
    })
  }

const updateNow = ref(false)
const currentIdx = ref(null)
const contentUpdate = ref(null)

const commentUpdate = function (comment_id, content_) {
    updateNow.value = !updateNow.value
    currentIdx.value = comment_id
    contentUpdate.value = content_
}


const commentUpdatePush = function (comment_id, idx) {
    axios({
        method: 'put',
        url: `${store.API_URL}/api/v1/articles/${comment_id}/comments/update/`,
        data: {
            content: contentUpdate.value,
        },
        headers: {
            Authorization : `Token ${store.token}`
        }
    })
      .then(res => {
        console.log(article.value.comment_set[idx])
        article.value.comment_set[idx].content = contentUpdate.value
        console.log('수정완료')
        fetchData()
        contentUpdate.value = null
        currentIdx.value = null
        updateNow.value = !updateNow.value
      })
      .catch(err => {
        console.log(err)
      })
}

</script>

<style scoped>
a {
    cursor: pointer;
    color: blue;
}
</style>