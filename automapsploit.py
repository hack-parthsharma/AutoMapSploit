import sys
import os

full_ip = sys.argv[1]


ip = sys.argv[1].split('.')
separator = '.'
ip.pop()
ip_begin = separator.join(ip)
ip_end = ip = sys.argv[1].split('.')[3]
full_ip = ip_begin + "." + ip_end

nmap_cmd = "nmap -T4 --open -sS -vvv --min-rate=1000 --max-retries=2 -A -Pn "
ss_cmd = "searchsploit -x --nmap "

for i in range(1, 255):
    os.system(nmap_cmd + "-p- " + ip_begin + "." +
              i + " -oX " + full_ip + "_out.xml")
    os.system(ss_cmd + full_ip + "_out.xml > " + full_ip + "_ss.txt")
