# Electroencephalogram Data
This reposistory contains html and ipynb file for comeplete analysis of EEG Data.

## Web-Page
Published Web-Page is available <a href="https://newtein.github.io/eeg/" target="_blank"> here.</a>


Dataset Link: https://archive.ics.uci.edu/ml/datasets/eeg+database

## Index
### Initiating
0 : Unzipping of Nested Dataset using os 

### Section 1 - Pickling of Data
1.1 : Creating 2-Pickles for alcohol and control 

1.2 : Creating Pickles for every recording
### Section 2 - Data Visualization
2.1 : Understanding the data (Selected one alcohol and control recording) 

2.11 : Grouped random channel 'FT7' on the basis of stimulus and plotted 

2.12 : Grouped random channel 'FT7' on the basis of alcohol and control and plotted 

2.13 : Grouped random channel 'FT7' on the basis of stimulus and plotted mean on scatter plot 

2.14 : Grouped all channels on the basic of stimulus and plotted mean on scatter plot 

2.15 : Grouped all channels on the basic of alcohol and control and plotted mean 

2.16 : Grouped all channels on the basic of alcohol and control and plotted mean on Histogram 

2.17 : Grouped all channels on the basic of alcohol and control and plotted Empirical Cumulative Distribution Function (ECDF)

2.2 : Data Visualization (All alcohol and control recording)
2.21 : Grouped all channels on the basic of alcohol and control and plotted mean 

2.22 : Grouped all channels on the basic of alcohol and control and plotted Heatmaps 

2.23 : Grouped all channels on the basic of stimulus and plotted Heatmaps 

2.31 : Grouped all channels on the basic of alcohol and control and plotted ECDF 

2.32 : Grouped all channels on the basic of stimulus and plotted ECDF
### Section 3 -Correlations


3.11 : Cross-Correlations across different channels grouped by stimulus in a recording

3.12 : Plotted Correlations using networkx 

3.12 : Observing and Ploting Highest Cross-Correlation Pairs across different channels in every alcohol recording for S1 obj 

3.13 : Observing and Ploting Highest Cross-Correlation Pairs across different channels in every alcohol recording for S1 match 

3.14 : Observing and Ploting Highest Cross-Correlation Pairs across different channels in every alcohol recording for S1 nomatch

3.21 : Observing and Ploting Highest Cross-Correlation Pairs across different channels in every control recording for S1 obj 

3.22 : Observing and Ploting Highest Cross-Correlation Pairs across different channels in every control recording for S1 match 

3.23 : Observing and Ploting Highest Cross-Correlation Pairs across different channels in every control recording for S1 nomatch 

3.3 : Observing that Y and nd is most Correlated

### Section 4 - Hypothesis Testing
4 : Hypothesis Testing 

4.1 : Restructuring Dataset to accommodate mean, std and number of observations 

4.2 : Defining and calculating Hypothesis 

4.21 : Hypothesis testing across S1 obj and Analyzing the results 

4.22 : Hypothesis testing across S1 match and Analyzing the results 

4.23 : Hypothesis testing across S1 nomatch and Analyzing the results 

4.3 : Common accpeted and rejected channels after Hypothesis Test of all 122 recordings 

4.41 : Correlation between stimulus of Alcohol 

4.42 : Correlation between stimulus of Control 

4.43 : Correlation between S1 obj 

4.44 : Correlation between s2 match 

4.45 : Correlation between s2 nomatch
