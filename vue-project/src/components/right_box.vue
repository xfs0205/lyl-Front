<script setup lang="js">
import { ref, onMounted, onUnmounted } from 'vue'
import Table from '@/components/Lists/table.vue'
import group2 from '@/components/groups/group2.vue';
import weatherdata from '@/assets/weatherData.json'
import axios from 'axios';

const data = ref({
    "head": [],
    "body": [["张三", "男", "18"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"],
    ["张三", "男", "18"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"]]
})

// 用于存储从服务器获取的数据
const newData = ref()

// 设置定时器，每隔10秒获取一次数据
const getData = () =>{
    axios.get('http://47.102.108.198:8899/get')
        .then(re => {
            newData.value = {
                "header": ["日期", "属性", "值"],
                "data": [
                    ["温度", re.data.Temperature, "正常"],
                    ["湿度", re.data.Humidity, "正常"],
                    ["风速", re.data.WindSpeed, "正常"],
                    ["风向", re.data.Direction, "正常"],
                    ["气压", re.data.AirPressure, "正常"],
                    ["光照", re.data.Lighting, "正常"],
                    ["降雨量", re.data.Rainfall, "正常"]
                ],
                "index": true,
                "columnWidth": [50],
                "align": ["center"]
            }
        })
        .catch(error => console.error('Error:', error));
}

let intervalId = null;

// 在组件挂载时设置定时器
onMounted(() => {
    getData();
    intervalId = setInterval(getData, 5000);
});

// 在组件销毁时清除定时器
onUnmounted(() => {
    clearInterval(intervalId);
});
</script>

<template>
    <div class="top">
        <dv-border-box1 style="display: flex;height: 100%;">
            <div style="width: 100%;" h18rem color-white flex justify-center items-center>
                <strong style="color: orange; text-shadow: 2px 2px 4px #000000;font-size: 12px;">实时墒情信息</strong>
            </div>
            <Table :data="data" style="height: 80%;width: 80%;margin-left: 10%;" />
        </dv-border-box1>
    </div>
    <div class="bottom">
        <dv-border-box8 style="display: flex;height: 100%;">
            <div class="title">
                <dv-decoration-7 style="width:70%;height:100%;">
                    <strong style="
                    color: orange;
                    font-style: italic;
                    text-shadow: 2px 2px 4px #000000;
                    font-size: 17px;
                    ">实时环境信息</strong>
                </dv-decoration-7>
            </div>
            <div class="time-list">
                <group2></group2>
            </div>
            <div class="center-list">
                <dv-scroll-board :config="newData" style="width:90%;height:90%" />
            </div>
        </dv-border-box8>
        <div style="width: 90%;height: 3px;background-color: #ccc;position: absolute;top: 35.5%;left: 5%;" />
    </div>
</template>

<style scoped lang="scss">
.top {
    width: 100%;
    height: 30%;
    background-color: transparent;
}

.bottom {
    position: relative;
    width: 100%;
    height: 70%;
    background-color: rgb(0, 0, 0, 0);

    .title {
        width: 100%;
        height: 10%;
        background-color: rgb(0, 0, 0, 0);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .time-list {
        width: 100%;
        height: 25%;
        background-color: rgb(0, 0, 0, 0);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .center-list {
        width: 100%;
        height: 65%;
        background-color: rgb(0, 0, 0, 0);
        display: flex;
        justify-content: center;
        align-items: center;
    }

}
</style>