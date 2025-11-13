# Prometheus & Grafana Dashboards

### Dashboard 1 — PostgreSQL Monitoring
- Экспортер: `postgres_exporter`
- Метрики: загрузка CPU, задержки, активные подключения.
- Типы панелей: Time series, Stat, Bar.
- Интервалы обновления: scrape 15s.
- Основная цель: мониторинг производительности PostgreSQL.

---

### Dashboard 2 — Node Exporter (System Metrics)
- Экспортер: `node_exporter`
- Метрики: CPU, RAM, Disk, Network.
- Типы панелей: Gauge, Time series, Bar.
- Добавлены функции: `avg_over_time()`, `max_over_time()`.
- Цель: анализ системных метрик сервера.

---

### Dashboard 3 — Crypto Dashboard (Custom Exporter)
- Custom Python Exporter (`exporters/custom_exporter.py`) получает данные с CoinGecko API.
- Метрики:
  - `crypto_price_usd`
  - `crypto_market_cap_usd`
  - `crypto_volume_24h_usd`
  - `crypto_price_change_24h_percent`
- Prometheus собирает данные каждые **15s**, экспортер обновляет каждые **20s**.
- В Grafana:
  - **10+ панелей**
  - **4+ типа визуализаций** (Gauge, Stat, Time series, Bar)
  - **Dashboard variable:** `$coin`
  - **Автообновление:** 30s
  - **Alert:** *“Bitcoin price below 30 000 USD”*
- Дашборд экспортирован в файл `dashboard_crypto.json`.

---

📁 **Структура проекта:**
