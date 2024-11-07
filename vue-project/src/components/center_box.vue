<script setup lang="js">
import { ref } from 'vue'
import utils from '@/components/videos/video.js'
import Video from '@/components/videos/video.vue'
import MapContainer from '@/components/groups/MapContainer.vue';
import Table from '@/components/Lists/table.vue'
import group1 from '@/components/groups/group1.vue';
import shangqingJson from '@/assets/shangqing.json';

const data = ref(shangqingJson)
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
            ">实时监控一</strong>
                </div>
                <div style="height: 77%; width: 100%; padding: 0; display: flex">
                    <Video :signalingUrl="utils.signalingUrl" :roomId="utils.roomId1" :clientId="utils.clientId"
                        :height="100" />
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
            ">实时监控二</strong>
                </div>
                <div style="height: 77%; width: 100%; padding: 0; display: flex">
                    <Video :signalingUrl="utils.signalingUrl" :roomId="utils.roomId2" :clientId="utils.clientId"
                        :height="100" />
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
          ">草原生物量信息</strong>
            </div>
            <div class="bottom-center">
                <group1></group1>
            </div>
        </dv-border-box10>
    </div>
</template>

<style scoped lang="css">
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
