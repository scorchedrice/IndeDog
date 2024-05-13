<template>
    <div class = "container row align-items-center">
        <div class="col">
            <h1>오늘의 추천 영화</h1>
        </div>
        <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel" style="width: 200px;">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="@/assets/icon/site_icon_1.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/icon/site_icon_1.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/icon/site_icon_1.jpg" class="d-block w-100" alt="...">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
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