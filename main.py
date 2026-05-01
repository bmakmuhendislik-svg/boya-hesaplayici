import flet as ft


def main(page: ft.Page):
    # Sayfa (Uygulama) Ayarları
    page.title = "Marshall Boya Sarfiyat"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 700

    # Boya Referans Değerleri Sözlüğü (m2/L)
    boya_degerleri = {
        "Antibakteriyel Hijyen": 7.0,
        "Sil-Pak (10 kat fazla silinir)": 7.0,
        "Silikonlu Özel Mat (Amiral Gemi)": 7.0,
        "Lüksima Özel Mat": 7.0,
        "Maximum Silikonlu İpek Mat": 8.0,
        "Plastik Mat": 7.0,
        "Maximum Silikonlu Mat (1.Sınıf)": 7.0,
        "Tavan Boyası **": 7.0,
        "Pastel Yarı Mat": 10.0,
        "Pastel Mat": 10.0,
        "Geçiş Astarı (*Tek Kat)": 15.0,
        "Saten Alçı Astarı (*Tek Kat)": 25.0,
        "FİT Silikonlu": 7.0,
        "Akrikor Elastomerik (Özel İş)": 2.5,
        "Akrikor Saf Akrilik (Özel İş)": 2.5,
        "Akrikor Silikonlu+Akrilik": 2.5,
        "Akrikor Anti Alkali + Akrilik Grenli": 0.75,
        "Akrikor Anti Alkali + Örtücü Astar (1 kat)": 15.0,
        "Akrikor Silikonlu+ Örtücü Astar (1 kat)": 9.25,
        "Akrikor Akrilik": 2.5
    }

    # Logo (Dosya yoksa hata vermemesi için basit bir kontrol yapılabilir, Flet web url de destekler)
    logo = ft.Image(src=f"marshall_logo.png", width=150, height=60, fit=ft.ImageFit.CONTAIN)

    # Başlık
    baslik = ft.Text("Boya Sarfiyat Hesaplama", size=22, weight=ft.FontWeight.BOLD)

    # Boya Seçimi Dropdown
    boya_secici = ft.Dropdown(
        label="Boya Çeşidi Seçiniz",
        options=[ft.dropdown.Option(isim) for isim in boya_degerleri.keys()],
        value="Antibakteriyel Hijyen",
        width=350
    )

    # Alan Girişi
    alan_girisi = ft.TextField(
        label="Boyanacak Alan (m²)",
        hint_text="Örn: 120",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=350
    )

    # Sonuç Gösterim Alanı
    sonuc_metni = ft.Text("Sonuç burada gösterilecek", size=16, color=ft.colors.BLACK87, weight=ft.FontWeight.W_500)
    sonuc_kutusu = ft.Container(
        content=sonuc_metni,
        bgcolor=ft.colors.BLUE_GREY_50,
        padding=20,
        border_radius=10,
        width=350,
        alignment=ft.alignment.center
    )

    # Hesaplama Fonksiyonu
    def hesapla(e):
        try:
            # Kullanıcı virgül girerse noktaya çevir
            alan = float(alan_girisi.value.replace(',', '.'))
            if alan <= 0:
                raise ValueError

            secilen_boya = boya_secici.value
            sarfiyat_orani = boya_degerleri[secilen_boya]
            gerekli_litre = alan / sarfiyat_orani

            sonuc_metni.value = f"Boya Tipi: {secilen_boya}\nSarfiyat Değeri: {sarfiyat_orani} m²/L\nGerekli Miktar: {gerekli_litre:.2f} Litre"
            sonuc_metni.color = ft.colors.GREEN_800
        except:
            sonuc_metni.value = "Lütfen geçerli bir alan değeri (m²) giriniz!"
            sonuc_metni.color = ft.colors.RED_700

        page.update()

    # Hesapla Butonu
    hesapla_btn = ft.ElevatedButton(
        text="HESAPLA",
        on_click=hesapla,
        width=350,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_800,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    # Geliştirici Bilgisi
    footer = ft.Text(
        "Programlayan: Fatih Faruk Markal\nB-MAK Mühendislik & Mimarlık",
        size=12,
        color=ft.colors.GREY_600,
        text_align=ft.TextAlign.CENTER
    )

    # Elemanları Sayfaya Ekle
    page.add(
        logo,
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
        baslik,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        boya_secici,
        alan_girisi,
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
        hesapla_btn,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        sonuc_kutusu,
        ft.Divider(height=40, color=ft.colors.TRANSPARENT),
        footer
    )


ft.app(target=main)