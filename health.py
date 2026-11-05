
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="NutriScan AI | Health Management",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# 2. CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main application */
.stApp {
    background-color: #f5f7fb;
    color: #202b3c;
}

/* Header */
.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #17365D;
    margin-bottom: 5px;
}

.subtitle {
    color: #718096;
    font-size: 15px;
    margin-bottom: 25px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #10243e;
}

section[data-testid="stSidebar"] * {
    color: #ffffff;
}

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: white;
    border-radius: 15px;
    border: 1px solid #e6eaf0;
    padding: 12px;
}

/* Buttons */
.stButton > button {
    background-color: #176b55;
    color: white;
    border: none;
    border-radius: 9px;
    padding: 12px 20px;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    background-color: #105440;
    color: white;
}

/* Dashboard Metric Cards */
.stApp [data-testid="stMetric"] {
    background-color: #ffffff !important;
    border: 1px solid #dce4ee !important;
    border-radius: 14px !important;
    padding: 20px !important;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.04);
}

/* Metric Labels */
.stApp [data-testid="stMetricLabel"],
.stApp [data-testid="stMetricLabel"] p {
    color: #64748b !important;
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* Metric Values */
.stApp [data-testid="stMetricValue"],
.stApp [data-testid="stMetricValue"] div {
    color: #17365D !important;
    font-size: 30px !important;
    font-weight: 750 !important;
}

/* Metric Delta */
.stApp [data-testid="stMetricDelta"] {
    color: #176b55 !important;
}

/* Text input */
.stTextInput input, .stTextArea textarea {
    border-radius: 9px;
}

/* Footer */
.footer {
    text-align: center;
    color: #8a94a6;
    font-size: 13px;
    margin-top: 40px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 3. LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

# Current Gemini model
MODEL_NAME = "gemini-3.8-flash"


# --------------------------------------------------
# 4. APPLICATION HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🥗 NutriScan AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your personal AI-powered food and nutrition assistant.'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# 5. SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("# 🥗 NutriScan AI")

    st.caption("HEALTH MANAGEMENT SYSTEM")

    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Select a page",
        [
            "🏠 Home",
            "🍎 Food Analysis",
            "ℹ️ About"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### Application Information")

    st.write("🤖 AI Engine: Google Gemini")

    st.write("📷 Image Analysis: Enabled")

    st.write("🥑 Nutrition Estimation: Enabled")

    st.divider()

    st.caption("Developed using Python and Streamlit")


# --------------------------------------------------
# 6. GEMINI CLIENT
# --------------------------------------------------

@st.cache_resource
def get_gemini_client(api_key):
    return genai.Client(api_key=api_key)


# --------------------------------------------------
# 7. GEMINI IMAGE ANALYSIS FUNCTION
# --------------------------------------------------

def get_gemini_response(image_bytes, mime_type, user_prompt):

    client = get_gemini_client(API_KEY)

    prompt = f"""
    You are an AI food recognition and nutrition assistant.

    Analyse the uploaded food image carefully.

    User request:
    {user_prompt}

    Follow these instructions:

    1. Identify every visible food item.
    2. Estimate the portion size of each item.
    3. Estimate calories for each food item in kcal.
    4. Estimate protein in grams.
    5. Estimate carbohydrates in grams.
    6. Estimate fat in grams.
    7. Calculate approximate total calories.
    8. Provide a short nutritional summary.
    9. Suggest one or two improvements for a balanced meal.

    Present your response using the following structure:

    FOOD IDENTIFICATION

    List all detected food items.

    NUTRITION BREAKDOWN

    Create a table with:
    Food Item | Portion | Calories | Protein | Carbs | Fat

    TOTAL NUTRITION

    Provide estimated totals for:
    Calories, Protein, Carbohydrates and Fat.

    HEALTH SUMMARY

    Explain the nutritional value of the meal.

    IMPORTANT:
    - Only analyse food if food is visible.
    - If no food is visible, say so clearly.
    - Do not invent ingredients or quantities.
    - All nutritional values must be labelled estimates.
    - Explain that image-based calorie estimation
      may not be exact.
    """

    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type=mime_type
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[
            prompt,
            image_part
        ]
    )

    return response.text


# --------------------------------------------------
# 8. HOME PAGE
# --------------------------------------------------

if page == "🏠 Home":

    st.markdown("## Welcome to NutriScan AI")

    st.write(
        "Understand your food better with artificial "
        "intelligence. Upload a food image and receive "
        "an estimated nutritional breakdown."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Technology", "Gemini AI")

    with col2:
        st.metric("Image Recognition", "Available")

    with col3:
        st.metric("Nutrition Analysis", "Available")

    st.markdown("### What can you do?")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.markdown("### 📷 Food Recognition")
            st.write(
                "Upload a photograph and let AI "
                "identify the food items."
            )

        with st.container(border=True):
            st.markdown("### 🔥 Calorie Estimation")
            st.write(
                "Get an approximate calorie breakdown "
                "for your meal."
            )

    with c2:
        with st.container(border=True):
            st.markdown("### 🥑 Nutrition Analysis")
            st.write(
                "Understand estimated protein, "
                "carbohydrates and fat."
            )

        with st.container(border=True):
            st.markdown("### 💡 Health Insights")
            st.write(
                "Receive general suggestions for "
                "maintaining a balanced meal."
            )

    st.info(
        "Go to Food Analysis from the sidebar "
        "to start analysing your meal."
    )


# --------------------------------------------------
# 9. FOOD ANALYSIS PAGE
# --------------------------------------------------

elif page == "🍎 Food Analysis":

    st.markdown("## 🍎 Food & Calorie Analysis")

    st.write(
        "Upload your food photograph and let "
        "Gemini AI analyse its nutritional value."
    )

    st.divider()

    left, right = st.columns(
        [1, 1],
        gap="large"
    )

    with left:

        st.markdown("### Upload Food Image")

        uploaded_file = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"],
            help="Upload a JPG, JPEG or PNG image."
        )

        if uploaded_file is not None:

            try:
                image = Image.open(uploaded_file)
                image.verify()

                uploaded_file.seek(0)

                image = Image.open(uploaded_file).convert("RGB")

                st.image(
                    image,
                    caption="Your uploaded food image",
                    use_container_width=True
                )

            except Exception:
                st.error("The uploaded image is invalid.")
                uploaded_file = None

        st.markdown("### Your Instructions")

        user_prompt = st.text_area(
            "Enter your prompt",
            value=(
                "Identify all food items and estimate "
                "their total calories and nutritional values."
            ),
            height=130
        )

        analyse_button = st.button(
            "🔍 Analyse My Food",
            type="primary",
            use_container_width=True
        )

    with right:

        st.markdown("### AI Analysis Results")

        if analyse_button:

            if not API_KEY:

                st.error(
                    "Gemini API key is missing. "
                    "Please check your .env file."
                )

            elif uploaded_file is None:

                st.warning(
                    "Please upload a food image first."
                )

            elif not user_prompt.strip():

                st.warning(
                    "Please enter an analysis prompt."
                )

            else:

                try:

                    with st.spinner(
                        "Gemini AI is analysing your food..."
                    ):

                        uploaded_file.seek(0)

                        image_bytes = uploaded_file.getvalue()

                        result = get_gemini_response(
                            image_bytes,
                            uploaded_file.type,
                            user_prompt
                        )

                    if not result:

                        st.warning(
                            "The AI returned an empty response. "
                            "Please try again."
                        )

                    else:

                        st.session_state["analysis_result"] = result

                        st.session_state["analysed_image"] = (
                            uploaded_file.name
                        )

                        st.success(
                            "Food analysis completed successfully!"
                        )

                except Exception as e:

                    st.error(
                        "Unable to analyse the image. "
                        "Please check your API key, internet "
                        "connection and Gemini model availability."
                    )

                    with st.expander("Technical error details"):
                        st.code(str(e))

        # Display saved result
        if st.session_state.get("analysis_result"):

            st.markdown(
                st.session_state["analysis_result"]
            )

            st.caption(
                "Image: "
                + st.session_state.get(
                    "analysed_image",
                    "Uploaded image"
                )
            )

            st.divider()

            if st.button("Clear Analysis"):

                st.session_state.pop(
                    "analysis_result",
                    None
                )

                st.session_state.pop(
                    "analysed_image",
                    None
                )

                st.rerun()

        else:

            with st.container(border=True):

                st.markdown("### 📊 Your results will appear here")

                st.write(
                    "Upload an image and click "
                    "'Analyse My Food' to see your "
                    "AI-generated nutrition report."
                )

                st.caption(
                    "No analysis has been generated yet."
                )


# --------------------------------------------------
# 10. ABOUT PAGE
# --------------------------------------------------

elif page == "ℹ️ About":

    st.markdown("## About NutriScan AI")

    st.write(
        """
        NutriScan AI is an AI-powered Health Management
        application developed using Python and Streamlit.

        The application uses Google's Gemini AI to analyse
        food photographs and provide estimated nutritional
        information.
        """
    )

    st.markdown("### Project Objectives")

    st.write(
        """
        - Identify food items from photographs.
        - Estimate calorie intake.
        - Provide nutritional information.
        - Help users understand their meals.
        - Encourage awareness of balanced eating habits.
        """
    )

    st.markdown("### Technologies Used")

    st.write(
        """
        - Python
        - Streamlit
        - Google Gemini API
        - Google GenAI SDK
        - Pillow
        - Python-dotenv
        """
    )

    st.warning(
        "This application provides general AI-generated "
        "nutrition estimates. It is not a substitute for "
        "professional medical or dietary advice."
    )


# --------------------------------------------------
# 11. FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        NutriScan AI | Health Management System
        <br>
        Powered by Python, Streamlit and Google Gemini
        <br><br>
        AI-generated nutrition values are estimates only.
    </div>
    """,
    unsafe_allow_html=True
)
