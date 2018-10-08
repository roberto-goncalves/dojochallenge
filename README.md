# dojochallenge

* Describe how'd you provision a set of linux machines and how'd you orchestrate, monitor and troubleshoot these services in a cloud environment such as AWS

A: On the most basic configuration, any of these resources could be migrated to a EC2 instance with docker. This type of configuration is easy to setup, as the scripts was configured to use environment variables, but, if it needs to be scalable it might be painful. 

On a scalable problem, it is possible to create new AMI with AWS-CLI and launch instances at they are needed, each one of them with a web_scrapper and a apache in it, encapsulated.

If the problem needs more parallel executions, it could be changed to adapt to AWS Lambda and API Gateway and creating on a back-server-side a REST API that receives a JSON and change the HTML content of it's respective server.

Monitoring & Troubleshooting in this case could be the same, using ELK Stack (Elasticsearch, Logstash, Kibana) to monitor logs and create fields about it. Using Logstash to parse apache and web_scrapper could be possible to generate a error tag that wherever have a 404 or some python random error, it could be monitored, and with a field that it would call (instance) the troubleshooting is easy, since you know the instance and the problem.

* Reasoning behind your technical choices. Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.

A: My technical choice was to do something simple and functional. The worst trade-off that I think is about pulling down and up on docker-compose to build a new image, that could be easily managed with docker stack and service update, and I need to search more about it, what are the principal difference between them.

Other thing that is really bothering me is while(True) loop on python script, I would remove it too, it is ugly. I would find a way to pass it to a CRON job, to be more elegant.

Another thing that I might change is the regex expression, it would work in a great number of cases, but not all of them. I could use a library or could develop one to create a Abstract Syntax Tree and change the value inside tag properly. 

And another thing that is bothering me is that index.html shared between services, I think there might be a better way of doing it.

# Lab

docker-compose build

docker-compose up

Web-page on port 60005
