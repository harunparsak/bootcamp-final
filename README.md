# Bootcamp Final Project

Bu proje, Flask ile geliştirilmiş, öğrenme amaçlı yapılmış basit bir mesajlaşma uygulamasıdır.
Arka planda PostgreSQL veritabanı kullanır. Uygulama, Docker konteynerlerinde çalışır ve 
yönetimi systemd servisi ile gerçekleşir.

## Özellikler

- Flask tabanlı web uygulaması
- PostgreSQL veritabanı
- Adminer ile veritabanı arayüzü
- Docker ve Docker Compose ile konteynerleştirme
- systemd ile servis haline getirme
- cron-job ile her iki dakikada bir log arşivleme

## Kurulum

Projeyi çalıştırmak için sisteminizde Docker ve Docker Compose kurulu olmalıdır.

1. Bu repoyu klonlayın:
```bash
git clone <repo-url>
cd bootcamp-final
