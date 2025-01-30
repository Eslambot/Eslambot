import telebot
import random
import datetime

tok = "8017430249:AAHq2vIXxcbDUF1bQE6s54bIbDgVDkuaHgU"  
bot = telebot.TeleBot(tok)
first_names = ['Juan', 'Maria', 'Jose', 'Ana', 'Pedro', 'Luis', 'Carmen', 'Ramon', 'Elena', 'Carlos']
last_names = ['Dela Cruz', 'Garcia', 'Reyes', 'Ramos', 'Mendoza', 'Santos', 'Flores', 'Gonzales', 'Bautista', 'Villanueva']
domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']
cities = ['Manila', 'Cebu City', 'Davao City', 'Quezon City', 'Makati']
provinces = ['Metro Manila', 'Cebu', 'Davao del Sur', 'Quezon', 'Rizal']
streets = ['Rizal', 'Bonifacio', 'Aguinaldo', 'Mabini', 'Quezon']
street_types = ['Street', 'Avenue', 'Boulevard', 'Road']

def generate_random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_email(name):
    return f"{name.lower().replace(' ', '.')}@{random.choice(domains)}"

def generate_random_phone():
    return f"09{random.randint(100000000, 999999999)}"

def generate_random_id():
    return f"{random.randint(1000, 9999)}-{random.randint(100000, 999999)}-{random.randint(0, 9)}"

def generate_random_address():
    return f"{random.randint(100, 999)} {random.choice(streets)} {random.choice(street_types)}"

def generate_random_postal_code():
    return f"{random.randint(1000, 9999)}"

def generate_random_birthdate():
    year = random.randint(1970, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{day:02d}/{month:02d}/{year}"

def generate_random_gender():
    return random.choice(["ذكر", "أنثى"])

def generate_random_balance():
    return f"${random.randint(100, 10000):,.2f}"

def generate_fake_paypal_details():
    full_name = generate_random_name()
    email = generate_random_email(full_name)
    phone = generate_random_phone()
    personal_id = generate_random_id()
    street = generate_random_address()
    postal_code = generate_random_postal_code()
    city = random.choice(cities)
    state = random.choice(provinces)
    birthdate = generate_random_birthdate()
    gender = generate_random_gender()
    balance = generate_random_balance()

    message = (
        "🌟 **تفاصيل حساب PayPal وهمي** 🌟\n\n"
        f"👤 **الاسم الكامل**: {full_name}\n"
        f"📧 **البريد الإلكتروني**: {email}\n"
        f"📞 **رقم الهاتف**: {phone}\n"
        f"🆔 **رقم الهوية**: {personal_id}\n"
        f"🎂 **تاريخ الميلاد**: {birthdate}\n"
        f"🚻 **الجنس**: {gender}\n"
        f"💰 **الرصيد**: {balance}\n\n"
        "🏠 **العنوان**:\n"
        f"   - **الشارع**: {street}\n"
        f"   - **الرمز البريدي**: {postal_code}\n"
        f"   - **المدينة**: {city}\n"
        f"   - **الولاية**: {state}\n\n"
        f"🔗 **تم الإنشاء بواسطة**: 𝗘𝗦𝗟𝗮𝗺\n"
        f"📅 **تاريخ الإنشاء**: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    )

    return message

def welcome_message():
    return (
        "🌺 **أهلاً وسهلاً !** 🌺\n\n"
        "مرحباً فيك، هذا البوت يساعدك بإنشاء معلومات عشوائية حقيقية.\n"
        "إذا تريد معلومات، اكتب `/es` وانتظر النتيجة.\n\n"
        "مع السلامة! ❤️"
    )

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, welcome_message(), parse_mode="Markdown")

@bot.message_handler(commands=['es'])
def send_fake_details(message):
    bot.send_message(message.chat.id, generate_fake_paypal_details(), parse_mode="Markdown")

print("تم البدأ روح لبوتك !")
bot.infinity_polling()
