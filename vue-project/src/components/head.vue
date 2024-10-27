<script setup></script>

<template>
    <div class="module-box">
        <div style="flex:0 1 30%">
            <div small-bg>
                <dv-decoration-10 style="width:100%;height:5px;" />
                <dv-decoration3 style="width:100%;height:30px;"/>
                <dv-decoration2 :dur="2" style="width:100%;height:5px;" />
            </div>
        </div>
        <div style="flex: 0 1 40%">
            <div class="d-flex">
                <dv-decoration8 style="width:300px;height:50px;flex: 1;" />
                <div class="index-title">XXX草原生态检测系统</div>
                <dv-decoration8 :reverse="true" style="width:300px;height:50px;flex: 1;" />
            </div>
        </div>
        <div style="flex:0 1 30%">
            <div small-bg>
                <dv-decoration-10 style="width:100%;height:5px;" />
                <dv-decoration3 style="width:100%;height:30px;"/>
                <dv-decoration2 :dur="2" style="width:100%;height:5px;" />
            </div>
        </div>
    </div>
    <div class="low">
        <div small-bg>
            <dv-decoration5 :dur="2" style="width:300px;height:40px;" />
        </div>
    </div>
</template>

<style scoped lang="scss">
/* 布局结构分配 */
.module-box {
    display: flex;
    margin: 10px;
}

.d-flex {
    display: flex;
    align-items: center;
}

.index-title {
    font-size: 20px;
    white-space: nowrap;
    flex: 1;
    text-align: center;
    color: aliceblue;
}

.low {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 5px;
}
</style>