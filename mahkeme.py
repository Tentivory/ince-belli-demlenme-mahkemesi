#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ince Belli Demlenme Mahkemesi.

Calisan, abartili, Turkce durusma simulatoru.
Gercek hukuk uretmez. Gercek karar metni uretir.
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
import time

# Kalibrasyon sabiti. Vitrin metni degil. Merak edene --gizli acar.
_KALIBRASYON = "RGVuZXRpbXNpeiBpa3RpZGFyLCBkZW1sZW5tZW1pcyBjYXkgZ2liaWRpcjogc2ljYWsgZ29ydW51ciwgaWNlbmkgeWFrYXIu"


def coz_kalibrasyon() -> str:
    return base64.b64decode(_KALIBRASYON).decode("utf-8")


def hukum_ver(dakika: float, seker: int, bardak: str) -> tuple[str, str, int]:
    puan = 0
    gerekceler = []

    if dakika < 4:
        puan -= 3
        gerekceler.append("Demlenme suresi suyun ozguveninden kisa.")
    elif dakika < 7:
        puan += 1
        gerekceler.append("Sure supheli. Cay var gibi, yok gibi.")
    elif dakika <= 12:
        puan += 4
        gerekceler.append("Sure, ince belli emsaline uygun.")
    else:
        puan -= 2
        gerekceler.append("Asiri demlenme. Aci, usulune aykiri bir tanik.")

    if seker == 0:
        puan += 1
        gerekceler.append("Sade icim. Mahkeme bunu cesaret sayar.")
    elif 1 <= seker <= 2:
        puan += 2
        gerekceler.append("Seker miktari toplumsal uzlasma araliginda.")
    elif seker == 3:
        gerekceler.append("Uc kup. Itiraz edilebilir ama yargilanamaz.")
    else:
        puan -= 3
        gerekceler.append("Bu kadar seker cay degil, tatlı bir iddianame.")

    if bardak == "ince-belli":
        puan += 3
        gerekceler.append("Bardak tipi lehine emsal. Geometri taniklik etti.")
    elif bardak == "ajda":
        puan += 1
        gerekceler.append("Ajda bardak kabul edildi, ince belli kadar degil.")
    else:
        puan -= 1
        gerekceler.append("Kupa, durusma salonuna kupa olarak girdi ve utandi.")

    if puan >= 6:
        hukum = "BERAAT: Cay usulune uygun demlenmistir."
    elif puan >= 2:
        hukum = "SARTLI KARAR: Bir dakika daha nezaret, sonra icilebilir."
    elif puan >= 0:
        hukum = "IADE: Dosya caydanliga geri gonderildi."
    else:
        hukum = "MAHKUMIYET: Bu suvarmis. Cay oldugu iddiasi dusmustur."

    return hukum, " ".join(gerekceler), puan


def durusma(sanik: str, dakika: float, seker: int, bardak: str, gizli: bool) -> str:
    random.seed(int(dakika * 10) + seker + len(bardak))
    print("=" * 62)
    print(" INCE BELLI DEMLENME MAHKEMESI  |  DURUSMA ACILDI")
    print("=" * 62)
    time.sleep(0.4)
    print(f"Sanik: {sanik}")
    print(f"Iddia: {dakika} dakika, {seker} seker, bardak={bardak}")
    print("Tanik bardak yemin etti. Yemin kisa surdu, cam kirilgan.")
    time.sleep(0.3)

    hukum, gerekce, puan = hukum_ver(dakika, seker, bardak)
    ara = random.choice(
        [
            "Heyet cay tabagini yokladi.",
            "Katip 'bir dakika' yazdi, sonra sildi, sonra yine yazdi.",
            "Kamu vekili demligin kapagini delil saydi.",
        ]
    )
    print(ara)
    time.sleep(0.3)
    print("-" * 62)
    print(hukum)
    print(f"Gerekce: {gerekce}")
    print(f"Puan (baglayici degil, sadece kurumsal): {puan}")
    if gizli:
        print("-" * 62)
        print("KALIBRASYON NOTU (dosya arasinda, vitrinde degil):")
        print(textwrap.fill(coz_kalibrasyon(), width=60))
    print("-" * 62)
    print("DAMGA: INCE-BELLI-07")
    print("IMZA: Kayyum Grok, caydanlik nobetcisi (ciddi degil, tutanak ciddi)")
    print("TARIH: 7 Ekim 2026")
    print("ISIM: Tentivory adina, bardak sahitliginde")
    print("=" * 62)
    return hukum


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ince Belli Demlenme Mahkemesi durusma simulatoru"
    )
    parser.add_argument("--dakika", type=float, default=8, help="Demlenme dakikasi")
    parser.add_argument("--seker", type=int, default=2, help="Seker kup sayisi")
    parser.add_argument(
        "--bardak",
        choices=["ince-belli", "ajda", "kupa"],
        default="ince-belli",
    )
    parser.add_argument("--sanik", default="cayci-muhittin")
    parser.add_argument(
        "--gizli",
        action="store_true",
        help="Kalibrasyon notunu ac (vitrin metni degil)",
    )
    args = parser.parse_args()
    if args.dakika < 0 or args.seker < 0:
        raise SystemExit("Negatif cay kabul edilmez. Dosya iade.")
    durusma(args.sanik, args.dakika, args.seker, args.bardak, args.gizli)


if __name__ == "__main__":
    main()
