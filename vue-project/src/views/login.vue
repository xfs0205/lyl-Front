<template>
  <div>
    <div class="login-container">
      <div
        class="login-panel"
        style="
          background-color: rgb(255, 255, 255, 0.1);
          border-radius: 10px;
          width: 20vw;
          border: 2px solid grey;
        "
      >
        <h2 style="text-align: center; padding: 10px; color: white">
          用户登录
        </h2>
        <div style="padding: 10px">
          <span style="color: white; padding: 2px">用户账号</span>
          <input
            v-model="user.username"
            type="text"
            placeholder="请输入账号"
            style="
              font-size: 15px;
              height: 40px;
              border: 0.5px solid grey;
              margin-top: 3px;
            "
          />
        </div>
        <div style="padding-left: 10px; padding-right: 10px">
          <span style="color: white">用户密码</span>
          <input
            v-model="user.password"
            type="password"
            placeholder="请输入密码"
            style="
              font-size: 15px;
              height: 40px;
              border: 0.5px solid grey;
              margin-top: 3px;
            "
          />
        </div>
        <div style="padding-left: 10px; padding-right: 10px">
          <el-button
            @click="sendPostRequest"
            size="large"
            type="primary"
            style="width: 100%; margin-top: 10px"
          >
            立即登录
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import axios from "axios";
import { ElMessage } from "element-plus";
import { useRouter } from 'vue-router';

const user = ref({
  username: "",
  password: "",
});
const router = useRouter();
// 发送 POST 请求的函数
const sendPostRequest = async () => {

  await axios
    .post("/fsxback/login", {
      name: user.value.username,
      password: user.value.password,
    },{
        withCredentials: true 
    })
    .then((re) => {  
      if (re.data == "success") {
        router.push({ name: 'home' });
      }
    })
    .catch((e) => {
      console.log(e);
      ElMessage.error("账号或密码错误");
      //输入错误
    });
};
</script>
<style scoped lang="scss">
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url("../assets/背景.png");
  background-size: cover;

  .login-panel {
    width: 300px;
    height: 300px;

    .login-btn {
      margin-top: 20px;
      display: inline-block;
      background-color: #7f72d1;
      color: #fff;
      width: 100%;
      line-height: 20px;
      border-radius: 5px;
      text-align: center;
    }

    .to-register {
      text-decoration: underline;
      cursor: pointer;
    }

    .to-register:hover {
      color: #7f72d1;
    }

    input {
      outline: none;
      line-height: 50px;
      padding: 0 10px;
      font-size: 16px;
      border-radius: 5px;
      box-sizing: border-box;
      margin-bottom: 10px;
      width: 100%;
      border: none;
      border: 2px solid #f1f1f1;
      background-color: #f1f1f1;
      transition: all 1s;
    }

    input:focus {
      border: 2px solid #7f72d1;
    }
  }
}
</style>
