<template>
	<div class="container" style="background-color: green;">
        <h1>회원가입 페이지입니다.</h1>
		<div>
			<UserDetail/>
		</div>
		<br>
		<div>
			<IDandPW/>
		</div>
	</div>
</template>
<script setup>
import IDandPW from '@/components/signup/IDandPW.vue'
import UserDetail from '@/components/signup/UserDetail.vue'
</script>


<style scoped></style>