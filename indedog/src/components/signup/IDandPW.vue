<template>
	<div class="container" style="background-color: blue;">
        
        <div id="userId">
            <div class="row g-3 align-items-center">
                <div class="col-auto">
                    <label for="inputId" class="col-form-label">ID</label>
                </div>
                <div class="col-auto">
                    <input type="text" id="userIdInput" class="form-control" aria-describedby="passwordHelpInline" @input="idInput">
                </div>
                <div class="col-auto">
                    <span id="IdHelpInline" class="form-text">
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
                    <input type="password" id="password_init" class="form-control" aria-describedby="passwordHelpInline" @input="passwordInput">
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
                    <input type="password" id="password_check" class="form-control" aria-describedby="passwordHelpInline"  @input="passwordInput">
                </div>
                <div class="col-auto">
                    <span id="same_check" class="form-text">
                        {{ isSame }}
                    </span>
                </div>
            </div>
        </div>
    </div>
        
    </template>
<script setup>
import {ref} from 'vue'
import { onBeforeRouteLeave } from 'vue-router';
onBeforeRouteLeave((to, from) => {
    document.querySelector('#menu').style.display='block';
})
const userId = ref('')
const passwordInit = ref('')
const passwordSecond = ref('')
const isSame = ref('')
const idInput = function (event) {
    userId.value = event.currentTarget.value
}
const passwordInput = function (event) {
    if (event.currentTarget.id === 'password_init') {
        passwordInit.value = event.currentTarget.value
	} else {
		passwordSecond.value = event.currentTarget.value
		if (passwordInit.value === passwordSecond.value) {
			isSame.value = '비밀번호가 일치합니다!'
		} else if (passwordSecond.value !== '') {
			isSame.value = '비밀번호가 동일하지 않습니다!'
		}
	}
}

const sameCheck = function () {
	console.log(passwordInit.value)
}

</script>


<style scoped></style>