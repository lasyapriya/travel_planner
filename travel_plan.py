import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Custom CSS for Background & Input Labels
page_bg_img = """
<style>
/* Background Image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/thumbnails/057/779/146/small/serene-stone-pathway-winding-through-lush-green-meadow-and-mountains-photo.jpeg");
    background-size: cover;
    background-position: center;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 10px;
}

/* Custom Input Labels */
.custom-label {
    font-size: 25px;
    font-weight: bold;
    font-family: 'Poppins', sans-serif;
    color: #d2b3e5; /* Light Violet */
    text-shadow: 2px 2px 3px #5D3FD3, 2px 2px 5px #FFD700; /* Dark purple + Gold for contrast */
    display: block;
    margin-bottom: 5px;
}
/* Output Box Styling */
.output-box {
    background: white; /* Light transparent background */
    border: 4px solid #FFD700; /* Gold border for elegance */
    border-radius: 10px;
    padding: 15px;
    font-size: 20px;
    font-weight: bold;
    color: #51256c /* Light violet text */
    text-shadow: 1px 1px 3px #5D3FD3, 0px 0px 5px #FFD700;
}



</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: white;'>✈️ Travel Planner ✈️</h1>", unsafe_allow_html=True)

# Sidebar - Travel Tips
st.sidebar.header("🌍 Travel Tips")
st.sidebar.write("✅ Pack light but smart 🧳") 
st.sidebar.write("✅ Book flights in advance ✈️") 
st.sidebar.write("✅ Explore local food 🍲") 
st.sidebar.write("✅ Check weather before packing 🌤️")

# Custom Labels with Input Fields
st.markdown('<span class="custom-label">Enter your destination:</span>', unsafe_allow_html=True)
destination = st.text_input(" ", key="destination")

st.markdown('<span class="custom-label">Enter your preferences (e.g., adventure, sightseeing, food):</span>', unsafe_allow_html=True)
preferences = st.text_area(" ", key="preferences")

st.markdown('<span class="custom-label">Enter your budget range ($):</span>', unsafe_allow_html=True)
budget = st.text_input(" ", key="budget")

st.markdown('<span class="custom-label">Enter your trip duration (days):</span>', unsafe_allow_html=True)
trip_duration = st.text_input(" ", key="trip_duration")

# Submit Button
if st.button("Get Travel Recommendations"):
    if destination and preferences and budget and trip_duration:
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = f"Suggest a travel plan for {destination} based on these preferences: {preferences}. Budget: {budget}. Trip duration: {trip_duration} days."
        
        response = model.generate_content(prompt)
        st.markdown('<div class="output-box">🌟 Recommended Itinerary:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="output-box">{response.text}</div>', unsafe_allow_html=True)

    else:
        st.warning("Please fill in all fields before submitting!")
