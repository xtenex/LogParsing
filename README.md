# LogParsing
Yet another log parser to identify user-agent

I must include more features, feel free to improve it as Your necesity
The log parser  works with logs like following sample:

65.98.119.36 - - [Tue Feb 22 16:32:25 UTC 2017] "GET /_js/master.js HTTP/1.1" 200 6943 "http://search.yahoo.com/mobile/s?rewrite=72&.tsrc=log&first=1&p=AWS%20logs&pintl=en" "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0"
147.106.118.104 - - [Tue Feb 22 18:18:59 UTC 2017] "GET /_media/play_button_gray.png HTTP/1.1" 200 6966 "http://search.yahoo.com/mobile/s?rewrite=72&.tsrc=apple&first=1&p=sumologic.com&pintl=en" "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36"
65.98.119.36 - - [Tue Feb 22 16:08:01 UTC 2017] "GET /_js/master.1332956664.js HTTP/1.1" 200 6980 "http://search.yahoo.com/mobile/s?rewrite=72&.tsrc=apple&first=1&p=sumologic.com&pintl=en" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.4) Gecko/2008102920 Firefox/3.0.4"
70.69.152.165 - - [Tue Feb 22 18:33:40 UTC 2017] "GET /_media/customer_tab_selected_top.png HTTP/1.1" 200 7037 "http://www.accel.com" "Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; SCH-R720 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"

to do:
1.- best way to show IP´s avoiding first and final brackets
2.- improve the way that parse logs in order to identify the place where user agent is just in case that is located on different places
3.- add options in case the log has separators
4.- improve to use all the features on the library using options to show useful information
5.- Improve for statistic pruposes.
