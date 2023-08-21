import streamlit as st
import numpy as np
import seaborn as sn
import joblib
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas

st.set_page_config(
    layout="centered"
)
test, training = st.tabs(['Try it', 'Training'])

st.sidebar.title("Moreen-Ai")
flat_array = [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
]
model = joblib.load('./pages/digit_reader/LogisticRegression')

with test:
    col1, col2 = st.columns(2)
    
    with col1:
        st.title("Write something")
        canvas_width, canvas_height = 304, 304
        grid_size = 8
        cell_size = canvas_width // grid_size

        st.write("Draw here:")
        canvas = st_canvas(
            fill_color="white",
            stroke_color="black",
            stroke_width=1.5 * cell_size,
            height=canvas_height,
            width=canvas_width,
            drawing_mode="freedraw",
        )

        if canvas.image_data is not None:
            # Convert the image data to grayscale
            grayscale_image = canvas.image_data.mean(axis=2)

            # Reshape the grayscale image into an 8x8 grid
            grid = grayscale_image.reshape(grid_size, cell_size, grid_size, cell_size).mean(axis=(1, 3))

            # Scale the values to range from 0 to 16
            min_value = np.min(grid)
            max_value = np.max(grid)
            scaled_grid = 16 * (grid - min_value) / (max_value - min_value)

            # Extract the values as a single-dimensional array
            flat_array = scaled_grid.flatten()    
    with col2:
        has_na = np.isnan(flat_array).any()
        if not has_na:
            st.write("<h1 style='font-size:400px;'>{}</h1>".format(model.predict([flat_array])[0]), unsafe_allow_html=True)
      
    if not has_na:
        st.table(model.predict_proba([flat_array]))
        
with training:
    st.title("Models' perfomance and metrices")
    st.write("#### The models' score is {}%".format(100))
    cm = [[178,   0,   0,   0,   0,   0,   0,   0,   0,   0],
       [  0, 182,   0,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0, 177,   0,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0, 183,   0,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0, 181,   0,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0, 182,   0,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0, 181,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0, 179,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0, 174,   0],
       [  0,   0,   0,   0,   0,   0,   0,   0,   0, 180]]
    fig = plt.figure()
    chart = sn.heatmap(cm, annot=True, fmt='.0f')
    plt.xlabel("Predicted")
    plt.ylabel("Truth")
    st.pyplot(fig)