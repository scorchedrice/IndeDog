<template>
    <div class="container">
        <div class="accordion accordion-flush" id="mobile_notice" style="width: 100%">
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#mobile_notice_sub" aria-expanded="false" aria-controls="#mobile_notice_sub">
                        공지사항
                    </button>
                </h2>
                <div id="mobile_notice_sub" class="accordion-collapse collapse" data-bs-parent="#mobile_notice">
                    <div class="accordion-body">공지사항 나열~</div>
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