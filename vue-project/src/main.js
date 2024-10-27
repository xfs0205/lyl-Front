import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import DataVVue3 from '@kjgl77/datav-vue3'
import ElementPlus from 'element-plus'
import VueAMap, {initAMapApiLoader} from '@vuemap/vue-amap';
import VueAMapLoca from '@vuemap/vue-amap-loca';

import '@vuemap/vue-amap/dist/style.css'
import 'element-plus/dist/index.css'
import '@/assets/main.css'

const app = createApp(App)

initAMapApiLoader({
    key: '	042300a5572900783dbffb75f2207852',
    securityJsCode: 'acc97adc8e6b28babc347a0a4754cc41', 
    Loca:{
     version: '2.0.0'
    } 
  })

app.use(createPinia())
app.use(router)
app.use(DataVVue3)
app.use(ElementPlus)
app.use(VueAMap)
app.use(VueAMapLoca)

app.mount('#app')
