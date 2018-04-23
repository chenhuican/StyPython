#!/usr/bin/env python
#coding:utf-8
from math import sqrt
#recommendations.py
'''
	协作型过滤
'''

critics={'Lisa Rose':{'Lady in the Water':2.5,
					   'Snakes on a Plane':3.5,
					   'Just My Luck':3.0,
					   'Superman Resturns':3.5,
					   'You, Me and Dupree':2.5,
					   'The Night Listener':3.0
		},
		'Gene Seymour':{'Lady in the Water':3.0,
						'Snakes on a Plane':3.5,
						'Just My Luck':1.5,
						'Superman Resturns':5.0,
						'The Night Listener':3.0,
						'You, Me and Dupree':3.5
		},
		'Michael Phillips':{'Lady in the Water':4.0,
						'Snakes on a Plane':2.5,
						'Just My Luck':3.5,
						'Superman Resturns':5.0,
						'The Night Listener':3.0,
						'You, Me and Dupree':3.5
		},
		'Claudia Puig':{'Snakes on a Plane':3.5,
						'Just My Luck':3.0,
						'The Night Listener':4.5,
						'Superman Resturns':4.0,
						'You, Me Dupree':2.0

		},
		'Jack Matthnews':{'Lady in the Water':3.0,
						  'Snakes on a Plane':4.0,
						  'Just My Luck':2.0,
						  'Superman Resturns':3.0,
						  'The Night Listener':3.0,
						  'You, Me and Duprees':2.0
		},
		'Toby':{'Snakes on a Plane':4.5,'You, Me and Dupree':1.0, 'Superman Resturns':4.5},
}

def sim_distance(prefs, person1, person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1

	if len(si)==0:
		return 0

	sum_of_squares = sum(pow(prefs[person1][item]-prefs[person2][item],2) 
						for item in prefs[person1] if item in prefs[person2])

	return 1/(1+sqrt(sum_of_squares))