import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
file=pd.read_csv('StudentsPerformance.csv')
mathScore=file['math score'].to_list()

m_mean=statistics.mean(mathScore)
m_mode=statistics.mode(mathScore)
m_median=statistics.median(mathScore)
m_standardDev=statistics.stdev(mathScore)

print('The Mean,Median,Mode and the StandardDeviation Of Math Scores of All Students is {} , {} , {} & {} respectively'.format(m_mean,m_median,m_mode,m_standardDev))

m_standardDeviation1_start,m_standardDeviation1_end=m_mean-m_standardDev,m_mean+m_standardDev
m_standardDeviation2_start,m_standardDeviation2_end=m_mean-(2*m_standardDev),m_mean+(2*m_standardDev)
m_standardDeviation3_start,m_standardDeviation3_end=m_mean-(3*m_standardDev),m_mean+(3*m_standardDev)

figure= ff.create_distplot([mathScore],["Math Scores"], show_hist=False)
figure.add_trace(go.Scatter(x=[m_mean,m_mean],y=[0,0.17],mode="lines",name="Mean Of Math Scores of All Students"))
figure.add_trace(go.Scatter(x=[m_standardDeviation1_start,m_standardDeviation1_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 START"))
figure.add_trace(go.Scatter(x=[m_standardDeviation1_end,m_standardDeviation1_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
figure.add_trace(go.Scatter(x=[m_standardDeviation2_start,m_standardDeviation2_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 START"))
figure.add_trace(go.Scatter(x=[m_standardDeviation2_end,m_standardDeviation2_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
figure.show()


listingOf1StandardDeviation=[m for m in mathScore if m>m_standardDeviation1_start and m<m_standardDeviation1_end]
listingOf2StandardDeviation=[m for m in mathScore if m>m_standardDeviation2_start and m<m_standardDeviation2_end]
listingOf3StandardDeviation=[m for m in mathScore if m>m_standardDeviation3_start and m<m_standardDeviation3_end]

print('{}% is there in 1StandardDeviation  '.format(len(listingOf1StandardDeviation)*100.0/len(mathScore)))
print('{}% is there in 2StandardDeviation  '.format(len(listingOf2StandardDeviation)*100.0/len(mathScore)))
print('{}% is there in 3StandardDeviation  '.format(len(listingOf3StandardDeviation)*100.0/len(mathScore)))