<template>
	<div class="container" style="background-color: blue;">
        <form @submit.prevent="signUp">
        <div id="userId">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="inputId" class="col-form-label">ID</label>
                </div>
                <div class="col-auto">
                    <input type="text" v-model.trim="username" id="userIdInput" aria-describedby="passwordHelpInline">
                </div>
                <div class="col-auto">
                    <span id="IdHelpInline">
                        <button>
                            중복확인
                        </button>
                    </span>
                </div>
            </div>
        </div>
        <br>
        <div id="password">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="inputPassword6" class="col-form-label">Password</label>
                </div>
                <div class="col-auto">
                    <input type="password" id="password_init" aria-describedby="passwordHelpInline" v-model="password1">
                </div>
                <div class="col-auto">
                    <span id="passwordHelpInline" class="form-text">
                        8자 이상, 20자 이하이여야 합니다.
                    </span>
                </div>
            </div>
        </div>
        <br>
        <div id="password_check">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="inputPassword6" class="col-form-label">Password</label>
                </div>
                <div class="col-auto">
                    <input type="password" id="password_check" aria-describedby="passwordHelpInline" v-model="password2">
                </div>
                <div class="col-auto">
                    <span id="same_check" class="form-text">
                        {{ isSame }}
                    </span>
                </div>
            </div>
            <input type="submit" value="회원가입">
        </div>
        </form>
    </div>
        
    </template>
<script setup>
import {ref} from 'vue'
import { onBeforeRouteLeave } from 'vue-router';
import {useCounterStore} from '@/stores/counter'

// onBeforeRouteLeave((to, from) => {
//     document.querySelector('#menu').style.display='block';
// })
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const isSame = ref('')
// const idInput = function (event) {
//     userId.value = event.currentTarget.value
// }
const store = useCounterStore()

// const passwordInput = function (event) {
//     if (event.currentTarget.id === 'password_init') {
//         passwordInit.value = event.currentTarget.value
// 	} else {
// 		passwordSecond.value = event.currentTarget.value
// 		if (passwordInit.value === passwordSecond.value) {
// 			isSame.value = '비밀번호가 일치합니다!'
// 		} else if (passwordSecond.value !== '') {
// 			isSame.value = '비밀번호가 동일하지 않습니다!'
// 		}
// 	}
// }

// const sameCheck = function () {
// 	console.log(passwordInit.value)
// }

const signUp = function () {
    console.log(username.value)
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    store.signUp(payload)
}

</script>


<style scoped></style>