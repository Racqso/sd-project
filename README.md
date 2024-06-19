# sd-project
TripleTen Sprint 6 - Software Development project
This project is meant to provide a tool that will convert coffee ratings to easy-to-understand, interactive graphs for quick visual reference.

csv file sourced from https://corgis-edu.github.io/corgis/csv/coffee/

Libraries and methods used:
pandas as pd
numpy as np
plotly.express as px
streamlit as st
matplotlib.pyplot as plt

st.title()
st.header()
st.subheader()
st.text()
st.write()
st.checkbox()
groupby()
count()
sort_values()
tail()
drop()
px.scatter()
px.histogram()

This tool can be launched through the Render link: https://sd-project-626d.onrender.com.

To run the code on your local machine, you will need to:
Clone or download source code from GitHub. You can download it directly from GitHub, or use a tool like Git Bash.
Steps for downloading through Git Bash:
1. Install git onto your machine if you do not already have it (and any other programs that are in the requirements.txt document).
2. Open your terminal or command prompt.
3. Navigate to the directory where you want to download the repository using the 'cd' command to navigate to the specific directory.
4. Clone the repository using the 'git clone' command followed by the URL of the GitHub repository (in this case: https://github.com/Racqso/sd-project.git).
5. Execute the source code by runnning the command 'streamlit run app.py' (if there are issues running it on your local machine, you may need to move the app.py document to be nested under the .streamlit directory).
