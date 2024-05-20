<template>
    <div>

    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>

<!-- <div class = "col-5 align-items-center justify-content-start" style="padding-left: 0px; padding-right: 0px; border: 5px solid black;">
    <h1 style="text-align: center;">상영중인 영화</h1>
    <div id="carousel_now_in_theater" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
        <div v-for="movie in recentMovie"
            :key="movie.id">
            <div v-if="movie.id==10000" class="carousel-item active" style="margin: auto;">
                <div class="container" style="text-align: center;">
                    <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                        <img :src="movie.img_src" class="d-block w-100" alt="...">
                    </RouterLink>
                    <div>
                        <h2>{{ movie.title }} - {{ movie.director }}</h2>
                        <h3 v-if="movie.title_en !=''">{{ movie.title_en }}</h3>
                        <p>Genre: {{ movie.genre }}</p>
                        <p>RunningTime: {{ movie.length }}</p>
                    </div>
                </div>
            </div>
            <div v-if="movie.id>10000" class="carousel-item" style="margin: auto">
                <div class="container row align-items-center">
                    <div>
                        <RouterLink :to="{ name: 'movie_detail', params: { 'id': movie.id } }">
                            <img :src="movie.img_src" class="d-block w-100" alt="...">
                        </RouterLink>
                    </div>
                    <div>
                        <h2>{{ movie.title }} - {{ movie.director }}</h2>
                        <p>Genre: {{ movie.genre }}</p>
                        <p>RunningTime: {{ movie.length }}</p>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carousel_now_in_theater" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carousel_now_in_theater" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
        </button>
    </div> -->