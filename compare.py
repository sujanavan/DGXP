import csv

equal=0
equal_n=[]
equal_a=[]
equal_b=[]

both_zero=0
both_zero_n=[]
both_zero_a=[]
both_zero_b=[]

unique_a=0
unique_a_n=[]
unique_a_a=[]
unique_a_b=[]

unique_b=0
unique_b_n=[]
unique_b_a=[]
unique_b_b=[]

big_a=0
big_a_n=[]
big_a_a=[]
big_a_b=[]

big_b=0
big_b_n=[]
big_b_a=[]
big_b_b=[]

total=0

with open('input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print row[0],row[1],row[2]
        if float(row[1]) == float(row[2]) and float(row[1])!=0 and float(row[2])!=0 :
        	equal+=1
        	equal_n.append(row[0])
        	equal_a.append(row[1])
        	equal_b.append(row[2])
        if float(row[1]) == 0 and float(row[2])==0 :
        	both_zero+=1
        	both_zero_n.append(row[0])
        	both_zero_a.append(row[1])
        	both_zero_b.append(row[2])
        if float(row[1]) == 0 and float(row[2])!=0 :
        	unique_b+=1
        	unique_b_n.append(row[0])
        	unique_b_a.append(row[1])
        	unique_b_b.append(row[2])
        if float(row[2]) == 0 and float(row[1])!=0 :
        	unique_a+=1
        	unique_a_n.append(row[0])
        	unique_a_a.append(row[1])
        	unique_a_b.append(row[2])
        if float(row[1]) > float(row[2]) and float(row[2])!=0:
        	big_a+=1
        	big_a_n.append(row[0])
        	big_a_a.append(row[1])
        	big_a_b.append(row[2])
        if float(row[2]) > float(row[1]) and float(row[1])!=0:
        	big_b+=1
        	big_b_n.append(row[0])
        	big_b_a.append(row[1])
        	big_b_b.append(row[2])
        total+=1


print " Total Records = " , total
print " Equal (Non-Zero) = " , equal 
print " Both Zero = " , both_zero
print " Unique A = " , unique_a
print " Unique B = " , unique_b
print " A > B = " , big_a 
print " B > A = " , big_b 

f = open('Equal_Non_Zero.csv','w')
f.write('Equal (Non-Zero) =   ,' + str(equal)+'\n')
for i in range(len(equal_n)):
	f.write(str(equal_n[i]) +','+ str(equal_a[i]) +','+ str(equal_b[i])+ '\n')
f.close()

f = open('Both_Zero.csv','w')
f.write('Both Zero =  ,' + str(both_zero)+'\n')
for i in range(len(both_zero_n)):
	f.write(str(both_zero_n[i]) +','+ str(both_zero_a[i]) +','+ str(both_zero_b[i])+ '\n')
f.close()

f = open('Unique_A.csv','w')
f.write('Unique A = ,' + str(unique_a)+'\n')
for i in range(len(unique_a_n)):
	f.write(str(unique_a_n[i]) +','+ str(unique_a_a[i]) +','+ str(unique_a_b[i])+ '\n')
f.close()

f = open('Unique_B.csv','w')
f.write('Unique B = ,' + str(unique_b)+'\n')
for i in range(len(unique_b_n)):
	f.write(str(unique_b_n[i]) +','+ str(unique_b_a[i]) +','+ str(unique_b_b[i])+ '\n')
f.close()

f = open('A>B.csv','w')
f.write('A > B = ,' + str(big_a)+'\n')
for i in range(len(big_a_n)):
	f.write(str(big_a_n[i]) +','+ str(big_a_a[i]) +','+ str(big_a_b[i]) +','+ str(float(big_a_a[i]) - float(big_a_b[i]))+ '\n')
f.close()

f = open('B>A.csv','w')
f.write('B > A = ,' + str(big_b)+'\n')
for i in range(len(big_b_n)):
	f.write(str(big_b_n[i]) +','+ str(big_b_a[i]) +','+ str(big_b_b[i]) +','+ str(float(big_b_b[i]) - float(big_b_a[i]))+ '\n')
f.close()
