# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 13:33:35 2025

@author: pc
"""
#ikiye bölme algoritması
import numpy as np

# Fonksiyon ve türevi
def f(x):
    return (x - 1)**2 * (x - 2) * (x - 3)

def df(x):
    return 3 * x**2 - 12 * x + 11  # f'(x)

# İkiye-bölme algoritması
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
xa = 1.0
xb = 2.5
minimum_nokta = ikiye_bolme_algoritmasi(df, xa, xb)
print(f"Yaklaşık ekstremum noktası: x = {minimum_nokta:.6f}, f(x) = {f(minimum_nokta):.6f}")
