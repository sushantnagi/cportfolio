import streamlit as st
from PIL import Image
import os

# Configure page settings
st.set_page_config(
    page_title="Tutor Portfolio - Sushant Nagi",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Using default Streamlit colors for better dark mode compatibility

# Main page content (formerly Qualifications page)

# Create three columns for the first section
col1, col2, col3 = st.columns([1, 0.1, 2])

# Column 1: Profile Picture
with col1:
    # Try to load profile image, use placeholder if not found
    profile_path = "assets/profile_placeholder.png"
    if os.path.exists(profile_path):
        try:
            image = Image.open(profile_path)
            st.image(image)
            st.markdown("### Sushant Nagi")
        except:
            st.info("📷 Place your profile photo in assets/profile_photo.jpg")
    else:
        st.info("📷 Place your profile photo in assets/profile_photo.jpg")

# Column 2: Divider
with col2:
    st.markdown("---")

# Column 3: Educational Qualifications
with col3:
    st.markdown("## 🎓 Educational Qualifications")
    
    # Education details based on provided information
    st.markdown("""
    **Delhi Technological University**  
    *Bachelor of Technology in Engineering Physics*  
    📅 Aug 2021 – Aug 2025  
    📊 CGPA: 6.72
    
    **Hansraj Model School, Punjabi Bagh**  
    *CBSE 12th*  
    📅 2021  
    📊 84.6%
    
    **Hansraj Model School, Punjabi Bagh**  
    *CBSE 10th*  
    📅 2019  
    📊 95.2%
    """)

st.markdown("---")

# Create three columns for Achievements, divider, and Experience
col1, col2, col3 = st.columns([2, 0.1, 2])

with col1:
    # Achievements Section
    st.markdown("## 🏆 Achievements")
    
    achievements = [
        "🥇 High Distinction Excellence, Australian National Chemistry Quiz, 2016",
        "🥇 High Distinction, Australian National Chemistry Quiz, 2017", 
        "🥈 State Rank 2, Green Olympiad, 2015",
        "🏅 Several Gold, Silver and Bronze medals in SOF Science, Mathematics and English Olympiads"
    ]
    
    for achievement in achievements:
        st.write(achievement)

with col2:
    st.html(
            '''
                <div class="divider-vertical-line1"></div>
                <style>
                    .divider-vertical-line1 {
                        border-left: 2px solid rgba(49, 51, 63, 0.2);
                        height: 320px;
                        margin: auto;
                    }
                </style>
            '''
        )

with col3:
    # Experience Section
    st.markdown("## 👨‍🏫 Experience")
    st.markdown("""
    **Tutoring Experience**  
    Taught several students for SAT/Olympiads (Grade 8-12) from:
    - 🇺🇸 USA
    - 🇬🇧 UK  
    - 🇦🇺 Australia
    - 🌍 Middle East
    - 🇪🇺 Europe
    """)

st.markdown("---")

# Create three columns for Demo Videos, divider, and Book a Free Trial
col1, col2, col3 = st.columns([2, 0.1, 2])

with col1:
    # Section 2: Demo Videos
    st.markdown("## 🎥 Demo Videos")
    url = "https://youtube.com/playlist?list=PL4cUxeGkcC9gC2x7Zt8yq6k7bV1F7H8bH"  # Replace with actual playlist URL
    
    st.markdown(f"""
    <a href="{url}" target="_self">Click here</a> to watch some Demo Videos on topics of:
    <ul>
    <li><b>Algebra 1</b>: Linear equations, inequalities, and graphing</li>
    <li><b>Algebra 2</b>: Quadratic functions, exponentials, and logarithms</li>
    <li><b>Geometry</b>: Proofs, area, volume, and coordinate geometry</li>
    </ul>
    """, unsafe_allow_html=True)

with col2:
    st.html(
            '''
                <div class="divider-vertical-line2"></div>
                <style>
                    .divider-vertical-line2 {
                        border-left: 2px solid rgba(49, 51, 63, 0.2);
                        height: 220px;
                        margin: auto;
                    }
                </style>
            '''
        )

with col3:
    # Section 3: Book a Free Trial
    st.markdown("## 📅 Book a Free Trial")
    contact_url = "https://contacturl.contact/contact"  # Replace with your actual URL
    
    st.markdown(f"""
    <a href="{contact_url}" target="_self">Click here</a> to book a free trial / contact.
    """, unsafe_allow_html=True)

# Why Choose Me section
st.markdown("---")
st.markdown("""
### Why Choose Me as Your Tutor?

✅ **Proven Track Record**: Multiple olympiad medals and high academic achievements  
✅ **International Experience**: Taught students from USA, UK, Australia, Middle East, and Europe  
✅ **Subject Expertise**: Mathematics, Physics, Chemistry, and SAT preparation  
✅ **Personalized Approach**: Tailored learning plans for each student  
✅ **Free Trial Session**: 50-minute trial to assess your needs  

""")
contact_url1 = "https://contacturl.contact/contact"  # Replace with your actual URL
# Call-to-action box
st.markdown(f"🚀 **Ready to Excel?** Join tens of students who have improved their grades and achieved their academic goals with personalized tutoring! <a href='{contact_url1}' target='_self'>Click here</a> to book a free trial / contact.", unsafe_allow_html=True)