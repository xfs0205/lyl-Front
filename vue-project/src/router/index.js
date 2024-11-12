import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import loginVue from "@/views/login.vue";
import axios from "axios";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: loginVue,
    },
  ],
});

router.beforeEach(async (to, from, next) => {
  // 检查即将进入的路由是否是首页
  if (to.name === "home") {
    try {
      const response = await axios.get('/fsxback/verify', {
        headers: {
          Accept: "application/json",
        },
        withCredentials: true // 确保发送cookie
      });
      console.log(response.status);
      
      if (response.data) {
        next();
      } else {
        next({ name: "login", replace: true });
      }
    } catch (error) {
      // 如果请求失败，重定向到登录页面
      console.log("错误",error);
      next({ name: "login", replace: true });
    }
  } else {
    // 如果不是首页，直接放行
    next();
  }
});

export default router;
