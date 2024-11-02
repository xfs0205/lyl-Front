<script setup lang="js">
import { onUnmounted, onMounted, ref, defineProps, h } from 'vue';
import * as Ayame from '@open-ayame/ayame-web-sdk/dist/ayame.min.js';

const options = Ayame.defaultOptions;

let videoCodec;
let conn;
let reConnect = true;
const remoteVideoElement = ref(null);


const props = defineProps({
  signalingUrl: String,
  roomId: String,
  clientId: String,
  height: {
    type: Number,
    default: 80
  }
});

options.clientId = props.clientId ? props.clientId : options.clientId;
options.video.direction = 'recvonly';
options.audio.direction = 'recvonly';

const disconnect = () => {
  reConnect = false;
  if (conn) {
    conn.disconnect();
  }
}

const startConn = async () => {
  try {
    reConnect = true;
    options.video.codec = videoCodec;
    conn = Ayame.connection(props.signalingUrl, props.roomId, options, true);
    await conn.connect(null);
    conn.on("open", ({ authzMetadata }) => console.log("连接打开", authzMetadata));
    conn.on("disconnect", async (e) => {
      console.log(e);
      if (remoteVideoElement.value) {
        remoteVideoElement.value.srcObject = null;
      }
      if (reConnect) {
        await conn.connect(null);
      }
    });
    conn.on("addstream", (e) => {
      remoteVideoElement.value.srcObject = e.stream;
    });
  } catch (error) {
    console.error("连接失败:", error);
    // 这里可以添加更多的错误处理逻辑
  }
};

onMounted(() => {
  startConn();
});

onUnmounted(() => {
  if (conn) {
    disconnect();
  }
});
</script>

<template>
  <div class="vedio-p" :style="{ height: props.height + '%' }">
    <video id="remote-video" autoplay playsinline controls ref="remoteVideoElement"></video>
  </div>
</template>

<style scoped lang="scss">
.vedio-p {
  display: flex;
  margin-left: 10%;
}
</style>