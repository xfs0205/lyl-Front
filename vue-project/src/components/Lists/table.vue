<script setup lang="js">
import { defineProps, ref } from 'vue'

// 定义组件的 props
const props = defineProps({
    data: {
        type: Object,
        default: () => ({
            head: [],
            body: [[], [], []]
        })
    },
    height: {
        type: Number,
        default: 15
    },
    front_size: {
        type: Number,
        default: 10
    }
})
</script>

<template>
    <el-scrollbar style="height: 100%;width: 100%; justify-content: center;">
        <div class="list-component">
            <!-- 渲染头部信息 -->
            <div class="list-header" v-if="props.data.head.length > 0">
                <div v-for="(item, index) in props.data.head" :key="index" class="header-item">
                    <strong style="color: whitesmoke;font-size: 12px;">{{ item }}</strong>
                </div>
            </div>
            <!-- 渲染列表数据 -->
            <div class="list-body">
                <div v-for="(row, rowIndex) in props.data.body" :key="'row' + rowIndex" class="body-row"
                :style="{ height: props.height + 'px'}"
                >
                    <div v-for="(cell, cellIndex) in row" :key="'cell' + cellIndex" class="body-cell"
                    :style="{ width: (100 / row.length) + '%', fontSize: props.front_size + 'px'}"
                    >
                        {{ cell }}
                    </div>
                </div>
            </div>
        </div>
    </el-scrollbar>
</template>

<style scoped lang="scss">
.list-component {
    width: 100%;
    border: 0;
}

.list-header {
    display: flex;
    background-color: rgba(255, 255, 255, 0.5);
}

.header-item {
    flex: 1;
    text-align: center;
    border-right: 1px solid #ccc;

    &:last-child {
        border-right: none;
    }
}

.list-body {
    display: flex;
    flex-direction: column;
    background-color: rgba(34, 52, 102, 0.4);
}

.body-row {
    display: flex;
    border: 0;
    background-color: rgba(255, 255, 255, 0.05); 
    justify-content: center;
    align-items: center;
    &:nth-child(odd) {
        background-color: rgba(255, 255, 255, 0.18); 
    }
}

.body-cell {
    flex: 1;
    text-align: center;
    border: 0;
    color: aliceblue;
    font-size: 10px;
}
</style>