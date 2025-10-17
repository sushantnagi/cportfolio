# Tutor Portfolio - Sushant Nagi

A comprehensive Streamlit-based portfolio website for showcasing tutoring qualifications, demo videos, and contact information.

## Features

### Page 1: Qualifications
- Personal profile section with photo
- Educational qualifications from Delhi Technological University
- Achievements and awards
- Teaching experience
- Navigation to other sections

### Page 2: Demo Videos
- Placeholder sections for YouTube videos
- Covers Algebra 1, Algebra 2, and Geometry
- Easy integration guide for actual video content

### Page 3: Contact
- Interactive contact form
- Direct email contact with copy functionality
- WhatsApp integration with QR code
- FAQ section
- Automated email generation

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash   ```

### Running the Application

```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`

## Customization

### Adding Your Profile Photo
1. Replace the placeholder in `assets/` folder with your actual photo
2. Name it `profile_photo.jpg` or update the path in `page1_qualifications.py`

### Adding YouTube Videos
1. Upload your demo videos to YouTube
2. In `page2_demo_videos.py`, replace the placeholder divs with:
   ```python
   st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
   ```

### WhatsApp Integration
1. In `page3_contact.py`, update the `whatsapp_number` variable with your actual number
2. Customize the pre-filled message if desired

### Email Configuration
- The contact form generates mailto links by default
- For production use, consider integrating with email services like EmailJS or SendGrid

## File Structure

```
Tutor Portfolio/
├── main.py                 # Main application with navigation
├── pages/
│   ├── __init__.py
│   ├── page1_qualifications.py
│   ├── page2_demo_videos.py
│   └── page3_contact.py
├── assets/
│   └── profile_placeholder.png
├── requirements.txt
└── README.md
```

## Technologies Used

- **Streamlit**: Web application framework
- **streamlit-option-menu**: Navigation menu component
- **Pillow**: Image processing
- **qrcode**: QR code generation for WhatsApp

## Deployment

### Streamlit Cloud
1. Push your code to a GitHub repository
2. Connect to Streamlit Cloud
3. Deploy directly from your repository

### Local Network
```bash
streamlit run main.py --server.address 0.0.0.0
```

## Support

For issues or questions about this portfolio template, please contact sushantnagi667@gmail.com

## License

This project is open source and available under the MIT License.