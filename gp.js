<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title></title>
	<script src="https://code.jquery.com/jquery-latest.js"></script>
</head>
<body>
    <input type="text" placeholder="get请求" id="tel1"/>
    <button id="ajax1">确定</button>
    <p><span id="reslut1"></span></p>
	
	<input type="text" placeholder="user" id="tel2"/>
	<br>
    <input type="text" placeholder="pwd" id="tel3"/>
    <button id="ajax2">确定</button>
    <p><span id="reslut2"></span></p>	
    <script>
    $(function(){   //get请求
        $('#ajax1').on('click',function(){
            var $telValue=$('#tel1').val();
            $.ajax({
                type: 'GET',
                url: 'http://pickmi.club',				
				data:{
					user:$telValue
				},
                success: function(data){
                    var reslutData=data;
                    console.log(reslutData);    
                    $('#reslut1').text(data["msg"]);
                }             
            })
        })       
    })
    $(function(){   //post请求
        $('#ajax2').on('click',function(){
            var $telValue1=$('#tel2').val();
			var $telValue2=$('#tel3').val();
            $.ajax({
                type: 'POST',
                url: 'http://pickmi.club/login',
				data:{
					user:$telValue1,
					pwd:$telValue2
				},
                success: function(data){
                    var reslutData=data;										
                    console.log(reslutData);
					data=JSON.parse(data);
                    $('#reslut2').text(data["msg"]);
                }             
            })
        })       
    })
    </script>
</body>
</html>
