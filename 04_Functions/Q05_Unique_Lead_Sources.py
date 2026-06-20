lead_sources=[]
n=int(input("Enter the number of inputs:"))
for i in range(n):
    num=input("Enter the lead sources:")
    lead_sources.append(num)
unique_LeadSources=set(lead_sources)
print(unique_LeadSources)