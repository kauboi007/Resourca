# ⚛️ Quantum Resource Estimator

A clean, minimal tool to estimate **quantum resources** (qubits, runtime, error correction overhead, etc.) for your Q# programs

---

## 🚀 What This Does

This project uses Q#'s built-in resource estimation to give you:

* 🔢 **Physical Qubits**
* 🧠 **Logical Qubits**
* ⏱️ **Estimated Runtime**
* ⚙️ **rQOPS (reliable quantum ops/sec)**
* 🧱 **Code Distance (error correction strength)**
* 🛡️ **QEC Scheme used**

---

## 📁 Project Structure

```
.
├── src/
│   └── GRQ.qs              # Your Q# quantum program (must be inside src)
├── estresources.py         # Python script to run estimation
└── README.md          
```

> ⚠️ **Important:** The Q# file you want to estimate **must be placed inside the `src/` folder**.
> The estimator expects your quantum code to live there — otherwise it won’t find it and will just sit there judging you silently.

---

## 🧰 Requirements

Make sure you have:

* Python (3.9+ recommended)
* Q# + Azure Quantum Development Kit
* `qsharp` Python package
* `qsharp_widgets` (for visualization support)

Install dependencies:

```bash
pip install qsharp qsharp-widgets
```

---

## 🧪 How to Use

### 1. Write Your Q# Program

Place your file inside the `src/` folder and define your operation:

```qsharp
operation GRQ() : Unit {
    // your quantum logic here
}
```

---

### 2. Run the Estimator

```bash
python estresources.py
```

---

### 3. Read the Output

Example output:

```
Physical Qubits : 1,234,567
Runtime         : 2 hours
rQOPS           : 1e9
Code Distance   : 15
Logical Qubits  : 120
QEC Scheme      : surface_code
```

---

## 🧠 What These Mean (Quick Intuition)

* **Physical Qubits** → actual hardware needed (this is the scary number)
* **Logical Qubits** → ideal qubits before error correction
* **Code Distance** → higher = more error protection (but more cost)
* **Runtime** → how long your algorithm runs
* **rQOPS** → how fast the quantum computer must be
* **QEC Scheme** → error correction strategy used

---

## 🤝 Contributing

Pull requests welcome. If you can reduce qubit counts by 10x, you’re basically a wizard.

---

## 🧾 TL;DR

1. Put your Q# file in `src/`
2. Define your operation
3. Run:

```bash
python estresources.py
```

---

Quantum is the future.
