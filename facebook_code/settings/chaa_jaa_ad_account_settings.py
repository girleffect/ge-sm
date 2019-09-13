ad_account = {
    'accountId': '****',
    'accountName': '****',
  }

chaa_jaa_ad_account = {'accountId': '****',
    'accountName': '****',
  }



chaa_jaa_campaigns = [{'campaignId' : ****, 'campaignName': '****'}]


campaign_output_details = {'Campaign Id': ['campaignId','1a',None],
'Campaign name': ['campaignName','1a',None],
'Ad Set ID':['id',1,'Adset'],
'Ad set name':['name',2,'Adset'],
'Delivery status':['status',2, None],
'Lifetime budget':['lifetime_budget',2, 'Adset'],
'Reach':['reach',2, 'Metric'],
'Impressions':['impressions',2, 'Metric'],
'Frequency':['frequency',2, 'Metric'],
'Result type': ['optimization_goal', 3, 'Adset'], 
'Results': ['results', 3, None], 
'Cost per result': ['cpr', 3, None], 
'Amount spent': ['spend', 3, 'Metric'],
'Starts': ['start_time', 3, 'Adset'],
'Ends': ['end_time', 3, 'Adset'],
'Clicks': ['clicks', 3, 'Metric'], 
'Unique Clicks': ['unique_clicks', 3, 'Metric'], 
'Cost per click': ['cpc', 3, 'Metric'],
'Cost per 1000 impressions': ['cpm', 3, 'Metric'],
'Cost per 1000 reach': ['cpp', 3, 'Metric'],
'Cost per unique click': ['cost_per_unique_click', 3, 'Metric'],
'Cost per unique inline click': ['cost_per_unique_inline_link_click', 3, 'Metric'],
'Cost per thruplay': ['cost_per_thruplay', 3, 'Metric'],
'Photo View': ['actions', 3, 'photo_view'],
'Cost per photo view': ['cost_per_action_type', 3, 'photo_view'],
'Shares': ['actions', 3, 'post'],
'Cost per share': ['cost_per_action_type', 3, 'post'],
'Likes': ['actions', 3, 'like'],
'Cost per like': ['cost_per_action_type', 3, 'like'],
'Comments': ['actions', 3, 'comment'],
'Cost per comment': ['cost_per_action_type', 3, 'comment'],
'Link Clicks': ['actions', 3, 'link_click'],
'Cost per link click': ['cost_per_action_type', 3, 'link_click'],
'Post engagements': ['actions', 3, 'post_engagement'],
'Cost per post engagement': ['cost_per_action_type', 3, 'post_engagement'],
#'Messages': ['actions', 3, 'onsite_conversion.messaging_conversation_start'],
#'Cost per message': ['cost_per_action_type', 3, 'onsite_conversion.messaging_conversation_start'],
'Post landing page': ['actions', 3, 'landing_page_view'],
'Cost per landing page': ['cost_per_action_type', 3, 'landing_page_view'],
}


result_dict = {'POST_ENGAGEMENT': ('Post engagement', 'cost_per_action_type_post_engagement'), 
			   'REACH': ('Reach', 'cpp'),
			  'THRUPLAY': ('Thruplay', 'cost_per_thruplay'),
			  'LANDING_PAGE_VIEWS': ('Landing page views', 'landing_page_view'),
			  'LINK_CLICKS': ('Link clicks', 'cost_per_action_type_link_click')			  
			  }