#  Algorithmic Power & Efficiency Analysis: Spiking Neural Networks

This document details the mathematical and architectural framework of our **Spiking Neural Network (SNN)**. By leveraging event-driven processing and temporal sparsity, this architecture achieves ultra-low-power execution suitable for edge-based medical diagnostics.

---

## 1. Mathematical Framework of the Spiking Neuron

The computational efficiency of the network is anchored in the **Leaky Integrate-and-Fire (LIF)** neuron model. Unlike traditional continuous-activation nodes, an LIF neuron updates its internal state dynamically over discrete simulated time steps ($t$).

### Membrane Potential Update
The internal state of a post-synaptic neuron $i$ is governed by its membrane potential, $V_i(t)$. When incoming binary spikes ($x_j(t) \in \{0, 1\}$) arrive from pre-synaptic neurons $j$ across synaptic weights ($w_{ij}$), the potential updates as:

$$V_i(t) = \beta V_i(t-1) + \sum_{j} w_{ij} x_j(t)$$

Where:
* $\beta \in (0, 1)$ is the **decay factor** modeling the biological "leak" of charge over time.
* $x_j(t)$ is the incoming **binary spike** (either $1$ or $0$) at time step $t$.
* $w_{ij}$ is the synaptic weight connecting neuron $j$ to neuron $i$.

### Spike Generation Threshold
The neuron evaluates its membrane potential against a hard threshold ($V_{\text{th}}$). If the accumulated voltage crosses this limit, the neuron fires a binary spike ($S_i(t)$) and resets its potential:

$$S_i(t) = \begin{cases} 1 & \text{if } V_i(t) \ge V_{\text{th}} \\ 0 & \text{otherwise} \end{cases}$$

$$V_i(t) \leftarrow V_i(t) \cdot (1 - S_i(t)) + V_{\text{reset}} \cdot S_i(t)$$

---

## 2. Hardware Arithmetic Optimization: Sparse Accumulation (AC)

Because the input vector $x(t)$ consists strictly of binary elements ($0$ or $1$), the standard algebraic requirement for floating-point matrix multiplication is entirely bypassed. 

The weight-update summation simplifies based on the incoming spike state:
* When $x_j(t) = 0$: No mathematical operation is executed.
* When $x_j(t) = 1$: The synaptic weight $w_{ij}$ is directly added to the accumulator.

$$\text{Operation Cost} = V_i(t-1) + w_{ij}$$

This shifts the fundamental computing primitive from a **Multiply-Accumulate (MAC)** operation to a pure **Accumulate (AC)** operation. 

### Energy Profile per Operation (45nm CMOS substrate)
At the silicon level, eliminating the multiplier array yields drastic energy savings per computational step:

* **Standard Multiply-Accumulate (MAC):** $\approx 4.9 \text{ pJ}$
* **SNN Sparse Accumulate (AC):** **$\approx 0.9 \text{ pJ}$**

---

## 3. Quantifying Temporal Sparsity

The network's low power consumption is a direct function of **temporal sparsity**—the fraction of total neurons actively firing during an inference window.

Let $N$ be the total number of neurons in a layer, and $T$ be the total simulated observation time windows ($T = 4 \text{ to } 8$ steps). The total energy consumed by an SNN layer ($E_{\text{SNN}}$) is formulated as:

$$E_{\text{SNN}} = \left( N \times s \times T \right) \times E_{\text{AC}}$$

Where:
* $s$ is the **average firing rate** (sparsity factor), representing the percentage of neurons that spike per time step. In highly optimized neuroimaging architectures, $s \approx 0.10 \text{ to } 0.20$ (meaning 80%+ of the network remains dormant at any given instant).
* $E_{\text{AC}}$ is the baseline energy cost of a single 32-bit addition ($0.9 \text{ pJ}$).

Because execution scales linearly with the sparse firing rate ($s$) rather than the dense layout of the network matrix, the model minimizes idle power dissipation entirely.

---

## 4. Neuromorphic Hardware Deployment Roadmap

While this software model optimizes inference on standard digital hardware by bypassing zero-value operations in code, the architecture is natively structured for compilation onto **Neuromorphic Edge Processors** (e.g., Intel Loihi, SynSense, or SpiNNaker).

Neuromorphic hardware implements the LIF differential equations directly via physical, sub-threshold silicon circuits. On these native architectures, energy consumption drops to the **microjoule ($\mu J$) per inference** scale because power is drawn exclusively when a physical spike propagates across a wire.

### Clinical and Practical Value
* **Zero Cloud Latency:** Diagnostics execute locally within the hospital imaging suite.
* **Data Privacy Compliance:** Patient MRI/PET data remains entirely on-device, satisfying strict medical data privacy standards without needing remote cloud processing.
