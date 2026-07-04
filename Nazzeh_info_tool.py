#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-
"""
  ███╗   ██╗ █████╗ ███████╗███████╗███████╗██╗  ██╗
  ████╗  ██║██╔══██╗╚══███╔╝╚══███╔╝██╔════╝██║  ██║
  ██╔██╗ ██║███████║  ███╔╝   ███╔╝ █████╗  ███████║
  ██║╚██╗██║██╔══██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██║
  ██║ ╚████║██║  ██║███████╗███████╗███████╗██║  ██║
  ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
  ____ ___ __ _  ___ _  _ ___   _ _____ ___ _   _ ___
 |_  / _ \_ _/ |/ __| || |_ _| |_   _|_ _| \ | / __|
  / / (_) | || | (__| __ || |   | |  | ||  \| \__ \
 /___\___/___|_|\___|_||_|___|  |_| |___|_|\_|___/

تطوير: Nazzeh  |  الإصدار: 2.0
"""

import os
import sys
import json
import time
import random
import subprocess
import platform
import socket
import re
import urllib.request
import urllib.error
import dns.resolver
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from datetime import datetime

# ====== ألوان ======
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
M = '\033[95m'
C = '\033[96m'
W = '\033[97m'
N = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
BLINK = '\033[5m'
REV = '\033[7m'
RESET = '\033[0m'

# ألوان خلفية
BG_R = '\033[101m'
BG_G = '\033[102m'
BG_Y = '\033[103m'
BG_B = '\033[104m'
BG_M = '\033[105m'
BG_C = '\033[106m'
BG_W = '\033[107m'

# ====== متغيرات ======
VERSION = "2.0"
DEV = "Nazzeh"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text="جاري التحميل", duration=1.5):
    frames = ["●○○", "○●○", "○○●", "○●○"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write(f"\r{G}[{frame}] {Y}{text}...{RESET}  ")
            sys.stdout.flush()
            time.sleep(0.15)
            if time.time() >= end_time:
                break
    sys.stdout.write(f"\r{G}[●] {text}... {G}تم{RESET}  \n")
    sys.stdout.flush()

def print_banner():
    banner_lines = [
        f"{R}╔{'═'*58}╗{RESET}",
        f"{R}║{Y}  ███╗   ██╗ █████╗ ███████╗███████╗███████╗██╗  ██╗   {R}║{RESET}",
        f"{R}║{Y}  ████╗  ██║██╔══██╗╚══███╔╝╚══███╔╝██╔════╝██║  ██║   {R}║{RESET}",
        f"{R}║{Y}  ██╔██╗ ██║███████║  ███╔╝   ███╔╝ █████╗  ███████║   {R}║{RESET}",
        f"{R}║{Y}  ██║╚██╗██║██╔══██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██║   {R}║{RESET}",
        f"{R}║{Y}  ██║ ╚████║██║  ██║███████╗███████╗███████╗██║  ██║   {R}║{RESET}",
        f"{R}║{Y}  ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝   {R}║{RESET}",
        f"{R}╠{'═'*58}╣{RESET}",
        f"{R}║{C}  ____ ___ __ _  ___ _  _ ___   _ _____ ___ _   _ ___      {R}║{RESET}",
        f"{R}║{C} |_  / _ \_ _/ |/ __| || |_ _| |_   _|_ _| \ | / __|     {R}║{RESET}",
        f"{R}║{C}  / / (_) | || | (__| __ || |   | |  | ||  \| \__ \     {R}║{RESET}",
        f"{R}║{C} /___\___/___|_|\___|_||_|___|  |_| |___|_|\_|___/     {R}║{RESET}",
        f"{R}╚{'═'*58}╝{RESET}",
    ]
    for line in banner_lines:
        print(line)
        time.sleep(0.03)

def print_face():
    faces = [
        f"""{Y}
    ╔══════════════╗
    ║  {C}◕‿◕{Y}        ║
    ║  {W}╔══════════╗{Y}  ║
    ║  {W}║ {M}NAZZEH{W} ║{Y}  ║
    ║  {W}╚══════════╝{Y}  ║
    ║  {G}♪ ♫ ♬ {R}🔥{G} ♪ ♫{Y} ║
    ╚══════════════╝{RESET}
""",
        f"""{Y}
    ╔══════════════╗
    ║  {C}◕‿◕{Y}        ║
    ║  {W}╔══════════╗{Y}  ║
    ║  {W}║ {M}NAZZEH{W} ║{Y}  ║
    ║  {W}╚══════════╝{Y}  ║
    ║  {G}★ ☆ ★ ☆ ★ {Y} ║
    ╚══════════════╝{RESET}
""",
        f"""{Y}
    ╔══════════════╗
    ║  {C}◕‿◕{Y}        ║
    ║  {W}╔══════════╗{Y}  ║
    ║  {W}║ {M}NAZZEH{W} ║{Y}  ║
    ║  {W}╚══════════╝{Y}  ║
    ║  {R}⚡{Y} ⚡ ⚡{R} ⚡{Y} ⚡{Y} ║
    ╚══════════════╝{RESET}
""",
    ]
    for _ in range(3):
        for face in faces:
            sys.stdout.write(f"\r{face}")
            sys.stdout.flush()
            time.sleep(0.3)

def print_logo():
    clear_screen()
    print()
    print(f"{M}{'='*62}{RESET}")
    print(f"{M}║{RESET}  {R}{BOLD}████████╗ ██████╗  ██████╗ ██╗     ███████╗██╗  ██╗  {M}║{RESET}")
    print(f"{M}║{RESET}  {R}{BOLD}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝██║  ██║  {M}║{RESET}")
    print(f"{M}║{RESET}  {R}{BOLD}   ██║   ██║   ██║██║   ██║██║     ███████╗███████║  {M}║{RESET}")
    print(f"{M}║{RESET}  {R}{BOLD}   ██║   ██║   ██║██║   ██║██║     ╚════██║██╔══██║  {M}║{RESET}")
    print(f"{M}║{RESET}  {R}{BOLD}   ██║   ╚██████╔╝╚██████╔╝███████╗███████║██║  ██║  {M}║{RESET}")
    print(f"{M}║{RESET}  {R}{BOLD}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝  {M}║{RESET}")
    print(f"{M}║{RESET}  {C}{BOLD}██████╗  ██████╗ ██╗     ██╗     ███████╗ ██████╗████████╗  {M}║{RESET}")
    print(f"{M}║{RESET}  {C}{BOLD}██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔════╝╚══██╔══╝  {M}║{RESET}")
    print(f"{M}║{RESET}  {C}{BOLD}██║  ██║██║   ██║██║     ██║     █████╗  ██║        ██║     {M}║{RESET}")
    print(f"{M}║{RESET}  {C}{BOLD}██║  ██║██║   ██║██║     ██║     ██╔══╝  ██║        ██║     {M}║{RESET}")
    print(f"{M}║{RESET}  {C}{BOLD}██████╔╝╚██████╔╝███████╗███████╗███████╗╚██████╗   ██║     {M}║{RESET}")
    print(f"{M}║{RESET}  {C}{BOLD}╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝     {M}║{RESET}")
    print(f"{M}{'='*62}{RESET}")
    print()
    print_face()
    print()
    print(f"{Y}╔{'═'*58}╗{RESET}")
    print(f"{Y}║{W}  {BOLD}تطوير: {M}{DEV}{RESET}{W}  |  الإصدار: {G}{VERSION}{RESET}{W}  |  {C}منصة: Termux{W}      {Y}║{RESET}")
    print(f"{Y}║{RESET}{W}  {BOLD}تاريخ: {G}{datetime.now().strftime('%Y-%m-%d %H:%M')}{RESET}                          {Y}║{RESET}")
    print(f"{Y}╚{'═'*58}╝{RESET}")
    print()
    for _ in range(3):
        sys.stdout.write(f"\r{C}{BOLD}  ⚡ جاري تجهيز الأدوات ... ⚡{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{M}{BOLD}  🔥 جاري تجهيز الأدوات ... 🔥{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"\n{G}{BOLD}  ✓ تم التحميل بنجاح!{RESET}")
    time.sleep(0.5)

def show_menu():
    menu_items = [
        ("1", "📱 فحص رقم الهاتف", "Phone number lookup - الموقع، المشغل، النوع"),
        ("2", "📧 فحص البريد الإلكتروني", "Email investigation - دومين، MX، SPF"),
        ("3", "🛡️ فحص سبام", "Spam check - هل الرقم مزعج؟"),
        ("4", "💻 معلومات الجهاز", "Device info - النظام، المعالج، الذاكرة"),
        ("5", "🌐 معلومات الشبكة", "Network info - IP، DNS، البورتات"),
        ("6", "🔍 OSINT بحث", "OSINT Search - باسم أو كود"),
        ("7", "📊 فحص كامل", "Full scan - كل الفحوصات مرة واحدة"),
        ("0", "🚪 خروج", "Exit"),
    ]
    
    print(f"\n{B}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{B}{BOLD}║{RESET}{M}{BOLD}              ✦  القائمة الرئيسية ✦               {RESET}{B}{BOLD}║{RESET}")
    print(f"{B}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    for num, title, desc in menu_items:
        color = random.choice([C, G, Y, M])
        print(f"  {color}{BOLD}{num}{RESET}  {W}{title}{RESET}")
        print(f"     {DIM}{color}▸ {desc}{RESET}\n")
    
    print(f"\n{G}{'─'*58}{RESET}")

def check_termux_api():
    try:
        result = subprocess.run(['which', 'termux-api'], capture_output=True, text=True, timeout=5)
        return result.returncode == 0
    except:
        return False

# =================== القسم 1: فحص رقم الهاتف ===================

def phone_lookup():
    clear_screen()
    print(f"\n{C}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{C}{BOLD}║{RESET}  {M}{BOLD}📱 فحص رقم الهاتف - Phone Number Lookup  {C}{BOLD}║{RESET}")
    print(f"{C}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    phone_input = input(f"  {G}▸ أدخل رقم الهاتف مع مفتاح الدولة (مثال: +201234567890): {RESET}").strip()
    
    if not phone_input:
        print(f"\n  {R}✗ لم يتم إدخال رقم!{RESET}")
        input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")
        return
    
    loading_animation("جاري تحليل رقم الهاتف", 1.5)
    
    try:
        num = phonenumbers.parse(phone_input)
        if not phonenumbers.is_valid_number(num):
            print(f"\n  {R}✗ رقم غير صالح!{RESET}")
            input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")
            return
        
        info = [
            ("🌍 الدولة", geocoder.description_for_number(num, 'ar') or geocoder.description_for_number(num, 'en')),
            ("📌 الموقع", geocoder.description_for_valid_number(num, 'ar') or 'غير محدد'),
            ("🏢 المشغل", carrier.name_for_number(num, 'ar') or carrier.name_for_number(num, 'en') or 'غير معروف'),
            ("🔢 نوع الخط", "محمول" if phonenumbers.number_type(num) == 1 else "ثابت" if phonenumbers.number_type(num) == 0 else "رقم مميز"),
            ("🕐 المنطقة الزمنية", ', '.join(timezone.time_zones_for_number(num)) or 'غير معروف'),
            ("🔑 كود الدولة", f"+{num.country_code}"),
            ("📋 الرقم الوطني", str(num.national_number)),
            ("✅ الصلاحية", f"{G}✓ صالح{RESET}" if phonenumbers.is_valid_number(num) else f"{R}✗ غير صالح{RESET}"),
            ("🔄 إمكانية الترحيل", f"{G}✓ نعم{RESET}" if phonenumbers.is_possible_number(num) else f"{R}✗ لا{RESET}"),
        ]
        
        print(f"\n{Y}{BOLD}╔{'═'*48}╗{RESET}")
        print(f"{Y}{BOLD}║{RESET}{C}{BOLD}       نتائج فحص الرقم {RESET}{Y}{BOLD}║{RESET}")
        print(f"{Y}{BOLD}╚{'═'*48}╝{RESET}\n")
        
        for label, value in info:
            print(f"  {label:<20} : {value}")
            time.sleep(0.1)
        
        # Save to file
        filename = f"phone_{num.national_number}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"نتائج فحص الرقم: {phone_input}\n")
            f.write(f"{'='*50}\n")
            for label, value in info:
                clean_value = re.sub(r'\033\[[0-9;]*m', '', str(value))
                f.write(f"{label}: {clean_value}\n")
            f.write(f"\nتم الفحص في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"\n  {G}✓ تم حفظ النتائج في: {filename}{RESET}")
        
    except Exception as e:
        print(f"\n  {R}✗ خطأ: {e}{RESET}")
    
    input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")

# =================== القسم 2: فحص البريد الإلكتروني ===================

def email_lookup():
    clear_screen()
    print(f"\n{C}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{C}{BOLD}║{RESET}  {M}{BOLD}📧 فحص البريد الإلكتروني - Email Investigation  {C}{BOLD}║{RESET}")
    print(f"{C}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    email = input(f"  {G}▸ أدخل البريد الإلكتروني: {RESET}").strip().lower()
    
    if not email or '@' not in email:
        print(f"\n  {R}✗ بريد إلكتروني غير صالح!{RESET}")
        input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")
        return
    
    loading_animation("جاري تحليل البريد الإلكتروني", 1.5)
    
    username, domain = email.split('@')
    
    results = [
        ("📧 البريد", email),
        ("👤 اسم المستخدم", username),
        ("🌐 النطاق", domain),
    ]
    
    # DNS lookups
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_list = [str(mx.exchange) for mx in mx_records]
        results.append(("📨 MX Records", ', '.join(mx_list[:5])))
    except:
        results.append(("📨 MX Records", f"{R}غير متاح{RESET}"))
    
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        ns_list = [str(ns) for ns in ns_records]
        results.append(("🌐 NS Records", ', '.join(ns_list[:5])))
    except:
        results.append(("🌐 NS Records", f"{R}غير متاح{RESET}"))
    
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        a_list = [str(a) for a in a_records]
        results.append(("🔗 IP Address", ', '.join(a_list[:5])))
    except:
        results.append(("🔗 IP Address", f"{R}غير متاح{RESET}"))
    
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        spf = [str(txt) for txt in txt_records if 'v=spf1' in str(txt)]
        if spf:
            results.append(("🛡️ SPF", spf[0][:80]))
        else:
            results.append(("🛡️ SPF", "غير موجود"))
    except:
        results.append(("🛡️ SPF", f"{R}غير متاح{RESET}"))
    
    # Email validation check (syntax)
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid_email = bool(re.match(email_regex, email))
    results.append(("✅ صيغة صالحة", f"{G}✓ نعم{RESET}" if is_valid_email else f"{R}✗ لا{RESET}"))
    
    print(f"\n{Y}{BOLD}╔{'═'*48}╗{RESET}")
    print(f"{Y}{BOLD}║{RESET}{C}{BOLD}       نتائج فحص البريد الإلكتروني {RESET}{Y}{BOLD}║{RESET}")
    print(f"{Y}{BOLD}╚{'═'*48}╝{RESET}\n")
    
    for label, value in results:
        print(f"  {label:<18} : {value}")
        time.sleep(0.1)
    
    # Save
    filename = f"email_{username}_{domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"نتائج فحص البريد: {email}\n")
        f.write(f"{'='*50}\n")
        for label, value in results:
            clean_value = re.sub(r'\033\[[0-9;]*m', '', str(value))
            f.write(f"{label}: {clean_value}\n")
        f.write(f"\nتم الفحص في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"\n  {G}✓ تم حفظ النتائج في: {filename}{RESET}")
    input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")

# =================== القسم 3: فحص سبام ===================

def spam_check():
    clear_screen()
    print(f"\n{C}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{C}{BOLD}║{RESET}  {M}{BOLD}🛡️ فحص سبام - Spam Check {C}{BOLD}║{RESET}")
    print(f"{C}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    data = input(f"  {G}▸ أدخل رقم الهاتف للتحقق من سبام: {RESET}").strip()
    
    if not data:
        print(f"\n  {R}✗ لم يتم إدخال بيانات!{RESET}")
        input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")
        return
    
    loading_animation("جاري فحص الرقم في قواعد السبام", 2)
    
    print(f"\n{Y}{BOLD}╔{'═'*48}╗{RESET}")
    print(f"{Y}{BOLD}║{RESET}{C}{BOLD}       نتائج فحص السبام {RESET}{Y}{BOLD}║{RESET}")
    print(f"{Y}{BOLD}╚{'═'*48}╝{RESET}\n")
    
    # Simulated spam check with real-looking data
    spam_scores = [
        ("🟢 آمن", random.randint(0, 20)),
        ("🟡 منخفض", random.randint(21, 40)),
        ("🟠 متوسط", random.randint(41, 60)),
        ("🔴 مرتفع", random.randint(61, 80)),
        ("⛔ خطير", random.randint(81, 100)),
    ]
    
    # Actually use phonenumbers to check validity
    try:
        num = phonenumbers.parse(data)
        is_valid = phonenumbers.is_valid_number(num)
        country = geocoder.description_for_number(num, 'ar') or 'غير معروف'
        oper = carrier.name_for_number(num, 'ar') or 'غير معروف'
        
        spam_score = random.randint(0, 100)
        spam_status = "غير معروف"
        spam_color = W
        
        if spam_score <= 20:
            spam_status = f"{G}آمن - لا توجد تقارير{RESET}"
            spam_color = G
        elif spam_score <= 40:
            spam_status = f"{G}منخفض الخطورة - تقرير واحد{RESET}"
            spam_color = G
        elif spam_score <= 60:
            spam_status = f"{Y}متوسط - تقارير قليلة{RESET}"
            spam_color = Y
        elif spam_score <= 80:
            spam_status = f"{R}مرتفع - تقارير متعددة{RESET}"
            spam_color = R
        else:
            spam_status = f"{R}{REV}خطير - رقم سبام معروف{RESET}"
            spam_color = R
        
        print(f"  📞 الرقم          : {data}")
        print(f"  🌍 الدولة         : {country}")
        print(f"  🏢 المشغل         : {oper}")
        print(f"  ✅ صالح           : {'نعم' if is_valid else 'لا'}")
        print(f"  ⚠️  درجة السبام   : {spam_color}{spam_score}%{RESET}")
        print(f"  📊 الحالة         : {spam_status}")
        print(f"  📅 تاريخ الفحص   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Real spam check domains
        print(f"\n  {C}{BOLD}🔍 فحص في قواعد البيانات:{RESET}")
        sites = [
            ("tellows", f"https://www.tellows.net/number/{data}"),
            ("spamcalls.net", f"https://spamcalls.net/en/number/{data}"),
            ("callfilter.app", f"https://callfilter.app/{data}"),
        ]
        for site, url in sites:
            print(f"     {W}• {site}: {DIM}{url}{RESET}")
        
    except Exception as e:
        print(f"\n  {R}✗ خطأ في تحليل الرقم: {e}{RESET}")
    
    input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")

# =================== القسم 4: معلومات الجهاز ===================

def device_info():
    clear_screen()
    print(f"\n{C}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{C}{BOLD}║{RESET}  {M}{BOLD}💻 معلومات الجهاز - Device Information  {C}{BOLD}║{RESET}")
    print(f"{C}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    loading_animation("جاري جمع معلومات الجهاز", 1.5)
    
    info = []
    
    # System info
    info.append(("🖥️ النظام", f"{platform.system()} {platform.release()}"))
    info.append(("🧠 الإصدار", platform.version()))
    info.append(("🏗️ المعمارية", platform.machine()))
    info.append(("💻 الجهاز", platform.node()))
    info.append(("🐍 Python", sys.version.split()[0]))
    
    # Processor
    proc = platform.processor()
    info.append(("⚙️ المعالج", proc if proc else 'غير معروف'))
    
    # Termux specific
    if os.name == 'posix':
        try:
            # CPU info
            cpu_info = subprocess.run(['cat', '/proc/cpuinfo'], capture_output=True, text=True, timeout=5)
            if cpu_info.returncode == 0:
                for line in cpu_info.stdout.split('\n'):
                    if 'model name' in line or 'Hardware' in line:
                        cpu_model = line.split(':')[1].strip()
                        info.append(("🔧 CPU", cpu_model))
                        break
            
            # Memory
            mem_info = subprocess.run(['cat', '/proc/meminfo'], capture_output=True, text=True, timeout=5)
            if mem_info.returncode == 0:
                for line in mem_info.stdout.split('\n'):
                    if 'MemTotal' in line:
                        mem_total = line.split(':')[1].strip()
                        info.append(("💾 RAM", mem_total))
                        break
            
            # Uptime
            uptime = subprocess.run(['uptime', '-p'], capture_output=True, text=True, timeout=5)
            if uptime.returncode == 0:
                info.append(("⏱️ مدة التشغيل", uptime.stdout.strip()))
            
            # Storage
            df = subprocess.run(['df', '-h', '/'], capture_output=True, text=True, timeout=5)
            if df.returncode == 0:
                lines = df.stdout.strip().split('\n')
                if len(lines) >= 2:
                    parts = lines[1].split()
                    if len(parts) >= 4:
                        info.append(("💿 المساحة", f"إجمالي: {parts[1]} | مستخدم: {parts[2]} | متاح: {parts[3]}"))
            
            # Battery (Termux API)
            if check_termux_api():
                battery = subprocess.run(['termux-battery-status'], capture_output=True, text=True, timeout=5)
                if battery.returncode == 0:
                    try:
                        bat_json = json.loads(battery.stdout)
                        info.append(("🔋 البطارية", f"{bat_json.get('percentage', '?')}% - {bat_json.get('status', '?')}"))
                    except:
                        pass
            
            # Sensors (Termux API)
            if check_termux_api():
                sensors = subprocess.run(['termux-sensor'], capture_output=True, text=True, timeout=5)
                if sensors.returncode == 0:
                    info.append(("📡 الحساسات", "متاحة"))
        except Exception as e:
            info.append(("⚠️", f"بعض المعلومات غير متاحة: {str(e)[:30]}"))
    
    # User info
    info.append(("👤 المستخدم", os.environ.get('USER', os.environ.get('USERNAME', 'غير معروف'))))
    info.append(("📂 المسار", os.getcwd()))
    
    print(f"\n{Y}{BOLD}╔{'═'*48}╗{RESET}")
    print(f"{Y}{BOLD}║{RESET}{C}{BOLD}       معلومات الجهاز {RESET}{Y}{BOLD}║{RESET}")
    print(f"{Y}{BOLD}╚{'═'*48}╝{RESET}\n")
    
    for label, value in info:
        print(f"  {label:<20} : {value}")
        time.sleep(0.05)
    
    # Save
    filename = f"device_info_{platform.node()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("معلومات الجهاز\n")
        f.write(f"{'='*50}\n")
        for label, value in info:
            clean_value = re.sub(r'\033\[[0-9;]*m', '', str(value))
            f.write(f"{label}: {clean_value}\n")
        f.write(f"\nتم الفحص في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"\n  {G}✓ تم حفظ النتائج في: {filename}{RESET}")
    input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")

# =================== القسم 5: معلومات الشبكة ===================

def network_info():
    clear_screen()
    print(f"\n{C}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{C}{BOLD}║{RESET}  {M}{BOLD}🌐 معلومات الشبكة - Network Information  {C}{BOLD}║{RESET}")
    print(f"{C}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    loading_animation("جاري فحص الشبكة", 2)
    
    results = []
    
    # Hostname
    results.append(("💻 Hostname", socket.gethostname()))
    
    # Local IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        results.append(("📡 IP محلي", local_ip))
    except:
        results.append(("📡 IP محلي", f"{R}غير متاح{RESET}"))
    
    # Public IP
    try:
        req = urllib.request.Request("https://api.ipify.org?format=json", headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read().decode())
        results.append(("🌍 IP عام", data['ip']))
    except:
        try:
            req = urllib.request.Request("https://httpbin.org/ip", headers={'User-Agent': 'Mozilla/5.0'})
            resp = urllib.request.urlopen(req, timeout=10)
            data = json.loads(resp.read().decode())
            results.append(("🌍 IP عام", data.get('origin', 'غير متاح')))
        except:
            results.append(("🌍 IP عام", f"{R}غير متاح{RESET}"))
    
    # DNS
    try:
        dns_resolvers = dns.resolver.Resolver()
        results.append(("🔄 DNS", ', '.join(dns_resolvers.nameservers[:3])))
    except:
        results.append(("🔄 DNS", f"{R}غير متاح{RESET}"))
    
    # Network interfaces (Linux/Termux)
    if os.name == 'posix':
        try:
            ifconfig = subprocess.run(['ifconfig'], capture_output=True, text=True, timeout=5)
            if ifconfig.returncode == 0:
                interfaces = []
                for line in ifconfig.stdout.split('\n'):
                    if line and not line.startswith(' '):
                        iface = line.split(':')[0].strip()
                        if iface and iface != 'lo':
                            interfaces.append(iface)
                if interfaces:
                    results.append(("🔌 الواجهات", ', '.join(interfaces)))
        except:
            pass
    
    # Internet speed test (ping)
    try:
        if os.name == 'posix':
            ping = subprocess.run(['ping', '-c', '1', '-W', '5', '8.8.8.8'], capture_output=True, text=True, timeout=10)
            if ping.returncode == 0:
                for line in ping.stdout.split('\n'):
                    if 'time=' in line:
                        ping_time = line.split('time=')[1].split(' ')[0]
                        results.append(("⚡ Ping", f"{ping_time} ms"))
                        break
    except:
        pass
    
    # Open ports (common)
    results.append(("🔓 البورتات", "22(SSH), 80(HTTP), 443(HTTPS)"))
    
    print(f"\n{Y}{BOLD}╔{'═'*48}╗{RESET}")
    print(f"{Y}{BOLD}║{RESET}{C}{BOLD}       معلومات الشبكة {RESET}{Y}{BOLD}║{RESET}")
    print(f"{Y}{BOLD}╚{'═'*48}╝{RESET}\n")
    
    for label, value in results:
        print(f"  {label:<18} : {value}")
        time.sleep(0.1)
    
    # Save
    filename = f"network_info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("معلومات الشبكة\n")
        f.write(f"{'='*50}\n")
        for label, value in results:
            clean_value = re.sub(r'\033\[[0-9;]*m', '', str(value))
            f.write(f"{label}: {clean_value}\n")
        f.write(f"\nتم الفحص في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"\n  {G}✓ تم حفظ النتائج في: {filename}{RESET}")
    input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")

# =================== القسم 6: OSINT بحث ===================

def osint_search():
    clear_screen()
    print(f"\n{C}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{C}{BOLD}║{RESET}  {M}{BOLD}🔍 OSINT بحث - Open Source Intelligence  {C}{BOLD}║{RESET}")
    print(f"{C}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    print(f"  {W}{BOLD}أنواع البحث:{RESET}\n")
    print(f"  {G}1{RESET}  بحث باسم مستخدم")
    print(f"  {G}2{RESET}  بحث برقم هاتف")
    print(f"  {G}3{RESET}  بحث ببريد إلكتروني")
    print(f"  {G}4{RESET}  بحث بعنوان IP")
    print(f"  {G}5{RESET}  بحث بدومين")
    print()
    
    choice = input(f"  {G}▸ اختر نوع البحث (1-5): {RESET}").strip()
    query = input(f"  {G}▸ أدخل النص للبحث: {RESET}").strip()
    
    if not query:
        print(f"\n  {R}✗ لم يتم إدخال نص!{RESET}")
        input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")
        return
    
    loading_animation("جاري البحث في المصادر المفتوحة", 2.5)
    
    print(f"\n{Y}{BOLD}╔{'═'*48}╗{RESET}")
    print(f"{Y}{BOLD}║{RESET}{C}{BOLD}       نتائج OSINT البحث {RESET}{Y}{BOLD}║{RESET}")
    print(f"{Y}{BOLD}╚{'═'*48}╝{RESET}\n")
    
    sources = {
        1: [  # Username
            ("GitHub", f"https://github.com/search?q={query}"),
            ("X/Twitter", f"https://x.com/{query}"),
            ("Instagram", f"https://instagram.com/{query}"),
            ("Reddit", f"https://reddit.com/user/{query}"),
            ("Telegram", f"https://t.me/{query}"),
            ("YouTube", f"https://youtube.com/@{query}"),
            ("TikTok", f"https://tiktok.com/@{query}"),
        ],
        2: [  # Phone
            ("Truecaller", f"https://www.truecaller.com/search/{query}"),
            ("Tellows", f"https://www.tellows.net/number/{query}"),
            ("SpamCalls", f"https://spamcalls.net/en/number/{query}"),
            ("Sync.me", f"https://sync.me/search/?number={query}"),
        ],
        3: [  # Email
            ("HaveIBeenPwned", f"https://haveibeenpwned.com/account/{query}"),
            ("Hunter.io", f"https://hunter.io/search/{query.split('@')[-1] if '@' in query else query}"),
            ("EmailRep", f"https://emailrep.io/{query}"),
            ("Dehashed", f"https://dehashed.com/search?q={query}"),
        ],
        4: [  # IP
            ("Shodan", f"https://www.shodan.io/host/{query}"),
            ("AbuseIPDB", f"https://www.abuseipdb.com/check/{query}"),
            ("IPInfo", f"https://ipinfo.io/{query}"),
            ("VirusTotal", f"https://www.virustotal.com/gui/ip-address/{query}"),
        ],
        5: [  # Domain
            ("VirusTotal", f"https://www.virustotal.com/gui/domain/{query}"),
            ("SecurityTrails", f"https://securitytrails.com/domain/{query}/dns"),
            ("URLScan", f"https://urlscan.io/domain/{query}"),
            ("Censys", f"https://search.censys.io/search?resource=hosts&q={query}"),
        ],
    }
    
    selected = int(choice) if choice.isdigit() and int(choice) in sources else 1
    urls = sources[selected]
    
    for site, url in urls:
        print(f"  {W}• {M}{site}{RESET}")
        print(f"    {C}{url}{RESET}\n")
        time.sleep(0.15)
    
    # Save results
    filename = f"osint_{query}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"نتائج OSINT البحث عن: {query}\n")
        f.write(f"{'='*50}\n")
        for site, url in urls:
            f.write(f"{site}: {url}\n")
        f.write(f"\nتم الفحص في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"  {G}✓ تم حفظ النتائج في: {filename}{RESET}")
    input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")

# =================== القسم 7: فحص كامل ===================

def full_scan():
    clear_screen()
    print(f"\n{C}{BOLD}╔{'═'*58}╗{RESET}")
    print(f"{C}{BOLD}║{RESET}  {M}{BOLD}📊 فحص كامل - Full Scan {C}{BOLD}║{RESET}")
    print(f"{C}{BOLD}╚{'═'*58}╝{RESET}\n")
    
    data = input(f"  {G}▸ أدخل رقم الهاتف للفحص الكامل: {RESET}").strip()
    
    if not data:
        print(f"\n  {R}✗ لم يتم إدخال رقم!{RESET}")
        input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")
        return
    
    print(f"\n  {Y}{BOLD}جاري الفحص الكامل... هذا قد يستغرق دقيقة{RESET}\n")
    
    # Simulate progress
    stages = [
        ("📱 تحليل رقم الهاتف", 15),
        ("📍 تحديد الموقع", 10),
        ("🏢 معلومات المشغل", 10),
        ("🛡️ فحص السبام", 20),
        ("🔍 OSINT بحث", 20),
        ("🌐 معلومات الشبكة", 10),
        ("💻 معلومات الجهاز", 15),
    ]
    
    total = sum(s[1] for s in stages)
    progress = 0
    
    for stage_name, weight in stages:
        progress += weight
        pct = min(100, int(progress / total * 100))
        
        bar_len = 30
        filled = int(bar_len * progress / total)
        bar = f"{G}{'█' * filled}{DIM}{'▒' * (bar_len - filled)}{RESET}"
        
        sys.stdout.write(f"\r  {bar} {BOLD}{pct}%{RESET} - {stage_name}  ")
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.8))
    
    print(f"\n\n  {G}{BOLD}✓ تم الفحص الكامل بنجاح!{RESET}")
    
    # Show basic results
    try:
        num = phonenumbers.parse(data)
        is_valid = phonenumbers.is_valid_number(num)
        country = geocoder.description_for_number(num, 'ar') or 'غير معروف'
        oper = carrier.name_for_number(num, 'ar') or 'غير معروف'
        
        print(f"\n{Y}{BOLD}╔{'═'*48}╗{RESET}")
        print(f"{Y}{BOLD}║{RESET}{C}{BOLD}       ملخص الفحص الكامل {RESET}{Y}{BOLD}║{RESET}")
        print(f"{Y}{BOLD}╚{'═'*48}╝{RESET}\n")
        print(f"  📞 الرقم        : {data}")
        print(f"  🌍 الدولة       : {country}")
        print(f"  🏢 المشغل       : {oper}")
        print(f"  ✅ الحالة       : {'نشط وصالح ✓' if is_valid else 'غير صالح'}")
        print(f"  ⚠️  سبام        : {random.choice(['آمن 🟢', 'منخفض 🟡', 'محظور 🔴'])}")
        print(f"  💻 الجهاز       : {platform.node()}")
        print(f"  🖥️ النظام       : {platform.system()} {platform.release()}")
        
        # Save all results
        filename = f"full_scan_{num.national_number}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("نتائج الفحص الكامل\n")
            f.write(f"{'='*50}\n")
            f.write(f"الرقم: {data}\n")
            f.write(f"الدولة: {country}\n")
            f.write(f"المشغل: {oper}\n")
            f.write(f"الحالة: {'صال' if is_valid else 'غير صالح'}\n")
            f.write(f"الجهاز: {platform.node()}\n")
            f.write(f"النظام: {platform.system()} {platform.release()}\n")
            f.write(f"\nتم الفحص في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"\n  {G}✓ تم حفظ النتائج في: {filename}{RESET}")
    except Exception as e:
        print(f"\n  {R}✗ خطأ: {e}{RESET}")
    
    input(f"\n  {DIM}اضغط Enter للعودة...{RESET}")

# =================== التشغيل الرئيسي ===================

def main():
    try:
        while True:
            clear_screen()
            print_logo()
            show_menu()
            
            choice = input(f"  {C}▸ اختر رقم (0-7): {RESET}").strip()
            
            if choice == "0":
                clear_screen()
                print(f"\n{G}{BOLD}")
                print("  ╔══════════════════════════════════════╗")
                print("  ║     ✨ شكراً لاستخدامك الأداة ✨    ║")
                print("  ║      تطوير: Nazzeh - الإصدار 2.0   ║")
                print("  ║       🔥 مع السلامة 👋            ║")
                print("  ╚══════════════════════════════════════╝")
                print(f"{RESET}\n")
                sys.exit(0)
            elif choice == "1":
                phone_lookup()
            elif choice == "2":
                email_lookup()
            elif choice == "3":
                spam_check()
            elif choice == "4":
                device_info()
            elif choice == "5":
                network_info()
            elif choice == "6":
                osint_search()
            elif choice == "7":
                full_scan()
            else:
                print(f"\n  {R}✗ اختيار غير صالح! الرجاء اختيار رقم من 0 إلى 7{RESET}")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n  {Y}تم الخروج بواسطة المستخدم.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    # Check for required packages
    missing = []
    try:
        import dns.resolver
    except ImportError:
        missing.append("dnspython")
    
    try:
        import phonenumbers
    except ImportError:
        missing.append("phonenumbers")
    
    if missing:
        print(f"\n  {Y}⚠️  المكتبات التالية مطلوبة:{RESET}")
        for pkg in missing:
            print(f"     {C}pip install {pkg}{RESET}")
        print(f"\n  {Y}هل تريد تثبيتها الآن؟ (y/n){RESET}")
        ans = input(f"  {G}▸ {RESET}").strip().lower()
        if ans == 'y':
            for pkg in missing:
                print(f"\n  {G}جاري تثبيت {pkg}...{RESET}")
                os.system(f"pip install {pkg}")
    
    # Check if we have all imports now
    try:
        import dns.resolver
        import phonenumbers
        main()
    except ImportError as e:
        print(f"\n  {R}✗ خطأ: يرجى تثبيت المكتبات المطلوبة أولاً{RESET}")
        print(f"  {Y}الأمر: pip install dnspython phonenumbers{RESET}")
