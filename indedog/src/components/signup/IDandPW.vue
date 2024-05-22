<template>
	<div>
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
                        <button @click="checkId">
                            중복확인
                        </button>
                    </span>
                </div>
                <p v-if="isSameId == true">사용할 수 없는 Id입니다.</p>
                <p v-if="isSameId == false">사용 가능한 Id입니다.</p>
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
                    <input type="password" id="password_check" aria-describedby="passwordHelpInline" v-model="password2"
                    @input="checkPasswordSame"
                    >
                </div>
                <p v-if="passwordSame == false">동일한 비밀번호인지 확인!</p>
                <div class="col-auto">
                    <span id="same_check" class="form-text">
                        {{ isSame }}
                    </span>
                </div>
            </div>
            <p v-if="passwordWarning == true">비밀번호는 8자 이상 20자 이하로 설정해주세요.</p>
            <input type="submit" value="회원가입" @click="checkPasswordLength">
        </div>
        </form>
    </div>
        
    </template>
<script setup>
import {ref} from 'vue'
import { onBeforeRouteLeave } from 'vue-router';
import {useCounterStore} from '@/stores/counter'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const isSame = ref('')
const store = useCounterStore()
const isSameId = ref(null)
const passwordWarning = ref(false)
const passwordSame = ref(null)

const signUp = function () {
    console.log(username.value)
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    store.signUp(payload)
}

const checkId = function () {
    for (const userInfo of store.userList) {
        console.log('###')
        console.log(userInfo.username)
        console.log('###')
        if (userInfo.username == username.value) {
            isSameId.value = true
            console.log('same')
            return
        }
    }
    isSameId.value = false
    console.log('ok')
}

const checkPasswordLength = function () {
    if (password1.value.length < 8 || password1.value.length > 20 || password2.value.length < 8 || password2.value.length > 20) {
        passwordWarning.value = true
    }
}

const checkPasswordSame = function () {
    console.log(password1.value)
    console.log(password2.value)
    if (password1.value == password2.value) {
        passwordSame.value = true
    } else {
        passwordSame.value = false
    }
}

</script>


<style scoped></style>