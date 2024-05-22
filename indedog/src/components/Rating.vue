<template>
    <div class="form-floating">
        <h1>이곳의 평점은?</h1>
        <div style="display: flex;">
            <vue3-star-ratings
                v-model="curRating"
                :starSize="50"
                starColor="#ff9800"
                inactiveColor="#333333"
                :numberOfStars="5"
                :disableClick="true"
                />
            <h2 class="ms-2">{{ curRating }}</h2>
        </div>
        <div class="row">
            <div>
                <hr>
                <vue3-star-ratings
                    v-model="rating"
                    :starSize="20"
                    starColor="#ff9800"
                    inactiveColor="#333333"
                    :numberOfStars="5"
                    :disableClick="false"
                    />
            </div>
            <div>
                {{ rating }}
            </div>
        </div>
        <div>
            <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 150px" v-model="content"></textarea>
            <label for="floatingTextarea2"></label>
            <input type="submit" value="댓글작성" @click.prevent="createComment(address)">
        </div>
        </div>
        <hr>
        <h1>
            코멘트들...
        </h1>
        <div v-for="comment in comments">
            <div>
                <vue3-star-ratings
                    v-model="comment.point"
                    :starSize="20"
                    starColor="#ff9800"
                    inactiveColor="#333333"
                    :numberOfStars="5"
                    :disableClick="true"
                    />
            </div>
            {{ comment.content }}
            {{ comment.user }}
        </div>
</template>
  
<script setup>
import { defineComponent, ref, onMounted } from "vue"
import vue3StarRatings from "vue3-star-ratings"
import { useCounterStore } from "@/stores/counter"
import axios from 'axios'

const store = useCounterStore()
const comments = ref(null)
const sumRating = ref(0)
const curRating = ref(0.0)

const cinemaName = defineProps({
    address: String
})
defineComponent({
    components: {
        vue3StarRatings
    }
})

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/cinemas/`
    })
    .then(res => {
        console.log(res)
        comments.value = []
        for(const cinema of res.data){
            if(cinema.address === cinemaName.address){
                comments.value = cinema.comment_set
            }
        }
        comments.value.forEach(element => {
            sumRating.value += element.point
        })
        curRating.value = (sumRating.value / comments.value.length).toFixed(2)
        console.log(curRating.value)
    })
    .catch(err => {
        console.log(err)
    })
})

const fetchData = async (address) => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/cinemas/`
    })
    .then(res => {
        console.log(res)
        comments.value = []
        for(const cinema of res.data){
            if(cinema.address === address){
                comments.value = cinema.comment_set
            }
        }
        comments.value.forEach(element => {
            sumRating.value += element.point
        })
        curRating.value = (sumRating.value / comments.value.length).toFixed(2)
        console.log(curRating.value)
    })
    .catch(err => {
        console.log(err)
    })
}

const rating = ref(0)
const content = ref('')
const createComment = function(address) {
    sumRating.value = 0
    console.log(store.loginUser)
    if(!store.loginUser){
        window.alert('로그인을 하셔야 댓글등록이 가능해요!')
        return
    }
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/cinema/${address}/comments/`,
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
        content.value = ''; // content 초기화
        rating.value = 0; // rating 초기화
        // window.location.reload()
        fetchData(address)
      })
      .catch(err => {
        console.log(err)
        window.alert('댓글을 적어주세요')
      })
}
// 아래는 평점 확인 용 임시 js
const checkStar = function () {
    console.log(rating.value)
}
</script>