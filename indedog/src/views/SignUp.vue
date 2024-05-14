<template>
	<div class="container" style="background-color: green;">
        <h1>회원가입 페이지입니다.</h1>
	</div>
</template>

<script setup>
import { onBeforeRouteLeave } from 'vue-router';
onBeforeRouteLeave((to, from) => {
	document.querySelector('#menu').style.display='block';
})



</script>


<style scoped></style>