# arxiv LLM daily — 2026-11-04

the 30 most recent papers from cs.CL and cs.AI.

### [DreamX: Video Diffusion Model is a Universal Latent Action Learner](http://arxiv.org/abs/2611.05377v1)
_Jisoo Kim, Chaehyun Kim, Junsu Kim, Jiho Park, Seongchan Kim, +4 more_ • 2026-11-03

Learning a universal action representation from video requires modeling dynamics that are consistent across different executions of the same action yet invariant to changes in embodiment and appearance. Existing latent action models infer actions from visual transitions, but their representations often entangle the...

### [From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence](http://arxiv.org/abs/2611.05376v1)
_Hao Fei_ • 2026-11-03

For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they are not looking at, fail to find the r...

### [Aligning Language Models with General Preferences: An Empirical Study of Direct Nash Optimization](http://arxiv.org/abs/2611.05373v1)
_Austin Tsai, Saurav Nanda, Ganapathy Parthasarathy, Bhuvnesh Kumar, Parivesh Choudhary_ • 2026-11-03

Direct Nash Optimization (DNO) aligns a language model to a general preference function by approximating the Nash equilibrium of a two-player preference game. Its practical variant, DNO-Prct, iterates on-policy sampling, LLM-based rating of the samples together with a teacher's gold response, large-margin preference...

### [Suppressing Misaligned Behaviors in Language Models, Durably](http://arxiv.org/abs/2611.05358v1)
_Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen_ • 2026-11-03

Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narr...

### [Reading Why: Born-Measured Attention with Exact Word Evidence on Light and Qubits](http://arxiv.org/abs/2611.05355v1)
_Teerawat Tongloy, Jiraporn Pongsopa, Rangsan Jomtarak_ • 2026-11-03

When a language model answers, we can usually only estimate why. We build a transformer in which every step is a Born measurement - attention $|\langle q|k\rangle|^4$ normalised over each row, a measured product in place of the feed-forward nonlinearity, and a Born readout. With its denominators held at their values...

### [Adversarial Speculative Reasoning Improves Long Horizon Agents](http://arxiv.org/abs/2611.05345v1)
_Hongyin Luo, Wei Fang, Lijie Yang, Owen Stepan, Daniel Suit, +3 more_ • 2026-11-03

Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growing effort to train better draft models has been focused solely on acceptance rate. We argue that this view does not hold true for long-hor...

### [A Circuit for In-Context Learning](http://arxiv.org/abs/2611.05344v1)
_Andrew Gao, William Gao_ • 2026-11-03

In-context learning (ICL) lets a pretrained language model perform a task specified by demonstrations in its prompt, with no parameter updates. With arbitrary labels the model must acquire a mapping it cannot have memorized, so the learning happens within a single forward pass. Prior work found candidate parts but n...

### [Weight-space programming for auditing clinical decision networks](http://arxiv.org/abs/2611.05341v1)
_Humza Nusrat, Omar Nusrat_ • 2026-11-03

Machine learning models in radiotherapy are commissioned by testing them on cases with known answers, which may not reveal a shortcut that the test cases share with the training data. Frontier language models have recently been reported to read and write the raw weights of small neural networks, an ability called we...

### [MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection](http://arxiv.org/abs/2611.05340v1)
_Omar Nusrat_ • 2026-11-03

Medical physicists turn a prescription into a delivered dose and check one another's calculations, because one error in a beam calibration or a monitor-unit (MU) calculation can affect every patient treated with it. MedPhysBench has ten seeded generators of calculation items in radiation therapy, diagnostic imaging,...

### [A simple adaptive accelerated optimistic dual averaging method for unconstrained convex optimization in $p$-norm geometry](http://arxiv.org/abs/2611.05334v1)
_Bowen Li, Danqing Zhou, Chuan He_ • 2026-11-03

Efficient preconditioning plays an important role in large-scale first-order optimization. In this paper, we propose an adaptive accelerated optimistic dual averaging ($\text{A}^2$ODA) method for unconstrained convex optimization that adopts low-cost preconditioning based on $p$-norm geometry for $p\in[2,\infty]$. T...

### [PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](http://arxiv.org/abs/2611.05320v1)
_Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang, Feixiang Ruan, +9 more_ • 2026-11-03

Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request and one calibration episode of the rob...

### [HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation](http://arxiv.org/abs/2611.05319v1)
_Zhen Tao, Xun Zhou, Xuhui Chen, Ziyue Qiao, Qingqiang Sun_ • 2026-11-03

In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone. Yet users and items remain asymmetric: only the user is given a structured profile; it enters a bandwidth-limited reranker prompt; and it is frozen after warmup. We recast LLM-based recommendation as an agentic-communicati...

### [MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution](http://arxiv.org/abs/2611.05313v1)
_Dian Jin, Jinluan Yang, Kairong Han, Baohong Li, Zijing Hu, +7 more_ • 2026-11-03

Skill memories encode past experiences as textual prompts to improve reinforcement learning (RL) for self-evolving agents. Complementing RL, On-Policy Self-Distillation (OPSD) provides dense, fine-grained supervision to internalize knowledge from skill-guided trajectories and accelerate policy learning. However, sel...

### [You don't need long context](http://arxiv.org/abs/2611.05306v1)
_Peter Belcak, Saurav Muralidharan, Jindong Jiang, Yonggan Fu, Wonmin Byeon, +7 more_ • 2026-11-03

Later tokens are costlier to generate than earlier tokens. On frontier open weight models, the disparity in cost may rise to as much as 7x. Through frequent compaction, we show across a broad range of long-horizon and long-input tasks that frontier language models sacrifice little to no task accuracy when maintainin...

### [LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers](http://arxiv.org/abs/2611.05304v1)
_Minsoo Cheong, Sungjoo Yoo_ • 2026-11-03

Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped language models match the performance of non-looped models several times their size. While this architecture effectively reduces parameter...

### [Personas Are Not People: Identity as State, Not Attribute](http://arxiv.org/abs/2611.05292v1)
_Tamunotonye Harry, Yuanyuan Feng_ • 2026-11-03

Synthetic populations, large sets of simulated people, are increasingly used in place of real people to pretest surveys, simulate users and communities, and evaluate AI systems. Each simulated person is defined by a persona, a written profile of fixed traits, demographics, and attitudes that a language model is inst...

### [False Reassurance in LLM Severe-Weather Guidance: A Replayable Evaluation Against Real NWS Alerts](http://arxiv.org/abs/2611.05290v1)
_Kadharmoideen Fadurudeen_ • 2026-11-03

An LLM assistant that cannot see official severe-weather alerts may tell users that conditions are calm while a warning is active. We call this false reassurance and measure it by replaying 117 frozen cases built from real U.S. National Weather Service (NWS) alerts (69 alert cases, 32 no-alert controls, 16 non-U.S....

### [Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment](http://arxiv.org/abs/2611.05287v1)
_Ariana M. Villegas-Suarez, Guido Freire, Sohan Venkatesh, Bartosz Cywiński_ • 2026-11-03

Fine-tuning a large language model (LLM) on harmful data in a narrow domain, such as bad medical advice, can make it broadly misaligned. How realistic this risk is remains unclear, since models are very rarely fine-tuned on explicitly harmful data in practice. In this work, we show that fine-tuning on data the model...

### [Beyond Accuracy: What Language-Subspace Interventions Capture, Remove, and Improve](http://arxiv.org/abs/2611.05278v1)
_Shaanil Punglia, Dadhichi Telwadkar, Vaibhav Rathore, Siddharth Sureka, Neha Bhargava_ • 2026-11-03

Language-subspace interventions aim to improve multilingual reasoning by suppressing language-related components in mid-layer activations. Using MATH and MGSM across four open-weight LLMs, we ask three questions: do estimated language subspaces capture translation-associated variation? Does projecting them out remov...

### [The Geometry of Ignorance: Detecting Suppressed Knowledge in LLMs through Activation Fragmentation](http://arxiv.org/abs/2611.05272v1)
_Adar Peleg, Dvir Alsheich, Tomer Ashuach, Avi Mendelson_ • 2026-11-03

Evaluating whether a large language model (LLM) genuinely knows a concept remains a fundamental problem, since behavioral metrics can be fooled by suppression: a model that refuses to answer may still harbor recoverable knowledge. The framework measures the geometric coherence of \textit{anon-vectors}, the differenc...

### [JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks](http://arxiv.org/abs/2611.05263v1)
_Shanka Subhra Mondal, Jiayun Wang_ • 2026-11-03

Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer high-level plans, navigate through i...

### [Going Deeper With Memories](http://arxiv.org/abs/2611.05255v1)
_Afshin Khadangi_ • 2026-11-03

Byte level language models avoid tokenizer dependence and provide universal coverage, but processing every byte at full resolution is expensive. We introduce DeepMem, a causal multiscale architecture that separates semantic compression from exact byte preservation. A learned invertible subband transform constructs a...

### [ARLoop: Fully-Open Pre-trained Looped Transformers with Attention Residuals](http://arxiv.org/abs/2611.05234v1)
_Yuekun Yao, Yupei Du, Dawei Zhu, Huan Sun_ • 2026-11-03

Looped transformers increase effective depth by repeatedly applying a shared set of transformer layers, offering a parameter-efficient way to scale computation. However, standard residual connections aggregate information across recurrent depth into a single stream, providing limited control over which intermediate...

### [Fairness Metrics based on the AUC in Clinical Predictive AI](http://arxiv.org/abs/2611.05222v1)
_João Matos, Ben Van Calster, Richard D. Riley, Paula Dhiman, Gary S. Collins_ • 2026-11-03

Fairness evaluation of clinical prediction models for binary outcomes often involves fairness metrics that compare the area under the receiver operating characteristic curve (AUC, or c-statistic) across subgroups. However, the AUC has been shown to be a non-collapsible metric, meaning that its subgroup specific and...

### [What Does the Model See? Representation Validity in Multimodal LLM-Based Video Analysis](http://arxiv.org/abs/2611.05181v1)
_Christian Pipal, Eva-Maria Vogel, Morgan Wack_ • 2026-11-03

Multimodal large language models (MLLMs) allow social scientists to analyze video at scale, but researchers must decide which parts of a video to provide as input. We use the term representation validity to examine how text, audio, video, and combined inputs affect measurement and subsequent analysis. We compare inp...

### [OperAItor: An Agentic Framework for Fault-Tolerant Operation of Chemical Processes](http://arxiv.org/abs/2611.05179v1)
_Javal Vyas, Mehmet Mercang{ö}z_ • 2026-11-03

OperAItor, an open-source framework for developing and evaluating large language model agents for supervisory fault management in chemical processes. The framework is demonstrated on a dynamic reactor-distillation process representing isopropanol dehydrogenation, with physically based thermodynamics and modified rea...

### [AgentAM: An AI Agent for Spatter- and Defect-Aware Process Optimization in Laser Powder Bed Fusion](http://arxiv.org/abs/2611.05171v1)
_Olabode T. Ajenifujah, Amir Barati Farimani_ • 2026-11-03

Predictive models for laser powder bed fusion (LPBF) are rarely used on the shop floor because querying them requires programming and model-specific knowledge. We present AgentAM, a large language model (LLM) agent that gives process engineers natural-language access to CFD-trained surrogates of spatter and melt poo...

### [Learning Behaviorally Relevant Dynamics in Multimodal Neural Recordings](http://arxiv.org/abs/2611.05167v1)
_Parastoo Azizeddin, Eray Erturk, Maryam M. Shanechi_ • 2026-11-03

Multimodal neural data can enable a more complete understanding of brain dynamics underlying behavior. Modalities such as spiking activity, local field potentials (LFPs), and behavior capture diverse spatiotemporal aspects of brain processes, yet prior neural-behavioral models that separate sources of variability re...

### [When Self-Verification Hurts: Calibrated Answer Repair for Financial Question Answering](http://arxiv.org/abs/2611.05166v1)
_Celine Guo, Weida Liang, Yujian Fu, Anqi Dang, Yanzheng Jin, +2 more_ • 2026-11-03

Financial question answering can fail even when a model extracts a plausible number from the supplied evidence: the answer may attach it to the wrong entity, period, unit, or accounting concept. Asking the model to verify and revise its draft can help, but open-ended revision may alter content that was already corre...

### [Basin2Vec: Learning Basin-Centric Embeddings for Scalable Hydrological Modeling](http://arxiv.org/abs/2611.05164v1)
_Muhammad Talha, Xiaofeng Liu, Yuan Yang, Pang-Ning Tan, A. Pouyan Nejadhashemi_ • 2026-11-03

Reliable streamflow prediction across time and in ungauged basins requires representations that capture hydrologically relevant basin characteristics. Existing methods rely on either fixed handcrafted attributes or general-purpose Earth observation embeddings not tailored to basin structure. We introduce \textbf{Bas...

_snapshot taken at 2026-11-04T20:31:37+00:00_
