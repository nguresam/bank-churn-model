import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="⚡", page_title='CRA CHURN MODEL')

path = "./data/churn.csv"
st.sidebar.header('CRAG CHURN MODEL')
data = st.sidebar.file_uploader("Upload Dataset", type=['csv', 'txt', 'xlsx'])

if data is not None:
    df = pd.read_csv(data, encoding="ISO-8859-1", low_memory=False)
    df["AgeBin"] = pd.cut(df["Age"], 5)
    df["BalanceBin"] = pd.cut(df["Balance"], 5)
    df["CreditScoreBin"] = pd.cut(df["CreditScore"], 5)
    df["EstimatedSalaryBin"] = pd.cut(df["EstimatedSalary"], 5)
    #df[["AgeBin", "Exited"]].groupby(["AgeBin"], as_index=False).mean().sort_values(by="AgeBin", ascending=True)
    #df[["BalanceBin", "Exited"]].groupby(["BalanceBin"], as_index=False).mean().sort_values(by="BalanceBin",
    #                                                                                        ascending=True)
    #df[["EstimatedSalaryBin", "Exited"]].groupby(["EstimatedSalaryBin"], as_index=False).mean().sort_values(
    #    by="EstimatedSalaryBin", ascending=True)
    #df[["CreditScoreBin", "Exited"]].groupby(["CreditScoreBin"], as_index=False).mean().sort_values(by="CreditScoreBin",
    #                                                                                                ascending=True)
# Default Dataset if none is uploaded.
else:
    df = pd.read_csv(path, encoding="ISO-8859-1", low_memory=False)
    df["AgeBin"] = pd.cut(df["Age"], 5)
    df["BalanceBin"] = pd.cut(df["Balance"], 5)
    df["CreditScoreBin"] = pd.cut(df["CreditScore"], 5)
    df["EstimatedSalaryBin"] = pd.cut(df["EstimatedSalary"], 5)
    #df[["AgeBin", "Exited"]].groupby(["AgeBin"], as_index=False).mean().sort_values(by="AgeBin", ascending=True)
    #df[["BalanceBin", "Exited"]].groupby(["BalanceBin"], as_index=False).mean().sort_values(by="BalanceBin",
    #                                                                                        ascending=True)
    #df[["EstimatedSalaryBin", "Exited"]].groupby(["EstimatedSalaryBin"], as_index=False).mean().sort_values(
    #    by="EstimatedSalaryBin", ascending=True)
    #df[["CreditScoreBin", "Exited"]].groupby(["CreditScoreBin"], as_index=False).mean().sort_values(by="CreditScoreBin",
    #                                                                                             ascending=True)


menu = ['Business Snapshot', 'Analysis', 'About']
selection = st.sidebar.selectbox("Key Performance Indicator (KPI) ", menu)

st.sidebar.write('''Churn analysis may be summed up as all analytical research on “a customer,” “a product or service,” and “the probability of abandonment.” Before the customer leaves us or is about to leave, our aim is to become aware of this scenario (even though the person may not be aware of this situation himself) and then to take some preventive action.''')

churn = df.loc[df["Exited"]==1]
not_churn = df.loc[df["Exited"]==0]

if selection == 'Business Snapshot':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Use the full page instead of a narrow central column
    # st.set_page_config(layout="wide")
    st.subheader('Data Summary')
    st.dataframe(df.head())

    #col1, col2 = st.columns(2)

    # Column1
    #with col1:
        # Monthly revenue

    df.hist(figsize=(20, 20))
    st.pyplot()

    #st.set_option('deprecation.showPyplotGlobalUse', False)
    #plt.figure(figsize=(15, 10))
    #plt.xlabel('CreditScore')
    #plt.hist(not_churn["CreditScore"], bins=15, alpha=0.7, label='Not Churn')
    #plt.legend(loc='upper right')
    #st.pyplot()

elif selection == 'Analysis':
    st.subheader('Data Distribution Against Dependant Variable')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig, axarr = plt.subplots(2, 2, figsize=(20, 12))
    sns.countplot(x='EstimatedSalary', hue='Exited', data=df, ax=axarr[0][0])
    sns.countplot(x='NumOfProducts', hue='Exited', data=df, ax=axarr[0][1])
    sns.countplot(x='HasCrCard', hue='Exited', data=df, ax=axarr[1][0])
    sns.countplot(x='IsActiveMember', hue='Exited', data=df, ax=axarr[1][1]);
    st.pyplot(fig)

# adding html  Template
footer_temp = """
<!-- CSS  -->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" 
type="text/css" rel="stylesheet" media="screen,projection"/>
<link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" 
integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
<footer class="page-footer grey darken-4">
<div class="container" id="aboutapp">
<div class="row">
<div class="col l6 s12">
<h5 class="white-text">Banking Churn Model</h5>
<h6 class="grey-text text-lighten-4">This is a Banking Churn Model.</h6>
<p class="grey-text text-lighten-4">2023 Cohort</p>
</div>
<div class="col l3 s12">
<h5 class="white-text">Connect With Us</h5>
<ul>
<a href="https://www.facebook.com/AfricaDataSchool/" target="_blank" class="white-text">
<i class="fab fa-facebook fa-4x"></i>
</a>
<a href="https://www.linkedin.com/company/africa-data-school" target="_blank" class="white-text">
<i class="fab fa-linkedin fa-4x"></i>
</a>
<a href="https://www.youtube.com/watch?v=ZRdlQwNTJ7o" target="_blank" class="white-text">
<i class="fab fa-youtube-square fa-4x"></i>
</a>
<a href="https://github.com/Africa-Data-School" target="_blank" class="white-text">
<i class="fab fa-github-square fa-4x"></i>
</a>
</ul>
</div>
</div>
</div>
<div class="footer-copyright">
<div class="container">
Made by <a class="white-text text-lighten-3" href="https://africadataschool.com/">Sammy Ngure</a><br/>
<a class="white-text text-lighten-3" href="https://africadataschool.com/"></a>
</div>
</div>
</footer>
"""

if selection == 'About':
    st.header("About App")
    components.html(footer_temp, height=500)
