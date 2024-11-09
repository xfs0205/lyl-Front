<script setup lang="js">
import left_right_box from '@/components/Lists/left_right_box.vue'
import { ref } from 'vue'
import {HelpFilled} from "@element-plus/icons-vue"
import shangqingJson from '@/assets/forest.json';
import device from '@/assets/device.json';
const handleNodeClick = (data) => {
    console.log(data)
}

const data = [
    shangqingJson
]

const defaultProps = {
    children: 'children',
    label: 'label',
}

const data2 = ref(device)

</script>

<template>
    <div class="top">
        <dv-border-box1>
            <div style="width: 100%;" h18rem color-white flex justify-center items-center>
                <strong style="color: orange;font-style: italic; text-shadow: 2px 2px 4px #000000;">信息发布</strong>
            </div>
            <div style="margin-top: 5px;margin-left: 15px;margin-bottom: 15px;">
                <div style="color: orange;font-size: 10px; text-align: left;">2024年10月18日，建设草原生态监测站</div>
            </div>
        </dv-border-box1>
    </div>
    <div class="bottom">
        <dv-border-box13 style="height: 100%;
        width: 100%;padding-left: 10px;padding-bottom: 10px;
        padding-right: 10px;padding-top: 20px;
        position: relative;">
            <div class="left">
                <el-tree :data="data" :props="defaultProps" @node-click="handleNodeClick" default-expand-all />
            </div>
            <div class="right">
                <el-scrollbar style="height: 100%;width: 100%; justify-content: center;">
                    <div style="text-align: left;color: orange;"><strong>设备列表</strong></div>
                    <left_right_box v-for="(item, index) in data2" :key="index">
                        <template #title>
                            <div class="title" style="color: aliceblue;">{{ item.row1 }}
                            <el-icon color="white" style="vertical-align: middle;">
                                <HelpFilled /></el-icon>{{ item.state }}</div>
                        </template>
                        <template #content>
                            <div class="content" style="color: aliceblue;">{{ item.row2 }}
                                <span style="text-align: end;">{{ item.number }}</span>
                            </div>
                        </template>
                    </left_right_box>
                </el-scrollbar>
            </div>
        </dv-border-box13>
    </div>
</template>

<style scoped lang="css">
.top {
    width: 100%;
    height: 30%;
    background-color: rgb(0, 0, 0, 0);
}

.bottom {
    width: 100%;
    height: 70%;
    background-color: rgb(0, 0, 0, 0);

    .left {
        position: absolute;
        display: flex;
        width: 50%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0);
    }

    .right {
        right: 0;
        position: absolute;
        display: flex;
        width: 50%;
        height: 100%;
        background-color: (0,0,0,0);
    }
}

.el-tree {
    background: rgba(0, 0, 0, 0);
    width: 100%;
    font-size: 10px;
    color: aqua;
}
</style>