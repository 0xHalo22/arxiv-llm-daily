# arxiv LLM daily — 2026-11-02

the 30 most recent papers from cs.CL and cs.AI.

### [Latent Reasoning in Continuous Space for Unified Multimodal Models](http://arxiv.org/abs/2610.42149v1)
_Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin_ • 2026-10-30

Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scal...

### [Flide: Accelerating Decision Inference with Exact State Forking](http://arxiv.org/abs/2610.42148v1)
_Bobo Li, Jiajia Song, Hao Fei, Wynne Hsu, Mong Li Lee_ • 2026-10-30

Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix rec...

### [Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention](http://arxiv.org/abs/2610.42147v1)
_Ales Kubicek, Andrea Caciolai, Liangzu Peng, Sukrit Sumant, Benjamin Hoover, +5 more_ • 2026-10-30

Agentic workflows are increasingly shifting towards long-horizon tasks, such as open-ended scientific work, where models benefit from long context windows. However, at ultra-long context (above 1M tokens), full attention is prohibitively expensive. A promising approach is sparse attention, in which a dedicated index...

### [Hierarchical World Models with Implicit Dynamics](http://arxiv.org/abs/2610.42146v1)
_Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran, +2 more_ • 2026-10-30

Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity. Existing hierarchical methods often use rigid macro-actions or latent skills, leading to b...

### [RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory](http://arxiv.org/abs/2610.42141v1)
_Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, +1 more_ • 2026-10-30

Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can...

### [DecisionRank: On-Policy Distillation for Decision-Model Rerankers](http://arxiv.org/abs/2610.42128v1)
_Yanran Wu, Dian Yu, Chongyang Bai, Jieyi Zhang, Rui Liu, +8 more_ • 2026-10-30

Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency. However, transferring a generative LLM's ranking knowledge to a decision model remains challenging: the teacher expresses preferences through a ranked list of document ID sequences, while the s...

### [ACCT: Asymmetric Cross-LLM Context Transfer](http://arxiv.org/abs/2610.42116v1)
_Yuzhe Liu, Haolin Tian, Tonghan Wang_ • 2026-10-30

In real-world deployments, large language model (LLM) systems are increasingly evolving from single-model invocation toward heterogeneous deployments in which different models are dynamically invoked for inference. When the same context is reused across models, however, each newly selected target model typically has...

### [Subquadratic Attention with a Hierarchical Tree-Structured Indexer](http://arxiv.org/abs/2610.42112v1)
_Leon Lufkin, Cutter Dawes, Alexander Speicher, Kamesh Krishnamurthy, Tomás Figliolia, +1 more_ • 2026-10-30

The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size...

### [CausalWAM: Learning the Causes of Actions in World Action Models](http://arxiv.org/abs/2610.42096v1)
_Juntao Cheng, Jinzhou Tang, Fan Feng, Henrik I. Christensen, Yujia Zheng_ • 2026-10-30

World action models (WAMs) learn latent variables from observations and use these to both predict the evolution of the scene and to generate actions. The prediction has to be of the whole scene, whereas only a portion of the scene causes actions. WAMs fitted to demonstrations do not, in general, guarantee that they...

### [RangeSWA: Training-Free Length Extrapolation for Continuous Diffusion Language Models](http://arxiv.org/abs/2610.42084v1)
_Guangfu Guo, Xiaoqian Lu, Linsey Pang, Weiran Yao, Haolin Chen, +2 more_ • 2026-10-30

Continuous diffusion language models show promising potential in text generation tasks, but are prone to problems such as text repetition, semantic drift, and generation quality degradation when the generation length exceeds the training length. To address these challenges, we propose RangeSWA, a training-free lengt...

### [The Knowledge Layer Model (KLM): Evidence-Visible AI Output, Routing Diagnostics, and Negative Results](http://arxiv.org/abs/2610.42066v1)
_Omer Asim Ozturk, Cihan Aydiner_ • 2026-10-30

AI answers require more than apparent correctness: reviewers need to inspect their recorded basis. We introduce the Knowledge Layer Model (KLM), an open, implementation-neutral specification for inference records with versioned epistemic assessments, evidence relations, and explicit unknowns. SEDIM, the knowledge an...

### [PersonaChatBench: Evaluating Chat Assistants with Diverse Simulated Users](http://arxiv.org/abs/2610.42060v1)
_Zheyuan Deng, Taoran Li, Jingwen Zhang, Yuante Li, Dachuan Zhao, +26 more_ • 2026-10-30

Conversational assistants are expected to help people with diverse backgrounds, preferences, and communication styles. Yet evaluations centered on a single cooperative user provide limited insight into how reliably an assistant serves users with different personas. We introduce PersonaChatBench, a framework for eval...

### [CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness](http://arxiv.org/abs/2610.42054v1)
_Xiao Yu, Justin Chih-Yao Chen, Zaid Khan, Hyunji Lee, Mohit Bansal_ • 2026-10-30

Reinforcement learning with verifiable rewards (RLVR) has become the standard method for training language models to reason. However, RLVR typically relies solely on outcome correctness, which does not guarantee that the CoT causally contributes to the final answer. Without this connection, outcome rewards may fail...

### [Near-Optimal Second-Order Convex Finite-Sum Optimization under Individual Smoothness](http://arxiv.org/abs/2610.42040v1)
_Xinliang Zhang, Lesi Chen, Zonghan Li, Jingzhao Zhang_ • 2026-10-30

We study the stochastic second-order oracle complexity of solving smooth convex finite-sum optimization with $n$ components. Very recently, Tsedenov \& Kovalev (2026) showed that the minimax optimal complexity under averaged smoothness and convexity is $\tildeΘ(n + n^{6/7} ε^{-2/7})$ by establishing nearly matching...

### [Same Question, Different Answers: Auditing Persona-Dependent Variation in Six LLMs on Smoking-Cessation Advice](http://arxiv.org/abs/2610.42039v1)
_Artin Yousefi, Aizierjiang Aiersilan, Lorien C Abroms, David A Broniatowski_ • 2026-10-30

Hundreds of millions of people now ask large language model (LLM) chatbots for health advice, which raises a question that is simple to pose and hard to answer: does everyone get the same advice? We audit six widely deployed LLMs from four providers on smoking cessation, a domain with codified clini- cal guidance an...

### [Learning Clean Generative Processes from Noisy Measurements](http://arxiv.org/abs/2610.42036v1)
_Fabian Kruse, Lorenzo Baldassari, Ivan Dokmanić_ • 2026-10-30

We study how to learn a generative model of clean images using only noisy observations. Diffusion processes and their generalizations to non-Gaussian noise require posterior predictions at every noise level. We first show that it is possible to learn these predictions from independent noisy views using Noise2Noise r...

### [There Is No Free Loop: When Does Looping a Trained Model Pay for Its Inference Compute?](http://arxiv.org/abs/2610.42030v1)
_Rhea Sanjay Sukthanker, Pashmina Cameron_ • 2026-10-30

Looping re-applies a block of layers so that each token passes through the block more than once. Adding a loop to a trained model is attractive because it leaves the parameter count, and hence the disk size, the memory footprint and the training cost unchanged. Unfortunately, every generated token pays for the loop....

### [Know When the Equation Is Wrong: Structural Uncertainty for LLM-Guided Symbolic Regression under Extrapolation](http://arxiv.org/abs/2610.42024v1)
_Mostafa Cham, Bayu Adhi Tama, Jianwu Wang_ • 2026-10-30

Large language models (LLMs) can help discover mathematical equations from data, but most LLM-guided symbolic regression methods focus on a single best equation without quantifying uncertainty over alternative functional forms. This is challenging because distinct equations can fit the observed data similarly while...

### [Asynchronous Flow Map Language Models](http://arxiv.org/abs/2610.42018v1)
_Chanhyuk Lee, Wonjung Kim, Patrick Pynadath, Jaehoon Yoo, Satoshi Hayakawa, +3 more_ • 2026-10-30

The order in which tokens are predicted in language modeling has a profound impact on the quality of generated sequences. Autoregressive and masked diffusion models iteratively fill in tokens and can exploit such orderings across generation steps, but how to leverage an ordering for one-step parallel language modeli...

### [TurnTurk-GPT: Text-Based Turn-Taking Prediction for Turkish](http://arxiv.org/abs/2610.42010v1)
_Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Nur Yağmur Tuncer, Mustafa Sertaç Türkel_ • 2026-10-30

This paper presents TurnTurk-GPT, a text-based turn-taking predictor for Turkish obtained by fine-tuning a Turkish GPT-2 model with the TurnGPT objective on synthetic and real dialogue, and evaluates it on real Turkish conversation against rule baselines, a zero-shot Turkish language model and a widely used multilin...

### [TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents](http://arxiv.org/abs/2610.42004v1)
_Xiangyu Kong, Ruirui Yang, Xia Hou_ • 2026-10-30

Multi-turn negotiation remains a challenging problem for large language model (LLM) agents. While LLMs can conduct natural-language dialogue, existing benchmarks predominantly assess only agreement rates, overlooking whether negotiated commitments actually create value once executed. To address this gap, we introduc...

### [AutoAnalysis: An automated, self-updating meta-analysis of human-AI collaboration](http://arxiv.org/abs/2610.42001v1)
_Michelle Vaccaro, Abdullah Almaatouq, Thomas W. Malone_ • 2026-10-30

As generative artificial intelligence (AI) becomes more capable and widely used, understanding when and how humans should work with these systems is becoming increasingly important. However, the empirical evidence in this space offers conflicting recommendations, which leaves individuals and organizations without cl...

### [Less Loss, Fixed Weights: Logit Corrections for Forgetting](http://arxiv.org/abs/2610.42000v1)
_Hanyu Yang_ • 2026-10-30

When a language model is fine-tuned to follow instructions, or further pretrained on a new subject, it often gets worse at predicting standard web text. This is known as "forgetting." We ask whether this loss can be undone by simple, fixed adjustments to the model's final token predictions. Across 14 pairs of base a...

### [SecPO: Principled Adversarial Training for Prompt Injection Security](http://arxiv.org/abs/2610.41998v1)
_Sizhe Chen, Yibo Peng, Jaewon Chang, Chawin Sitawarin, David Wagner_ • 2026-10-30

Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers from attack success rates (ASRs) approaching 100% under ada...

### [DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention](http://arxiv.org/abs/2610.41994v1)
_Zhangchi Feng, Harry Jiang, Yangyifei Luo, Ray Zhang, Richong Zhang_ • 2026-10-30

Linear attention scales linearly with sequence length, but its finite-state memory can limit long-context retrieval. In gated linear recurrences, memory retention depends on state decay, which is shaped jointly by gate parameters A_log and dt_bias and by input activations. In controlled Gated DeltaNet (GDN) experime...

### [ID2Pattern: Pretraining Generalizable Identity Behavior Patterns for Transaction Risk Foundation Models](http://arxiv.org/abs/2610.41988v1)
_Ze Zhao, Haoyu Jiang, Weiyu Han, Ruobing Zuo, Xiao Tan, +2 more_ • 2026-10-30

Large-scale behavioral pretraining offers a promising route to generalizable representations in online payment systems. However, high-cardinality identity fields such as card, device, and account IDs, though rich in behavioral signals, remain underexploited. Their continually growing vocabularies and limited semanti...

### [When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity](http://arxiv.org/abs/2610.41970v1)
_Jun Liu, Dajie Sun, Zhenglun Kong, Zhenjiang Fan, Peiyan Dong, +6 more_ • 2026-10-30

World-action models increasingly apply test-time scaling, spending extra inference computation on candidate selection and adaptive allocation to improve control. Such gains are credible only when candidates carry exploitable signal, nominal compute savings become real speedup, and evaluation stays reliable. We audit...

### [Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity](http://arxiv.org/abs/2610.41968v1)
_Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah, Jinbin Zhang, Nilesh Gupta, +2 more_ • 2026-10-30

Weight pruning can reduce the storage and inference cost of large language models (LLMs), but preserving quality at high sparsity levels remains challenging. Existing methods face a quality-cost trade-off in this regime. One-shot pruning is cheap but degrades sharply as sparsity increases, even when followed by post...

### [Chronos-2: A foundation model for multivariate time series forecasting](http://arxiv.org/abs/2610.41956v1)
_Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han, +20 more_ • 2026-10-30

Accurate forecasting with uncertainty quantification is critical in a variety of scientific applications ranging from epidemiology and economics to energy systems and earth sciences. Yet most forecasting models still need to be developed and trained separately for each domain-specific dataset. Time series foundation...

### [Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions](http://arxiv.org/abs/2610.41951v1)
_Ning E, Changde Du, Yizhuo Lu, Huiguang He_ • 2026-10-30

Multimodal Large Language Models (MLLMs) have achieved impressive performance across a wide range of reasoning tasks, yet it remains unclear whether their internal representations and decision criteria align with the latent structure of human cognition. In this work, we propose a novel framework to align MLLMs with...

_snapshot taken at 2026-11-02T22:27:27+00:00_
