<script lang="ts" setup>
import { onMounted, ref, onBeforeUnmount, watch } from 'vue';
import * as echarts from 'echarts';
import type { ECharts, EChartsOption } from 'echarts';
import { useLocalCity } from "@/stores/useLocalCity"

const store = useLocalCity()

const time_data = ref<String[]>([])
const hid_tmp = ref([])
const dow_tmp = ref([])

const chartDom = ref<HTMLElement | null>(null);
let myChart: ECharts | null = null;
const option = ref<EChartsOption>()

onMounted(() => {
    watch(
        () => store.cityData.weather,
        (newData) => {
            if (newData && newData.forecasts) {
                for (const i of newData.forecasts) {
                    time_data.value.push(i.date.slice(-5) as String);
                    hid_tmp.value.push(i.dayTemp as never);
                    dow_tmp.value.push(i.nightTemp as never);
                }
                option.value = {
                    textStyle: {
                        color: '#fff' // 设置默认文本颜色为白色
                    },
                    title: {
                        text: '',
                        textStyle: { // 可以在这里覆盖默认的文本样式
                            color: '#fff' // 如果标题也需要白色，可以这样设置
                        }
                    },
                    tooltip: {
                        trigger: 'axis',
                        textStyle: { // 覆盖默认的文本样式
                            color: '#fff' // 提示框文本颜色设置为白色
                        }
                    },
                    legend: {
                        textStyle: { // 覆盖默认的文本样式
                            color: '#fff' // 图例文本颜色设置为白色
                        }
                    },
                    grid: {
                        top: '20%',
                        right: '17%',
                        bottom: '13%',
                        left: '20%',
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: true,
                        data: time_data.value,
                        axisLabel: {

                        }
                    },
                    yAxis: {
                        type: 'value',
                        axisLabel: {
                            formatter: '{value} °C',
                        }
                    },
                    series: [
                        {
                            name: '最高温度',
                            type: 'line',
                            data: hid_tmp.value,
                            markPoint: {
                                symbolSize: 30,
                                data: [{ type: 'max', name: 'Max' }]
                            },
                            markLine: {
                                data: [{ type: 'average', name: 'Avg' }]
                            }
                        },
                        {
                            name: '最低温度',
                            type: 'line',
                            data: dow_tmp.value,
                            markPoint: {
                                symbolSize: 30,
                                data: [{ name: '最低', value: -2, xAxis: 1, yAxis: -1.5 }]
                            },
                            markLine: {
                                data: [{ type: 'average', name: 'Avg' }]
                            }
                        }
                    ]
                };
                if (chartDom.value) {
                    myChart = echarts.init(chartDom.value);
                    myChart.setOption(option.value);
                }
            }
        },
        { immediate: true }
    );




});

onBeforeUnmount(() => {
    if (myChart !== null) {
        myChart.dispose();
    }
});
</script>

<template>
    <div ref="chartDom" style="width: 100%; top: 5px;height: 30%;margin: 0;display: flex;color: aliceblue;"></div>
</template>

<style scoped></style>