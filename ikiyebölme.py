# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 13:33:35 2025

@author: pc
"""

# İkiye bölme algoritması
import numpy as np

# Fonksiyon
def f(x):
    return (x1 - 2*x2 + x3+1)**2 + (x1 + x2 -x3 +3)**2 + (-2*x1 +x2 -x3)**2

# Fonksiyonun türevi
def df(x):
    # Türev hesaplama
    term1 = 2 * (x - 1) * ((x - 2) * (x - 3))  # İlk terim
    term2 = (x - 1)**2 * (2 * x - 5)           # İkinci terim
    return term1 + term2  # Toplam türev

# İkiye bölme algoritması
def ikiye_bolme_algoritmasi(f_turev, xa, xb, tol=1e-4, max_iter=100):
    # Adım 1: Başlangıç kontrolü
    if f_turev(xa) * f_turev(xb) >= 0:
        raise ValueError("Başlangıç koşulu sağlanmıyor: f'(xa) * f'(xb) < 0 olmalı.")

    for i in range(max_iter):
        # Adım 2: Orta noktayı hesapla
        xk = xa + (xb - xa) / 2

        # Adım 3: Sonlanma kontrolü
        if abs(f_turev(xk)) < 1e-10 or (xb - xa) < tol:
            return xk  # Çözüm bulundu

        # f'(xk) * f'(xa) > 0 ise xa ← xk, değilse xb ← xk
        if f_turev(xk) * f_turev(xa) > 0:
            xa = xk
        else:
            xb = xk

    return xk  # Maksimum iterasyonla bulunan yaklaşık çözüm

# Kullanım
# Yeni başlangıç aralığı seçimi
xa = 0.5
xb = 3.0

minimum_nokta = ikiye_bolme_algoritmasi(df, xa, xb)
print(f"Yaklaşık ekstremum noktası: x = {minimum_nokta:.6f}, f(x) = {f(minimum_nokta):.6f}")