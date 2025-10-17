import streamlit as st
import qrcode
from io import BytesIO
import streamlit.components.v1 as components


st.set_page_config(
    
    # page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Using default Streamlit colors for better dark mode compatibility

# Page 3: Contact

st.markdown("""
Ready to start your learning journey? Get in touch to book your free trial session or ask any questions about tutoring services.
""")

# Create two columns for contact form and contact info
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 📝 Contact Form")
    
    # Contact form
    with st.form("contact_form"):
        name = st.text_input("Full Name *", placeholder="Enter your full name")
        email = st.text_input("Email Address *", placeholder="your.email@example.com")
        phone = st.text_input("Phone Number", placeholder="+1 (123) 456-7890")
        
        grade_level = st.selectbox(
            "Grade Level / Academic Level *",
            ["", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12", "College Freshman", "College Sophomore", "Other"]
        )
        
        subjects = st.multiselect(
            "Subjects of Interest *",
            ["Mathematics", "Physics", "Chemistry", "SAT Math", "SAT Physics", "SAT Chemistry", "Olympiad Preparation", "Other"]
        )
        
        tutoring_type = st.radio(
            "Preferred Tutoring Type *",
            ["One-on-One Online", "Group Sessions", "Intensive Crash Course", "Exam Preparation"]
        )
        
        availability = st.text_area("Preferred Schedule / Availability", placeholder="e.g., Weekends, After 6 PM EST, etc.")
        
        message = st.text_area(
            "Message *", 
            placeholder="Tell me about your learning goals, current challenges, or any specific topics you'd like to focus on..."
        )
        
        submitted = st.form_submit_button("Send Message 📧", use_container_width=True)
        
        if submitted:
            # Validation
            if not name or not email or not grade_level or not subjects or not message:
                st.error("Please fill in all required fields marked with *")
            else:
                # Create email content
                email_subject = f"Tutoring Inquiry from {name}"
                email_body = f"""
New tutoring inquiry received:

Name: {name}
Email: {email}
Phone: {phone}
Grade Level: {grade_level}
Subjects: {', '.join(subjects)}
Tutoring Type: {tutoring_type}
Availability: {availability}

Message:
{message}

---
Sent via Tutor Portfolio Contact Form
                """
                
                # Create mailto link
                mailto_link = f"mailto:sushantnagi667@gmail.com?subject={email_subject}&body={email_body}"
                
                st.success("✅ Form submitted successfully!")
                st.markdown(f"""
                **Next Steps:**
                1. [Click here to open your email client]({mailto_link}) 
                2. Or copy the message below and send manually
                3. I'll respond within 24 hours!
                """)
                
                # Display formatted message for manual copying
                with st.expander("📋 Copy Message for Manual Send"):
                    st.code(f"To: sushantnagi667@gmail.com\nSubject: {email_subject}\n\n{email_body}", language="text")

with col2:
    st.markdown("### 📧 Contact Details")
    
    # Email with copy functionality
    st.markdown("**Email Address:**")
    email_address = "edu@sushant.cc"
    
    col_email, col_copy = st.columns([3, 1])
    with col_email:
        st.code(email_address)
    with col_copy:
        email_to_copy = email_address
    
        if st.button("📋", help="Copy email"):
            components.html(f"""
                <script>
                    navigator.clipboard.writeText("{email_to_copy}");
                </script>
                """, height=0)
            st.toast("✅ Email copied to clipboard!")
       
            
    
    # WhatsApp Section
    st.markdown("### 💬 WhatsApp")
    
    whatsapp_number = "919599468699"  # Placeholder - you'll replace this
    whatsapp_message = "Hi, I would like to book a free trial session."
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"
    
    # WhatsApp contact button
    st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <div style="
            background-color: #25D366; 
            color: white; 
            padding: 10px 20px; 
            border-radius: 10px; 
            text-align: center; 
            margin: 10px 0;
            display: block;
        ">
            💬 Contact on WhatsApp
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    # Generate QR Code for WhatsApp
    st.markdown("**WhatsApp QR Code:**")
    
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(whatsapp_url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to bytes for Streamlit
    buffer = BytesIO()
    qr_img.save(buffer, "PNG")
    buffer.seek(0)
    
    st.image(buffer, width=200, caption="Scan to chat on WhatsApp")
    
    # Contact info box
    st.info("""
    📞 **Contact Information**
    
    **Email:** sushantnagi667@gmail.com  
    **WhatsApp:** +91 95994 68699  
    """)

st.markdown("---")

# FAQ Section
st.markdown("## ❓ Frequently Asked Questions")

with st.expander("💰 What are your tutoring rates?"):
    st.write("""
    Rates vary based on:
    - Subject complexity
    - Grade level
    - Session frequency
    - Group vs individual sessions
    
    Contact me for a personalized quote. First session is always free!
    """)

with st.expander("⏰ What are your available hours?"):
    st.write("""
    I offer flexible scheduling to accommodate students from different time zones:
    - Weekdays: 4 PM - 10 PM EST
    - Weekends: 9 AM - 8 PM EST
    - Special arrangements for different time zones
    """)

with st.expander("🔧 What platform do you use for online tutoring?"):
    st.write("""
    I primarily use:
    - Zoom for video sessions
    - Interactive whiteboard tools
    - Screen sharing for problem solving
    - Google Drive for resource sharing
    """)

with st.expander("📚 Do you provide study materials?"):
    st.write("""
    Yes! I provide:
    - Custom practice problems
    - Study guides and notes
    - Past exam papers and solutions
    - Recommended textbooks and resources
    """)

# Implementation notes
st.markdown("---")
st.markdown("### 🛠️ Setup Instructions:")
st.info("""
**To complete the WhatsApp integration:**

1. Replace `+1234567890` with your actual WhatsApp number
2. Update the pre-filled message if needed
3. The QR code will automatically update with your number

**For email functionality:**
- The form creates a mailto link automatically
- Consider integrating with email services like EmailJS for better functionality
- Copy button functionality can be enhanced with JavaScript
""")