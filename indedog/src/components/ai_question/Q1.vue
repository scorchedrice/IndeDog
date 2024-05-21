<template>
    <div>
        <h1>안녕하세요? 오늘 날씨 어때요?</h1>
        <template>
            <fwb-radio v-model="picked" name="radio" label="Radio 1" value="one" />
            <fwb-radio v-model="picked" name="radio" label="Radio 2" value="two" />
        </template>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { FwbRadio } from 'flowbite-vue'

const picked = ref()
</script>

<style scoped>

</style>
