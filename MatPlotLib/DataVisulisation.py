import matplotlib.pyplot as plt 
# x=[1,2,3,4]
# y=[10,20,15,25]
# plt.plot(x,y)
# plt.show()
# x=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# y=[10,20,15,25,30,18,35]
# plt.title(" Bakery sales data in week")
# plt.xlabel("Days of week")
# plt.ylabel("Sales in rupees")
# plt.plot(x,y,marker='o',linestyle='-.',color='b')
# plt.xlim('Tue','Sat')
# plt.ylim(0,35)
# plt.grid()
# plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
# plt.show()
# Sales product Analysis--->
# x=['Cake','Pastry','Bread','Cookies','Doughnut']
# y=[20,15,30,10,25]
# plt.title("Product sale Analysis")
# plt.xlabel("Products")
# plt.ylabel("Number of sales")
# plt.bar(x,y,color='orange',label='Sales data')
# plt.legend()

# # For Pie chart-->
# regions=['North','South','East','West']
# revenue=[3000,2000,1500,1000]
# plt.pie(revenue,labels=regions,autopct='%1.1f%%',startangle=90,shadow=True,colors=['yellow','skyblue','lightgreen','coral'])
# plt.title("Revenue by region")

# For Histogram-->
# data=[22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,130,111,115,80,75,65,54,44,43,42]
# plt.hist(data,bins=10,color='purple',edgecolor='black')
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram")
# For Scatter plot-->
# hours_studies=[1,2,3,4,5,6,7,8]
# exam_score=[50,55,60,65,70,75,80,85]
# scatter plot-->
# plt.scatter(hours_studies,exam_score,color='green',marker='o',label='Student Data')
# plt.xlabel("Hours Studies")
# plt.ylabel("Exam Score")
# plt.title("Hours Studies vs Exam Score")
# plt.legend()
# plt.scatter([1,2,3],[40,58,34])
# plt.scatter([1,2,3],[67,54,59])
# plt.xlabel("hours Studies")
# plt.ylabel("Exam Score")
# plt.title("Hours Studies vs Exam Score")
# plt.legend(['Student A','Student B']) 
# plt.grid()
# x=[1,2,3,4]
# y=[10,20,15,25]
# plt.subplot(1,2,1)
# plt.plot(x,y,color='orange')
# plt.title("Line Chart")
# plt.subplot(1,2,2)
# plt.bar(x,y,color=['green','blue'])
# plt.title("Bar Chart")
# plt.tight_layout()
# plt.show()
# Saving thye data-->
# savefig('filename.extension',dpi=value,bbox_inches='tight') //this is used to save the file
x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y,color='orange',marker='o')
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig('line_chart.png',dpi=300,bbox_inches='tight') 
plt.show()