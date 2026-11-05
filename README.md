# 🥗 NutriScan AI – Health Management System

**NutriScan AI** is an AI-powered Health Management application developed using Python, Streamlit and Google's Gemini API. The application analyses food images and provides estimated calorie information and nutritional values to help users understand their daily food intake.

Users can upload an image of their meal, and the AI identifies visible food items and generates an estimated nutritional breakdown, including calories, protein, carbohydrates and fat.

## 🚀 Features

- **Food Recognition:** Identifies food items from uploaded images using Google Gemini AI.
- **Calorie Estimation:** Estimates the calorie content of individual food items.
- **Nutrition Analysis:** Provides estimated protein, carbohydrates and fat values.
- **Food Image Upload:** Supports JPG, JPEG and PNG image formats.
- **AI Health Insights:** Provides general nutritional summaries and suggestions for balanced meals.
- **Interactive Dashboard:** Displays application information through a clean and user-friendly interface.
- **Custom Prompts:** Allows users to provide instructions for food analysis.
- **Error Handling:** Displays appropriate messages for missing images, API issues and invalid inputs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Frontend and web application |
| Google Gemini API | AI-powered food image analysis |
| Google GenAI SDK | Communication with Gemini |
| Pillow (PIL) | Image processing |
| Python-dotenv | Environment variable management |
| Pandas | Data handling and analysis |
| Plotly | Data visualization (for future extensions) |

## 📂 Project Structure

```text
Health_Management_App/
│
├── health.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Food_Analysis.py
│   ├── 3_Nutrition_History.py
│   └── 4_About.py
│
├── database/
│
├── images/
│
└── venv/
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local computer.

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd Health_Management_App
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```cmd
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the root project directory.

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

Execute the following command:

```bash
python -m streamlit run health.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 📸 How to Use

1. Launch the NutriScan AI application.
2. Navigate to the Food Analysis section.
3. Upload a food image (JPG, JPEG or PNG).
4. Enter your desired analysis prompt.
5. Click the **Analyse My Food** button.
6. Wait for Gemini AI to process the image.
7. View the estimated food items, calories and nutritional information.

## 🧠 How It Works

The application uses Google's Gemini multimodal AI model to process uploaded food images.

**Workflow:**

```text
User Uploads Food Image
          |
          v
   Image Processing
          |
          v
    Gemini AI API
          |
          v
   Food Recognition
          |
          v
  Nutrition Estimation
          |
          v
  Display Results
```

## 🔮 Future Enhancements

The project can be extended with the following features:

- User registration and login system.
- Daily calorie intake tracking.
- Food analysis history.
- Database integration using MySQL or SQLite.
- Interactive nutrition dashboards and charts.
- Daily nutritional goals.
- Personalized meal recommendations.
- Weekly and monthly nutrition reports.

## ⚠️ Disclaimer

NutriScan AI provides AI-generated estimates of calories and nutritional values based on uploaded food images. These values may not be completely accurate because portion sizes, ingredients and cooking methods cannot always be determined from photographs.

This application is intended for general nutritional awareness and educational purposes. It is not a substitute for professional medical or dietary advice.

## 👨‍💻 Project Information

**Project Name:** NutriScan AI – Health Management System

**Category:** Artificial Intelligence / Health Management

**Developed Using:** Python, Streamlit and Google Gemini AI

---

*NutriScan AI – Making food and nutrition awareness smarter with Artificial Intelligence.*
