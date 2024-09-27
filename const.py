# Define the host address for the application, usually set to localhost (127.0.0.1)
APP_HOST: str = "127.0.0.1"

# Enable or disable debug mode for the application; True means debug mode is on
APP_DEBUG_MODE: bool = True

# Set the port number on which the application will run; 5000 is a common default for web apps
APP_PORT: int = 5000

# Path to the folder where HTML templates are stored for rendering
APP_TEMPLATE_FOLDER: str = "templates"

# Define a constant for the folder that contains static files (like CSS, JS, images)
APP_STATIC_FOLDER: str = "static"

# Define a constant for the base URL path to access static files
APP_STATIC_URL_PATH: str = "/"

HEART_DISEASE_COLUMNS = {
    "age": "อายุ",
    "sex": "เพศ (1 = ชาย; 0 = หญิง)",
    "cp": "ประเภทอาการเจ็บหน้าอก",
    "trestbps": "ค่าความดันโลหิต",
    "chol": "คอเลสเตอรอลในเลือด (mg/dl)",
    "fbs": "น้ำตาลในเลือดขณะอดอาหาร > 120 มก./ดล. (1 = จริง; 0 = เท็จ)",
    "restecg": "ผลการตรวจคลื่นไฟฟ้าหัวใจขณะพัก",
    "thalach": "อัตราการเต้นของหัวใจสูงสุดที่ได้รับ",
    "exang": "การออกกำลังกายทำให้เกิดโรคหลอดเลือดหัวใจตีบ (1 = ใช่; 0 = ไม่ใช่)",
    "oldpeak": "ภาวะซึมเศร้าเกิดจากการออกกำลังกายสัมพันธ์กับการพักผ่อน",
    "slope": "ความชันของส่วน ST ของการออกกำลังกายสูงสุด",
    "ca": "จำนวนหลอดเลือดที่ตีบ (0-4)",
    "thal": "สถานะของ thalassemia (1 = ปกติ; 2 = ค่าต่ำ; 3 = ค่าปานกลาง; 4 = ค่าต่ำมาก)",
    "target": "สถานะการเกิดโรคหัวใจ (1 = มีโรคหัวใจ; 0 = ไม่มีโรคหัวใจ)",
}

SELECTED_FEATURES = [
    "age",  # อายุ
    "sex",  # เพศ (1 = ชาย; 0 = หญิง)
    "cp",  # ประเภทอาการเจ็บหน้าอก
    "trestbps",  # ค่าความดันโลหิต
    "chol",  # คอเลสเตอรอลในเลือด (mg/dl)
    "fbs",  # น้ำตาลในเลือดขณะอดอาหาร > 120 มก./ดล. (1 = จริง; 0 = เท็จ)
    "restecg",  # ผลการตรวจคลื่นไฟฟ้าหัวใจขณะพัก
    "thalach",  # อัตราการเต้นของหัวใจสูงสุดที่ได้รับ
    "exang",  # การออกกำลังกายทำให้เกิดโรคหลอดเลือดหัวใจตีบ (1 = ใช่; 0 = ไม่ใช่)
    "oldpeak",  # ภาวะซึมเศร้าเกิดจากการออกกำลังกายสัมพันธ์กับการพักผ่อน
    "slope",  # ความชันของส่วน ST ของการออกกำลังกายสูงสุด
    "ca",  # จำนวนหลอดเลือดที่ตีบ (0-4)
    "thal",  # สถานะของ thalassemia (1 = ปกติ; 2 = ค่าต่ำ; 3 = ค่าปานกลาง; 4 = ค่าต่ำมาก)
]
