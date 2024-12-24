import streamlit as st

st.title ("Architectural Portfolio")
st.write("____")

st.header ("Nawrin Ahmed")

qr= r"algo images/qr.png"
qr1, qr2=st.columns([5,1])

with qr1:
	st.write('''I am a dedicated art and architecture enthusiast skilled in all facets of architectural work. My skills include drafting, model making, and proficiency in 3D softwares and rendering. I have actively participated in workshops, social initiatives, and club activities, where I demonstrated exceptional teamwork and leadership abilities, with opportunities to win various competitions. I am committed to contributing my best to the success of the organization.''')

with qr2:
	st.image(qr, width=100)
	st.caption('Scan This to See the Portfolio')


st.markdown('<p style="font-size: 28px; font-weight: bold;">Basic Information</p>', unsafe_allow_html=True)
st.write("____")



col1, col2, col3 = st.columns([1, 3, 2])
profile= r"algo images/IMG_3215.jpg"


with col1:

    st.markdown('<p style="font-size: 16px; font-weight: bold;">Name</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px; font-weight: bold;">Date of Birth</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px; font-weight: bold;">Address</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px; font-weight: bold;">Nationality</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px; font-weight: bold;">Institution</p>', unsafe_allow_html=True)
    


with col2:
    st.markdown('<p style="font-size: 16px;">Nawrin Ahmed</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">December 17, 2002</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">34, North Dhanmondi, Dhaka</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">Bangladeshi</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 16px;">BUET</p>', unsafe_allow_html=True)


with col3:
    st.image(profile, width=200)

st.markdown('<p style="font-size: 28px; font-weight: bold;">Contact Information</p>', unsafe_allow_html=True)
icons, contact = st.columns([1,5])
icon_1= r"algo images/phone.png"
icon_2=r"algo images/email.png"
icon_3=r"algo images/Whatsapp.png"
icon_4=r"algo images/linkedin.png"


with icons:
    st.image(icon_1, width=40)
    st.image(icon_3, width=40)
    st.image(icon_2, width=40)
    st.image(icon_4, width=40)

with contact:
    st.markdown('<p style="font-size: 16px;">+880-1534117908</p>', unsafe_allow_html=True)
    st.markdown(' ')
    st.markdown('<p style="font-size: 16px;">+880-1831640646</p>', unsafe_allow_html=True)
    st.markdown(' ')
    st.markdown('<p style="font-size: 16px;">nawrinahmedprithilla17@gmail.com</p>', unsafe_allow_html=True)
    st.markdown(' ')
    st.markdown('<p style="font-size: 16px;">https://www.linkedin.com/in/NawrinAhmed/</p>', unsafe_allow_html=True)
