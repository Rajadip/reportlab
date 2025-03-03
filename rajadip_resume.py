from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.platypus import ListFlowable, ListItem, Paragraph
from textwrap import wrap

from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

registerFont(TTFont('Times_new', '/home/dba/Code/Python/reportLab/Times-New-Roman/Times New Roman/times new roman.ttf', subfontIndex=0))
registerFont(TTFont('Times_new-Bold', '/home/dba/Code/Python/reportLab/Times-New-Roman/Times New Roman/times new roman bold.ttf', subfontIndex=1))
registerFont(TTFont('Times_new-Italic', '/home/dba/Code/Python/reportLab/Times-New-Roman/Times New Roman/times new roman italic.ttf', subfontIndex=2))
registerFont(TTFont('Times_new-BoldItalic', '/home/dba/Code/Python/reportLab/Times-New-Roman/Times New Roman/times new roman bold italic.ttf', subfontIndex=3))


def getBullet(c, x, y, item):
	c.circle(x*inch, (y+0.03)*inch, 0.02*inch, fill=True, stroke=True)
	if isinstance(item, tuple):
		c.setFont("Times_new-Bold", 10)
		c.drawString((x+0.1)*inch, y*inch, item[0])
		c.setFont("Times_new", 10)
		c.drawString((x+0.85)*inch, y*inch, item[1])
	else:
		c.setFont("Times_new", 10)
		c.drawString((x+0.1)*inch, y*inch, item)

c = canvas.Canvas("Rajadip_resume_march_2025.pdf", pagesize=A4)

c.setFont("Times_new-Bold", 20)
c.drawString(0.5*inch,11.2*inch,"Rajadip Patil")
# Contact
c.setFont("Times_new-Bold", 10)
c.drawString(5.8*inch,11.4*inch,"Contact: ")
c.drawString(5.8*inch,11.2*inch,"Email: ")
c.setFont("Times_new", 10)
c.drawString(6.4*inch,11.4*inch,"+91 9145809229")
c.drawString(6.3*inch,11.2*inch,"rajadippatil@gmail.com")
y = 11
c.line(0.2*inch,y*inch, 8*inch, y*inch)

summary = "IT professional with backend development experience, specialising in server-side logic, database management, and API integration. Adept at writing clean, maintainable code and collaborating with cross-functional teams to deliver scalable software solutions."
y -= 0.25
c.setFont("Times_new", 10)
t = c.beginText()
wraped_text = "\n".join(wrap(summary, 125))
Nolines = wraped_text.count('\n')
t.setTextOrigin(0.4*inch, y*inch)
t.textLines(wraped_text)
c.drawText(t)
y -= (Nolines*0.2)+0.1
c.line(0.2*inch,y*inch, 8*inch, y*inch)

c.setFont("Times_new-Bold", 12)
y -= 0.25
c.drawString(1*inch,y*inch,"SKILLS SUMMARY")
c.drawString(5.1*inch,y*inch,"TECHNICAL STRENGTHS")
c.setFont("Times_new", 10)
skills = {
	"Languages: ": "Python, SQL, bash.",
	"Databases: ": "MySQL, MongoDB, Redis, Elasticsearch.",
	"Deployment: ": "Kubernetes, helm, ansible-playbooks, jenkins, ArgoCD.",
	"Libraries: ": "numpy, pandas, matplotlib, openCV, reportlab, flask, re.",
	"Commands: ": "git, ascp, rsync, scp, tcpdump.",
	"Tools: " : "grafana, elk, graylog, rabbitMQ, dbeaver, workbench."
}
y -= 0.25
for row in skills.items():
	getBullet(c, 0.3, y, row)
	y -= 0.2

strengths = [
	"Database designing and Administration.",
	"Advanced Querying and performance Tuning.",
	"Python microservices and machine learning libraries.",
	"Working on image processing.",
	"Working with devops technologies.",
	"Cluster monitoring and debugging."
]

y += (len(skills)*0.2)
for row in strengths:
	getBullet(c, 4.8, y, row)
	y -= 0.2

c.line(0.2*inch,y*inch, 8*inch, y*inch)

y -= 0.25
c.setFont("Times_new-Bold", 12)
c.drawString(1*inch,y*inch,"WORK EXPERIENCE")

c.setFont("Times_new-BoldItalic", 10)
y-=0.25
c.drawString(0.3*inch,y*inch,"Software Developer     Technicolor")
c.setFont("Times_new-Italic", 10)
c.drawString(1.45*inch,y*inch,"at                     ,Bangalore (May, 2022 - Present)")
y-=0.2

c.setFont("Times_new", 10)
t = c.beginText()
desc = "Technicolor is well known for providing visual effects, motion graphics and animation service. Our challenge was maintaining uniformity in files and assets being released by artists among cross sites. We were maintaining assets by syncing them cross sites and keeping track for synced data and creating reports meaningful reports out of data."
wraped_text = "\n".join(wrap(desc, 122))
Nolines = wraped_text.count('\n')+1
t.setTextOrigin(0.6*inch, y*inch)
t.textLines(wraped_text)
c.drawText(t)
y -= (Nolines*0.2)
li = [
	"Handling sync solutions,syncing files using Aspera and rsync.",
	"Writting efficient Python microservices for data manipulation.",
	"Used pub-sub model using RabbitMQ and Python worker.",
	"Used Kubernetes for seemless deployments, helm charts for describing cluster resources easily.",
	"Used ArgoCD to sync deployments across desired sites and ansible-playbook to manage system configuration.",
	"Working on database Advanced Querying and performance Tuning.",
	"User grafana for monitoring cluster resources and graylogs for checking logs easily and Power BI for data visualisation.",
	"SonarQube for unit testing, code coverage, and code analysis."
]
for each in li:
	getBullet(c, 0.7, y, each)
	y -= 0.2

y -= 0.1
c.setFont("Times_new-BoldItalic", 10)
c.drawString(0.3*inch,y*inch,"Software Developer     mPokket")
c.setFont("Times_new-Italic", 10)
c.drawString(1.45*inch,y*inch,"at                ,Bangalore (Nov, 2019 – May, 2022)")
y-=0.2

c.setFont("Times_new", 10)
t = c.beginText()
desc = "mPokket is an Instant Loan App with backend in python microservices. Using both SQL(MySQL) and NoSQL(MongoDB, Elasticsearch) databases with pub-sub model for processing live data."
wraped_text = "\n".join(wrap(desc, 120))
# Nolines = wraped_text.count('\n')
t.setTextOrigin(0.6*inch, y*inch)
t.textLines(wraped_text)
c.drawText(t)

y -= 0.4
li = [
	"Designing NoSQL database storage structures (MongoDB, Elasticsearch, Couchbase,).",
	"Efficient Python microservices for data manipulation.",
	"Worked on image processing, such as the masking process, face detection.",
	"Used RabbitMQ for queuing and writing a subscriber for data manipulation.",
	"Database performance tuning (MySQL, Elasticsearch).",
	"Worked with Kubernetes and Jenkins for seamless deployment and efficient applications.",
	"Using python liberaries like numpy, pandas, matplotlib for data analysis and visualisation."
]
for each in li:
	getBullet(c, 0.7, y, each)
	y -= 0.2

y -= 0.1
c.setFont("Times_new-BoldItalic", 10)
c.drawString(0.3*inch,y*inch,"Software Developer     Arthogyan")
c.setFont("Times_new-Italic", 10)
c.drawString(1.45*inch,y*inch,"at                   ,Hyderabad (April, 2019 – Oct, 2019)")
y-=0.2

c.setFont("Times_new", 10)
t = c.beginText()
desc = "This project is about prediction of getting financial goals using user’s current financial situation and their experiences using python pandas, numpy and other machine learning libraries."
wraped_text = "\n".join(wrap(desc, 122))
# Nolines = wraped_text.count('\n')
t.setTextOrigin(0.6*inch, y*inch)
t.textLines(wraped_text)
c.drawText(t)

y -= 0.4
li = [
	"SQL querying.",
	"Developing application architecture.",
	"Handling AWS services (EC2, Lambda functions, SQS, DynamoDB etc.).",
	"Developing backend in Python machine learning libraries (NumPy, pandas, Matplotlib, Scikit-learn, etc.)."
]
for each in li:
	getBullet(c, 0.7, y, each)
	y -= 0.2

y -= 0.1
c.setFont("Times_new-BoldItalic", 10)
c.drawString(0.3*inch,y*inch,"Python Developer, Database Administrator     Shivah Foundation")
c.setFont("Times_new-Italic", 10)
c.drawString(2.8*inch,y*inch,"at                                 ,Kolhapur (July, 2017 – April, 2019)")
y-=0.2

c.setFont("Times_new", 10)
t = c.beginText()
desc = "Here we were working on Web Application developed and Deployed for the NSS Department of the “Shivaji University” to reduce their most of the manual work and make it paperless which will be used by 250 colleges under Shivaji University."
wraped_text = "\n".join(wrap(desc, 122))
# Nolines = wraped_text.count('\n')
t.setTextOrigin(0.6*inch, y*inch)
t.textLines(wraped_text)
c.drawText(t)

y -= 0.4
li = [
	"Develop application flow.",
	"Designing Database, administration and Structuring SQL queries.",
	"MySQL performance tuning.",
	"Development of backend in python, flask and report generation in python report-lab."
]
for each in li:
	getBullet(c, 0.7, y, each)
	y -= 0.2	
y += 0.03
c.line(0.2*inch,y*inch, 8*inch, y*inch)

y -= 0.25
c.setFont("Times_new-Bold", 10)
c.drawString(0.3*inch,y*inch,"github:")
c.drawString(5*inch,y*inch,"LinkedIn:")
c.setFont("Times_new", 10)
c.drawString(0.75*inch,y*inch,"https://github.com/rajadip")
c.drawString(5.6*inch,y*inch,"https://in.linkedin.com/in/rajadip-patil")

c.showPage()
c.save()
