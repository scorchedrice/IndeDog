<template>
    <div class="container">
        <div class="accordion accordion-flush" id="mobile_recommend" style="width: 100%">
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#mobile_recommend_sub" aria-expanded="false" aria-controls="mobile_recommend_sub">
                        추천영화
                    </button>
                </h2>
                <div id="mobile_recommend_sub" class="accordion-collapse collapse" data-bs-parent="#mobile_recommend">
                    <div class="accordion-body">추천영화 나열~</div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import {ref, onMounted, computed } from 'vue'

</script>

<style scoped>

</style>