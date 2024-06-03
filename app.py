import streamlit as st
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt

df = pd.read_csv('/Racqso/sd-project/coffee.csv')

# renaming columns
df=df.rename(
    columns={
        'Location.Country':'country',
        'Location.Region':'region',
        'Location.Altitude.Min':'altitude_min',
        'Location.Altitude.Max':'altitude_max',
        'Location.Altitude.Average':'altitude_avrg',
        'Year':'year',
        'Data.Owner':'owner',
        'Data.Type.Species':'species',
        'Data.Type.Variety':'variety',
        'Data.Type.Processing method':'processing_method',
        'Data.Production.Number of bags':'number_bags',
        'Data.Production.Bag weight':'bag_weight',
        'Data.Scores.Aroma':'aroma',
        'Data.Scores.Flavor':'flavor',
        'Data.Scores.Aftertaste':'aftertaste',
        'Data.Scores.Acidity':'acidity',
        'Data.Scores.Body':'body',
        'Data.Scores.Balance':'balance',
        'Data.Scores.Uniformity':'uniformity',
        'Data.Scores.Sweetness':'sweetness',
        'Data.Scores.Moisture':'moisture',
        'Data.Scores.Total':'total_score',
        'Data.Color':'color'
    }
)  

#create header using streamlit
st.title('Top Coffee From Around the World')
st.header('According to the scores from coffee.csv file')

# create scatter plots for use with checkbox
fig1 = px.scatter(df, x="country", y="total_score", title='Coffee total scores based on country', symbol='species')

df_update = df.drop(df.index[df['total_score'] == 0])

fig2 = px.scatter(df_update, x="country", y="total_score", title='Coffee total scores based on country', symbol='species')

# create pre-selected checkbox
check = st.checkbox('Uncheck to see outlier (row 985 -- Honduras zero-value total_score)', value=True)
if check:
    st.write(fig2)
else:
    st.write(fig1)

st.subheader('Top 10 individual sample scores')
top_values = df['total_score'].sort_values(ascending=False).head(10)
st.write(top_values)

st.text('The highest score was:')
max_total_score = df['total_score'].max()
st.write(max_total_score)

st.text('which corresponds to the following row')
highest_total_scores = df_update[df_update['total_score'] > 90]
st.write(highest_total_scores)

st.text('Can see above that an Ethiopian coffee scored the highest individual score (the only one above 90). Next we want to see which country scored the highest overall average total_score, but we will first narrow down to the top 5 countries with the most entries so as to have better representative scores.')

st.text('The top five countries with the highest sample sizes (count):')

#number of entries per country
country_total_score_count = df.groupby('country')['total_score'].count() 

#to see more statistically significant data with larger number of samples
mean_count = country_total_score_count.sort_values().tail(5) 
#will focus on top 5 countries with largest samples
st.write(mean_count)

sizes = [61, 65, 128, 168, 201]
labels = ['Brazil','United States', 'Colombia','Guatemala','Mexico']
explode = (0, 0, 0, 0, 0.05)

pie0, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

st.pyplot(pie0)

st.subheader('Mean values for top 5 sampled countries', divider='blue') 

brazil_filt = df['country'] == 'Brazil'
us_filt = df['country'] == 'United States'
col_filt = df['country'] == 'Colombia'
guat_filt = df['country'] == 'Guatemala'
mexi_filt = df['country'] == 'Mexico'

st.text('Brazil')
brazil_filt_mean = df[brazil_filt].mean(axis=0, numeric_only=True)
st.write(brazil_filt_mean)
print()
st.text('USA')
us_filt_mean = df[us_filt].mean(axis=0, numeric_only=True)
st.write(us_filt_mean)
print()
st.text('Colombia')
col_filt_mean = df[col_filt].mean(axis=0, numeric_only=True)
st.write(col_filt_mean)
print()
st.text('Guatemala')
guat_filt_mean = df[guat_filt].mean(axis=0, numeric_only=True)
st.write(guat_filt_mean)
print()
st.text('Mexico')
mexi_filt_mean = df[mexi_filt].mean(axis=0, numeric_only=True)
st.write(mexi_filt_mean)

# create dataframe with characteristic information of top 5 countries with highest number of samples (rounding score to 100th decimal place)
data = {
        'country': ['Brazil', 'United States', 'Colombia', 'Guatemala', 'Mexico'],
        'aroma': [7.68, 7.57, 7.67, 7.55, 7.46],
        'flavor': [7.64, 7.6, 7.61, 7.49, 7.38],
        'acidity': [7.55, 7.62, 7.59, 7.6, 7.42],
        'body': [7.57, 7.65, 7.63, 7.47, 7.38],
        'balance': [7.56, 7.65, 7.68, 7.47, 7.32],
        'sweetness': [9.99, 9.58, 9.96, 9.86, 9.97],
        'moisture': [0.1, 0.06, 0.06, 0.1, 0.12],
        'total_score': [82.95, 81.86, 83.19, 81.83, 80.84],
        'altitude_min': [713.33, 339.69, 1217.41, 3501.26, 1220.53],
        'altitude_max': [727.26, 339.69, 1318.19, 3514.02, 1226.25],
        'altitude_avrg': [720.3, 339.69, 1267.8, 3507.64, 1223.39]
       }

means_df = pd.DataFrame(data)

#create header using streamlit
st.subheader('Total score by country', divider='blue')
# create a plotly histogram figure
fig00 = px.histogram(means_df, x='country', y='total_score')
# display the figure with streamlit
st.write(fig00)

#create header using streamlit
st.subheader('Coffee sweetness by country and total score', divider='blue')
# create a plotly histogram figure
fig0 = px.histogram(means_df, x='total_score', y='country', color='sweetness')
# display the figure with streamlit

fig01 = px.histogram(df_update, x='total_score', y='country', color='sweetness')
# display the figure with streamlit

check = st.checkbox('Check to see only top 5 sample countries)', value=False)
if check:
    st.write(fig0)
else:
    st.write(fig01)

st.text('Can see the top 5 countries with the largest sample sizes simply based on the sum of sweetness scores, while also seeing the ratio of particular scores per country.')

#create header using streamlit
st.subheader('Coffee scores by total score and aroma', divider='blue') 
# create a plotly scatterplot
fig = px.scatter(means_df, x='total_score', y='aroma', color='country')
# display the figure with streamlit
 
# create a plotly scatterplot
fig02 = px.scatter(df_update, x='total_score', y='aroma', color='country')
# display the figure with streamlit

check = st.checkbox('Check to see only top 5 sample countries', value=False)
if check:
    st.write(fig)
else:
    st.write(fig02)

st.subheader('Comparison of coffee growing altitudes', divider='blue')
pd.options.plotting.backend = "plotly"
fig10 = means_df.plot(x='country', y=['altitude_max', 'altitude_min', 'altitude_avrg'])
st.write(fig10)

st.subheader('Comparison of main coffee characteristics', divider='blue') 
# create line graphs for coffee character between countries
pd.options.plotting.backend = "plotly"
fig11 = means_df.plot(x='country', y=['aroma', 'flavor', 'balance', 'acidity'])
st.write(fig11)

st.text('When comparing altitude and character, as demonstrated in the two graphs above, there does not seem to be a direct correlation between altitude and improved or worsened character.')

st.text('Conclusion: From the above information, we see and can conclude that the highest rated coffee entry was from Ethiopia, but if we look only at the top 5 entries with the most recorded samples (i.e. Brazil, United States, Colombia, Guatemala, and Mexico) we see that amongst them, the country with the highest average total score was Colombia.')
