import streamlit as st
import qrcode
from io import BytesIO
import streamlit.components.v1 as components
import pyperclip
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from streamlit_extras.let_it_rain import rain


# Load environment variables
load_dotenv()

st.set_page_config(
    
    # page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Using default Streamlit colors for better dark mode compatibility

# Email sending function
def send_email(sender_name, sender_email, sender_phone, contacting_as, subject_text, message_text):
    """Send email notification via SMTP"""
    try:
        # Get SMTP credentials from environment variables
        smtp_email = os.getenv("SMTP_EMAIL")
        smtp_password = os.getenv("SMTP_APP_PASSWORD")
        
        if not smtp_email or not smtp_password:
            return False, "SMTP credentials not configured"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = smtp_email
        msg['To'] = "sushantnagi667@gmail.com, edu@sushant.cc"
        msg['Reply-To'] = sender_email  # Set reply-to as sender's email
        msg['Subject'] = f"Tutoring Inquiry from {sender_name}" + (f" - {subject_text}" if subject_text else "")
        
        # Email body
        body = f"""
New tutoring inquiry received:

Name: {sender_name}
Email: {sender_email}
Phone: {sender_phone if sender_phone else 'Not provided'}
Contacting as: {contacting_as}
Subject: {subject_text if subject_text else 'N/A'}

Message:
{message_text}

---
Sent via Tutor Portfolio Contact Form
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(smtp_email, smtp_password)
        
        # Send email to both recipients
        server.send_message(msg)
        server.quit()
        
        return True, "Email sent successfully!"
        
    except Exception as e:
        return False, f"Error sending email: {str(e)}"

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
        phone = st.text_input("Phone Number (with country code) *", placeholder="+1 (123) 456-7890")
        
        contacting_as = st.selectbox(
            "Contacting as *",
            ["", "Student", "Parent", "Institute/Agency", "Other"]
        )
        
        subject = st.text_input("Subject", placeholder="Brief subject of your inquiry")
        
        message = st.text_area(
            "Message *", 
            placeholder="Tell me about your learning goals, current challenges, or any specific topics you'd like to focus on..."
        )
        
        submitted = st.form_submit_button("Send Message 📧", use_container_width=True)
        
        if submitted:
            # Validation
            if not name or not email or not contacting_as or not message:
                st.error("Please fill in all required fields marked with *")
            else:
                # Send email via SMTP
                with st.spinner("Sending your message..."):
                    success, response_message = send_email(
                        sender_name=name,
                        sender_email=email,
                        sender_phone=phone,
                        contacting_as=contacting_as,
                        subject_text=subject,
                        message_text=message
                    )
                
                if success:
                    st.success("✅ Message sent successfully! I'll get back to you within 48 hours." \
                    " Contact via WhatsApp if urgent.")
                    rain(
                        emoji="📮",
                        font_size=54,
                        falling_speed=5,
                        animation_length="1",
                        )
                else:
                    st.error(f"❌ Failed to send message: {response_message}")
                    st.warning("Please try contacting via email or WhatsApp directly.")
                    
                    # Fallback: Create mailto link
                    email_subject = f"Tutoring Inquiry from {name}" + (f" - {subject}" if subject else "")
                    email_body = f"""
New tutoring inquiry received:

Name: {name}
Email: {email}
Phone: {phone}
Contacting as: {contacting_as}
Subject: {subject if subject else 'N/A'}

Message:
{message}

---
Sent via Tutor Portfolio Contact Form
                    """
                    
                    mailto_link = f"mailto:sushantnagi667@gmail.com?subject={email_subject}&body={email_body}"
                    
                    st.markdown(f"""
                    **Alternative Options:**
                    1. [Click here to open your email client]({mailto_link}) 
                    2. Or contact via WhatsApp below
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
        if st.button("📋", help="Copy email", key="copy_email_btn"):
            try:
                pyperclip.copy(email_address)
                st.toast("✅ Email copied to clipboard!")
            except:
                # Fallback: show the email for manual copy
                st.toast("⚠️ Please copy manually: " + email_address)
       
            
    
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
    
    **Email:** edu@sushant.cc  
    **WhatsApp:** +91 95994 68699  
    """)

st.markdown("---")

# FAQ Section
st.markdown("## ❓ Frequently Asked Question(s)")

with st.expander("💰 What are your tutoring rates?"):
    st.write("""
    Rates vary based on:
    - Subject complexity
    - Grade level
    - Session frequency
    - Group vs individual sessions
    
    Contact me for a personalized quote. First session is always free!
    """)

# with st.expander("⏰ What are your available hours?"):
#     st.write("""
#     I offer flexible scheduling to accommodate students from different time zones:
#     - Available: 6:30 PM EST to 12:30 PM EST (next day)
#     - Covering most time zones globally
#     - Special arrangements can be made upon request
#     """)

# # Implementation notes
# st.markdown("---")
# st.markdown("### 🛠️ Setup Instructions:")
# st.info("""
# **To complete the WhatsApp integration:**

# 1. Replace `+1234567890` with your actual WhatsApp number
# 2. Update the pre-filled message if needed
# 3. The QR code will automatically update with your number

# **For email functionality:**
# - The form creates a mailto link automatically
# - Consider integrating with email services like EmailJS for better functionality
# - Copy button functionality can be enhanced with JavaScript
# """)