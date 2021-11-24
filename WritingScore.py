import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
file=pd.read_csv('StudentsPerformance.csv')
writingScore=file['writing score'].to_list()

w_mean=statistics.mean(writingScore)
w_mode=statistics.mode(writingScore)
w_median=statistics.median(writingScore)
w_standardDev=statistics.stdev(writingScore)

print('The Mean,Median,Mode and the StandardDeviation Of Writing Scores of All Students is {} , {} , {} & {} respectively'.format(w_mean,w_median,w_mode,w_standardDev))

w_standardDeviation1_start,w_standardDeviation1_end=w_mean-w_standardDev,w_mean+w_standardDev
w_standardDeviation2_start,w_standardDeviation2_end=w_mean-(2*w_standardDev),w_mean+(2*w_standardDev)
w_standardDeviation3_start,w_standardDeviation3_end=w_mean-(3*w_standardDev),w_mean+(3*w_standardDev)

figure= ff.create_distplot([writingScore],["Writing Scores"], show_hist=False)
figure.add_trace(go.Scatter(x=[w_mean,w_mean],y=[0,0.17],mode="lines",name="Mean Of Writing Scores of All Students"))
figure.add_trace(go.Scatter(x=[w_standardDeviation1_start,w_standardDeviation1_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 START"))
figure.add_trace(go.Scatter(x=[w_standardDeviation1_end,w_standardDeviation1_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
figure.add_trace(go.Scatter(x=[w_standardDeviation2_start,w_standardDeviation2_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 START"))
figure.add_trace(go.Scatter(x=[w_standardDeviation2_end,w_standardDeviation2_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
figure.show()


listingOf1StandardDeviation=[w for w in writingScore if w>w_standardDeviation1_start and w<w_standardDeviation1_end]
listingOf2StandardDeviation=[w for w in writingScore if w>w_standardDeviation2_start and w<w_standardDeviation2_end]
listingOf3StandardDeviation=[w for w in writingScore if w>w_standardDeviation3_start and w<w_standardDeviation3_end]

print('{}% is there in 1StandardDeviation  '.format(len(listingOf1StandardDeviation)*100.0/len(writingScore)))
print('{}% is there in 2StandardDeviation  '.format(len(listingOf2StandardDeviation)*100.0/len(writingScore)))
print('{}% is there in 3StandardDeviation  '.format(len(listingOf3StandardDeviation)*100.0/len(writingScore)))