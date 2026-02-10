Práctica 10: Infraestructura de Microservicios, Caché y Gestión de Versiones
📝 Descripción
Este proyecto consiste en el despliegue de una arquitectura de microservicios eficiente y segura para la empresa "Cloud-Fast". El sistema utiliza un Proxy Inverso con Nginx que gestiona una caché de nivel 1, una API en Python/Flask para la lógica de negocio y un servidor Redis como caché de nivel 2 para optimizar el rendimiento de consultas pesadas.
+1

🏗️ Arquitectura del Sistema
La infraestructura se compone de tres contenedores aislados en una red privada virtual:


Nginx (Proxy Inverso): Único punto de entrada (Puerto 80) con caché HTTP de 60 segundos.


API Service (Backend): Desarrollado en Flask, simula procesos lentos y se conecta a Redis.


Redis (Caché de Datos): Base de datos en memoria para persistencia de nivel 2, inaccesible desde el exterior.
