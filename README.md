# Laboratorio de Monitoreo y Observabilidad 📊

Este repositorio contiene la configuración especializada de observabilidad para auditar y diagnosticar el estado del ecosistema en tiempo real, implementando mecanismos avanzados de descubrimiento automático dentro de un clúster distribuido.

## 🎯 Componentes Clave

*   **Prometheus Engine**: Configurado para realizar un escaneo y raspado dinámico (*scraping*) de objetivos en Kubernetes mediante el uso de anotaciones en los servicios.
*   **Grafana Dashboards**: Paneles visuales corporativos vinculados a Prometheus como fuente de datos para trazar métricas de series temporales en tiempo real.
*   **Métricas Personalizadas**: Inyección nativa en el código de la API forzando respuestas `text/plain` (`media_type="text/plain"`) compatibles con los estándares de Prometheus para exponer indicadores de negocio críticos como `app_uptime_seconds`.

## 🛡️ Características
*   Monitoreo reactivo de Pods activos (`up == 1`).
*   Auto-descubrimiento automático de nuevos endpoints de API.
