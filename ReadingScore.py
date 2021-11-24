import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
file=pd.read_csv('StudentsPerformance.csv')
readingScore=file['reading score'].to_list()

r_mean=statistics.mean(readingScore)
r_mode=statistics.mode(readingScore)
r_median=statistics.median(readingScore)
r_standardDev=statistics.stdev(readingScore)

print('The Mean,Median,Mode and the StandardDeviation Of Reading Scores of All Students is {} , {} , {} & {} respectively'.format(r_mean,r_median,r_mode,r_standardDev))

r_standardDeviation1_start,r_standardDeviation1_end=r_mean-r_standardDev,r_mean+r_standardDev
r_standardDeviation2_start,r_standardDeviation2_end=r_mean-(2*r_standardDev),r_mean+(2*r_standardDev)
r_standardDeviation3_start,r_standardDeviation3_end=r_mean-(3*r_standardDev),r_mean+(3*r_standardDev)

figure= ff.create_distplot([readingScore],["Reading Scores"], show_hist=False)
figure.add_trace(go.Scatter(x=[r_mean,r_mean],y=[0,0.17],mode="lines",name="Mean Of Reading Scores of All Students"))
figure.add_trace(go.Scatter(x=[r_standardDeviation1_start,r_standardDeviation1_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 START"))
figure.add_trace(go.Scatter(x=[r_standardDeviation1_end,r_standardDeviation1_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
figure.add_trace(go.Scatter(x=[r_standardDeviation2_start,r_standardDeviation2_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 START"))
figure.add_trace(go.Scatter(x=[r_standardDeviation2_end,r_standardDeviation2_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
figure.show()


listingOf1StandardDeviation=[r for r in readingScore if r>r_standardDeviation1_start and r<r_standardDeviation1_end]
listingOf2StandardDeviation=[r for r in readingScore if r>r_standardDeviation2_start and r<r_standardDeviation2_end]
listingOf3StandardDeviation=[r for r in readingScore if r>r_standardDeviation3_start and r<r_standardDeviation3_end]

print('{}% is there in 1StandardDeviation  '.format(len(listingOf1StandardDeviation)*100.0/len(readingScore)))
print('{}% is there in 2StandardDeviation  '.format(len(listingOf2StandardDeviation)*100.0/len(readingScore)))
print('{}% is there in 3StandardDeviation  '.format(len(listingOf3StandardDeviation)*100.0/len(readingScore)))