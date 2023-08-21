import streamlit as st
import joblib

st.set_page_config(
    layout="centered"
)
root = "./pages/iris_flower_classifier/"
st.sidebar.title("Moreen-AI")
st.title('Iris Flower Classifier')

test, about = st.tabs(['Test it','About Iris Flowers'])
model = joblib.load('./pages/iris_flower_classifier/LogisticRegression')
with test:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        sl = st.slider('Sepal Length (cm)', min_value=4.3, max_value=7.9, value=5.8, step=0.1)
    with col2:
        sw = st.slider('Sepal Width (cm)', min_value=2.0, max_value=4.4, value=3.0, step=0.1)
    with col3:
        pl = st.slider('Petal Length (cm)', min_value=1.0, max_value=6.9, value=3.8, step=0.1)
    with col4:
        pw = st.slider('Petal Width (cm)', min_value=0.1, max_value=2.5, value=1.2, step=0.1)

    target = model.predict([[sl,sw,pl,pw]])[0]
    
    if target == 0:
        image = "{}iris_setosa.jpg".format(root)
        descr = '''
        ## Iris Setosa
        
**Description:** Iris setosa is a species of iris flower known for its distinctive appearance. It has relatively small and delicate flowers with sepals and petals that are usually white, but they can also have shades of pink or lavender. The flowers have a prominent yellow or orange spot at the base of each petal, which serves as a guide for pollinators. Iris setosa is well-adapted to cold climates and can be found in various habitats, including wetlands and rocky slopes.
        '''
    elif target == 1:
        image = "{}iris_versicolor.jpg".format(root)
        descr = '''
        ## Iris Versicolor
        
**Description:** Iris versicolor, often referred to as the blue flag iris, is a medium-sized iris species with a wide distribution across North America. It typically has blue to purple petals with intricate patterns of darker veins. The flowers are larger than those of Iris setosa and have a distinct yellow or white patch on the falls. Iris versicolor prefers moist habitats such as marshes, swamps, and the edges of lakes and streams.
        '''
    elif target == 2:
        image = "{}iris_virginica.jpg".format(root)
        descr = '''
        ## Iris Virginica
        
**Description:** Iris virginica, also known as the Southern blue flag, is another iris species found in North America. It has larger flowers compared to the other iris species, with a range of colors including purple, blue, and sometimes white. The petals of Iris virginica are often marked with dark purple or brown veins. This species thrives in wetland environments and can be found in swamps, wet meadows, and along the shores of ponds and rivers.
        '''
        
    col5, col6 = st.columns(2)
    with col5:
        st.image(image, use_column_width=True)
    with col6:
        st.write(descr)
        
with about:
    page1 = '''
    # Iris Flower and Dataset Documentation

Welcome to the Iris Flower and Dataset Documentation section of our app! In this section, you'll learn about the fascinating Iris flower and the well-known Iris dataset used for machine learning.

## Iris Flower
'''

    st.write(page1)
    
    col7, col8 = st.columns(2)
    with col7:
        st.write('''                 
                ### Overview
                The Iris flower is a genus of flowering plants that encompasses a diverse range of species. These flowers are renowned for their vibrant colors, unique patterns, and ecological significance. Irises are found in various regions around the world and hold cultural and horticultural importance.

                ### Characteristics
                Irises typically have long, narrow leaves and large, showy flowers. The flowers consist of six petal-like segments: three upright petals called "standards" and three drooping petals called "falls." Irises come in a variety of colors, including shades of blue, purple, white, and yellow.
                 ''')
    with col8:
        st.image("{}iris.jpg".format(root), caption="Iris Flower")

    page2 = '''
## Iris Dataset

### Overview
The Iris dataset is a classic dataset frequently used for machine learning and data analysis. It contains measurements of various features of three different species of Iris flowers: Setosa, Versicolor, and Virginica. The dataset serves as a benchmark for testing algorithms and exploring classification techniques.

### Features
The dataset includes the following four features for each iris flower:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes
There are three target classes corresponding to the Iris species:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

'''
    st.write(page2)

    st.image("{}iris_species.png".format(root), use_column_width=True, caption="Iris Flower Species")

    page3 ='''
### Video Introduction

You can also watch a video introduction to the Iris dataset and its significance:

'''
    st.write(page3)
    st.video("https://youtu.be/5dLG3JDk2VU")

    page4 = '''
## Conclusion

We hope this documentation has provided you with a better understanding of the captivating Iris flower and the informative Iris dataset. Feel free to explore our app's features and try out the classification functionality using the provided input fields.

Happy exploring!
    '''
    st.write(page4)