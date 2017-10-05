#!/usr/bin/python

import collections
import re
import optparse

usage="usage: %prog [options] arg1"
opt_arg = optparse.OptionParser(usage=usage)
opt_arg.add_option('-r', '--request',action='store_true' ,dest='req', help = 'Top 10 requested pages')
opt_arg.add_option('-s', '--success', action='store_true',dest='success', help = 'Rate of successful requests')
opt_arg.add_option('-u', '--unsuccess', action='store_true', dest='failed', help = 'Rate of Unsucessful requests')
opt_arg.add_option('-U', '--unsuccess_pages', action= 'store_true', dest='failed_pages', help = 'Top 10 failed page requests')
opt_arg.add_option('-c', '--clients', action= 'store_true', dest='clients', help = 'Top 10 client IPs with most request')
opt_arg.add_option('-m', '--minutes', action= 'store_true', dest='minutes', help = 'Shows the number of request in every minute in ascending order')
opt_arg.add_option('-i', '--ipPage', action= 'store_true', dest='ip_page', help = 'shows top 5 pages for top 10 client IPs')


(options,args) = opt_arg.parse_args();


if len(args) != 1:
    print ('Number of arguments are invalid')
    opt_arg.print_help()
else:
    if not options.req and not options.success and not options.failed and not options.failed_pages and not options.clients and not options.minutes and not options.ip_page:
        print("Please enter one or more options")
        opt_arg.print_help()
        exit()
    try:
        file = open(args[0])
    except:
        print ("File does not exists")
        
    count=success=failure=0
    
    request_log = []
    ip_log = []
    failure_log = []
    request_minutes = []
    common_ip = []
    ip_page = []
    
    
    for line in file:
        
        log_data = re.split(r'[?,\s]', line)
        
        if options.req:
            request_log.append(log_data[6])
        
        if options.clients or options.ip_page:
            ip_log.append(log_data[0])
        
        if options.success or options.failed or options.failed_pages:
            count +=1 
    
            if log_data[-3][0] in ("2","3"):
                success +=1
            else:
                if(options.failed_pages):
                    failure_log.append(log_data[6])
                failure +=1
                
        if options.minutes:              
            request_minutes.append(log_data[3][1:-3])

    if options.req:
        req_data = collections.Counter(request_log)
    
        print ("\n" +"Page" + "                " + "Count" +"\n")
        
        for stat in req_data.most_common(10):
            print(stat[0] + "      " + str(stat[1]))
    
    if options.clients or options.ip_page:
        ip_data = collections.Counter(ip_log)
        
        if options.clients:
            print ("\n" +"IP" + "              " + "Count"+ "\n")
          
        for stat in ip_data.most_common(10):
            if options.clients:
                print(stat[0]+"     " +str(stat[1]))
            common_ip.append(stat[0])
    
    if options.failed_pages:    
        failure_data = collections.Counter(failure_log)
    
        print("\n" +"Faild Page" +"               " +"Count " + "\n")
        
        for stat in failure_data.most_common(10):
            print(stat[0]+"     " +str(stat[1]))
         
    if options.minutes:
        minute_data = collections.Counter(request_minutes)
        
        print("Minute"+"                    "+"Count")
        for stat in minute_data.most_common():
           print(stat[0]+"     " +str(stat[1]))	
    
    if options.success:  
        print ("\n"+"Successful Requests % ="+ str(round(float(success)/count *100, 2)))
    if options.failed:
        print("\n"+"Unsuccessful Requests %s=" + str(round(float(failure)/count*100,2)))
        
    if options.ip_page:
        file.seek(0);
        for line in file :
            if line.split()[0] in common_ip:
                ip_page.append(line.split()[0] + ":" + re.split(r'[?,\s]', line)[6])
        
        ip_page_data = collections.Counter(ip_page);
        
        
        print("IP"+"                 "+"Page"+"                  "+"Count")
        index = 0;
        for ip in common_ip:
            count = 0;
            for stat in ip_page_data.most_common():
                if(stat[0].split(':')[0] == common_ip[index]):
                    print(stat[0].split(':')[0]+"     " +stat[0].split(':')[1]+"     "+str(stat[1]))

                    count +=1
                    if count == 5:
                        break
            index +=1
    
    file.close()
            
        
