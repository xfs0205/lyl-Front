<script setup lang="js">
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';

var chartDom = ref(null);
var option;

option = {
  grid: {
    left: '5%', // 增加左边距
    right: '5%', // 增加右边距
    bottom: '3%',
    top: "5%",
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
    axisLabel: {
        rotate: 30,
        fontSize: 6,
        color: '#fff'
    },
    interval: 0 
  },
  yAxis: {
    type: 'value',
    min: 0,
    max: 30,
    axisLabel: {
        color: '#fff'
    },
  },
  series: [
    {
      data: [15, 23, 22, 21, 13, 14, 26, 15, 23, 22, 21, 13],
      type: 'line'
    }
  ]
};

onMounted(() => {
    var myChart = echarts.init(chartDom.value);
    option && myChart.setOption(option);
});
</script>

<template>
    <div ref="chartDom" style="display: flex;width: 100%;height: 100%;"></div>
</template>

<style lang="scss"></style>