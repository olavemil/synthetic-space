---
title: "Processes"
---

# Colony Processes

## Configuration

- Colony size: 8–16
- Suggestion fraction: 33%
- Consensus threshold: 60%
- Approval threshold: 3
- Voice space: main
- Suggestion model: lmstudio/liquid/lfm2-24b-a2b
- Writer model: lmstudio/nvidia/nemotron-3-nano

## on_message Flow

```
1. PREPROCESS (default) → summarize message history
2. REFLECT → each individual reflects on colony state
3. MESSAGING → internal colony messaging phase
4. DELIBERATE → suggesters propose, all vote (Borda)
5. RECOMPOSE (default) → unified colony voice
6. SEND → deliver to voice space
```

## heartbeat Flow

```
1. REFLECT → per-individual reflections (randomized order)
2. MESSAGING → internal colony messaging phase
3. CONTRIBUTE → each individual proposes one principle
4. REWRITE → colony writer synthesizes constitution draft
5. VOTE → round 1 (+ round 2 if needed)
6. PEER APPROVAL → each individual endorses 2 others
7. SPAWN CYCLE → eligible individuals reproduce
9. ORGANIZE → knowledge organization
10. CREATE → artifact creation
```

# Active Policies

## on_message

- preprocess: enabled
- postprocess: enabled

## thinking

- stages: default (single contribution + synthesis)
- post_spawn: none