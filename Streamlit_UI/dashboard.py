import streamlit as st
import plotly.express as px

def app():

    st.subheader("💡 Ideation:")

    inspiration = '''
    Enhancing Image Authenticity Verification through Deep Learning Techniques: A Study on the Detection and Mitigation of Fake Images
    '''

    st.subheader("👨🏻‍💻 Abstract")

    what_it_does = '''
    This study addresses the urgent need for an advanced image authenticity verification system in journalism and content curation. It proposes a comprehensive solution that leverages deep learning
    techniques, specifically convolutional neural networks, and generative adversarial networks, to enhance image authenticity verification. By drawing insights from seminal works in the field, this research aims to combat the proliferation of fake images, ultimately contributing to the preservation of credibility and trustworthiness in media content dissemination.'''

    st.markdown(what_it_does, unsafe_allow_html=True)

    stats, buff, graph = st.columns([2, 0.5, 2])

    stats.subheader("🧠 ML Process")

    stats.markdown("<h5> 📊 Getting the Data and EDA Process </h5>", unsafe_allow_html=True)

    stats.markdown("*The dataset was taken from Kaggle and you can find it [here](https://www.kaggle.com/hamzaboulahia/hardfakevsrealfaces).*")

    stats.markdown('''The Dataset contains 1288 faces out of which
    <li> 589 are Real </li> 
    <li> 700 are Fake </li>
    ''', unsafe_allow_html=True) 

    fig = px.bar(x=['Real', 'Fake'], y=[589, 700], height=400)
    graph.plotly_chart(fig, use_container_width=True)

    st.write('The "fake" faces collected in this dataset are generated using the StyleGAN2, which present a harder challenge to classify them correctly even for the human eye.')

    st.image('./Streamlit_UI/faces_1.png', use_column_width=True)
    st.image('./Streamlit_UI/faces_2.png', use_column_width=True)

    st.subheader("⚙️ Model Architecture")

    st.image('./Streamlit_UI/model.png', use_column_width=True)

    ml_process = f'''
- We designed a Sequential Model having 5 Convolutional Layers and 4 Dense Layers.
- The first layer started with 32 filters and kernel of 2x2.
- The number of filters are doubled at every next layer and kernel is is incremented by 1.
- We introduced some Max Pooling Layers after Convolutional Layers to avoid over-fitting and reduce Computational Costs.
- We used ReLU activation in all layers except output layer to reduce computation cost and introduce non-linearity.
- Finally, the Output Layer contained 2 neurons (1 for each class) and softmax activation.
'''
    st.write(ml_process)

    results = f'''
    - The model with least Validation Loss was saved during the training and reloaded before obtaining the final results.
    - The model was able to classify all of the samples correctly.
    '''
    loss, buff, acc = st.columns([2, 0.4, 2])

    loss.image('./Streamlit_UI/loss.png', use_column_width=True)
    acc.image('./Streamlit_UI/accuracy.png', use_column_width=True)

    st.subheader("📈 Evaluation")
    st.markdown(results, unsafe_allow_html=True)

    st.write("Classification Report:")
    
    cfr = '''
 Report Title     precision    recall  f1-score   support

        Real       1.00      1.00      1.00        59
        Fake       1.00      1.00      1.00        70

    accuracy                           1.00       129
   macro avg       1.00      1.00      1.00       129
weighted avg       1.00      1.00      1.00       129
'''
    st.code(cfr)

    st.write(" ")

    
