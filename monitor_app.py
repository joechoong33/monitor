import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import codecs
import streamlit.components.v1 as components
import datetime
#from streamlit import components
#from evidently.dashboard import Dashboard
#from evidently.tabs import DataDriftTab, NumTargetDriftTab
#from sklearn import datasets
#from evidently.model_profile import Profile
#from evidently.profile_sections import DataDriftProfileSection, NumTargetDriftProfileSection

st.set_page_config(page_title="Monitor Dashboard",layout='wide')
def main():
    html_temp1 = """<div style="background-color:red;padding:5px">
                            		<h1 style="color:white;text-align:center;">Model Monitoring Dashboard</h1>
                            		</div>
                            		</div>
                            		</br>"""
    st.markdown(html_temp1, unsafe_allow_html=True)

    menu = ["Summary And Performance Trend","Model Performance", "SHAP Plots", "Data And Target Drift"]
    choice = st.sidebar.selectbox("Menu", menu, 2)
    # for hide menu
    hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
    model_type = ['nb','all','almr','als','alc','aeg','tpa','apa','post','tws','ths','lady']
    models = st.sidebar.multiselect('Select Models', model_type)

    date1 = st.sidebar.date_input("Test date picker:", [datetime.date(2021, 7, 6)])

    st.sidebar.button('Test Button')

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.sidebar.title("About")
    st.sidebar.info(" **Dashboard** - Please give feedback on adding features that you think are useful")

    st.sidebar.markdown(
        """ Developed by DS Team    
        """)
    if choice == "Model Performance":
        # color codes  ff1a75  6D7B8D
        html_temp2 = """<div style="background-color:#98AFC7;padding:5px">
                                        		<h3 style="color:white;text-align:center;">Model Performance</h3>
                                        		</div>
                                        		<div>
                                        		</br>"""
        st.markdown(html_temp2, unsafe_allow_html=True)
        calc_file = codecs.open('cancer_performance.html','r')
        page = calc_file.read()
        #components.html(page,width=1000, height=1000,scrolling=True)
        col1, col2, col3 = st.beta_columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            components.html(page,width=1000, height=1000,scrolling=True)
        with col3:
            st.write("")

    elif choice == "SHAP Plots":
        html_temp3 = """
                        		<div style="background-color:#98AFC7;padding:5px">
                        		<h3 style="color:white;text-align:center;">SHAP PLOTS</h3>
                        		</div>
                        		<br></br>"""

        st.markdown(html_temp3, unsafe_allow_html=True)
        plot_type = ['bar','beeswarm','decision','heatmap','waterfall','force_plot']
        plots = st.multiselect('Select Plot Type:', plot_type)
        #st.subheader("Shap Plots Examples")
        st.write("Model Water Shap Plot")
        col1, col2, col3 = st.beta_columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            st.image('water.JPG')
        with col3:
            st.write("")
        
        st.write("Model Beeswarm Plot")
        col4, col5, col6 = st.beta_columns([1,6,1])
        with col4:
            st.write("")
        with col5:
            st.image('bee.JPG')
        with col6:
            st.write("   ")
        # st.write("Check similarity of Resume and Job Description")
    elif choice == "Data And Target Drift":
        html_temp4 = """
        <div style="background-color:#98AFC7;padding:5px">
        <h3 style="color:white;text-align:center;">Data And Target Drift</h3>
        </div>
        <br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)
        
        #boston = datasets.load_boston()
        #boston_frame = pd.DataFrame(boston.data, columns = boston.feature_names)
        #column_mapping = {}

        #column_mapping['target'] = 'target'
        #column_mapping['prediction'] = None
        #column_mapping['datetime'] = None

        #column_mapping['numerical_features'] = ['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX',
        #                               'PTRATIO', 'B', 'LSTAT']
        #column_mapping['categorical_features'] = ['CHAS', 'RAD']
        #boston_frame['target'] = boston.target
        #boston_data_and_target_drift_dashboard = Dashboard(tabs=[DataDriftTab, NumTargetDriftTab])
        #boston_data_and_target_drift_dashboard.calculate(boston_frame[:200], boston_frame[200:], 
        #                                           column_mapping = column_mapping)
        
        #boston_data_and_target_drift_dashboard.save('boston.html')
        
        calc_file = codecs.open('boston.html','r')
        page = calc_file.read()
        #components.html(page,width=1000, height=1000,scrolling=True)
        col1, col2, col3 = st.beta_columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            Feats = st.slider( label="No. Of Top Features", min_value=1, max_value=5, value=0, key="red")
            components.html(page,width=1000, height=1000,scrolling=True)
        with col3:
            st.write("")
        #components.iframe('C:/Users/Wai/streamlit-app/boston_data_and_target_drift_with_mapping.html')
        #st.html(html_string)

    elif choice == "Summary And Performance Trend":
        html_temp4 = """
        <div style="background-color:#98AFC7;padding:5px">
        <h3 style="color:white;text-align:center;">Summary And Performance Trend</h3>
        </div>
        <br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)
        #st.markdown("## Summary")
        kpi1, kpi2, kpi3 = st.beta_columns(3)

        with kpi1:
            text1 = 'AUC'
            st.markdown(f"<h2 style='text-align: left; color: black;'>{text1}</h2>", unsafe_allow_html=True)
            number1 = 0.81 
            st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

        with kpi2:
            text2 = 'K-S'
            st.markdown(f"<h2 style='text-align: left; color: black;'>{text2}</h2>", unsafe_allow_html=True)
            number2 = 0.65
            st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

        with kpi3:
            text3 = 'CAP'
            st.markdown(f"<h2 style='text-align: left; color: black;'>{text3}</h2>", unsafe_allow_html=True)
            number3 = 0.75 
            st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

        st.markdown("""---""")
        st.write("")
        #st.write("")
        st.write("")

        chart1, chart2 = st.beta_columns([2,1])
        with chart1:
            #st.write("AUC Min-Max Trend")
            text1 = "AUC Min-Max Trend Line"
            st.markdown(f"<h2 style='text-align: center; color: black;'>{text1}</h2>", unsafe_allow_html=True)
            maxa = pd.DataFrame(np.random.uniform(low=0.7, high=0.85, size=(15,2)),columns=['Max','Min'])
            mina = pd.DataFrame(np.random.uniform(low=0.1, high=0.15, size=(15,1)),columns=['Min'])
            maxa['Min'] = maxa['Max'] - mina['Min']

            st.area_chart(maxa)
            #plt.figure(figsize=(8,5))
            #plt.plot(chart_data)
            #st.pyplot(plt)

        with chart2:
            #st.write("Top 5 Data Drift")
            text2 = "Top 5 Data Drift"
            st.markdown(f"<h2 style='text-align: center; color:black;'>{text2}</h2>", unsafe_allow_html=True)
            names = ['feat1', 'feat2', 'feat3','feat4' ,'feat5']
            size = [12,11,3,15,20]
            #plt.figure(figsize=(1,1))
            my_circle = plt.Circle( (0,0), 0.7, color='white')
            plt.pie(size, radius = 1.0,labels=names,labeldistance=1.1, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow','lightgray'])
            #plt.title('Top 5 Data Drift')
            p = plt.gcf()
            p.gca().add_artist(my_circle)
            #plt.show()
            st.pyplot(plt)

        st.markdown("""---""")
        #st.write("")

        chart3, chart4, chart5 = st.beta_columns(3)

        with chart3:
            
            text1 = "Models AUC"
            st.markdown(f"<h3 style='text-align: center; color: black;'>{text1}</h3>", unsafe_allow_html=True)
            chart_data3 = pd.DataFrame(np.random.uniform(low=0.7, high=0.85, size=(1,12)),columns=['nb','all','almr','als','alc','aeg',
            'tpa','apa','post','tws','ths','lady'])
            st.bar_chart(chart_data3.T)

        with chart4:
            
            text1 = "Models KS"
            st.markdown(f"<h3 style='text-align: center; color: black;'>{text1}</h3>", unsafe_allow_html=True)
            chart_data4 = pd.DataFrame(np.random.uniform(low=0.6, high=0.8, size=(1,12)),columns=['nb','all','almr','als','alc','aeg',
            'tpa','apa','post','tws','ths','lady'])
            st.bar_chart(chart_data4.T)

        with chart5:
            
            text1 = "Models CAP"
            st.markdown(f"<h3 style='text-align: center; color: black;'>{text1}</h3>", unsafe_allow_html=True)
            chart_data5 = pd.DataFrame(np.random.uniform(low=0.6, high=0.8, size=(1,12)),columns=['nb','all','almr','als','alc','aeg',
            'tpa','apa','post','tws','ths','lady'])
            st.bar_chart(chart_data5.T)

    else:
        pass


if __name__ == "__main__":
    main()
