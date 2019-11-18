<template>
  <view id="comunication">
    <button @click="doGet">GET请求</button>
    <br>
    <span class="resData">get请求到的数据：{{resData}}</span>
    <button @click="doPost">POST请求</button>
    <br>
    <span class="postData">post请求到的数据：{{postData}}</span>
	<button @click="doGet1">乘客获取司机信息</button>
	<br>
	<span class="do1Data">请求到的数据：{{do1Data}}</span>
	<button @click="doGet2">司机接快车订单</button>
	<br>
	<span class="do2Data">请求到的数据：{{do2Data}}</span>
    <form action="" enctype="application/x-www-form-urlencoded"></form>
  </view>
</template>
<script>
  export default {
    data (){
      return {
          resData:[],
        postData:[],
		do1Data:[],
		do2Data:[]
      }
    },
  
    methods: {
      doGet(){
        // 发起get请求
    uni.request({
    url: 'http://127.0.0.1:80/quikcar/release', //仅为示例，并非真实接口地址。
    data: {
        user:'12',
		pos:'324',
		adr:'sds'
    },
    header: {
        'custom-header': 'hello' //自定义请求头信息
    },
    success: (res) => {
        console.log(res.data);
        this.resData =res.data;
    }
});
      },
      doPost(){
		uni.request({
		url: 'http://127.0.0.1:80/login', //仅为示例，并非真实接口地址。
		data: {
		   user:'123',
		   pwd:'23'
		},
		header: {
		    'content-type': 'application/json' //自定义请求头信息
		},
		method:"POST",
		success: (res) => {
		    console.log(res.data);
		    this.postData =res.data ;
		}
      });
    }
	doGet1(){
		uni.request({
		    url: 'http://127.0.0.1:80/quikcar/data', //仅为示例，并非真实接口地址。
		    data: {
		        
		    },
		    header: {
		        'custom-header': 'hello' //自定义请求头信息
		    },
		    success: (res) => {
		        console.log(res.data);
		        this.do1Data =res.data;
		    }
		});
		
	}
	doGet2(){
		uni.request({
		    url: 'http://127.0.0.1:80/driver/quikcar/tkod', //仅为示例，并非真实接口地址。
		    data: {
		        oid:'',
				did:''
		    },
		    header: {
		        'custom-header': 'hello' //自定义请求头信息
		    },
		    success: (res) => {
		        console.log(res.data);
		        this.do2Data =res.data;
		    }
		});
		
	}
  },
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
