<script setup lang="js">
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';

var chartDom = ref(null);
var option;

const dataCount = 1000; // 你可以根据需要调整这个数值
const data = generateInsectData(dataCount); // 使用新的数据生成函数

option = {
    dataset: {
        source: data
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line'
        }
    },
    grid: {
        left: '5%',
        right: '5%',
        bottom: '39',
        top: '10',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        axisLine: { onZero: false },
        splitLine: { show: false },
        data: data.map(item => item[0]), // 时间戳作为X轴数据
        axisLabel: {
            color: '#fff' // 设置 X 轴标签文本颜色为白色
        }
    },
    yAxis: {
        scale: true,
        splitArea: {
            show: true
        },
        axisLabel: {
            color: '#fff' // 设置 X 轴标签文本颜色为白色
        }
    },
    dataZoom: [
        {
            type: 'inside',
            start: 50,
            end: 100,
        },
        {
            show: true,
            type: 'slider',
            bottom: 10,
            start: 0,
            end: 50,
            textStyle: {
        color: 'orange' // 设置提示框文字颜色为白色
    }
        }
    ],
    series: [
        {
            type: 'line',
            data: data.map(item => item[1]),
            symbolSize: 1,
            color: '#7fbe9e',
            areaStyle: {
                color: '#7fbe9e'
            },
        }
    ]
};

function generateInsectData(count) {
    let data = [];
    let xValue = +new Date(2011, 0, 1);
    let fiveMinutes = 5 * 60 * 1000; // 5分钟的毫秒数
    for (let i = 0; i < count; i++) {
        let insectCount = Math.random() * 100; // 生成一个0到100之间的随机昆虫数
        data[i] = [
            echarts.format.formatTime('yyyy-MM-dd\nhh:mm:ss', xValue),
            +insectCount.toFixed(0)
        ];
        xValue += fiveMinutes; // 增加时间戳5分钟
    }
    return data;
}

onMounted(() => {
    var myChart = echarts.init(chartDom.value);
    option && myChart.setOption(option);
});
</script>

<template>
    <div ref="chartDom" style="display: flex;width: 100%;height: 100%;"></div>
</template>

<style lang="scss"></style>