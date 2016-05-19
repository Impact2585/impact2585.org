from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from site_editor.models import *

def index(request):
	slides = Index.objects.all()
	content = ''
	for slide in slides:
		if slide.media_type == '0':
			content += """<div>
						<img class="carousel-images" src=/static/media/photos/""" + slide.carousel_media_file_name + """>
						<div class="carousel-text">
						<h3>""" + slide.carousel_title + """</h3>
						<p>""" + slide.carousel_description + """</p>
						</div>
				</div>"""
		else:
			content += """<div>
						<iframe width="640" height="360" class="carousel-videos" src=""" + slide.carousel_media_file_name + """frameborder="0" allowfullscreen></iframe>
						<div class="carousel-text">
						<h3>""" + slide.carousel_title + """</h3>
						<p>""" + slide.carousel_description + """</p>
						</div>
				</div>"""
	return render(request, 'index.html', {'content' : content})		

def media(request):
	media = Media.objects.all().order_by('year')
	content = ""
	if len(media) > 0:
		max_year = media[len(media)-1].year
		min_year = media[0].year
		firstImage = 1;
		albums = []
		completed_albums = []
		for x in range(max_year - min_year + 1):

			content += """<div><h3 style='padding-left: 10px;'>""" + str(x + min_year) + """ Albums</h3>
								 <table style="margin: auto">
								 <tr>"""
			for i in range(len(media)):
				current = media[i]
				if current.year == (x + min_year):
					for data in media:
						if str(data.album) == str(current.album):
							if data.album not in completed_albums:
								if data.album not in albums:
									content += """<td class="media-image">
											<div style="text-align: center">
												<h4>""" + data.album + """</h4>
											</div>""";
									albums.append(data.album)
									firstImage = 1
								else:
									firstImage = 0

								if firstImage == 1:
									content += """<a href=""" + str(data.image)[6:] + """ rel='prettyPhoto[""" + data.album + str(data.year) + """]'>
										<img src=""" + str(data.image)[6:] + """></a>"""
									firstImage = 0
								else:
									content += """<a href=""" + str(data.image)[6:] + """ rel='prettyPhoto["""+ data.album + str(data.year) +"""]'></a>"""
					completed_albums.append(current.album)
			content += "</td>"
			content += "</tr></table></div><hr />"

	return render(request, 'media.html', {'content' : content})

def robots(request):
	frc_robots = Robot.objects.filter(competition__startswith='0') # 0 = FRC
	vex_robots = Robot.objects.filter(competition__startswith='1') # 1 = VEX

	frc_content = ''
	vex_content = ''
	for robot in reversed(frc_robots):
		frc_content+="""<div class="robot">
				<a href=/static/media/photos/""" + robot.robot_image_file_name + """ rel="prettyPhoto"><img src=/static/media/photos/"""  + robot.robot_image_file_name +  """  alt=""" + str(robot.robot_name) + """></a>
				<h4>""" + str(robot.robot_name) + " - " + str(robot.game_name) + " " + str(robot.game_year) +"""</h4>
				<p>""" + str(robot.description) + """</p>
				<hr />
			</div>"""
	for robot in reversed(vex_robots):
		vex_content+="""<div class="robot">
				<a href=/static/media/photos/""" + robot.robot_image_file_name + """ rel="prettyPhoto"><img src=/static/media/photos/"""  + robot.robot_image_file_name +  """  alt=""" + str(robot.robot_name) + """></a>
				<h4>""" + str(robot.robot_name) + " - " + str(robot.game_name) + " " + str(robot.game_year) +"""</h4>
				<p>""" + str(robot.description) + """</p>
				<hr />
			</div>"""

	return render(request, 'robots.html', {'frc_robots' : frc_content, 'vex_robots' : vex_content})

def aboutus(request):
	return render(request, 'aboutus.html')	

def sponsors(request):
	return render(request, 'sponsors.html')		