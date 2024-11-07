<script setup lang="js">
import { ref, defineProps, defineEmits } from 'vue';

const emit = defineEmits(['label']);
const props = defineProps({
    data: {
        type: Array,
        required: true
    },
    keys: {
        type: Object,
        default: () => ({
            label: 'label',
            children: 'children'
        })
    },
    lightdata: {
        type: Array,
        default: () => [false]
    },
    isfsHead: {
        type: Boolean,
        default: () => true
    },
    fsindex: {
        type: Number,
        default: () => 0
    },
    fscolor: {
        type: String,
        default: () => '#fff'
    },
    fssize:{
        type: Number,
        default: () => 10
    },
    fsfontfamily:{
        type: String,
        default: () => 'Arial'
    }
});

const showTrees = ref(props.data.map(() => true))
const lightdata = ref([])
const showTreesLight = ref()

// 如果有子节点，就为每个子节点创建一个独立的 lightdata 状态
resetL()

// 如果是根级节点，就为每个子节点创建一个独立的 showTreeLight 状态
if (props.isfsHead) {
    showTreesLight.value = props.data.map(() => false)
}
// 点击事件
const HandleClick = (index) => {
    emit('label', [props.fsindex, index]);
    showTrees.value[index] = !showTrees.value[index];
    if (props.isfsHead) {
        showTreesLight.value = ref(props.data.map(() => false))
        showTreesLight.value[props.fsindex] = !showTreesLight.value[props.fsindex];
    }
    resetL()
};
// 处理返回事件
const HandleReturn = (indexs) => {
    const l = ref([props.fsindex])
    l.value = l.value.concat(indexs)
    // 如果是根级节点，就重置数据
    if (props.isfsHead) {
        showTreesLight.value = props.data.map(() => false)
        showTreesLight.value[props.fsindex] = !showTreesLight.value[props.fsindex];
    }
    // 如果有子节点，就子节点重置数据
    resetL()
    lightdata.value[indexs[0]][indexs[1]] = true
    emit('label', l.value);
}

function resetL(){
    lightdata.value = []
    props.data.map((item) => {
        if (item[props.keys.children] && item[props.keys.children].length)
            lightdata.value.push(item[props.keys.children].map(() => false))
        else lightdata.value.push([])
    })
}
</script>

<template>
    <ul>
        <li v-for="item, index in props.data" :key="index" class="fx-tree">
            <span v-if="props.isfsHead" class="tree-label no-select" 
                :class="{ 'active': showTreesLight[index]}" 
                :style="{ color: props.fscolor, fontSize: props.fssize + 'px', fontFamily: props.fsfontfamily }"
                @click="HandleClick(index)">
                <strong> {{ item[props.keys.label] }}</strong>
            </span>
            <span v-else class="tree-label no-select" 
                :class="{ 'active': props.lightdata[index] }"
                :style="{ color: props.fscolor, fontSize: props.fssize + 'px' }"
                @click="HandleClick(index)">{{
                    item[props.keys.label] }}</span>
            <fx-tree v-if="item[props.keys.children] && item[props.keys.children].length && showTrees[index]" 
                @label="HandleReturn" :data="item[props.keys.children]" :keys="props.keys" :fsindex="index"
                :isfsHead="false" :lightdata="lightdata[index]" />
        </li>
    </ul>
</template>

<style lang="scss" scoped>
.fx-tree {
    background-color: rgb(0,0,0,0);
    margin-left: 10px;
    list-style-type: none; // 隐藏默认的列表项符号

    .tree-label {
        position: relative; // 将定位上下文设置为文本元素
        padding-left: 20px; // 为图标留出空间
        cursor: pointer; // 设置鼠标悬浮时的小手光标

        &::before {
            content: ''; // 这是一个伪元素，用于放置图标
            position: absolute;
            left: 0; // 将图标放置在左边
            top: 50%; // 垂直居中
            transform: translateY(-50%); // 精确垂直居中
            width: 16px; // 图标宽度
            height: 16px; // 图标高度
            background-image: url('@/assets/tree.png'); // 图标路径
            background-size: cover; // 确保图标完全覆盖伪元素区域
        }
    }

    .tree-label:hover {
        background-color: rgba(115, 243, 255, 0.758);
    }

    .active {
        background-color: rgba(115, 243, 255, 0.758); // 定义被激活的样式
    }
}

.no-select {
    -webkit-user-select: none;
    /* Chrome/Safari */
    -moz-user-select: none;
    /* Firefox */
    -ms-user-select: none;
    /* IE/Edge */
    user-select: none;
    /* Standard syntax */
}
</style>