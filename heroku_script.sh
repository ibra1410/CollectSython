#!/usr/bin/env bash

# تثبيت Git
apt update && apt upgrade -y
apt install git -y

# استنساخ مشروع من مستودع Git
git clone https://github.com/sythontm/CollectSython

# الانتقال إلى دليل المشروع
cd CollectSython

# تثبيت التبعيات باستخدام sy-install.py
python3 sy-install.py

# بعد ذلك، انتظر قليلاً ثم قم بإدخال توكن البوت وايدي الحساب وعدد الحسابات يدويًا
