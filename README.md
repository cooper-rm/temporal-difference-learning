# Temporal Difference Learning

MSDS 684 - Reinforcement Learning | Lab 4

## Overview

This project implements and compares two temporal difference (TD) control algorithms — SARSA (on-policy) and Q-learning (off-policy) — using Gymnasium's CliffWalking-v0 environment. The goal is to understand the behavioral differences between on-policy and off-policy TD methods, particularly how SARSA learns a safer path while Q-learning finds the optimal but riskier route.

## Key Components

- **SARSA**: On-policy TD control with epsilon-greedy exploration
- **Q-learning**: Off-policy TD control with epsilon-greedy exploration
- **Experiments**: Multiple seeds (30+), varying step-size (alpha) and epsilon-decay schedules
- **Visualizations**: Learning curves with 95% confidence intervals, Q-value arrow grids, trajectory plots, and value function heatmaps

## Environment

**CliffWalking-v0**: A 4x12 gridworld where the agent must navigate from start to goal while avoiding a cliff along the bottom edge. Stepping into the cliff returns the agent to start with a -100 reward. Each normal step gives -1 reward.

## Usage

```bash
# Generate the lab report PDF
python generate_report.py
```
