<script setup lang="js">
import { onUnmounted, onMounted, ref, defineProps, defineEmits, watch } from 'vue';
import * as Ayame from '@open-ayame/ayame-web-sdk/dist/ayame.min.js';

const options = Ayame.defaultOptions;

let videoCodec;
let conn;
const remoteVideoElement = ref(null);

const props = defineProps({
  dataChannelName: String,
  signalingUrl: String,
  roomId: String,
  clientId: String,
  channelid: String,
  isConnect: {
    type: Boolean,
    default: true
  },
  height: {
    type: Number,
    default: 80
  }
});

options.clientId = props.clientId ? props.clientId : options.clientId;
options.video.direction = 'recvonly';
options.audio.direction = 'recvonly';

const disconnect = () => {
  if (conn) {
    conn.disconnect();
  }
}

const startConnVideo = async () => {
  try {
    // 视频连接设置
    options.video.codec = videoCodec;
    conn = Ayame.connection(props.signalingUrl, props.roomId, options, true);
    await conn.connect(null);

    // 视频连接事件处理
    conn.on("open", ({ authzMetadata }) => {
      console.log("视频连接打开");
    });
    conn.on("disconnect", async (e) => {
      console.log(e);
      if (remoteVideoElement.value) {
        remoteVideoElement.value.srcObject = null;
      }
      if (props.isConnect) {
        await conn.connect(null);
      }
    });
    conn.on("addstream", (e) => {
      remoteVideoElement.value.srcObject = e.stream;
    });
  } catch (error) {
    console.error("连接失败:", error);
  }
};



onMounted(async () => {
  startConnVideo();
});

// 监控isConnect属性的变化
watch(() => props.isConnect, (newVal, oldVal) => {
  if (newVal === false && oldVal === true) {
    disconnect();
  };
  if (newVal === true) {
    console.log("打开连接");
    startConnVideo();
  }
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