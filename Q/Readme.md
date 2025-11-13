Server setup
Use python build-in server functionality to host a file
"python3 -m http.server 8080"
Set up Firewall
ufw to setup Firewall: https://help.ubuntu.com/community/UFW

Troubleshooting
Address already in use error show if the server rerun.
Identify the process using port number
"sudo lsof -i :<PORT_NUMBER>"
Kill the process 
"kill -9 <PID>"
