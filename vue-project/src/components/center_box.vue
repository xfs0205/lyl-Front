<script setup lang="js">
import { ref, onMounted } from 'vue'
import utils from '@/components/videos/video.js'
import Video from '@/components/videos/video.vue'
import MapContainer from '@/components/groups/MapContainer.vue';
import Table from '@/components/Lists/table.vue'
import group1 from '@/components/groups/group1.vue';
import shangqingJson from '@/assets/shangqing.json';
import * as Ayame from '@open-ayame/ayame-web-sdk/dist/ayame.min.js';
import screenfull from "screenfull";
import { Right, TopLeft, Top, TopRight, BottomRight, Bottom, BottomLeft, Back } from '@element-plus/icons-vue';

const options = Ayame.defaultOptions;
const data = ref(shangqingJson)

const conn4dc = ref();
const datachannel = ref()
const speed = ref(24)
const isConnect1 = ref(true)
const isConnect2 = ref(true)
const isFullscreen = ref(false)

const video1 = ref(null)
const video2 = ref(null)

options.clientId = utils.clientId ? utils.clientId : options.clientId;
options.video.direction = 'recvonly';
options.audio.direction = 'recvonly';

screenfull.on('change', () => {
  // 更新你的应用状态
  isFullscreen.value = screenfull.isFullscreen;
});

const startDataChannel = async () => {
  try {
    console.log("开始创建数据通道1");

    conn4dc.value = Ayame.connection(utils.signalingUrl, utils.channelid, options, true)

    conn4dc.value.on('open', async (e) => {
      datachannel.value = await conn4dc.value.createDataChannel('videoChannel');
      console.log("数据通道创建完成", datachannel.value);
    });
    conn4dc.value.on('datachannel', (channel) => {
      if (!datachannel.value) {
        datachannel.value = channel;
      }
    });
    conn4dc.value.on('disconnect', async (e) => {
      console.log(e);
      datachannel.value = null;
      await conn4dc.value.connect(null);
    });
    await conn4dc.value.connect(null);
  } catch (error) {
    console.error("数据通道连接失败:", error);
  }
};

onMounted(async () => {
  await startDataChannel();
});

// 向上
const toUp = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0d, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x01,       // command (2 bytes)
      0x00,             // xx
      speedf,             // yy (速度为8，这里是8的十六进制表示)
      0xff              // end
    ]);

  }
  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0e, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x01,       // command (2 bytes)
      0x00,             // xx
      speedf,             // yy (速度为8)
      0xff              // end
    ]);
  }
  else
    return

  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 向右
const toRight = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0d, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x04,       // command (2 bytes)
      speedf,             // xx
      0x00,             // yy (速度为8)
      0xff              // end
    ]);
  }
  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0e, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x04,       // command (2 bytes)
      speedf,             // xx
      0x00,             // yy (速度为8)
      0xff              // end
    ])
  }

  else
    return

  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 向下
const toDown = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0d, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x02,       // command (2 bytes)
      0x00,             // xx
      speedf,             // yy (速度为8)
      0xff              // end
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0e, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x02,       // command (2 bytes)
      0x00,             // xx
      speedf,             // yy (速度为8)
      0xff
    ])
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 向左
const toLeft = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0d, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x03,       // command (2 bytes)
      speedf,             // xx
      0x00,             // yy (速度为8)
      0xff              // end 
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,             // head
      0x0e, 0x00, 0xa8, 0xc0, // ip (4 bytes)
      0x00, 0x50,       // port (2 bytes)
      0x00, 0x03,       // command (2 bytes)
      speedf,             // xx
      0x00,             // yy (速度为8)
      0xff              // end
    ]);
  }

  else
    return



  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 停止
const toStop = (index) => {
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x00,
      0x00,
      0x00,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x00,
      0x00,
      0x00,
      0xff
    ]);
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 左上
const toLeftUp = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x05,
      speedf,
      speedf,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x05,
      speedf,
      speedf,
      0xff
    ]);
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 右上
const toRightUp = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x06,
      speedf,
      speedf,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x06,
      speedf,
      speedf,
      0xff
    ]);
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 右下
const toRightDown = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x08,
      speedf,
      speedf,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x08,
      speedf,
      speedf,
      0xff
    ]);
  }
  else
    return

  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 左下
const toLeftDown = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x07,
      speedf,
      speedf,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x07,
      speedf,
      speedf,
      0xff
    ]);
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 放大
const toZoomIn = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0a,
      speedf,
      0x00,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0a,
      speedf,
      0x00,
      0xff
    ]);
  }

  else
    return

  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 缩小
const toZoomOut = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0b,
      speedf,
      0x00,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0b,
      speedf,
      0x00,
      0xff
    ]);
  }

  else
    return

  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 停止
const toZoomStop = (index) => {
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x09,
      0x00,
      0x00,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x09,
      0x00,
      0x00,
      0xff
    ]);
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 调焦缩小
const toFocusIn = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0f,
      speedf,
      0x00,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0f,
      speedf,
      0x00,
      0xff
    ]);
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 调焦放大
const toFocusOut = (index) => {
  let speedf = speed.value.toString(16)
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x10,
      speedf,
      0x00,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x10,
      speedf,
      0x00,
      0xff
    ]);
  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}
// 停止调焦
const toFocusStop = (index) => {
  let onvif_cmd
  if (index === 1) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0d, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0e,
      0x00,
      0x00,
      0xff
    ]);
  }

  else if (index === 2) {
    onvif_cmd = new Uint8Array([
      0x90,
      0x0e, 0x00, 0xa8, 0xc0,
      0x00, 0x50,
      0x00, 0x0e,
      0x00,
      0x00,
      0xff
    ]);

  }

  else
    return


  if (datachannel.value && datachannel.value.readyState === 'open') {
    datachannel.value.send(onvif_cmd);  // 直接发送字节数组
    console.log("发送信息：", onvif_cmd);
  } else {
    console.log("数据通道没有打开");
  }
}

const clickIsConnect = (index) => {
  if (index === 1)
    isConnect1.value = !isConnect1.value
  else if (index === 2)
    isConnect2.value = !isConnect2.value
  else
    return
}

const toggleFullScreen1 = () => {
  if (screenfull.isEnabled) {
    screenfull.toggle(video1.value);
  }
  if (screenfull.isFullscreen) {
    screenfull.exit();
  }
}
const toggleFullScreen2 = () => {
  if (screenfull.isEnabled) {
    screenfull.toggle(video2.value);
  }
  if (screenfull.isFullscreen) {
    screenfull.exit();
  }
}

</script>

<template>
  <div class="top">
    <dv-border-box12 style="margin-top: 10px">
      <div class="top_left">
        <div class="top_left_title">
          <strong style="
              margin-right: 20%;
              color: orange;
              font-style: italic;
              text-shadow: 2px 2px 4px #000000;
              font-size: 17px;
            ">实时监控</strong>
        </div>
        <div ref="video1" style="
            height: 77%;
            width: 100%;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
          ">
          <div v-if="!isFullscreen" style="
              display: flex;
              align-items: center;
              position: absolute;
              right: 40px;
              top: 3px;
              z-index: 1000;
            ">
            <el-popover ref="popover" placement="right" title="控制面板" :width="170" trigger="focus">
              <template #reference>
                <el-button class="m-2" style="background-color: rgb(255,255,255,0.3);color: white;">调整</el-button>
              </template>

              <div style="height: 270px;width: 100%;background-color: rgb(0,0,0,0.3);position: relative;">
                <el-button @mousedown="toLeftUp(1)" @mouseup="toStop(1)" :icon="TopLeft"
                  style="position: absolute;top: 2px;left:10px" circle />
                <el-button @mousedown="toUp(1)" @mouseup="toStop(1)" :icon="Top"
                  style="position: absolute;top: 2px;left:44px" circle />
                <el-button @mousedown="toRightUp(1)" @mouseup="toStop(1)" :icon="TopRight"
                  style="position: absolute;top: 2px;right:10px" circle />
                <el-button @mousedown="toRight(1)" @mouseup="toStop(1)" :icon="Right"
                  style="position: absolute;top: 50px;right:10px" circle />
                <el-button @mousedown="toRightDown(1)" @mouseup="toStop(1)" :icon="BottomRight"
                  style="position: absolute;top: 100px;right:10px" circle />
                <el-button @mousedown="toDown(1)" @mouseup="toStop(1)" :icon="Bottom"
                  style="position: absolute;top: 100px;left:44px" circle />
                <el-button @mousedown="toLeftDown(1)" @mouseup="toStop(1)" :icon="BottomLeft"
                  style="position: absolute;top: 100px;left:0" circle />
                <el-button @mousedown="toLeft(1)" @mouseup="toStop(1)" :icon="Back"
                  style="position: absolute;top: 50px;left:0" circle />
                <el-button @mousedown="toZoomIn(1)" @mouseup="toZoomStop(1)"
                  style="position: absolute;top: 150px;left: 0px;">放大</el-button>
                <el-button @mousedown="toZoomOut(1)" @mouseup="toZoomStop(1)"
                  style="position: absolute;top: 150px;left: 60px;">缩小</el-button>
                <el-button @mousedown="toFocusIn(1)" @mouseup="toFocusStop(1)"
                  style="position: absolute;top: 190px;left: 0px;">缩聚</el-button>
                <el-button @mousedown="toFocusOut(1)" @mouseup="toFocusStop(1)"
                  style="position: absolute;top: 190px;left: 60px;">放聚</el-button>
                <el-button v-show="isConnect1" @click="clickIsConnect(1)"
                  style="position: absolute;top: 50px;left: 32px;">关闭</el-button>
                <el-button v-show="!isConnect1" @click="clickIsConnect(1)"
                  style="position: absolute;top: 50px;left: 32px;">打开</el-button>
                <el-button @click="toggleFullScreen1" style="position: absolute;bottom: 10px;left: 1px;">
                  {{ isFullscreen ? '关闭宽屏模式' : '打开宽屏模式' }}
                </el-button>

              </div>
            </el-popover>
          </div>
          <div v-if="isFullscreen" style="
              display: flex;
              align-items: center;
              position: absolute;
              right: 40px;
              top: 20px;
              z-index: 1000;
              width: 145px;
              background-color: transparent;
            ">
            <div style="height: 270px;width: 100%;background-color: rgb(0,0,0,0);position: relative;">
              <el-button @mousedown="toLeftUp(1)" @mouseup="toStop(1)" :icon="TopLeft"
                style="position: absolute;top: 2px;left:10px" circle />
              <el-button @mousedown="toUp(1)" @mouseup="toStop(1)" :icon="Top"
                style="position: absolute;top: 2px;left:44px" circle />
              <el-button @mousedown="toRightUp(1)" @mouseup="toStop(1)" :icon="TopRight"
                style="position: absolute;top: 2px;right:10px" circle />
              <el-button @mousedown="toRight(1)" @mouseup="toStop(1)" :icon="Right"
                style="position: absolute;top: 50px;right:10px" circle />
              <el-button @mousedown="toRightDown(1)" @mouseup="toStop(1)" :icon="BottomRight"
                style="position: absolute;top: 100px;right:10px" circle />
              <el-button @mousedown="toDown(1)" @mouseup="toStop(1)" :icon="Bottom"
                style="position: absolute;top: 100px;left:44px" circle />
              <el-button @mousedown="toLeftDown(1)" @mouseup="toStop(1)" :icon="BottomLeft"
                style="position: absolute;top: 100px;left:0" circle />
              <el-button @mousedown="toLeft(1)" @mouseup="toStop(1)" :icon="Back"
                style="position: absolute;top: 50px;left:0" circle />
              <el-button @mousedown="toZoomIn(1)" @mouseup="toZoomStop(1)"
                style="position: absolute;top: 150px;left: 0px;">放大</el-button>
              <el-button @mousedown="toZoomOut(1)" @mouseup="toZoomStop(1)"
                style="position: absolute;top: 150px;left: 60px;">缩小</el-button>
              <el-button @mousedown="toFocusIn(1)" @mouseup="toFocusStop(1)"
                style="position: absolute;top: 190px;left: 0px;">缩聚</el-button>
              <el-button @mousedown="toFocusOut(1)" @mouseup="toFocusStop(1)"
                style="position: absolute;top: 190px;left: 60px;">放聚</el-button>
              <el-button v-show="isConnect1" @click="clickIsConnect(1)"
                style="position: absolute;top: 50px;left: 32px;">关闭</el-button>
              <el-button v-show="!isConnect1" @click="clickIsConnect(1)"
                style="position: absolute;top: 50px;left: 32px;">打开</el-button>
              <el-button @click="toggleFullScreen1" style="position: absolute;bottom: 10px;left: 1px;">
                {{ isFullscreen ? '关闭宽屏模式' : '打开宽屏模式' }}
              </el-button>

            </div>
          </div>
          <Video :dataChannelName="'video1'" :isConnect="isConnect1" :channelid="utils.channelid"
            :signalingUrl="utils.signalingUrl" :roomId="utils.roomId1" :clientId="utils.clientId" :height="100" />
        </div>
      </div>
      <div class="top_right">
        <div class="top_right_title">
          <strong style="
              margin-left: 20%;
              color: orange;
              font-style: italic;
              text-shadow: 2px 2px 4px #000000;
              font-size: 17px;
            ">生态量监测</strong>
        </div>
        <div style="height: 77%; width: 100%">
          <Table :data="data" :height="30" :front_size="10" />
        </div>
      </div>
      <div class="bottom_left">
        <div class="bottom_left_title">
          <strong style="
              margin-right: 20%;
              color: orange;
              font-style: italic;
              text-shadow: 2px 2px 4px #000000;
              font-size: 17px;
            ">生物量监测</strong>
        </div>
        <div ref="video2" style="height: 77%; width: 100%; padding: 0; display: flex; position: relative;            justify-content: center;
            align-items: center;">
          <Video :dataChannelName="'video2'" :isConnect="isConnect2" :channelid="utils.channelid"
            :signalingUrl="utils.signalingUrl" :roomId="utils.roomId2" :clientId="utils.clientId" :height="100" />

          <div v-if="!isFullscreen" style="
              display: flex;
              align-items: center;
              position: absolute;
              right: 40px;
              top: 3px;
              z-index: 1001;
            ">
            <el-popover ref="popover" placement="right" title="控制面板" :width="170" trigger="focus">
              <template #reference>
                <el-button class="m-2" style="background-color: rgb(255,255,255,0.3);color: white;">调整</el-button>
              </template>

              <div style="height: 270px;width: 100%;background-color: rgb(0,0,0,0.3);position: relative;">
                <el-button @mousedown="toLeftUp(2)" @mouseup="toStop(2)" :icon="TopLeft"
                  style="position: absolute;top: 2px;left:10px" circle />
                <el-button @mousedown="toUp(2)" @mouseup="toStop(2)" :icon="Top"
                  style="position: absolute;top: 2px;left:44px" circle />
                <el-button @mousedown="toRightUp(2)" @mouseup="toStop(2)" :icon="TopRight"
                  style="position: absolute;top: 2px;right:10px" circle />
                <el-button @mousedown="toRight(2)" @mouseup="toStop(2)" :icon="Right"
                  style="position: absolute;top: 50px;right:10px" circle />
                <el-button @mousedown="toRightDown(2)" @mouseup="toStop(2)" :icon="BottomRight"
                  style="position: absolute;top: 100px;right:10px" circle />
                <el-button @mousedown="toDown(2)" @mouseup="toStop(2)" :icon="Bottom"
                  style="position: absolute;top: 100px;left:44px" circle />
                <el-button @mousedown="toLeftDown(2)" @mouseup="toStop(2)" :icon="BottomLeft"
                  style="position: absolute;top: 100px;left:0" circle />
                <el-button @mousedown="toLeft(2)" @mouseup="toStop(2)" :icon="Back"
                  style="position: absolute;top: 50px;left:0" circle />
                <el-button @mousedown="toZoomIn(2)" @mouseup="toZoomStop(2)"
                  style="position: absolute;top: 150px;left: 0px;">放大</el-button>
                <el-button @mousedown="toZoomOut(2)" @mouseup="toZoomStop(2)"
                  style="position: absolute;top: 150px;left: 60px;">缩小</el-button>
                <el-button @mousedown="toFocusIn(2)" @mouseup="toFocusStop(2)"
                  style="position: absolute;top: 190px;left: 0px;">缩聚</el-button>
                <el-button @mousedown="toFocusOut(2)" @mouseup="toFocusStop(2)"
                  style="position: absolute;top: 190px;left: 60px;">放聚</el-button>
                <el-button v-show="isConnect2" @click="clickIsConnect(2)"
                  style="position: absolute;top: 50px;left: 32px;">关闭</el-button>
                <el-button v-show="!isConnect2" @click="clickIsConnect(2)"
                  style="position: absolute;top: 50px;left: 32px;">打开</el-button>
                <el-button @click="toggleFullScreen2" style="position: absolute;bottom: 10px;left: 1px;">
                  {{ isFullscreen ? '关闭宽屏模式' : '打开宽屏模式' }}
                </el-button>
              </div>
            </el-popover>
          </div>
          <div v-if="isFullscreen" style="
              display: flex;
              align-items: center;
              position: absolute;
              right: 40px;
              top: 20px;
              z-index: 1000;
              width: 145px;
              background-color: transparent;
            ">
            <div style="height: 270px;width: 100%;background-color: rgb(0,0,0,0);position: relative;">
              <el-button @mousedown="toLeftUp(2)" @mouseup="toStop(2)" :icon="TopLeft"
                style="position: absolute;top: 2px;left:10px" circle />
              <el-button @mousedown="toUp(2)" @mouseup="toStop(2)" :icon="Top"
                style="position: absolute;top: 2px;left:44px" circle />
              <el-button @mousedown="toRightUp(2)" @mouseup="toStop(2)" :icon="TopRight"
                style="position: absolute;top: 2px;right:10px" circle />
              <el-button @mousedown="toRight(2)" @mouseup="toStop(2)" :icon="Right"
                style="position: absolute;top: 50px;right:10px" circle />
              <el-button @mousedown="toRightDown(2)" @mouseup="toStop(2)" :icon="BottomRight"
                style="position: absolute;top: 100px;right:10px" circle />
              <el-button @mousedown="toDown(2)" @mouseup="toStop(2)" :icon="Bottom"
                style="position: absolute;top: 100px;left:44px" circle />
              <el-button @mousedown="toLeftDown(2)" @mouseup="toStop(2)" :icon="BottomLeft"
                style="position: absolute;top: 100px;left:0" circle />
              <el-button @mousedown="toLeft(2)" @mouseup="toStop(2)" :icon="Back"
                style="position: absolute;top: 50px;left:0" circle />
              <el-button @mousedown="toZoomIn(2)" @mouseup="toZoomStop(2)"
                style="position: absolute;top: 150px;left: 0px;">放大</el-button>
              <el-button @mousedown="toZoomOut(2)" @mouseup="toZoomStop(2)"
                style="position: absolute;top: 150px;left: 60px;">缩小</el-button>
              <el-button @mousedown="toFocusIn(2)" @mouseup="toFocusStop(2)"
                style="position: absolute;top: 190px;left: 0px;">缩聚</el-button>
              <el-button @mousedown="toFocusOut(2)" @mouseup="toFocusStop(2)"
                style="position: absolute;top: 190px;left: 60px;">放聚</el-button>
              <el-button v-show="isConnect2" @click="clickIsConnect(2)"
                style="position: absolute;top: 50px;left: 32px;">关闭</el-button>
              <el-button v-show="!isConnect2" @click="clickIsConnect(2)"
                style="position: absolute;top: 50px;left: 32px;">打开</el-button>
              <el-button @click="toggleFullScreen2" style="position: absolute;bottom: 10px;left: 1px;">
                {{ isFullscreen ? '关闭宽屏模式' : '打开宽屏模式' }}
              </el-button>
            </div>
          </div>
        </div>
      </div>
      <div class="bottom_right">
        <div class="bottom_right_title">
          <strong style="
              margin-left: 20%;
              color: orange;
              font-style: italic;
              text-shadow: 2px 2px 4px #000000;
              font-size: 17px;
            ">实时地理位置</strong>
        </div>
        <div style="height: 77%; width: 100%">
          <MapContainer></MapContainer>
        </div>
      </div>
    </dv-border-box12>
  </div>
  <div class="bottom">
    <dv-border-box10 style="display: flex; flex-direction: row">
      <div class="top-title">
        <strong style="
            color: orange;
            font-style: italic;
            text-shadow: 2px 2px 4px #000000;
            font-size: 17px;
          ">植株生长量数据</strong>
      </div>
      <div class="bottom-center">
        <group1></group1>
      </div>
    </dv-border-box10>
  </div>
</template>

<style scoped lang="css">
#overlay::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  /* 半透明背景 */
  pointer-events: auto;
  /* 允许点击事件 */
}


.top {
  display: flex;
  position: relative;
  flex-direction: column;
  width: 100%;
  height: 70%;

  .top_left {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgb(0, 0, 0, 0);
    top: 0;
    left: 0;
    width: 50%;
    height: 50%;
    padding: 22px 30px 0px 30px;

    .top_left_title {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      background-image: url("@/assets/title2.png");
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      height: 23%;
      width: 100%;
    }
  }

  .top_right {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-color: rgb(0, 0, 0, 0);
    top: 0;
    right: 0;
    width: 50%;
    height: 50%;
    padding: 22px 30px 0px 30px;

    .top_right_title {
      display: flex;
      align-items: center;
      /* justify-content: flex-end;  */
      background-image: url("@/assets/title1.png");
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      height: 23%;
      width: 100%;
    }
  }

  .bottom_left {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgb(0, 0, 0, 0);
    bottom: 0;
    left: 0;
    width: 50%;
    height: 50%;
    padding: 0px 30px 22px 30px;

    .bottom_left_title {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      background-image: url("@/assets/title2.png");
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      height: 23%;
      width: 100%;
    }
  }

  .bottom_right {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgb(0, 0, 0, 0);
    bottom: 0;
    right: 0;
    width: 50%;
    height: 50%;
    padding: 0px 30px 22px 30px;

    .bottom_right_title {
      display: flex;
      align-items: center;
      /* justify-content: flex-end;  */
      background-image: url("@/assets/title1.png");
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      height: 23%;
      width: 100%;
    }
  }
}

.bottom {
  display: flex;
  position: relative;
  width: 100%;
  height: 30%;
  padding: 5px;
  background-color: rgb(0, 0, 0, 0);

  .top-title {
    display: flex;
    align-items: center;
    justify-content: center;
    background-image: url("@/assets/title3.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    height: 20%;
    width: 100%;
  }

  .bottom-center {
    display: flex;
    height: 80%;
  }
}
</style>
