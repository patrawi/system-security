#### Activity 1: Can you find people trying to break into the servers?

##### 1.1 How many hackers are trying to get access to our servers? And how many attempts are there?

###### Ans.

There is 185 hackers and 33253 times. using extra field
by using regex (?P<src_ip>[^ ]+) port (?P<src_port>\d+)
![1.1](./image//Screenshot%202566-02-15%20at%2020.39.09.png)

##### 1.2 What time do hackers appear to try to hack our servers?

###### Ans.

The hacking starts from 9 September to 17 September on every 12.15.05

![1.2](./image//Screenshot%202566-02-15%20at%2020.51.40.png)

##### 1.3 Which server (mailsv, www1, www2, www3) seem to see the most attempts?

##### Ans.

www1 has the most attempts with 8798 attemps
![1.3](./image/Screenshot%202566-02-15%20at%2020.57.31.png)

##### 1.4 What is the most popular account that hackers use to try to break in?

###### Ans.

The most popular account is 10.3.10.46
![1.4](./image/Screenshot%202566-02-15%20at%2021.03.34.png)

#### Activity 2: Sensitive Files on Web Servers

##### 2.1 Can you find attempts to get access to sensitive information from our web servers? How many attempts were there?

###### Ans. There are 2 files that are sensitive which are password.pdf (51 times for GET method) and anna_nicole.html (62 times for GET method)

![2.1](./image/Screenshot%202566-02-15%20at%2021.41.40.png)
![2.1.2](./image/Screenshot%202566-02-15%20at%2021.44.13.png)

##### 2.2 What resource/file are hackers looking for?

###### Ans.

password.pdf and anna_nicole.html which is located in hidden folder.

#### Activity 3: (Optional)

##### Are there bots crawling our websites?

##### Ans.

Yes

##### 3.2 Can you find any bots crawling our websites?

Yes, there are 2 bots which are YandexBot and GoogleBot
![3.2](./image/Screenshot%202566-02-15%20at%2022.06.08.png)
