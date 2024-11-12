<!-- <script setup lang="js">
import Head from '@/components/head.vue';
import left_box from '@/components/left_box.vue';
import center_box from '@/components/center_box.vue';
import right_box from '@/components/right_box.vue';
import { ref } from 'vue'

import { onMounted, onBeforeUnmount } from 'vue';

function toggleFullScreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}

onMounted(() => {
  // 页面加载完成后自动全屏
  toggleFullScreen();
});

onBeforeUnmount(() => {
  // 组件销毁前退出全屏
  if (document.fullscreenElement) {
    document.exitFullscreen();
  }
});

</script> -->

<template>
  <dv-full-screen-container class="home gradient-background">
    <Head></Head>
    <div class="main">
      <div class="left">
        <left_box></left_box>
      </div>
      <div class="center">
        <center_box></center_box>
      </div>
      <div class="right">
        <right_box></right_box>
      </div>
    </div>
  </dv-full-screen-container>
</template>

<script setup lang="js">
import Head from '@/components/head.vue';
import left_box from '@/components/left_box.vue';
import center_box from '@/components/center_box.vue';
import right_box from '@/components/right_box.vue';




import { onMounted } from 'vue';
import { ref } from 'vue'; // 确保只导入一次

function triggerFullScreen() {
  // 定义一个变量来跟踪 F11 是否被触发
  let f11Pressed = false;

  // 监听键盘事件来检测 F11 是否被按下
  const keyDownListener = (event) => {
    if (event.key === 'F11') {
      f11Pressed = true;
      console.log('已按下 F11');
    }
  };

  // 监听键盘事件
  document.addEventListener('keydown', keyDownListener);

  // 创建键盘事件
  const event = new KeyboardEvent('keydown', {
    bubbles: true, cancelable: true, keyCode: 121
  });

  // 触发事件
  document.dispatchEvent(event);

  // 移除键盘事件监听器
  document.removeEventListener('keydown', keyDownListener);

  // 返回 F11 是否被触发的状态
  return f11Pressed;
}

onMounted(() => {
  // 页面加载完成后自动全屏
  const isF11Pressed = triggerFullScreen();
  if (!isF11Pressed) {
    console.log('未按下 F11');
  }
});
</script>

<style scoped lang="scss">
.home {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: rgb(0, 0, 0, 0);
}

.gradient-background {
  background: radial-gradient(
    circle,
    #33609a,
    #356098 10%,
    #052049 20%,
    #052049 100%
  );
  background-size: 200% 200%;
  background-position: center;
  transition: background 0.5s ease;
}

.main {
  display: flex;
  background-color: rgb(0, 0, 0, 0);
  width: 100%;
  height: calc(100% - 75px);
  background-color: rgb(0, 0, 0, 0);

  .left {
    display: flex;
    flex-direction: column;
    width: 16%;
    height: 100%;
    background-color: rgb(0, 0, 0, 0);
  }

  .center {
    display: flex;
    flex-direction: column;
    width: 60%;
    height: 100%;
    background-color: transparent;
  }

  .right {
    display: flex;
    flex-direction: column;
    width: 24%;
    height: 100%;
    background-color: rgb(0, 0, 0, 0);
  }
}
</style>
