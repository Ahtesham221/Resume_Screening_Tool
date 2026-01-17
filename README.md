# 🚀 AI-Powered Enterprise Resume Screener v2.0
**Internship Project | DevTriCode Artificial Intelligence Track**

An industry-grade, multi-page AI application designed to automate resume screening across **100+ job categories**. 

---

## 🔐 Deployment & Roadmap
This project is currently in **Phase 2** of the "User Authentication & Multi-Tenancy Integration Plan." 

- **Phase 1 (Upcoming):** JWT User Authentication & Tenant Registration.
- **Phase 2 (Completed):** Tenant-Aware Architecture, Relative Pathing, and Cloud Deployment.
- **Phase 3 (Upcoming):** Role-Based Access Control (RBAC) and Audit Logging.

## 🌟 Key Features
- **Multi-Page Architecture**: Organized into Home, AI Screener, Analytics, and Feedback portals.
- **Hybrid AI Architecture**: Combines a static KNN-Classifier with a dynamic Memory Layer that learns from user feedback.
- **Universal Document Support**: Supports PDF, DOCX, TXT, and Images (OCR via Tesseract).
- **Zipped Data Handling**: Optimized for cloud deployment by handling compressed datasets for faster performance.

## 📂 Project Structure
```text
├── Dataset/               # Zipped training datasets
├── pages/
│   ├── 1_Screener.py      # Universal Parser & AI Prediction
│   ├── 2_Analytics.py     # Data Visualization Dashboard
│   └── 3_Feedback.py      # Admin Portal & Correction Logs
├── app.py                 # Landing Page & Home UI
├── train_model.py         # Dataset Merging & Training Logic
├── model.pkl              # Trained ML "Brain"
├── tfidf.pkl              # TF-IDF Vectorizer
├── requirements.txt       # Python Dependency List
├── packages.txt           # System Dependency List (Tesseract)
└── README.md              # Project Documentation
