<template>
    <div style="position: fixed; top: 10px; left: 30px;" id="Menu">
        <img src="@/assets/icon/site_icon_1.jpg" class="rounded col" alt="Home" width="80px" height="80px" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasWithBothOptions" aria-controls="offcanvasWithBothOptions">
        <div class="offcanvas offcanvas-start" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1" id="offcanvasWithBothOptions" aria-labelledby="offcanvasWithBothOptionsLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasWithBothOptionsLabel">Menu</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
        <ul class="list-group list-group-flush">
            <div class = "accordion" id="login">
            <h2 class="accordion-header">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                로그인 / 회원가입
                </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
                <div class="accordion-body">
                    <div v-if="!store.token">
                    <form @submit.prevent="logIn">
                        <div id="login_form">
                            <div class="form-floating mb-3">
                                <input type="id" class="form-control" id="floatingInput" placeholder="name@example.com" v-model.trim="username">
                                <label for="floatingInput">ID</label>
                            </div>
                            <div class="form-floating">
                                <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model.trim="password">
                                <label for="floatingPassword">Password</label>
                            </div>
                            <br>
                            <div class="container" style="display: flex; justify-content: space-between;" v-if="!store.token">
                                <button type="submit" class="btn btn-outline-success" style="margin-left:auto;">
                                    Login
                                </button>
                            </div>
                        </div>
                    </form>
                    <hr>
                    <div>
                        <strong>아직 회원이 아니신가요?</strong>
                        <p class="text-primary" style="text-decoration: underline;" @click.prevent="goSignUp">회원가입</p>
                    </div>
                    </div>
                    <div v-if="store.token">
                        <div>
                            <img style="width: 50px; border-radius: 50px; border: solid black 1px;" src="../assets/avatar/basic3.png" alt="">
                        </div>
                        <h1>{{ store.loginUser }} 님</h1>
                        <h4>환영합니다!</h4>
                        <div>
                            <button @click.prevent="store.logOut" class="btn btn-outline-danger" style="margin-left:auto;">
                                Logout
                            </button>
                        </div>
                        <RouterLink :to="{ name: 'userpage', params: { 'username': store.loginUser }}">
                            유저페이지
                        </RouterLink>
                    </div>
                </div>
            </div>
            </div>
            <li class="list-group-item"><strong>Inde-Dog 소개</strong></li>
            <li class="list-group-item" @click.prevent="goNotice"><strong>공지사항 / 이벤트</strong></li>
            <li class="list-group-item"></li>
            <li class="list-group-item" @click.prevent="goMovieSearch">작품 검색</li>
            <li class="list-group-item" @click.prevent="goCinemaSearch">현재 상영작 / 상영관 검색</li>
            <li class="list-group-item" @click.prevent="goCommunity">커뮤니티</li>
            <li class="list-group-item" @click.prevent="goJob">구인공고</li>
        </ul>
        </div>
    </div>
    </div>
</template>

<script setup>
import {useRoute,useRouter} from 'vue-router'
import {ref} from 'vue'
import {useCounterStore} from '@/stores/counter.js'
import { FwbAvatar } from 'flowbite-vue'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function() {
    const payload = {
        username: username.value,
        password: password.value
    }
    username.value = null
    password.value = null
    store.logIn(payload)
}

const router = useRouter()

const goJob = function() {
    console.log('구인공고')
    router.push({name: 'job'})
}
const goNotice = function() {
    console.log('공지사항')
    router.push({name: 'notice'})
}
const goMovieSearch = function () {
    console.log('movie-search')
    router.push({name:'movie_search'})
}
const goCinemaSearch = function () {
    console.log('cinema-search')
    router.push({name: 'cinema_list'})
}
// const goNowInTheater = function () {
//     console.log('now in theater')
//     router.push({name: 'now_in_theater'})
// }
const goCommunity = function () {
    console.log('community')
    router.push({name: 'community'})
}
const goSignUp = function () {
    console.log('SignUp')
    router.push({name: 'signup'})
}
</script>

<style scoped>

</style>