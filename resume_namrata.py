from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from textwrap import wrap

def drawText(c,x,y,text,tsize,lwidth):
	t = c.beginText()
	t.setFont('Helvetica', tsize)
	t.setTextOrigin(x*inch,y*inch)
	wraped_text = "\n".join(wrap(text,lwidth))
	t.textLines(wraped_text)
	c.drawText(t)

c = canvas.Canvas("Namrata_resume_oct_2023.pdf", pagesize=A4)

c.rect(0.1*inch,0.1*inch,8.05*inch,11.5*inch)

c.setFont("Helvetica-Bold", 20)
c.drawString(2.6*inch,11.2*inch,"Namrata Rajadip Patil")
c.setFont("Helvetica", 12)
c.drawString(2.6*inch,11*inch,"Biotechnologist")

y = 10.6
# Experience
c.setFont("Helvetica", 14)
c.drawString(2.6*inch,y*inch,"EXPERIENCE")
y-=0.1
c.line(2.6*inch,y*inch, 8*inch, 10.5*inch)

c.setFont("Helvetica-Bold", 12)
y-= 0.2
c.drawString(2.6*inch,y*inch,u'\u2022 SEEMA BIOTECH - ')
c.setFont("Helvetica", 10)
c.drawString(4.25*inch,y*inch, 'Production Manager')
y -= 0.2
c.drawString(2.6*inch,y*inch, '   From Feb 2019 – Oct 2023 (4 Years 8 Month)')
y-=0.2
c.drawString(2.6*inch,y*inch, '   Work Area: ')
y-=0.15
c.drawString(2.6*inch,y*inch, u'     \u2022 Banana Tissue Culture Laboratory (Feb 2019 to Aug 2021).')
y-=0.15
c.drawString(2.6*inch,y*inch, u'     \u2022 Ornamental Tissue Culture Laboratory (Aug 2021 to Oct 2023).')
y-=0.15
c.drawString(2.6*inch,y*inch, u'     \u2022 Managing production and observing process.')

y -=0.3
# Projects
c.setFont("Helvetica", 14)
c.drawString(2.6*inch,y*inch,"PROJECTS")
y -= 0.1
c.line(2.6*inch,y*inch, 8*inch, y*inch)

c.setFont("Helvetica-Bold", 10)
y -= 0.2
c.drawString(2.6*inch,y*inch,u'\u2022 Title - ')
c.setFont("Helvetica", 10)
c.drawString(3.1*inch,y*inch, 'Anitphytopathogenic Properties of Chitin and Colloidal chitin.')
objective = 'To control plant diseases caused by fungal pathogens resulting vast crop damage globally.'
c.setFont("Helvetica-Bold", 10)
y -= 0.2
c.drawString(2.7*inch,y*inch, 'Objective:')
drawText(c, 3.38, y, objective, 10, 75)
c.setFont("Helvetica-Bold", 10)
y -= 0.3
c.drawString(2.7*inch,y*inch, 'Description:')
c.setFont("Helvetica-Bold", 10)
y -= 0.15
c.drawString(2.8*inch, y*inch,u'\u2022')
t1 = "Breeding for disease resistant varieties and the application of synthetic chemical fungicidesare the most widely accepted approaches in plant disease management. An alternative approach to avoid the undesired effects of chemical control could be biological control using antifungal bacteria that exhibit direct action against fungal pathogens."
drawText(c, 2.9, y, t1, 10, 80)
c.setFont("Helvetica-Bold", 10)
y -= 0.85
c.drawString(2.8*inch,y*inch,u'\u2022')
t2 = "In this case study, chitin and colloidal chitin were used as substrate in the soil and were checked for their disease control efficiency compared to normal infected plant."
drawText(c, 2.9, y, t2, 10, 80)
c.setFont("Helvetica-Bold", 10)
y -= 0.5
c.drawString(2.8*inch,y*inch,u'\u2022')
t3 = "It was done by considering various biochemical analysis for soil and plant both."
drawText(c, 2.9, y, t3, 10, 80)

c.setFont("Helvetica-Bold", 10)
y -= 0.2
c.drawString(2.7*inch,y*inch, 'Skills developed during project :')
c.setFont("Helvetica", 10)
y -= 0.15
c.drawString(2.8*inch,y*inch,u'\u2022 DNSA method for chitinase activity.')
y -= 0.18
c.drawString(2.8*inch,y*inch,u'\u2022 Lowry’s method for protein estimation.')
y -= 0.17
c.drawString(2.8*inch,y*inch,u'\u2022 Ninhydrin method for amino acid estimation.')

c.setFont("Helvetica-Bold", 10)
y -= 0.3
c.drawString(2.6*inch,y*inch,u'\u2022 Title - ')
c.setFont("Helvetica", 10)
c.drawString(3.1*inch,y*inch, 'Phytochemical and nutritional analysis of Murraya koenigii (curry leaves).')
objective = 'To analyse phytochemical and nutrional properties of curry leaves.'
c.setFont("Helvetica-Bold", 10)
y -= 0.2
c.drawString(2.7*inch,y*inch, 'Objective:')
drawText(c, 3.38, y, objective, 10, 75)
c.setFont("Helvetica-Bold", 10)
y -= 0.2
c.drawString(2.7*inch,y*inch, 'Description:')
c.setFont("Helvetica-Bold", 10)
y -= 0.15
c.drawString(2.8*inch,y*inch,u'\u2022')
t1 = "Analysed for phytochemicals such as flavonoids, terpenoids, alkaloids, tannins, saponins, phlobatannins through various tests."
drawText(c, 2.9, y, t1, 10, 80)
c.setFont("Helvetica-Bold", 10)
y -= 0.35
c.drawString(2.8*inch,y*inch,u'\u2022')
t2 = "Analysed for nutrional contents such as ascorbic acid (vitamin C) and sugar."
drawText(c, 2.9, y, t2, 10, 80)

c.setFont("Helvetica-Bold", 10)
y -= 0.2
c.drawString(2.7*inch,y*inch, 'Skills developed during project :')
c.setFont("Helvetica", 10)
y -= 0.15
c.drawString(2.8*inch,y*inch,u'\u2022 Titration for ascorbic acid analysis.')
y -= 0.18
c.drawString(2.8*inch,y*inch,u'\u2022 DNSA method for sugar analysis.')

# Additional
y -= 0.3
c.setFont("Helvetica", 14)
c.drawString(2.6*inch,y*inch,"ACHIEVEMENTS")
y -= 0.1
c.line(2.6*inch,y*inch, 8*inch, y*inch)
c.setFont("Helvetica", 10)
a1 = "Patent Agent Training Programme and Certification"
a2 = "Career Oriented Pantent Training Programme and Certification"
a3 = "Late Dr. Pandurang Dattatray Kulkarni” W.H.O. officer prize for securing highest number of marks in M.Sc. Part-I."
a4 = "Scholarship from Shivaji University for securing highest rank in M.Sc. Part-I."
a5 = "Secured third rank in merit order of Maharashtra in B.Sc."
a6 = "Participated in Quiz conpitition under Ferment inter-college programme at Willingdon College, Sangli."
a7 = "Participated in one day workshop on “Wine processing and wine testing” at Heritage Grape Winery."
a8 = "Participated and secured Consolation prize in National Level Quiz Competition in Biosciences."
y -= 0.15
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a1, 10, 85)
y -= 0.175
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a2, 10, 85)
y -= 0.175
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a3, 10, 85)
y -= 0.325
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a4, 10, 80)
y -= 0.175
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a5, 10, 80)
y -= 0.175
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a6, 10, 80)
y -= 0.325
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a7, 10, 80)
y -= 0.325
c.drawString(2.7*inch,y*inch,u'\u2022')
drawText(c, 2.8, y, a8, 10, 80)

# Additional
c.setFont("Helvetica", 14)
c.drawString(2.6*inch,1.65*inch,"ADDITIONAL INFORMATION")
c.line(2.6*inch,1.55*inch, 8*inch, 1.55*inch)
c.setFont("Helvetica", 10)
c.drawString(2.6*inch,1.35*inch,"LinkedIn Profile: https://www.linkedin.com/in/namrata-patil-399453243")

# side bar
c.setFillColor(HexColor('#3e415e'))
c.rect(0.1*inch,0.1*inch,2.2*inch,11.5*inch,fill=1, stroke=1)
c.setFillColor(HexColor('#3e41ee'))
c.rect(0.5*inch,9.2*inch,1.6*inch,2.25*inch,fill=1, stroke=1)
#c.drawImage('NAMRATAPHOTO.jpeg', 0.5*inch, 9.2*inch, width=1.6*inch, height=2.25*inch)
c.setFillColor(HexColor('#FFFFFF'))

# Contact
c.setFont("Helvetica-Bold", 16)
c.drawString(0.2*inch,8.9*inch,"Contact")
c.setStrokeColor(HexColor('#FFFFFF'))
c.line(0.1*inch,8.8*inch, 2.3*inch, 8.8*inch)
c.setFont("Helvetica", 10)
c.drawString(0.3*inch,8.6*inch,"+91 8483873291")
c.drawString(0.3*inch,8.4*inch,"namrata.r.patil18@gmail.com")

# Education
c.setFont("Helvetica-Bold", 16)
c.drawString(0.2*inch,8*inch,"Education")
c.setStrokeColor(HexColor('#FFFFFF'))
c.line(0.1*inch,7.9*inch, 2.3*inch, 7.9*inch)

c.setFont("Helvetica-Bold", 10)
c.drawString(0.3*inch,7.7*inch,"M.Sc.(2018) - 70.42%")
c.setFont("Helvetica", 10)
c.drawString(0.3*inch,7.5*inch,"Shivaji University, Kolhapur")

c.setFont("Helvetica-Bold", 10)
c.drawString(0.3*inch,7.2*inch,"B.Sc.(2016) - 77.15%")
c.setFont("Helvetica", 10)
c.drawString(0.3*inch,7.0*inch,"Vivekanand College, Kolhapur")

c.setFont("Helvetica-Bold", 10)
c.drawString(0.3*inch,6.7*inch,"H.S.C.(2013) - 65.17%")
c.setFont("Helvetica", 10)
c.drawString(0.3*inch,6.5*inch,"State Board")

c.setFont("Helvetica-Bold", 10)
c.drawString(0.3*inch,6.2*inch,"S.S.C.(2011) - 88.40%")
c.setFont("Helvetica", 10)
c.drawString(0.3*inch,6.0*inch,"State Board")

# Lab skills
c.setFont("Helvetica-Bold", 16)
c.drawString(0.2*inch,5.6*inch,"Skills")
c.setStrokeColor(HexColor('#FFFFFF'))
c.line(0.1*inch,5.5*inch, 2.3*inch, 5.5*inch)

c.setFont("Helvetica-Bold", 10)
c.drawString(0.3*inch,5.3*inch,u"\u2022 Plant tissue culture : ")
c.setFont("Helvetica", 10)
s = "Banana(Grand Nain), Ornamental Plants (Anthurium, Syngonium, Orchid), Stock MS media preparation, Stock preparation of BAP, NAA, IAA"
drawText(c, 0.4, 5.15, s, 10, 28)

c.setFont("Helvetica", 10)
c.drawString(0.3*inch,4.15*inch,u"\u2022")
s = "Microbial techniques : Microscopy, Inoculation, Aseptic techniques, Spread Plate, Pour Plate, Streak Plate, Gram’s Staining"
drawText(c, 0.4, 4.15, s, 10, 30)

c.setFont("Helvetica", 10)
s = "DNA isolation"
c.drawString(0.3*inch,3.3*inch,u"\u2022")
drawText(c, 0.4, 3.3, s, 10, 30)

c.setFont("Helvetica", 10)
s = "Polymerase Chain Reaction"
c.drawString(0.3*inch,3.1*inch,u"\u2022")
drawText(c, 0.4, 3.1, s, 10, 30)

c.setFont("Helvetica", 10)
s = "Lead and Team Management"
c.drawString(0.3*inch,2.9*inch,u"\u2022")
drawText(c, 0.4, 2.9, s, 10, 30)


# c.setFont("Helvetica-Bold", 10)
# c.drawString(0.3*inch,2.35*inch,u"\u2022 Biochemistry and Immuno-")
# c.drawString(0.3*inch,2.2*inch, "-logical techniques :")
# c.setFont("Helvetica", 10)
# s = "Antigen and Antibody Interaction, ELISA etc."
# drawText(c, 0.4, 2.075, s, 10, 30)

c.showPage()
c.save()

# 
