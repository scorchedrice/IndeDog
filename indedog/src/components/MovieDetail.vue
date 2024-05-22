<template>
    <div v-if="isLoading"><h1>불러오는중...</h1></div>
    <div v-if="!isLoading">
    <a :href="goBack">
        뒤로가기
    </a>
    <h1>영화 정보</h1>
    <div class="row align-items-center">
        <img :src="curMovie.img_src" alt="movie.poster" class="col-4">
        <div class="col-8">
            <div class="row">
                <div class="col-3">
                    <vue3-star-ratings
                    v-model="score"
                    :starSize="20"
                    starColor="#ff9800"
                    inactiveColor="#333333"
                    :numberOfStars="5"
                    :disableClick="true"
                    />
                </div>
                <div class="col">
                    {{ score }} / 5.0
                </div>
            </div>
            <h2>제목 : {{ curMovie.title }}</h2>
            <p v-if="curMovie.title_en">{{ curMovie.title_en }}</p>
            <p>제작연도 : {{ curMovie.making_year }}년</p>
            <p>감독 : {{ curMovie.director }}</p>
            <p>러닝타임 : {{ curMovie.length }}</p>
            <p v-if="keywords">
                키워드 : 
                <template 
                v-for="keyword in keywords">
                    <span>
                        <RouterLink :to="{ name: 'movie_search_result', params: { 'category': '키워드', 'name': keyword}}" style="text-decoration: none;">
                            #{{ keyword }}
                        </RouterLink>
                    </span>
                </template>
            </p>
            <button v-if="!isLike" @click.prevent="upLike(curMovie.id, 1)">
                좋아요
            </button>
            <button v-else @click.prevent="upLike(curMovie.id, 2)">
                좋아요 취소
            </button>
        </div>    
    </div>
    <br>
    <hr>
    <div class="row">
        <div v-if="isLoading">불러오는중...</div>
        <div v-else class="col-6">
            <h1>영화 평론</h1>
            <p>해당 구역에 최근에 좋아요 많은 게시물을 표시</p>
            <RouterLink :to="{ name: 'CommunityCreateView', state: { movie_id: curMovie.id, movie_name: curMovie.title } }">
                <p>평론 작성</p>
            </RouterLink>
            <hr>
            <RouterLink v-if="article" :to="{ name: 'CommunityDetailView', params: {'id': article.id} }">
                <h2>{{ article.title }}</h2>
            </RouterLink>
            <p>더보기 및 작성하기</p>
        </div>
        <div class="col-6">
            <h1>평점</h1>
            <div class="form-floating">
                <div class="row">
                    <div class="col-4">
                        <vue3-star-ratings
                            v-model="rating"
                            :starSize="20"
                            starColor="#ff9800"
                            inactiveColor="#333333"
                            :numberOfStars="5"
                            :disableClick="false"
                            />
                    </div>
                    <div class="col" >
                        {{ rating }}
                    </div>
                </div>
                <div>
                    <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 150px" v-model="content"></textarea>
                    <label for="floatingTextarea2"></label>
                    <input type="submit" value="댓글작성" @click="createComment(curMovie.id)">
                </div>
                <hr>
                <h1>코멘트들...</h1>
                <div v-if="isLoading">불러오는중...</div>
                <template v-else>
                    <div v-for="(comment, index) in curMovie.comment_set.slice().reverse()" style="display: flex;" :key="index">
                        <footer>
                            <span>{{ comment.user }} |</span>
                            <span>
                                <span v-if="!(updateNow && comment.id == currentIdx)">{{ comment.content }}</span>
                                <input v-if="updateNow && comment.id == currentIdx" type="text" v-model="contentUpdate">
                            </span>
                            <span>
                            <vue3-star-ratings
                            v-model="comment.point"
                            :starSize="20"
                            starColor="#ff9800"
                            inactiveColor="#333333"
                            :numberOfStars="5"
                            :disableClick="true"
                            />
                            {{ comment.point }}
                            </span>
                            <input type="button" v-if="store.loginUser == comment.user && !updateNow" @click.prevent="commentUpdate(comment.id, comment.content)" value="수정">
                            <input type="button" v-if="store.loginUser == comment.user && updateNow" @click.prevent="commentUpdatePush(comment.id, index)" value="수정완료">
                            <span> | </span>
                            <a v-if="store.loginUser == comment.user || store.isStaff" @click.prevent="commentDelete(comment.id, index)">
                                [삭제]
                            </a>
                            <hr>
                        </footer>
                    </div>
                </template>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router'
import { ref, defineComponent, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter.js'
import vue3StarRatings from "vue3-star-ratings"
import axios from 'axios'

// commentUpdate(comment.id)


const isLike = ref(false)
const rating = ref(0.0)
const score = ref(3.5)
const content = ref(null)
const contentUpdate = ref(null)
const scoreUpdate = ref(null)
const updateNow = ref(false)
const goBack = function () {
    window.history.back()
}

const updateComment = ref(false)
const route = useRoute()
const curMovie = ref()
const store = useCounterStore()
const articles = ref([])
const article = ref(null)
const keywords = ref(null)
const isLoading = ref(true)
const sumRate = ref(0)
const length = ref(0)
const likeusersList = ref([])

const currentIdx = ref(0)

defineComponent({
        components: {
            vue3StarRatings
        }
    })

for(const movie of store.movies){
    if (movie.id === Number(route.params.id)) {
        curMovie.value = movie
        likeusersList.value = movie.like_users
        if (curMovie.value.like_users.includes(store.loginPk)){
            isLike.value = true
        }
        break
    }
}

keywords.value = curMovie.value?.keywords?.filter(item => item.trim() !== '')

const fetchData = async () => {
    sumRate.value = 0
    for(const movie of store.movies){
    if (movie.id === Number(route.params.id)) {
        movie.like_users = likeusersList.value
        if (curMovie.value.like_users.includes(store.loginPk)){
            isLike.value = true
        }
        break
    }
}
    for(const comment of curMovie.value.comment_set){
        sumRate.value += comment.point
        console.log(comment.point)
    }
    score.value = (sumRate.value / curMovie.value.comment_set.length).toFixed(2)

    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/`
    })
    .then(res => {
        console.log(res)
        articles.value = []
        for(const article of res.data){
            if(curMovie.value.id === article.movie){
                articles.value.push(article)
            }
        }
        article.value = articles.value[articles.value.length-1]
        isLoading.value = false
    })
    .catch(err => {
        console.log(err)
    })
}

onMounted(fetchData)


const createComment = function(movie_id) {
    console.log(store.loginUser)
    if(!store.loginUser){
        window.alert('로그인을 하셔야 댓글등록이 가능해요!')
        return
    }
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/movie/${movie_id}/comments/`,
      data: {
        content: content.value,
        point: rating.value,
      },
      headers: {
        Authorization : `Token ${store.token}`
      }
    })
      .then(res => {
        console.log('댓글 생성');
        curMovie.value.comment_set.push(res.data)
        fetchData()
        content.value = ''; // content 초기화
        rating.value = 0; // rating 초기화
        // window.location.reload()
      })
      .catch(err => {
        console.log(err)
        window.alert('댓글을 적어주세요')
      })
}

const commentDelete = function (comment_id, idx) {
    axios({
        method: 'delete',
        url: `${store.API_URL}/api/v1/articles/movie/${comment_id}/comments/update/`,
        headers: {
            Authorization : `Token ${store.token}`
        }
    })
      .then(res => {
        console.log(curMovie.value.comment_set.length)
        length.value = curMovie.value.comment_set.length
        curMovie.value.comment_set.splice(length.value-1-idx, 1)
        console.log('삭제완료')
        fetchData()
      })
      .catch(err => {
        console.log(err)
      })
}

const commentUpdate = function (comment_id, content_) {
    updateNow.value = !updateNow.value
    currentIdx.value = comment_id
    contentUpdate.value = content_
}


const commentUpdatePush = function (comment_id, idx) {
    axios({
        method: 'put',
        url: `${store.API_URL}/api/v1/articles/movie/${comment_id}/comments/update/`,
        data: {
            content: contentUpdate.value,
        },
        headers: {
            Authorization : `Token ${store.token}`
        }
    })
      .then(res => {
        console.log(curMovie.value.comment_set[idx])
        curMovie.value.comment_set[idx].content = contentUpdate.value
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

// movies/<int:movie_pk>/like/
    const upLike = function(movie_pk, type) {
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
            url: `${store.API_URL}/api/v1/movies/${movie_pk}/like/`,
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

</script>

<style scoped>
a {
    cursor: pointer;
    color: blue;
}
</style>