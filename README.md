# HAED-IDS Framework
## Hybrid Anomaly-Ensemble Detection for Intrusion Detection Systems

### نظام متقدم لكشف التسلل الشبكي باستخدام تقنيات التعلم الآلي

---

## 📋 نظرة عامة

إطار عمل مبتكر وحديث لكشف الهجمات الشبكية المعروفة وغير المعروفة (Zero-Day) باستخدام:

- **Autoencoder**: للكشف عن الشذوذ بطريقة غير خاضعة للإشراف
- **Ensemble Learning**: دمج XGBoost, LightGBM, و Random Forest
- **Advanced Feature Engineering**: هندسة ميزات متقدمة لتحسين الكشف
- **Cost-Sensitive Learning**: تقليل الإنذارات الكاذبة
- **SMOTE + Data Balancing**: معالجة عدم التوازن في البيانات

---

## 🎯 الأهداف

✅ **كشف ممتاز للهجمات غير المعروفة** (Unknown Attack Detection)
✅ **خفض معدل الإنذارات الكاذبة** (False Positive Rate < 1%)
✅ **معدل كشف عالي** (Detection Rate > 98%)
✅ **إطار جديد لم يطرح من قبل**

---

## 📊 مجموعة البيانات

- **Dataset**: CICIDS2018
- **Path**: `C:\Users\SVUF25\Desktop\IDS-ML-Project\dataset2018`
- **الحجم**: ~3 مليون سجل
- **الميزات**: 82 ميزة شبكية

---

## 🛠️ المتطلبات

### بيئة التطوير
- **OS**: Windows/Linux/macOS
- **Python**: 3.8+
- **Environment**: Anaconda Navigator
- **Notebook**: Jupyter Notebook
- **RAM**: 32 GB

### المكتبات المطلوبة
```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
tensorflow>=2.10.0
xgboost>=1.5.0
lightgbm>=3.3.0
imbalanced-learn>=0.8.0
matplotlib>=3.5.0
seaborn>=0.12.0
plotly>=5.0.0
joblib>=1.1.0
```

---

## 📁 هيكل المشروع

```
HAED-IDS-Framework/
├── README.md
├── requirements.txt
├── environment.yml
├── setup.py
│
├── notebooks/
│   ├── 01_Data_Loading_Exploration.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Autoencoder_Training.ipynb
│   ├── 05_Ensemble_Models_Training.ipynb
│   ├── 06_Hybrid_Framework.ipynb
│   ├── 07_Zero_Day_Detection.ipynb
│   └── 08_Results_Visualization.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── feature_engineer.py
│   ├── autoencoder_model.py
│   ├── ensemble_models.py
│   ├── hybrid_framework.py
│   └── evaluator.py
│
├── models/
│   ├── autoencoder.h5
│   ├── xgboost_model.pkl
│   ├── lightgbm_model.pkl
│   └── random_forest_model.pkl
│
├── results/
│   ├── metrics.csv
│   ├── confusion_matrices.png
│   ├── roc_curves.png
│   └── feature_importance.png
│
└── dataset2018/
    └── [البيانات]
```

---

## 🚀 خطوات الاستخدام

### 1. تثبيت البيئة
```bash
conda env create -f environment.yml
conda activate haed-ids
```

### 2. تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### 3. تشغيل Jupyter Notebook
```bash
jupyter notebook
```

### 4. تنفيذ دفاتر الملاحظات بالترتيب:
1. `01_Data_Loading_Exploration.ipynb` - تحميل واستكشاف البيانات
2. `02_Data_Preprocessing.ipynb` - معالجة البيانات
3. `03_Feature_Engineering.ipynb` - هندسة الميزات
4. `04_Autoencoder_Training.ipynb` - تدريب Autoencoder
5. `05_Ensemble_Models_Training.ipynb` - تدريب نماذج Ensemble
6. `06_Hybrid_Framework.ipynb` - الإطار الهجين
7. `07_Zero_Day_Detection.ipynb` - كشف الهجمات غير المعروفة
8. `08_Results_Visualization.ipynb` - تصور النتائج

---

## 📈 النتائج المتوقعة

| المقياس | القيمة المتوقعة |
|--------|----------------|
| **Accuracy** | > 99% |
| **Precision** | > 98% |
| **Recall** | > 98% |
| **F1-Score** | > 98% |
| **FPR** | < 0.5% |
| **Detection Rate** | > 98% |

---

## 🔬 ميزات الإطار

### 1️⃣ Autoencoder للكشف عن الشذوذ
- بنية: 82 → 64 → 32 → 16 → 32 → 64 → 82
- Activation: ReLU للطبقات المخفية، Linear للمخرجات
- Loss: MSE مع Reconstruction Error Threshold

### 2️⃣ Ensemble Voting
- **XGBoost**: للتصنيف الدقيق
- **LightGBM**: للسرعة والكفاءة
- **Random Forest**: للتنوع والاستقرار

### 3️⃣ Cost-Sensitive Learning
- تجنيب أوزان للفئات غير المتوازنة
- تقليل تكلفة الإنذارات الكاذبة

### 4️⃣ Feature Engineering
- Statistical Features
- Statistical Features من Network Flows
- Temporal Features
- Frequency Domain Features

### 5️⃣ Zero-Day Detection
- كشف الحالات الشاذة غير المصنفة
- Isolation Forest للشذوذ الإضافي
- One-Class SVM كطريقة بديلة

---

## 📚 المراجع الأكاديمية

1. **ZeroDay-LLM Framework** - MDPI (2024)
2. **Transformer-Based Adaptive Detection** - ArXiv (2024)
3. **Autoencoder + Ensemble Fusion** - PLOS ONE (2024)
4. **Adversarially-Trained Ensemble** - IEEE TrustCom (2024)

---

## 👨‍💻 الكاتب

**Rittamar22** - Cybersecurity Researcher

---

## 📄 الترخيص

MIT License - استخدام حر للأغراض التعليمية والبحثية

---

## 🤝 المساهمة

نرحب بالمساهمات والتحسينات. يرجى فتح Issue أو Pull Request.

---

**آخر تحديث**: سبتمبر 2026
