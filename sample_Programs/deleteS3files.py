import os,time
from datetime import date, timedelta
today=time.strftime("%Y-%m-%d")
days_before = (date.today()-timedelta(days=139)).isoformat()
os.system("aws s3 ls s3://infor-devops-dev-appdata-us-east-1/hms-fqa-ecs-cluster/data/logCollector/ > fileslistfqa.txt")
file=open("fileslistfqa.txt","r+")
line=file.readlines()
content=[]
for i in line:
	a=i.rstrip()
	rawlist=a.split(" ")
	if (rawlist[0] < days_before):
		content.append(rawlist[-1])
print(content)
command="aws s3 rm s3://infor-devops-dev-appdata-us-east-1/hms-fqa-ecs-cluster/data/logCollector/"
for j in content:
	#print("aws s3 ls s3://infor-devops-dev-appdata-us-east-1/hms-fqa-ecs-cluster/data/logCollector/",j,sep='')
	run=command+j
	#print(run)
	os.system(run)