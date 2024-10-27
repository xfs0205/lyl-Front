<script setup lang="js">


</script>

<template>
  <div class="left_right_box button">
    <div style="text-align: left;font-size: 10px;white-space: nowrap; margin-top: 3px;margin-bottom: 5px;">
        <slot name="title"></slot>
    </div>
    <div style="text-align: left;font-size: 10px;white-space: nowrap;">
        <slot name="content"></slot>
    </div>
  </div>
</template>

<style scoped lang="scss">
.left_right_box{
    margin-top: 5px;
    display: flex;
    width: 90%;
    height: 40px;
}

.left_right_box > div {
    flex: 1; /* 子元素平均分配剩余空间 */
    display: flex;
    padding-left: 4px;
    align-items: center; /* 垂直居中对齐文本 */
}

/* 按钮样式 */
.button {
    display: inline-block;
    border: 2px solid #ff8e2c; /* 边框 */
    border-radius: 5px; /* 圆角 */
    background-color: (0,0,0,0); /* 背景色 */
    color: #333; /* 文字颜色 */
    text-align: center; /* 文字居中 */
    cursor: pointer; /* 鼠标悬停时显示手型 */
}

/* 文本样式 */
.text {
    font-size: 14px; /* 字体大小 */
    color: #666; /* 文字颜色 */
    margin: 0 5px; /* 文字之间的间距 */
}

/* 特殊文本样式，例如“离线” */
.text-offline {
    color: red; /* 红色文字 */
}
</style>