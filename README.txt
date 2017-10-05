Name:
	Appache httpd log parser
Source Files:
	parse_httpd_log.py
Usage:
	linux: ./parse_httpd_log.py -[rsuUc] <filepath>
	Windows: parse_httpd_log.py -[rsuUc] <filepath>

This tool helps to parse and analyze the appache httpd log file. The tool is written in python language and will run only on systems with python interpreter installed.
In linux make sure that the python interpreter in the path /usr/bin/ or run the tool with python command (ie. python parse_httpd_log.py -[rsuUc] <filepath>)
In windows make sure the python is added to the PATH environment or use the python interpreter full path to run the command (ie. C:\Python27\python.exe parse_httpd_log.py -[rsuUc] <filepath>)
Assume that the input appache log file is in the following format
"%h %l %u %t \"%r\" %>s %b" (hostIP <string/-> <string/-> [DD/MON/YYYY:HH:MM:SS TimeZone] "Request <page> http version" <error code> <request lenth>)

Options:
-r | --request 
	This option will list the top 10 requested pages in descending order. ie. Most visited page at the top.
-s | --success
	This option will show the success rate of requests in percentage.
-u | --unsuccess
	This option will show the unsuccessful request rate in percentage
-U | --unsuccess_pages
	This option will list the top 10 Unsuccessful pages in descending order
-c | --client
	This option will list the top 10 client IPs making most request in descending order
-m | --minutes
	This option will list number of requests in every minute in the log file in descending order
-i | --ipPage
	This option will list the top 5 pages requested by the top 10 clients.

Eg:
	parse_httpd_log.py -rsU /var/log/appche_httpd.log
