import streamlit as st

st.header ("Project: Residence Design")
st.write("____")
st.write (' ')
st. write ('''The project aims to combine contemporary aesthetics with functional living spaces, ensuring comfort for the family. The layout emphasizes natural light, cross-ventilation, and a  flow between indoor and outdoor areas. The design reflects the homeowners' lifestyle, balancing privacy with communal spaces to provide a personalized and harmonious living experience.''')


#show images
profile= r"algo images/IMG_3215.jpg"
image_6= r'algo images/portfolio_6.png'
image_1= r'algo images/portfolio_1.png'
image_2= r'algo images/portfolio_2.png'
image_3= r'algo images/portfolio_3.png'
image_4= r'algo images/portfolio_4.png'
image_5= r'algo images/portfolio_5.png'
image_7= r'algo images/portfolio_7.png'
image_8= r'algo images/portfolio_8.png'
image_9= r'algo images/portfolio_9.png'
image_10= r'algo images/portfolio_10.png'
image_11= r'algo images/portfolio_11.png'


st.image(image_6)
st.write (' ')

st.markdown('<p style="font-size: 24px; font-weight: bold;">Form Generation</p>', unsafe_allow_html=True)
st.write("____")
st.image(image_1)
st.caption('''The form is generated keeping cross ventilation in mind. The waterbody helps in micro cooling''')
st.header (' ')


st.markdown('<p style="font-size: 24px; font-weight: bold;">Conceptual Diagrams</p>', unsafe_allow_html=True)
st.write("____")
im1,im2= st.columns([4,2])

with im1:
	st.image(image_2)
	st.caption('''Two main roads around the site and greenery on the south side. Introducing waterbody and greenery to reduce sound pollution and cooling down the micro environment.''')

with im2:
	st.image(image_3)

st.write (' ')
st.markdown('<p style="font-size: 24px; font-weight: bold;">Ground Floor Plan</p>', unsafe_allow_html=True)
st.write("____") 
st.image(image_5)
st.caption ('Scale 1:100')


st.markdown('<p style="font-size: 24px; font-weight: bold;">Visualization</p>', unsafe_allow_html=True)
st.write("____")
st.image(image_7)
st.caption('Exterior View')

st.image(image_8)
st.caption('Interior of the Living Room')

st.image(image_10)
st.caption('Interior of the Master Bedroom')

st.image(image_9)
st.caption('Sectional View')
