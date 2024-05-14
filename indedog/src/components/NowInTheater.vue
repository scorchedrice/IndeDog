<template>
    <div class = "container">
        <h1>상영중인 영화</h1>
        <div id="carousel_now_in_theater" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
            <div class="carousel-item active">
                <div class="container row align-items-center">
                    <div class="col-4">
                        <img src="@/assets/movie_ex1.jpeg" class="d-block w-100" alt="...">
                    </div>
                    <div class="col-8">
                        <h2>이곳에 영화 정보를 적습니다.</h2>
                    </div>
                </div>
            </div>
            <div class="carousel-item">
                <div class="container row align-items-center">
                    <div class="col-4">
                        <img src="@/assets/movie_ex2.jpeg" class="d-block w-100" alt="...">
                    </div>
                    <div class="col-8">
                        <h2>이곳에 영화 정보를 적습니다.</h2>
                    </div>
                </div>
            </div>
            <div class="carousel-item">
                <div class="container row align-items-center">
                    <div class="col-4">
                        <img src="@/assets/movie_ex3.jpeg" class="d-block w-100" alt="...">
                    </div>
                    <div class="col-8">
                        <h2>이곳에 영화 정보를 적습니다.</h2>
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
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>
