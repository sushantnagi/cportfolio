import streamlit as st

# Using default Streamlit colors for better dark mode compatibility

# Page 2: Demo Videos

st.markdown("""
Watch these demonstration videos to see my teaching style and approach to various mathematical concepts. 
These videos cover key topics in Algebra 1, Algebra 2, and Geometry.
""")

# Video sections
st.markdown("---")

# Algebra 1 Section
st.markdown("## 📊 Algebra 1")
st.markdown("**Topic: Linear Equations and Graphing**")

# Placeholder for YouTube video 1
video_placeholder_1 = """
<div style="
    background-color: #f0f2f6; 
    border: 2px dashed #cccccc; 
    border-radius: 10px; 
    padding: 40px; 
    text-align: center; 
    margin: 20px 0;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
">
    <h3>🎬 Algebra 1 Demo Video</h3>
    <p>YouTube video will be embedded here</p>
    <p><strong>Placeholder URL:</strong> https://youtube.com/watch?v=ALGEBRA1_VIDEO_ID</p>
    <p><em>Replace with actual YouTube embed code</em></p>
</div>
"""
st.markdown(video_placeholder_1, unsafe_allow_html=True)

# Code comment for implementation
st.code("""
# To embed actual YouTube video, replace the placeholder above with:
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
""", language="python")

st.markdown("---")

# Algebra 2 Section
st.markdown("## 🔢 Algebra 2")
st.markdown("**Topic: Quadratic Functions and Transformations**")

# Placeholder for YouTube video 2
video_placeholder_2 = """
<div style="
    background-color: #f0f2f6; 
    border: 2px dashed #cccccc; 
    border-radius: 10px; 
    padding: 40px; 
    text-align: center; 
    margin: 20px 0;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
">
    <h3>🎬 Algebra 2 Demo Video</h3>
    <p>YouTube video will be embedded here</p>
    <p><strong>Placeholder URL:</strong> https://youtube.com/watch?v=ALGEBRA2_VIDEO_ID</p>
    <p><em>Replace with actual YouTube embed code</em></p>
</div>
"""
st.markdown(video_placeholder_2, unsafe_allow_html=True)

st.markdown("---")

# Geometry Section
st.markdown("## 📐 Geometry")
st.markdown("**Topic: Circle Theorems and Proofs**")

# Placeholder for YouTube video 3
video_placeholder_3 = """
<div style="
    background-color: #f0f2f6; 
    border: 2px dashed #cccccc; 
    border-radius: 10px; 
    padding: 40px; 
    text-align: center; 
    margin: 20px 0;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
">
    <h3>🎬 Geometry Demo Video</h3>
    <p>YouTube video will be embedded here</p>
    <p><strong>Placeholder URL:</strong> https://youtube.com/watch?v=GEOMETRY_VIDEO_ID</p>
    <p><em>Replace with actual YouTube embed code</em></p>
</div>
"""
st.markdown(video_placeholder_3, unsafe_allow_html=True)

st.markdown("---")

# Additional information
st.markdown("""
### 💡 What You'll Learn From These Videos:

**Algebra 1 Demo:**
- Step-by-step problem solving approach
- Visual representation techniques
- Common mistake identification and correction

**Algebra 2 Demo:**
- Advanced function analysis
- Real-world application examples  
- Interactive problem-solving methods

**Geometry Demo:**
- Proof construction strategies
- Geometric reasoning development
- Visualization and spatial thinking
""")

# Call to action
st.info("🎯 **Impressed with the teaching style?** These are just small samples of the comprehensive tutoring experience. Visit the Contact page to book a free trial and experience personalized learning!")

# Video implementation guide
st.markdown("---")
st.markdown("### 🛠️ Implementation Guide:")
st.info("""
**To add actual YouTube videos:**

1. Upload your demo videos to YouTube
2. Copy the video URLs
3. Replace the placeholder divs with: `st.video("YOUR_YOUTUBE_URL")`

**Example:**
```python
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

**Alternative embedding:**
```python
st.components.v1.iframe("https://www.youtube.com/embed/VIDEO_ID", height=400)
```
""")