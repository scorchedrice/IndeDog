<template>
    <div id="app">
      <NaverMap :center="{lat: 37.566535, lng: 126.97796}" :zoom="3">
        <NaverInfoWindow
          :content="'<div>Hello, world!</div>'"
          :position="map.getCenter()"
        />
      </NaverMap>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { NaverMap, NaverInfoWindow } from 'vue3-naver-maps';
  
  const map = ref(null);
  
  // NaverMap이 마운트된 후에 info-window를 생성합니다.
  map.value.$on('mounted', () => {
    const infoWindow = new NaverInfoWindow({
      content: '<div>Hello, world!</div>',
      position: map.value.getCenter()
    });
  
    map.value.addOverlay(infoWindow);
  });
  </script>