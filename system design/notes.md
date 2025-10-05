# 🖥 Basic Architecture

### HDD (Hard Disk Drive)
- **Largest capacity**, persistent storage, slower than RAM.  
- **SSD (Solid State Drive)**: much faster alternative, no moving parts.  
- **Persistence**: data remains after shutdown.  
- **Throughput vs. Latency**:  
  - Throughput = amount of data transferred per second.  
  - Latency = time to access a single piece of data.  

---

### RAM (Random Access Memory)
- **Volatile storage**: wiped on restart.  
- **Random access**: any cell accessed in same time.  
- Measured in **GB** with **nanosecond access times**.  

---

### CPU (Central Processing Unit)
- Executes program instructions.  
- **Key properties**:  
  - **Instruction Set Architecture (ISA)** (x86, ARM).  
  - **Clock speed** (GHz).  
  - **Cores** – independent execution units.  
  - **Pipelining & parallelism** – execution optimization.  

---

### Cache
- Holds frequently accessed data closer to CPU.  
- **Levels**:  
  - **L1** (fastest, smallest).  
  - **L2**.  
  - **L3** (largest, slower but still faster than RAM).  
- Based on **locality of reference**:  
  - **Temporal locality** – recently used data reused soon.  
  - **Spatial locality** – nearby memory likely accessed soon.  

---

### Memory Hierarchy

From **fastest & smallest** → **slowest & largest**:  



# ⚙️ Fundamentals of a System

Fundamentally in a system we:  
- **Move data**  
- **Store data**  
- **Transform data**  

---

# 📐 Metrics of a Good System

# 📐 Metrics of a Good System

### Availability
- Formula: Uptime / (Uptime + Downtime)
- Defines **Service Level Objectives (SLOs)** and **Service Level Agreements (SLAs)**.  

---

### Reliability
- Ability to perform its intended functions **without failure or errors** over a specified period of time.  

---

### Fault Tolerance
- How well the system can **detect and heal itself** from a problem.  

---

### Redundancy
- Example: having a **second server as backup**.  
- By having this redundancy, we are able to have **fault tolerance**.  
- If we had two servers that were both active, this would be called **active-active redundancy**.  

---

### Throughput
- Amount of data or operations the system can handle **over some period of time**.  

---

### Latency
- The period of time between a **client request** and a **response from the server**.  

---
