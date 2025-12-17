# Tamin DBF to PostgreSQL Converter

A Python/Django utility designed to liberate data from the legacy **ListDisk** software used by **Tamin Ejtemaei (Iranian Social Security Organization)**.

It parses the archaic `.dbf` (FoxPro/dBase) files, handles the legacy Farsi encodings (IranSystem/CP1256), and imports clean data into a modern **PostgreSQL** database.

## 🎯 The Problem

Companies in Iran are forced to use old, limited software to generate insurance files. The data is locked in DBF files with non-standard encodings, making it impossible to analyze or integrate with modern HR systems.

## ✨ Features

- **Legacy Decoding:** Handles custom Farsi character sets (IranSystem/Windows-1256).
- **Data Structuring:** Maps flat DBF structures to Relational SQL models (`Employee`, `Workplace`, `MonthlyList`).
- **Modern Stack:** Built on Django 5 & PostgreSQL.
- **Dockerized:** Ready to run in containers.

## 🛠 Usage

1. **Setup:**
   ```bash
   docker-compose up -d
   ```
