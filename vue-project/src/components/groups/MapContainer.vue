<script lang="js" setup>
import {ref} from "vue";

const zoom = ref(9);
const center = ref([110.349,38.9568]);

</script>

<template>
  <div class="map-page-container" style="width: 100%;height: 100%;">
    <el-amap
      :center="center"
      :zoom="zoom"
    >
    <el-amap-marker
        :position="center"
        :zIndex="100"
      >
    </el-amap-marker>
    </el-amap>
  </div>
</template>

<style>

</style>