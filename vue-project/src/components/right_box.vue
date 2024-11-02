<script setup lang="js">
import { ref } from 'vue'
import Table from '@/components/Lists/table.vue'
import group2 from '@/components/groups/group2.vue';

const data = ref({
    "head": [],
    "body": [["张三", "男", "18"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"],
    ["张三", "男", "18"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"], ["李四", "女", "19"]]
})

const config = ref({
  header: ['列1', '列2', '列3'],
  data: [
    ['行1列1', '行1列2', '行1列3'],
    ['行2列1', '行2列2', '行2列3'],
    ['行3列1', '行3列2', '行3列3'],
    ['行4列1', '行4列2', '行4列3'],
    ['行5列1', '行5列2', '行5列3'],
    ['行6列1', '行6列2', '行6列3'],
    ['行7列1', '行7列2', '行7列3'],
    ['行8列1', '行8列2', '行8列3'],
    ['行9列1', '行9列2', '行9列3'],
    ['行10列1', '行10列2', '行10列3'],
  ],
  index: true,
  columnWidth: [50],
  align: ['center'],
})
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
                <dv-scroll-board :config="config" style="width:90%;height:90%" />
            </div>
        </dv-border-box8>
        <div style="width: 90%;height: 3px;background-color: #ccc;position: absolute;top: 35.5%;left: 5%;"/>
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

    .time-list{
        width: 100%;
        height: 25%;
        background-color: rgb(0, 0, 0, 0);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .center-list{
        width: 100%;
        height: 65%;
        background-color: rgb(0, 0, 0, 0);
        display: flex;
        justify-content: center;
        align-items: center;
    }

}
</style>