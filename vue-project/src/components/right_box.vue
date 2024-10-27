<script setup lang="js">
import wenList from '@/components/wenList.vue'

</script>

<template>
    <div class="top">


    </div>
    <div class="bottom">
        
        <dv-border-box8  style="display: flex;height: 100%;">
            <wenList></wenList>
            <div dv-bg>
                dv-border-box7
            </div>
        </dv-border-box8>
    </div>
</template>

<style scoped lang="css">
.top {
    width: 100%;
    height: 30%;
    background-color: #fafafa;
}

.bottom {
    width: 100%;
    height: 70%;
    background-color: rgb(0, 0, 0, 0);
}
</style>