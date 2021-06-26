# Javascript-Integration-with-Docker
In this task you have to create a Web Application for Docker (one of the great Containerization Tool
which provides the user Platform as a Service (PaaS))by showing your own creativity and UI/UX designing 
skills to make the webportal user friendly.

## This app will help the user to run all the docker commands like:
      👉docker images
      👉docker ps
      👉docker run
      👉docker rm -f
      👉docker exec
      👉 add more if you want. (Optional) 
      
## Steps to be followed :-
Here i am  using Rhel8 
- step1  :- install apache webserver in your system using yum install httpd 
- step2  :- install docker in your system using yum install docker-ce --nobest 
- step3  :- go to cd /var/www/html paste the docker.png,css and html content in this path and 
- step4  :- now go to cd /var/www/cgi-bin paste the docker.py content in this folder 
- step5  :- also check vim /etc/Sudoers  <br /> 
            allow root to run any cmd anywhere  <br /> 
            write this = apache ALL(ALL) ALL  <br /> 
           
          https://drive.google.com/file/d/1tz40t7pG1qgUOi5k_wXuy-4ZWYK6F7Zk/view?usp=sharing
- step6  :- systemctl start docker (start docker service )
- step7  :- systemctl start httpd  (start apache service ) 
- step8  :- getenforce (it will show enforcing) <br /> 
            setenforce 0
            getenforce (it will show permissive)
- step9  :- systemctl stop firewalld (now disable firewall)
- step10 :- ifconfig ip address paste that ip address in html javascript code 

Now go to your browser and paste your ip address/index.html 
