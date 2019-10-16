channelsdict = {  
	'****': {
		'name': '****',
		'analyticsdat': 'analytics_CJ.dat',
		'playlist': '****',
		'youtubedat': 'youtube_CJdat.dat'
	}
}


#Metric details
std_metric_details = {'Views': ['views','1a','Metric'],
'Watch time':['watchtime',1,None], ## views * avg view time
'Avg view duration':['averageViewDuration',1,'Metric'],
'Avg view percentage':['averageViewPercentage',2,'Metric'],
'Comments':['comments',3,'Metric'],
'Likes':['likes',4,'Metric'],
'Dislikes':['dislikes',5,'Metric'],
'Shares':['shares',6,'Metric'],
'Subscribers':['subscribers',7, None], ## subs gained - subs lost
'Subscribers gained':['subscribersGained',7,'Metric'], 
'Subscribers lost':['subscribersLost',8,'Metric'], 
'Annotation Clicks':['annotationClicks',9,'Metric'], 
'Annotation clickable impressions':['annotationClickableImpressions',10,'Metric'],
'Annotation click through rate':['annotationClickThroughRate',11,'Metric']}

vid_details = [('ChName','Channel name'), ('ChId', 'Channel ID'), ('video', 'Video Id'), 
('videoname','Video name'), ('videourl', 'URL'), ('videopub','Date published'), ('estimatedMinutesWatched', 'Est Minutes Watched')]
