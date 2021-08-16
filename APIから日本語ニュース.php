<?php

$curl = curl_init();

curl_setopt_array($curl, [
	CURLOPT_URL => "https://newscatcher.p.rapidapi.com/v1/latest_headlines?lang=ja&media=True",
	CURLOPT_RETURNTRANSFER => true,
	CURLOPT_FOLLOWLOCATION => true,
	CURLOPT_ENCODING => "",
	CURLOPT_MAXREDIRS => 10,
	CURLOPT_TIMEOUT => 30,
	CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	CURLOPT_CUSTOMREQUEST => "GET",
	CURLOPT_HTTPHEADER => [
		"x-rapidapi-host: newscatcher.p.rapidapi.com",
		"x-rapidapi-key: 09c35d8e87msh8cf51e0f8dce97ap1d87aajsn85daff8f8a95"
	],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

$ne = json_decode($response);

var_export($ne);

if ($err) {
	echo "cURL Error #:" . $err;
} else {
	echo "aaa";
}

/*
$ne = json_decode($response);
var_export($ne);
*/

?>
