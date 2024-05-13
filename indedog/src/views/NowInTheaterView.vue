<template>
    <div>
        <h1>현재 상영중인 영화 목록을 나열합니다.</h1>
        <h2>동시에 상영관 목록도 나타냅니다.</h2>
        <button>
            <RouterLink :to="{name: 'now_cinema_detail'}">
                detail example
            </RouterLink>
        </button>
        <RouterView/>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>