<script setup lang="js">
import Head from '@/components/head.vue';
import left_box from '@/components/left_box.vue';
import center_box from '@/components/center_box.vue';
import right_box from '@/components/right_box.vue';

</script>

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

<style scoped lang="scss">
.home {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background-color: rgb(0, 0, 0, 0);
}

.gradient-background {
    background: radial-gradient(circle, #33609a, #356098 10%, #052049 20%, #052049 100%);
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
        width: 23%;
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
        width: 17%;
        height: 100%;
        background-color: rgb(0, 0, 0, 0);
    }

}
</style>