$dogecoin_url='http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132';

function value($dogecoin_url)
{
    $ch2 = curl_init();
    $timeout2 = 0;
    curl_setopt($ch2,CURLOPT_URL,$dogecoin_url);
    curl_setopt($ch2,CURLOPT_RETURNTRANSFER,1);
    curl_setopt($ch2,CURLOPT_CONNECTTIMEOUT,$timeout2);
    $data2 = curl_exec($ch2);
    curl_close($ch2);
    return $value;
}

$coin = json_decode(value($dogecoin_url)); 

$doge_price_raw = $coin->return->markets->DOGE->lasttradeprice;

$doge_price = $doge_price_raw * 100000000;

$doge_main = array('s', intval($doge_price));

print json_encode($doge_main);

exec ( "main.py $doge_main" );
