# PythonAutomate
Here are Python scripts for automation  <br />
Automatization the boring staff :-) <br />
![python_super_obrazek](https://github.com/user-attachments/assets/15ddbaf8-532f-47f5-aa74-cea12ef3cc10)

![Python Automation](https://img.shields.io/badge/Python%20Automation-yellowblue?style=flat-square)



### ⚙️ **Správa systému a serveru**

* **`os` a `subprocess`** (standardní knihovna) – spouštění příkazů, práce se soubory, procesy.
* **`psutil`** – získávání informací o procesech, CPU, paměti, diskových a síťových statistikách.
* **`shutil`** – kopírování, mazání a manipulace se soubory/složkami.

---

### 📡 **Síť a komunikace**

* **`paramiko`** – práce se vzdáleným serverem přes SSH, SFTP.
* **`fabric`** – vyšší úroveň nad `paramiko`, umožňuje spouštět skripty na vzdálených serverech.
* **`requests`** – volání HTTP/REST API (monitoring, správa cloudů).
* **`flask` nebo `fastapi`** – když chceš vytvořit vlastní servis/endpoint pro monitoring.

---

### 📊 **Monitoring a logování**

* **`logging`** (standardní) – logování aplikací.
* **`prometheus_client`** – export metrik pro Prometheus (monitoring).
* **`statsd`** – posílání statistik do StatsD/Graphite.
* **`rich`** nebo **`loguru`** – hezčí logy a výstupy v konzoli.

---

### ☁️ **Cloud / Kontejnery**

* **`boto3`** – AWS (EC2, S3, Lambda, …).
* **`google-cloud`** knihovny – Google Cloud služby.
* **`azure`** SDK – pro Azure.
* **`docker-py`** – správa Docker kontejnerů.
* **`kubernetes` (client-python)** – správa Kubernetes clusterů.

---

### 🔄 **Automatizace a plánování úloh**

* **`schedule`** – jednoduchý task scheduler v Pythonu.
* **`apscheduler`** – pokročilý plánovač (cron-like).
* **`celery`** – pro distribuované asynchronní úlohy.
* **`ansible`** (má i Python API) – pro správu konfigurace serverů.

---

👉 Typicky se kombinuje:

* `psutil` + `logging` pro monitoring,
* `paramiko`/`fabric` pro vzdálenou správu,
* `schedule`/`apscheduler` pro spouštění skriptů,
* a pak něco na vizualizaci/metriky (Prometheus, Grafana).

---



