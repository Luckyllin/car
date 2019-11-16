<template>
  <div id="comunication">
    <button @click="doGet">GET请求</button>
    <br>
    <span class="resData">get请求到的数据：{{resData}}</span>
    <button @click="doPost">POST请求</button>
    <br>
    <span class="postData">post请求到的数据：{{postData}}</span>
    <form action="" enctype="application/x-www-form-urlencoded"></form>
  </div>
</template>
<script>
  // 需要使用Vue，所以需要引入
  import Vue from 'vue'
  export default {
    data (){
      return {
          resData:[],
        postData:[]
      }
    },
    // vue高版本中，推荐使用axios进行网络请求，而不再使用vue-resource
    methods: {
      doGet(){
        // 发起get请求
        Vue.axios.get('/api', {
          // get传递的query参数（传递的参数应与后台人员协商，本次模拟不做限制，不做判断）
          params: {
            //name: '',
            //age: 
          }
        }).then((response) => {
          // then 指成功之后的回调 (注意：使用箭头函数，可以不考虑this指向)
          console.log(response);
          console.log(response.data);
          this.resData = response.data;
        }).catch((error) => {
          // catch 指请求出错的处理
          console.log(error);
        });
      },
      doPost(){
        // 提示：该方式传递的参数是json格式，如上传不成功，需检查后台接收的方式是不是application/x-www-form-urlencoded默认格式，jquery中ajax请求的就是application/x-www-form-urlencoded，后台需要body-parser解码
        Vue.axios.post('/api/login', {
          // 此参数就是写到请求体中的参数
          //user: '',
          //pwd: ''
        }).then((response) => {
          console.log(response);
          console.log(response.data);
          this.postData = response.data;
        }).catch((error) => {
          console.log(error);
        });
      }
    }
  }
</script>
<style scoped>
  #comunication {
    border: 1px solid gold;
    padding: 10px;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
  }
 
  button {
    background-color: #008CBA;
    padding: 10px 20px;
    border: none;
    font-size: 18px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    display: block;
  }
 
  button:hover {
    background-color: #008CDA;
    color: #ffffff;
  }
 
  a {
    background: rgba(255, 255, 0, 0.5);
    padding: 5px 20px;
    width: 350px;
    border-radius: 8px;
    text-decoration: none;
  }
  .resData,.postData{
    font-size: 20px;
    background: greenyellow;padding: 5px 10px 5px 20px;
    border-radius:18px;
    display: block;
    margin-bottom: 20px;
    margin-top: 10px;
    width: 900px;
  }
</style>
