<template>
  <div>
    <div>
        <h1>
            <div style="text-align: center; margin-top: 20px;">
                <img src="@/assets/icon/site_icon_1.jpg" class="rounded col" alt="Home" width="100px" height="100px">
            </div>
        </h1>
    </div>
  <div style="width: fit-content; text-align: center;">
    <RouterView />
  </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>