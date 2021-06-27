import json
from math import sqrt

def load_journal(journal):
	f=open(journal)
	data=json.load(f)
	
	return data
	
def compute_phi(journal,event):
	n11=0
	n00=0
	n10=0
	n01=0
	n1x=0
	n0x=0
	nx1=0
	nx0=0
	for i in journal:
		if event in i['events']:
			if i['squirrel']:
				n11 += 1
			else:
				n10 += 1
		elif i['squirrel']:
			n01 += 1
		else:
			n00 += 1
			
		if i['squirrel']:
			nx1 += 1
		else:
			nx0 += 1
			
		if event in i['events']:
			n1x += 1
		else:
			n0x += 1
			
	phi= (n11 * n00 - n10 * n01) / sqrt(n1x * n0x * nx1 * nx0)
		
	return phi
		
def compute_correlations(journal):
	data = load_journal(journal)
	corr={}
	for i in data:
		for j in i['events']:
			if j not in corr:
				phi = compute_phi(data,j)
				corr[j] = phi
	
	return corr
	
def diagnose(journal):
	correlations = compute_correlations(journal)
	maxi= -1
	mini = 1
	maxkey = ''
	minkey = ''
	for (key,value) in correlations.items():
		if value>maxi:
			maxi = value
			maxkey = key
			
		if value<mini:
			mini = value
			minkey = key
			
	return maxkey,minkey
	
def main():
	maxkey,minkey = diagnose("journal.json")
	print(maxkey,minkey)
	
	
if __name__ == '__main__':
	main()
