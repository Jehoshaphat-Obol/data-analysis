# import all the dependecies
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import pickle
import json

from pages.housing_price_prediction.components.Layout import Layout
st.set_page_config(
    page_icon="📊",
    layout='wide'
)
root = "./pages/housing_price_prediction"

# load the required data
@st.cache_data
def load_data():
    dataframe = pd.read_csv('./pages/housing_price_prediction/dataset/Housing.csv')
    return dataframe

dataframe = load_data()

# Design the sidebar
st.sidebar.title("Moreen-Ai")

charts, predictions = st.tabs(['📉Charts', '✨ Predictions'])

with charts:
    # data management
    bedrooms = st.sidebar.multiselect(
        "Number of Bedrooms",
        options=dataframe['bedrooms'].unique(),
        default=dataframe['bedrooms'].unique()
    )

    bathrooms = st.sidebar.multiselect(
        "Number of Bathrooms",
        options=dataframe['bathrooms'].unique(),
        default=dataframe['bathrooms'].unique()
    )

    stories = st.sidebar.multiselect(
        "Number of stories",
        options=dataframe['stories'].unique(),
        default=dataframe['stories'].unique()
    )

    mainroad = st.sidebar.multiselect(
        "Near the mainroad",
        options=dataframe['mainroad'].unique(),
        default=dataframe['mainroad'].unique()
    )

    guestroom = st.sidebar.multiselect(
        "Has a guest room",
        options=dataframe['guestroom'].unique(),
        default=dataframe['guestroom'].unique()
    )

    basement = st.sidebar.multiselect(
        "Has a basement",
        options=dataframe['basement'].unique(),
        default=dataframe['basement'].unique()
    )

    hotwaterheating = st.sidebar.multiselect(
        "Has Hot-water heating",
        options=dataframe['hotwaterheating'].unique(),
        default=dataframe['hotwaterheating'].unique()
    )

    airconditioning = st.sidebar.multiselect(
        "Has air conditioning system ",
        options=dataframe['airconditioning'].unique(),
        default=dataframe['airconditioning'].unique()
    )

    parking = st.sidebar.multiselect(
        "Has parking area",
        options=dataframe['parking'].unique(),
        default=dataframe['parking'].unique()
    )

    prefarea = st.sidebar.multiselect(
        "Is a prefered areae",
        options=dataframe['prefarea'].unique(),
        default=dataframe['prefarea'].unique()
    )

    furnishingstatus = st.sidebar.multiselect(
        "Furnishing Status",
        options=dataframe['furnishingstatus'].unique(),
        default=dataframe['furnishingstatus'].unique()
    )


    # query the data
    df_selections = dataframe.query(
        "bedrooms == @bedrooms & bathrooms == @bathrooms & stories == @stories & mainroad == @mainroad & guestroom == @guestroom & basement == @basement & hotwaterheating == @hotwaterheating & airconditioning == @airconditioning & parking == @parking & prefarea == @prefarea & furnishingstatus == @furnishingstatus"
    )


    # Design the main page
    title = "Housing Price Analytics"
    introduction = '''
    **Dataset source:** [kaggle.com](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction) 

    '''

    image = ""
    description=""

    # Insights
    total_houses = len(df_selections)
    average_price = df_selections['price'].mean()
    average__area = df_selections['area'].mean()

    min_cost = df_selections['price'].min()
    max_const = df_selections['price'].max()

    layout = Layout(title, introduction, image, description)
    layout.render()


    # Insights
    total_houses = len(df_selections)

    if(len(df_selections != 0)):
        average_price = df_selections['price'].mean().round()
        average_area = df_selections['area'].mean().round()

    else:
        average_area = 0
        average_price = 0

    # first row in the ui
    left1, middle1, right1 = st.columns(3)

    with left1:
        st.subheader('Houses Found')
        st.subheader('{}'.format(total_houses))

    with middle1:
        st.subheader('Average area(sq. feet)')
        st.subheader('{} USD'.format(average_area))
    with right1:
        st.subheader('Average Price (USD)')
        st.subheader(average_price)

    # first rowset    
    row1col1, row1col2,row1col3, row1col4 = st.columns((1,1,1,2))
    with row1col1:
        mainroad_df = df_selections.groupby('mainroad')['mainroad'].count().reset_index(name='count')
        fig1 = px.pie(mainroad_df, values='count', names='mainroad', title='Mainroad Distribution')
        st.plotly_chart(fig1, use_container_width=True)

    with row1col2:
        guestroom_df = df_selections.groupby('guestroom')['guestroom'].count().reset_index(name='count')
        fig2 = px.pie(guestroom_df, values='count', names='guestroom', title='Guestroom Distribution')
        st.plotly_chart(fig2, use_container_width=True)

    with row1col3:
        basement_df = df_selections.groupby('basement')['basement'].count().reset_index(name='count')
        fig3 = px.pie(basement_df, values='count', names='basement', title='basement Distribution')
        st.plotly_chart(fig3, use_container_width=True)

    with row1col4:
        with open("./animations/animation_ll5nx88j.json", 'r') as file:
            animation1 = json.load(file)
        st_lottie(
            animation1,
            width=360
        )
    # second rowse""t 
    row2col1, row2col2, row2col3= st.columns((2, 1, 1))
    with row2col1:
        st.dataframe(df_selections)

    with row2col2:
        airconditioning_df = df_selections.groupby('airconditioning')['airconditioning'].count().reset_index(name='count')
        fig5 = px.pie(airconditioning_df, values='count', names='airconditioning', title='Airconditioning Distribution')
        st.plotly_chart(fig5, use_container_width=True)

    with row2col3:
        hotwaterheating_df = df_selections.groupby('hotwaterheating')['hotwaterheating'].count().reset_index(name='count')
        fig4 = px.pie(hotwaterheating_df, values='count', names='hotwaterheating', title='Hot-water heating Distribution')
        st.plotly_chart(fig4, use_container_width=True)

    # third rowse""t 
    row3col1, row3col2, row3col3= st.columns((1, 1, 2))
    with row3col1:
        prefarea_df = df_selections.groupby('prefarea')['prefarea'].count().reset_index(name='count')
        fig6 = px.pie(prefarea_df, values='count', names='prefarea', title='prefarea Distribution')
        st.plotly_chart(fig6, use_container_width=True)

    with row3col2:
        bedrooms_df = df_selections.groupby('bedrooms')['bedrooms'].count().reset_index(name='count')
        fig7 = px.pie(bedrooms_df, values='bedrooms', names='bedrooms', title='Bedrooms Distributions')
        st.plotly_chart(fig7, use_container_width=True)

    with row3col3:
        stories_df = df_selections.groupby('stories')['stories'].count().reset_index(name='count')
        fig8 = px.bar(stories_df, y='stories', x='count', orientation='h', title='stories Distributions')
        st.plotly_chart(fig8, use_container_width=True)


with predictions:
    st.title('House Price Prediction, with Decision Tree Regressor')
    st.success('Fill in the forms below to get the price eastimation of your dream home')
    
    inpcol1, inpcol2, inpcol3, inpcol4, inpcol5  = st.columns(5)    
    with inpcol1:
        bedrooms_input = st.slider("Bedrooms", min_value=1, max_value=6, value=3)
        
    with inpcol2:
        bathrooms_input = st.slider("Bathrooms", min_value=1, max_value=4, value=1)
        
    with inpcol3:
        stories_input = st.slider("Stories", min_value=1, max_value=4, value=2)
     
    with inpcol4:
        parking_input = st.slider("Parking", min_value=1, max_value=6, value=3)
        
    with inpcol5:
        furnishingstatus_input = st.selectbox('Furnishing Status',dataframe.furnishingstatus.unique())
        
    check1, check2,check3,check4,check5, check6 = st.columns(6)
    with check1:
        mainroad_input = st.checkbox("Mainroad", value=True)
    with check2:
        guestroom_input = st.checkbox('Guestroom', value=True)
    with check3:
        basement_input = st.checkbox('Basement', value=True)
    with check4:
        hotwaterheating_input = st.checkbox('Hot water Heating', value=True)
    with check5:
        airconditioning_input = st.checkbox('Air Conditioning', value=True)
    with check6:
        prefarea_input = st.checkbox('Prefered Area', value=True)
        
    
    # process the user input
    if mainroad_input:
        mainroad_input = 1
    else:
        mainroad_input = 0
        
    if guestroom_input:
        guestroom_input = 1
    else:
        guestroom_input = 0
        
    if basement_input:
        basement_input = 1
    else:
        basement_input = 0
    
    if hotwaterheating_input:
        hotwaterheating_input = 1
    else:
        hotwaterheating_input = 0
    
    if airconditioning_input:
        airconditioning_input = 1
    else:
        airconditioning_input = 0
    
    if prefarea_input:
        prefarea_input = 1
    else:
        prefarea_input = 0
        
    if furnishingstatus_input == 'furnished':
        furnishingstatus_input = 0
    elif furnishingstatus_input == 'semi-furnished':
        furnishingstatus_input = 1
    elif furnishingstatus_input == 'unfurnished':
        furnishingstatus_input = 2
        

    with open('{}/DecisionTreeRegressor'.format(root), 'rb') as file:
        model = pickle.load(file)
    
    prediction = model.predict([[furnishingstatus_input,parking_input, bedrooms_input,stories_input,bathrooms_input, mainroad_input, guestroom_input, basement_input,hotwaterheating_input, prefarea_input,airconditioning_input]])
    
    pred1, pred2 = st.columns(2)
    
    with pred1:
        with open('./animations/cool.json', 'r') as file:
            animation2 = json.load(file)
            
            st_lottie(
                animation2,
                width=360
            )
    
    with pred2:
        st.header('Predicted House Value')
        st.header('{:,} USD'.format(prediction[0]))
            